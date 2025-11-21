const questionCard = document.getElementById('questionCard');
const resultsEl = document.getElementById('results');
const progressBar = document.getElementById('progress-bar');
const backBtn = document.getElementById('backBtn');
const toast = document.getElementById('toast');

const urlParams = new URLSearchParams(window.location.search);
const COMPACT = urlParams.get('compact') === '1';

const SCALE = COMPACT ? {
  1: "1",
  2: "2",
  3: "3",
  4: "4",
  5: "5",
} : {
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
const missingIds = new Set();

function updateProgress() {
  const pct = Math.round((answers.size / QUESTIONS.length) * 100);
  progressBar.style.width = `${pct}%`;
}

function showToast(msg, type='warn') {
  toast.textContent = msg;
  toast.classList.remove('hidden');
  toast.classList.toggle('warn', type === 'warn');
  setTimeout(() => {
    toast.classList.add('hidden');
  }, 2500);
}

function focusCard() {
  questionCard.scrollIntoView({ behavior: 'smooth', block: 'start' });
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
  questionCard.classList.remove('warn-pulse');
  questionCard.innerHTML = '';

  // Apenas contador (sem segmento/domínio na pergunta)
  const meta = document.createElement('div');
  meta.style.marginBottom = '8px';
  meta.innerHTML = `<span class="badge">Pergunta ${currentIndex + 1}/${QUESTIONS.length}</span>`;
  questionCard.appendChild(meta);

  // Se a pergunta estava faltando, destaca
  if (missingIds.has(q.id)) {
    questionCard.classList.add('warn-pulse');
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
    span.textContent = COMPACT ? SCALE[v] : `${v} — ${SCALE[v]}`;
    label.appendChild(input);
    label.appendChild(span);

    if (answers.has(q.id) && answers.get(q.id) === v) {
      input.checked = true;
    }

    input.addEventListener('change', () => {
      answers.set(q.id, v);
      missingIds.delete(q.id);
      updateProgress();
      setTimeout(() => {
        currentIndex += 1;
        renderCurrentQuestion();
        focusCard();
      }, 120);
    });

    scale.appendChild(label);
  }

  questionCard.appendChild(scale);
  backBtn.disabled = currentIndex === 0;
}

async function loadQuestions() {
  const res = await fetch('/api/questions');
  const data = await res.json();
  QUESTIONS = data.questions;
  DOMAINS = data.domains;
  PERSONAS = data.personas;
  currentIndex = 0;
  answers.clear();
  missingIds.clear();
  updateProgress();
  renderCurrentQuestion();
  focusCard();
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

  // Export JSON
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

  resultsEl.scrollIntoView({ behavior: 'smooth', block: 'start' });
}

async function submitQuiz() {
  const payload = [];
  const missing = [];
  for (let i = 0; i < QUESTIONS.length; i++) {
    const q = QUESTIONS[i];
    const v = answers.get(q.id);
    if (!v) {
      missing.push({ index: i, id: q.id });
    } else {
      payload.push({ id: q.id, value: Number(v) });
    }
  }
  if (missing.length) {
    missingIds.clear();
    missing.forEach(m => missingIds.add(m.id));
    const first = missing[0].index;
    currentIndex = first;
    renderCurrentQuestion();
    focusCard();
    const sample = missing.slice(0, 8).map(m => m.index + 1).join(', ');
    const rest = missing.length > 8 ? `, +${missing.length - 8}` : '';
    showToast(`Você deixou ${missing.length} pergunta(s) sem resposta. Indo para a ${first + 1}. Faltantes: ${sample}${rest}`, 'warn');
    return;
  }

  try {
    const res = await fetch('/api/score', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(payload)
    });
    const scored = await res.json();
    questionCard.classList.add('hidden');
    resultsEl.classList.remove('hidden');
    renderResults(scored);
  } catch (e) {
    showToast("Ocorreu um erro ao gerar o resultado.");
    console.error(e);
  }
}

// Navegação: voltar
backBtn.addEventListener('click', () => {
  if (currentIndex > 0) {
    currentIndex -= 1;
    renderCurrentQuestion();
    focusCard();
  }
});

// Navegação: swipe para voltar
let touchStartX = 0, touchStartY = 0;
questionCard.addEventListener('touchstart', (e) => {
  const t = e.touches[0];
  touchStartX = t.clientX;
  touchStartY = t.clientY;
}, { passive: true });

questionCard.addEventListener('touchend', (e) => {
  const t = e.changedTouches[0];
  const dx = t.clientX - touchStartX;
  const dy = Math.abs(t.clientY - touchStartY);
  if (dx > 50 && dy < 40) {
    // swipe direita -> voltar
    if (currentIndex > 0) {
      currentIndex -= 1;
      renderCurrentQuestion();
      focusCard();
    }
  }
}, { passive: true });

loadQuestions();