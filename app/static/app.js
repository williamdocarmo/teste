const questionCard = document.getElementById('questionCard');
const resultsEl = document.getElementById('results');
const progressBar = document.getElementById('progress-bar');
const backBtn = document.getElementById('backBtn');

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

let currentIndex = 0;
const answers = new Map(); // id -> value
const missingIds = new Set(); // perguntas faltantes

function updateProgress() {
  const pct = Math.round((answers.size / QUESTIONS.length) * 100);
  progressBar.style.width = `${pct}%`;
}

function renderCurrentQuestion() {
  if (!QUESTIONS.length) return;

  if (currentIndex < 0) currentIndex = 0;
  if (currentIndex >= QUESTIONS.length) {
    submitQuiz();
    return;
  }

  const q = QUESTIONS[currentIndex];
  questionCard.classList.remove('hidden');
  questionCard.innerHTML = '';

  const meta = document.createElement('div');
  meta.style.marginBottom = '8px';
  meta.innerHTML = `<span class="badge">${DOMAINS[q.domain]}</span> · <span class="badge">${PERSONAS[q.persona]}</span> · <span class="badge">${currentIndex + 1}/${QUESTIONS.length}</span>`;
  questionCard.appendChild(meta);

  // Se esta pergunta está marcada como não respondida, mostra um aviso
  if (missingIds.has(q.id)) {
    const hint = document.createElement('div');
    hint.className = 'hint';
    hint.textContent = 'Você pulou esta pergunta antes. Responda para continuar.';
    questionCard.appendChild(hint);
  }

  const h3 = document.createElement('h3');
  h3.textContent = q.text;
  questionCard.appendChild(h3);

  const scale = document.createElement('div');
  scale.className = 'scale';

  for (let v = 1; v <= 5; v++) {
    const label = document.createElement('label');
    const input = document.createElement('input');
    input.type = 'radio';
    input.name = `q_${q.id}`;
    input.value = String(v);
    input.required = true;
    const span = document.createElement('span');
    span.textContent = `${v} — ${SCALE[v]}`;
    label.appendChild(input);
    label.appendChild(span);

    if (answers.has(q.id) && answers.get(q.id) === v) input.checked = true;

    input.addEventListener('change', () => {
      answers.set(q.id, v);
      updateProgress();
      setTimeout(() => {
        currentIndex += 1;
        renderCurrentQuestion();
      }, 90);
    });

    scale.appendChild(label);
  }

  questionCard.appendChild(scale);
  backBtn.disabled = currentIndex === 0;
  // Scroll para o topo do card quando muda
  window.scrollTo({ top: 0, behavior: 'smooth' });
}

async function loadQuestions() {
  const res = await fetch('/api/questions');
  const data = await res.json();
  QUESTIONS = data.questions;
  DOMAINS = data.domains;
  PERSONAS = data.personas;
  currentIndex = 0;
  answers.clear();
  updateProgress();
  renderCurrentQuestion();
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

  const jsonCard = document.createElement('div');
  jsonCard.className = 'card';
  const jsonTitle = document.createElement('h4');
  jsonTitle.textContent = 'Exportar resultado';
  jsonCard.appendChild(jsonTitle);

  const jsonDesc = document.createElement('p');
  jsonDesc.textContent = 'Baixe um arquivo JSON com todos os percentuais, rankings e resumo.';
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
  const payload = [];
  for (const q of QUESTIONS) {
    const v = answers.get(q.id);
    if (!v) {
      alert("Há perguntas sem resposta. Use Voltar para completar.");
      currentIndex = QUESTIONS.findIndex(qq => !answers.get(qq.id));
      renderCurrentQuestion();
      return;
    }
    payload.push({ id: q.id, value: Number(v) });
  }

  try {
    const res = await fetch('/api/score', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(payload)
    });
    const scored = await res.json();
    questionCard.classList.add('hidden');
    renderResults(scored);
  } catch (e) {
    alert("Ocorreu um erro ao gerar o resultado.");
    console.error(e);
  }
}

backBtn.addEventListener('click', () => {
  if (currentIndex > 0) {
    currentIndex -= 1;
    renderCurrentQuestion();
  }
});

loadQuestions();