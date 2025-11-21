const form = document.getElementById('quizForm');
const submitBtn = document.getElementById('submitBtn');
const resultsEl = document.getElementById('results');
const progressBar = document.getElementById('progress-bar');

const SCALE = {
  1: "Nenhum Interesse",
  2: "Pouco Interesse",
  3: "Moderado",
  4: "Interessado",
  5: "Muito Interessado",
};

let QUESTIONS = [];
let DOMAINS = {};
let PERSONAS = {};

function updateProgress() {
  const answered = [...form.querySelectorAll('input[type="radio"]:checked')].length;
  const total = QUESTIONS.length;
  const pct = Math.round((answered / total) * 100);
  progressBar.style.width = `${pct}%`;
}

function renderQuestions() {
  form.innerHTML = '';
  QUESTIONS.forEach((q, idx) => {
    const qId = `q_${q.id}`;
    const div = document.createElement('div');
    div.className = 'question';

    const meta = document.createElement('div');
    meta.style.marginBottom = '6px';
    meta.innerHTML = `<span class="badge">${DOMAINS[q.domain]}</span> · <span class="badge">${PERSONAS[q.persona]}</span>`;
    div.appendChild(meta);

    const h3 = document.createElement('h3');
    h3.textContent = `${idx + 1}. ${q.text}`;
    div.appendChild(h3);

    const scale = document.createElement('div');
    scale.className = 'scale';

    for (let v = 1; v <= 5; v++) {
      const label = document.createElement('label');
      const input = document.createElement('input');
      input.type = 'radio';
      input.name = qId;
      input.value = String(v);
      input.required = true;
      input.addEventListener('change', updateProgress);
      const span = document.createElement('span');
      span.textContent = `${v} — ${SCALE[v]}`;
      label.appendChild(input);
      label.appendChild(span);
      scale.appendChild(label);
    }

    div.appendChild(scale);
    form.appendChild(div);
  });

  updateProgress();
  window.scrollTo({ top: 0, behavior: 'smooth' });
}

async function loadQuestions() {
  const res = await fetch('/api/questions');
  const data = await res.json();
  QUESTIONS = data.questions;
  DOMAINS = data.domains;
  PERSONAS = data.personas;
  renderQuestions();
}

function collectAnswers() {
  const answers = [];
  QUESTIONS.forEach(q => {
    const v = form.querySelector(`input[name="q_${q.id}"]:checked`);
    if (!v) return;
    answers.push({ id: q.id, value: Number(v.value) });
  });
  return answers;
}

function renderBars(container, items, title) {
  const card = document.createElement('div');
  card.className = 'card';
  const h4 = document.createElement('h4');
  h4.textContent = title;
  card.appendChild(h4);

  items.forEach(it => {
    const row = document.createElement('div');
    row.className = 'kv';
    const label = document.createElement('div');
    label.textContent = it.label;
    const value = document.createElement('div');
    value.className = 'value';
    value.textContent = `${it.score}%`;
    row.appendChild(label);
    row.appendChild(value);

    const bar = document.createElement('div');
    bar.className = 'bar';
    const fill = document.createElement('div');
    fill.style.width = '0%';
    bar.appendChild(fill);

    card.appendChild(row);
    card.appendChild(bar);

    requestAnimationFrame(() => {
      requestAnimationFrame(() => {
        fill.style.width = `${it.score}%`;
      });
    });
  });

  container.appendChild(card);
}

function renderResults(payload) {
  resultsEl.innerHTML = '';
  resultsEl.classList.remove('hidden');

  const grid = document.createElement('div');
  grid.className = 'grid';

  renderBars(grid, payload.domain_ranking.slice(0, 3), 'Top 3 Áreas Recomendadas');
  renderBars(grid, payload.domain_ranking, 'Áreas (Ranking Completo)');
  renderBars(grid, payload.persona_ranking, 'Perfis (Arquétipos)');

  resultsEl.appendChild(grid);

  const summary = document.createElement('div');
  summary.className = 'card';
  const t = payload.summary.top_domains.map(x => `${x.label}: ${x.score}%`);
  const personaTop = payload.summary.top_persona ? `${payload.summary.top_persona.label} (${payload.summary.top_persona.score}%)` : '—';
  summary.innerHTML = `
    <h4>Resumo</h4>
    <p><strong>Áreas em destaque:</strong> ${t.join(' · ')}</p>
    <p><strong>Perfil dominante:</strong> ${personaTop}</p>
    <p class="muted">${payload.summary.interpretation.hint}</p>
  `;
  resultsEl.appendChild(summary);

  // Card de exportação JSON
  const jsonCard = document.createElement('div');
  jsonCard.className = 'card';
  const jsonTitle = document.createElement('h4');
  jsonTitle.textContent = 'Exportar resultado';
  jsonCard.appendChild(jsonTitle);

  const jsonDesc = document.createElement('p');
  jsonDesc.textContent = 'Baixe um arquivo JSON com todos os percentuais, rankings e resumo para guardar, analisar ou compartilhar.';
  jsonCard.appendChild(jsonDesc);

  const jsonBtn = document.createElement('button');
  jsonBtn.type = 'button';
  jsonBtn.textContent = 'Baixar JSON do resultado';
  jsonBtn.addEventListener('click', () => {
    const blob = new Blob([JSON.stringify(payload, null, 2)], { type: 'application/json' });
    const url = URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url;
    const now = new Date();
    const ts = now.toISOString().slice(0,19).replace(/[:T]/g, '-');
    a.download = `resultado_carreira_ti_${ts}.json`;
    document.body.appendChild(a);
    a.click();
    document.body.removeChild(a);
    URL.revokeObjectURL(url);
  });
  jsonCard.appendChild(jsonBtn);

  resultsEl.appendChild(jsonCard);

  window.scrollTo({ top: resultsEl.offsetTop - 20, behavior: 'smooth' });
}

async function submitQuiz() {
  const answers = collectAnswers();
  if (answers.length !== QUESTIONS.length) {
    alert("Por favor, responda todas as perguntas antes de enviar.");
    return;
  }
  submitBtn.disabled = true;
  try {
    const res = await fetch('/api/score', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(answers)
    });
    const payload = await res.json();
    renderResults(payload);
  } catch (e) {
    alert("Ocorreu um erro ao gerar o resultado.");
    console.error(e);
  } finally {
    submitBtn.disabled = false;
  }
}

submitBtn.addEventListener('click', submitQuiz);
loadQuestions();