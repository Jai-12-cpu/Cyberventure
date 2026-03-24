// --- STATE MANAGEMENT ---
const DB_KEY = 'cyberventure_db';
let currentUser = null;

function loadDB() { return JSON.parse(localStorage.getItem(DB_KEY)) || {}; }
function saveDB(db) { localStorage.setItem(DB_KEY, JSON.stringify(db)); }
function getUser(username) { return loadDB()[username] || null; }

// --- NAVIGATION ---
function showScreen(id) {
  document.querySelectorAll('.screen').forEach(s => s.classList.remove('active'));
  document.getElementById(id).classList.add('active');
}

// --- AUTHENTICATION ---
function doLogin() {
  const user = document.getElementById('login-user').value.trim();
  const data = getUser(user);
  if (data && data.pwd === document.getElementById('login-pwd').value) {
    currentUser = user;
    goHub();
  }
}

// --- HUB & PROGRESSION ---
function goHub() {
  const u = getUser(currentUser);
  showScreen('screen-hub');
  // Logic to update HUD and Level Map
}

function incrLevel(username) {
  const u = getUser(username);
  if (u.subLv < 4) u.subLv++;
  else if (u.lv < 4) { u.lv++; u.subLv = 1; }
  saveDB({ ...loadDB(), [username]: u });
}

// --- MINI GAMES ---

// 1. Number Guess
function startNumGuess(diff) {
  // Logic for random number selection based on difficulty
}

// 2. Word Unjumble
function startWord(diff) {
  // Uses the WORDS object to pick a word and shuffle it
}

// 3. Game 24
function submit24() {
  const formula = document.getElementById('g24-formula').value;
  try {
    if (eval(formula) === 24) { /* Win */ }
  } catch (e) { /* Error */ }
}

// 4. Cat Finder
function startCatFinder(diff) {
  // Logic for grid generation and cat placement
}

// Initialize
setTimeout(() => showScreen('screen-auth'), 2000);
