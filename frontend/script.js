// ============================
//  GAME STATE & STORAGE
// ============================
const DB_KEY = 'cyberventure_db';
let currentUser = null;

function loadDB() {
  try { return JSON.parse(localStorage.getItem(DB_KEY)) || {}; } catch { return {}; }
}
function saveDB(db) { localStorage.setItem(DB_KEY, JSON.stringify(db)); }
function getUser(username) { return loadDB()[username] || null; }
function setUser(username, data) {
  const db = loadDB();
  db[username] = data;
  saveDB(db);
}
function deleteUser(username) {
  const db = loadDB();
  delete db[username];
  saveDB(db);
}

// ============================
//  SCREENS
// ============================
function showScreen(id) {
  document.querySelectorAll('.screen').forEach(s => s.classList.remove('active'));
  document.getElementById(id).classList.add('active');
}

// ============================
//  AUTH
// ============================
function showLogin() {
  document.getElementById('auth-login').style.display = '';
  document.getElementById('auth-register').style.display = 'none';
  setAuthMsg('');
}
function showRegister() {
  document.getElementById('auth-login').style.display = 'none';
  document.getElementById('auth-register').style.display = '';
  setAuthMsg('');
}
function setAuthMsg(text, type = '') {
  const el = document.getElementById('auth-msg');
  el.innerHTML = text ? `<div class="msg msg-${type}">${text}</div>` : '';
}

function doLogin() {
  const user = document.getElementById('login-user').value.trim();
  const pwd  = document.getElementById('login-pwd').value;
  if (!user || !pwd) return setAuthMsg('Enter username and password.', 'err');
  const data = getUser(user);
  if (!data) return setAuthMsg('Username not found.', 'err');
  if (data.pwd !== pwd) return setAuthMsg('Incorrect password.', 'err');
  currentUser = user;
  goHub();
}

function doRegister() {
  const user = document.getElementById('reg-user').value.trim();
  const pwd  = document.getElementById('reg-pwd').value;
  if (!user || !pwd) return setAuthMsg('Fill in all fields.', 'err');
  if (getUser(user)) return setAuthMsg('Username already taken.', 'err');
  setUser(user, { pwd, lv: 1, subLv: 1, lives: 3 });
  currentUser = user;
  goHub();
}

function doLogout() {
  currentUser = null;
  showScreen('screen-auth');
  showLogin();
}

// ============================
//  HUB
// ============================
const SUB_NAMES = { 1: 'Number Guess', 2: 'Unjumble', 3: 'Game 24', 4: 'Cat Finder' };
const SUB_ICONS = { 1: '🔢', 2: '🔤', 3: '➕', 4: '🐱' };

function goHub() {
  if (!currentUser) return showScreen('screen-auth');
  const u = getUser(currentUser);
  showScreen('screen-hub');
  updateHUD('hud-user', 'hud-level', 'hud-lives', u);
  buildLevelMap(u);
  document.getElementById('hub-notif').textContent =
    (u.lv === 4 && u.subLv === 4) ? 'ALL LEVELS COMPLETE!' :
    `Up next: Level ${u.lv} — ${SUB_NAMES[u.subLv]}`;
}

function updateHUD(userEl, levelEl, livesEl, u) {
  const ue  = document.getElementById(userEl);
  const le  = levelEl ? document.getElementById(levelEl) : null;
  const lve = document.getElementById(livesEl);
  if (ue)  ue.textContent = `USER: ${currentUser.toUpperCase()}`;
  if (le)  le.textContent = `LV ${u.lv} — ${SUB_NAMES[u.subLv]}`;
  if (lve) {
    lve.innerHTML = '';
    for (let i = 1; i <= 3; i++) {
      const span = document.createElement('span');
      span.className = 'heart' + (i > u.lives ? ' lost' : '');
      span.textContent = '❤️';
      lve.appendChild(span);
    }
  }
}

function buildLevelMap(u) {
  const map = document.getElementById('level-map');
  map.innerHTML = '';
  for (let lv = 1; lv <= 4; lv++) {
    for (let sub = 1; sub <= 4; sub++) {
      const isDone    = (lv < u.lv) || (lv === u.lv && sub < u.subLv);
      const isCurrent = (lv === u.lv && sub === u.subLv);
      const node = document.createElement('div');
      node.className = 'level-node' + (isDone ? ' done' : '') + (isCurrent ? ' current' : '');
      node.innerHTML = `
        <span class="node-icon">${isDone ? '✅' : isCurrent ? SUB_ICONS[sub] : '🔒'}</span>
        <span class="node-name">L${lv}-S${sub}</span>
        <span class="node-name" style="margin-top:4px;font-size:0.55rem">${SUB_NAMES[sub]}</span>`;
      map.appendChild(node);
    }
  }
}

function startCurrentLevel() {
  const u = getUser(currentUser);
  if (u.lv === 4 && u.subLv === 4 && isCompleted(u)) {
    showScreen('screen-victory');
    return;
  }
  const diff = u.lv - 1;
  if      (u.subLv === 1) startNumGuess(diff);
  else if (u.subLv === 2) startWord(diff);
  else if (u.subLv === 3) start24();
  else if (u.subLv === 4) startCatFinder(diff);
}

function isCompleted(u) { return u.lv >= 4 && u.subLv >= 4; }

function incrLevel(username) {
  const u = getUser(username);
  if (u.subLv < 4) u.subLv++;
  else if (u.lv < 4) { u.lv++; u.subLv = 1; }
  setUser(username, u);
}

function reduceLife(username) {
  const u = getUser(username);
  u.lives = Math.max(0, u.lives - 1);
  setUser(username, u);
}

function showResult(win, msg, afterFn) {
  showScreen('screen-result');
  const title = document.getElementById('result-title');
  const rmsg  = document.getElementById('result-msg');
  const btns  = document.getElementById('result-btns');
  title.className  = 'big-msg ' + (win ? 'win' : 'lose');
  title.textContent = win ? '✓ SUCCESS' : '✗ FAILED';
  rmsg.textContent  = msg;
  btns.innerHTML    = '';

  if (win) {
    const u = getUser(currentUser);
    if (u && u.lv === 4 && u.subLv === 4) {
      const btn = document.createElement('button');
      btn.className = 'btn btn-accent';
      btn.textContent = '★ Victory Screen';
      btn.onclick = () => showScreen('screen-victory');
      btns.appendChild(btn);
    } else {
      const btn = document.createElement('button');
      btn.className = 'btn btn-accent';
      btn.textContent = '▶ Next Level';
      btn.onclick = () => goHub();
      btns.appendChild(btn);
    }
  } else {
    const u = getUser(currentUser);
    if (!u || u.lives <= 0) {
      if (currentUser) deleteUser(currentUser);
      currentUser = null;
      rmsg.textContent += '\n\nYour account has been deleted.';
      const btn = document.createElement('button');
      btn.className = 'btn btn-danger';
      btn.textContent = 'Start Over';
      btn.onclick = () => { showScreen('screen-auth'); showLogin(); };
      btns.appendChild(btn);
    } else {
      const btn1 = document.createElement('button');
      btn1.className = 'btn';
      btn1.textContent = '↺ Retry';
      btn1.onclick = () => afterFn();
      btns.appendChild(btn1);

      const btn2 = document.createElement('button');
      btn2.className = 'btn';
      btn2.style.cssText = 'border-color:var(--muted);color:var(--muted)';
      btn2.textContent = 'Hub';
      btn2.onclick = () => goHub();
      btns.appendChild(btn2);
    }
  }
}

// ============================
//  GAME 1: NUMBER GUESS
// ============================
let ng = {};

function startNumGuess(diff) {
  const limits = [20, 50, 80, 100];
  const limit  = limits[diff] || 20;
  const rand   = Math.floor(Math.random() * limit) + 1;
  const maxGuesses = Math.floor(Math.sqrt(limit));
  ng = { limit, rand, maxGuesses, guessesLeft: maxGuesses, diff };

  showScreen('screen-numguess');
  const u = getUser(currentUser);
  updateHUD('ng-user', null, 'ng-lives', u);
  document.getElementById('ng-range').textContent = `Guess: 1 – ${limit}`;
  document.getElementById('ng-hint').textContent  = '—';
  document.getElementById('ng-hint').style.color  = 'var(--muted)';
  document.getElementById('ng-guesses').textContent = `Guesses remaining: ${maxGuesses}`;
  document.getElementById('ng-input').value = '';
  document.getElementById('ng-msg').innerHTML = '';
  document.getElementById('ng-instructions').textContent =
    '✨ Very hot (<3) | 🔥 Hot (<5) | 🌡 Warm (<7) | 🧊 Cold (<10) | ❄ Very Cold (10+)';
}

function submitGuess() {
  const val = parseInt(document.getElementById('ng-input').value);
  if (isNaN(val) || val < 1 || val > ng.limit) {
    document.getElementById('ng-msg').innerHTML =
      `<div class="msg msg-err">Enter a number between 1 and ${ng.limit}</div>`;
    return;
  }
  document.getElementById('ng-input').value = '';
  ng.guessesLeft--;

  if (val === ng.rand) {
    incrLevel(currentUser);
    showResult(true,
      `Correct! The number was ${ng.rand}. You cracked it in ${ng.maxGuesses - ng.guessesLeft} guess(es).`,
      () => startNumGuess(ng.diff));
    return;
  }

  const dist = Math.abs(val - ng.rand);
  let hint, color;
  if      (dist < 3)  { hint = '✨ Very Hot';  color = '#ff4444'; }
  else if (dist < 5)  { hint = '🔥 Hot';       color = '#ff8800'; }
  else if (dist < 7)  { hint = '🌡 Warm';      color = '#ffcc00'; }
  else if (dist < 10) { hint = '🧊 Cold';      color = '#44aaff'; }
  else                { hint = '❄ Very Cold';  color = '#aaccff'; }

  const hintEl = document.getElementById('ng-hint');
  hintEl.textContent = hint;
  hintEl.style.color = color;
  document.getElementById('ng-guesses').textContent = `Guesses remaining: ${ng.guessesLeft}`;
  document.getElementById('ng-msg').innerHTML = '';

  if (ng.guessesLeft <= 0) {
    reduceLife(currentUser);
    const u = getUser(currentUser);
    showResult(false,
      `Out of guesses! The number was ${ng.rand}. Lives remaining: ${u.lives}`,
      () => startNumGuess(ng.diff));
  }
}

document.getElementById('ng-input').addEventListener('keydown', e => {
  if (e.key === 'Enter') submitGuess();
});

// ============================
//  GAME 2: WORD UNJUMBLE
// ============================
const WORDS = {
  0: ["able","aged","aide","airy","apex","arch","atom","auto","avid","baby","band","bank","bark","base","bass","bath","bead","beam","bean","bear","beef","bend","best","bike","bill","blog","blue","blur","bold","bolt","book","boot","born","boss","bowl","buff","bulb","bump","busy","cafe","cake","calm","cane","cape","card","care","cart","case","cash","cave","cell","chin","chip","chop","city","claw","clay","clip","club","clue","coal","coat","code","coin","comb","cook","cool","copy","cord","core","corn","crab","crew","crib","crop","crow","cube","curl","dame","damp","dark","dart","dash","dawn","dear","deep","deer","desk","dial","dice","diet","disc","dish","doll","dome","done","door","dove","drop","drum","duck","duct","dusk","each","east","easy","echo","edge","envy","epic","even","exit","fair","fall","fare","farm","fast","fawn","feet","fell","fern","file","film","fine","fire","firm","fish","five","flag","flat","flea","flex","foal","foam","fond","font","food","form","free","fuse","fuss","gale","game","gate","germ","gill","gilt","glad","glue","goal","goat","gold","good","grey","grid","gulf","gull","hair","hale","half","hall","hare","heap","heat","herd","hero","hill","hive","home","hood","hoof","hoop","hour","huge","hunt","idea","inch","iron","item","jail","joke","just","keel","keen","keep","kelp","kerb","king","kite","knee","knot","lace","lamb","lamp","lane","late","lava","lawn","lead","leaf","lean","left","lens","life","limb","line","link","lion","live","load","loaf","loan","loft","logo","lone","long","look","loop","lord","lost","loud","luck","lure","lush","mail","mall","mane","many","mast","maze","meal","meet","menu","mice","mild","mill","mind","mine","mint","mole","mood","moon","moor","more","moss","much","musk","myth","name","nave","navy","near","neat","neck","need","nest","news","next","nice","note","noun","nova","null","numb","odds","once","only","open","oval","over","pace","page","pail","pair","palm","park","part","past","path","peak","pear","peel","pile","pill","pink","pith","pity","plan","plot","plum","plus","poem","poet","pony","pool","pore","port","pram","prey","prim","prow","pure","quay","quiz","raft","rail","rain","rake","ramp","rare","reed","rent","rest","rich","rife","ripe","rise","road","roof","rope","rose","ruby","rule","rung","rust","safe","saga","sage","sail","sake","sale","salt","same","sand","sane","save","scar","seal","seam","shed","ship","shoe","shop","shot","show","side","sign","silk","sink","site","size","skip","slab","slow","snap","snow","sock","sofa","soil","sole","solo","some","song","soup","span","spar","spot","stag","star","stem","such","sure","swan","tale","tall","tame","tank","tape","task","taxi","team","tear","tent","term","test","text","tick","tide","tile","till","time","tiny","toad","tofu","toil","tomb","tour","town","tram","trap","tray","trio","true","tube","tuna","tune","turf","turn","tusk","twig","twin","type","tyre","unit","used","vase","vast","veal","veil","very","vest","view","vote","wail","wall","wand","ward","warm","wary","wasp","wave","week","weir","well","west","whey","wide","wild","will","wind","wing","wipe","wire","wise","wish","wool","worn","wren","yawn","year","yoke","yolk","zany","zing"],
  1: ["actor","acute","adept","agile","album","alert","alike","alive","alone","alpha","amber","ample","angle","apple","apron","arena","arrow","aside","atlas","attic","audio","aunty","avail","awake","award","aware","awash","badge","baggy","balmy","barge","basic","basin","beach","beads","bench","berry","blank","blaze","bling","bliss","block","bloke","blond","blues","board","bonus","booth","bound","bower","brake","brass","brave","break","bride","brief","brisk","broad","broom","brown","bugle","built","bulky","bunch","cabin","cable","canny","canoe","chain","chalk","charm","chart","chess","chest","chief","chill","choir","civic","civil","claim","class","clear","clerk","cliff","cloak","clock","close","cloth","cloud","clove","clump","coach","coast","cocoa","comfy","comic","coral","court","cover","crane","crate","crisp","croak","crowd","crown","crumb","crust","curve","daily","dairy","daisy","dance","delta","denim","diary","digit","diner","disco","ditch","diver","dizzy","dodge","doubt","dozen","draft","drain","drama","dream","dress","drill","drink","drive","drone","dusty","eagle","early","elder","elect","elite","email","envoy","epoch","equal","error","ether","event","every","exact","extra","faint","fancy","feast","fence","ferry","fever","field","fight","final","first","flame","flare","flash","flask","fleet","flesh","float","floor","flora","flour","fluid","flute","force","forge","frame","frank","fraud","fresh","frost","fruit","fully","furry","fuzzy","giant","glade","gland","glare","gloom","gloss","glove","going","grace","grade","grain","grasp","grass","graze","greed","green","greet","grief","groan","group","grove","guard","guest","guide","guild","guilt","handy","happy","harsh","hasty","haven","havoc","heart","heavy","hedge","heist","hence","heron","honey","hotel","hound","human","humor","ideal","image","imply","index","inert","inner","input","intro","irony","ivory","jaunt","jewel","joint","joust","jumpy","karma","kebab","knack","knave","knife","knoll","known","label","lance","lanky","laser","latch","laugh","layer","leech","lemon","level","light","lilac","limit","linen","liner","liver","local","lodge","lofty","logic","loose","lower","lucid","lusty","lyric","magic","major","manor","maple","march","match","maxim","media","mercy","merit","metal","metro","might","mimic","miner","minor","minus","mirth","moist","money","month","moral","motor","motto","mourn","muddy","mural","music","nadir","naive","nasty","night","ninja","noble","noisy","north","novel","nurse","occur","ocean","offer","olive","opera","optic","orbit","order","organ","other","otter","ought","outer","ozone","paint","panic","paper","party","pasta","patch","pause","pearl","pedal","penny","perch","peril","petty","phase","phone","piano","piece","pilot","pinch","place","plain","plane","plant","plaza","plead","pluck","plume","plush","point","polar","pouch","pound","power","press","price","pride","prime","print","prior","prize","probe","prone","proof","prose","prowl","prune","pulse","punch","pupil","purse","queen","query","quest","quill","quite","quota","quote","radar","radio","rainy","rally","raven","reach","ready","realm","rebel","refer","reign","relax","repay","repel","reset","rider","rifle","rigid","risky","rivet","roast","robin","robot","rocky","rough","route","royal","ruddy","ruler","rural","rusty","sadly","saint","sandy","sauce","savvy","scene","scope","score","scout","seedy","sense","serum","setup","seven","sever","shade","shaft","shake","shall","shame","shape","share","shark","sharp","sheen","sheep","shelf","shell","shift","shine","shirt","shock","shore","short","shout","shrub","siege","sight","silly","since","skill","skirt","slant","slash","sleek","sleep","slice","slide","slope","sloth","smack","smart","smash","smear","smell","smirk","smoke","snack","snail","snake","snare","sneak","sniff","snore","snowy","solar","solid","solve","sorry","south","space","spare","spawn","speck","speed","spend","spice","spike","spill","spine","spoke","spore","sport","spout","spray","spree","squad","stain","stale","stall","stare","stark","start","state","steak","steam","steel","steep","steer","stick","stiff","still","sting","stock","stone","storm","story","stove","strap","stray","strip","strut","stuck","study","stump","stunt","style","sugar","suite","sunny","super","surge","swamp","swear","sweat","sweep","sweet","swift","swirl","swoop","sword","table","taboo","talon","tasty","taunt","tense","theme","thick","thing","third","throw","tiger","timid","tired","title","today","token","topic","total","touch","tough","trace","track","trade","trail","train","trait","tramp","trash","trend","trial","trick","trout","trove","truce","truck","truly","trunk","trust","truth","tulip","twice","twine","twist","ultra","under","unite","unity","until","urban","usual","utter","vague","valid","value","valve","vapor","vault","vicar","video","vigor","villa","viola","viral","vivid","vogue","voter","wager","wagon","waste","watch","water","weary","weave","wedge","weigh","weird","whale","wheat","wheel","while","white","whole","wield","windy","witty","woody","world","worry","worse","worst","wrath","wring","write","wrote","yacht","young","youth","zippy"],
  2: ["absent","accept","access","across","action","active","advent","affect","afford","agency","agenda","almost","always","animal","answer","anyone","around","arrive","assert","assign","assist","assume","attach","attend","august","autumn","avenue","behind","belief","belong","beside","better","beyond","border","bottle","bottom","bridge","bright","broken","budget","butter","button","canyon","carbon","castle","cattle","caught","center","change","charge","choice","chosen","circle","coffee","combat","comedy","coming","common","corner","costly","cotton","couple","course","create","credit","crisis","damage","danger","debate","decide","defend","degree","design","desire","detail","device","dinner","direct","divide","dollar","domain","double","dragon","during","easily","effect","effort","either","employ","engage","engine","ensure","entity","escape","estate","evolve","except","expect","expert","factor","family","famous","flower","follow","forbid","forget","formal","fossil","foster","friend","frozen","gather","gender","gentle","global","golden","gravel","ground","growth","happen","hardly","health","height","hidden","honest","humble","hunger","hunter","ignore","impact","inform","insist","invest","island","itself","joyful","jungle","kennel","kettle","kitten","knight","ladder","legend","lesson","letter","little","living","lonely","lovely","loving","manage","manner","marble","market","matter","method","middle","mirror","mobile","modest","moment","monkey","mortal","mother","motion","mutual","nature","nearly","needle","normal","notice","object","obtain","office","option","origin","output","parent","partly","planet","player","plenty","poetry","portal","potato","powder","prefer","pretty","prince","prison","profit","prompt","proper","proven","public","purple","pursue","puzzle","radius","random","reason","record","reduce","reform","relate","remain","remote","remove","repair","repeat","rescue","result","return","review","reward","riding","rising","robust","sample","saying","second","sector","simple","single","sister","social","soften","source","spread","statue","string","strong","stupid","submit","sudden","summit","talent","target","temple","tender","theory","throat","toward","travel","tunnel","unless","unlike","useful","valley","verbal","victim","vision","volume","wasted","winner","winter","wisdom","wonder","worker","yellow","zipper"],
  3: ["abandon","absence","account","achieve","acquire","address","advance","against","already","another","anxiety","anymore","anybody","balance","because","benefit","between","cabinet","capture","careful","century","certain","channel","chapter","clearly","climate","collect","college","combine","command","comment","compare","concern","connect","contain","content","context","control","corrupt","country","culture","curious","current","despite","develop","digital","discuss","distant","diverse","dynamic","educate","emotion","example","examine","explore","express","failure","feeling","feature","finance","foreign","freedom","general","genuine","however","imagine","improve","include","injured","inspire","involve","justify","kingdom","knowing","lacking","library","limited","meaning","meeting","mention","message","mission","mistake","monitor","mystery","network","nothing","obvious","officer","opinion","outside","patient","pattern","perform","perhaps","picture","program","project","protect","provide","publish","quality","quickly","reality","receive","replace","require","resolve","respect","respond","restore","science","segment","serious","similar","society","special","support","surface","survive","teacher","through","totally","trouble","typical","village","violent","visible","western","whether","without","working","worried","younger"]
};

let wd = {};

function startWord(diff) {
  const wordList = WORDS[diff] || WORDS[0];
  const selected = wordList[Math.floor(Math.random() * wordList.length)];
  const jumbled  = shuffleStr(selected);
  wd = { selected, jumbled, diff };

  showScreen('screen-word');
  const u = getUser(currentUser);
  updateHUD('wd-user', null, 'wd-lives', u);
  document.getElementById('wd-jumbled').textContent = jumbled.toUpperCase();
  document.getElementById('wd-hint').textContent    = `${selected.length} letters`;
  document.getElementById('wd-input').value         = '';
  document.getElementById('wd-msg').innerHTML       = '';
}

function shuffleStr(str) {
  let arr = str.split('');
  for (let i = arr.length - 1; i > 0; i--) {
    const j = Math.floor(Math.random() * (i + 1));
    [arr[i], arr[j]] = [arr[j], arr[i]];
  }
  const result = arr.join('');
  return result === str ? shuffleStr(str) : result;
}

function submitWord() {
  const val = document.getElementById('wd-input').value.trim().toLowerCase();
  if (!val) return;
  const sortStr = s => s.split('').sort().join('');
  if (sortStr(val) !== sortStr(wd.selected)) {
    document.getElementById('wd-msg').innerHTML =
      `<div class="msg msg-err">Not a valid anagram of the given letters!</div>`;
    return;
  }
  const wordList = WORDS[wd.diff];
  if (!wordList.includes(val)) {
    document.getElementById('wd-msg').innerHTML =
      `<div class="msg msg-err">"${val}" is not in the word list. Try again!</div>`;
    return;
  }
  incrLevel(currentUser);
  showResult(true, `Correct! The word was "${wd.selected}".`, () => startWord(wd.diff));
}

document.getElementById('wd-input').addEventListener('keydown', e => {
  if (e.key === 'Enter') submitWord();
});

// ============================
//  GAME 3: GAME 24
// ============================
let g24 = {};

function start24() {
  const avail = [1,2,3,4,5,6,7,8,9];
  const choices = [];
  for (let i = 0; i < 4; i++) {
    const idx = Math.floor(Math.random() * avail.length);
    choices.push(avail[idx]);
    avail.splice(idx, 1);
  }
  // Avoid known unsolvable sets
  const s = new Set(choices);
  const eq = (a) => a.every(x => s.has(x)) && s.size === a.length;
  if (eq([1,6,7,8]) || eq([3,4,6,7])) choices.splice(0, 4, 1, 2, 3, 4);
  g24 = { choices, usedNums: [], diff: getUser(currentUser).lv - 1 };

  showScreen('screen-24');
  const u = getUser(currentUser);
  updateHUD('g24-user', null, 'g24-lives', u);
  document.getElementById('g24-formula').value = '';
  document.getElementById('g24-msg').innerHTML  = '';
  renderG24Nums();
}

function renderG24Nums() {
  const numsEl = document.getElementById('g24-nums');
  numsEl.innerHTML = '';
  g24.choices.forEach(n => {
    const chip = document.createElement('div');
    chip.className   = 'num-chip';
    chip.textContent = n;
    numsEl.appendChild(chip);
  });

  const btnsEl = document.getElementById('g24-num-btns');
  btnsEl.innerHTML = '';
  g24.choices.forEach((n, i) => {
    const btn = document.createElement('button');
    btn.className   = 'op-btn num-op' + (g24.usedNums.includes(i) ? ' used' : '');
    btn.textContent = n;
    btn.id          = `nbtn${i}`;
    btn.onclick     = () => useNum(n, i, btn);
    btnsEl.appendChild(btn);
  });
}

function useNum(n, idx, btn) {
  if (g24.usedNums.includes(idx)) return;
  g24.usedNums.push(idx);
  btn.classList.add('used');
  document.getElementById('g24-formula').value += n;
}

function addToFormula(op) {
  const opMap = { '×': '*', '÷': '/' };
  document.getElementById('g24-formula').value += opMap[op] || op;
}

function clearFormula() {
  g24.usedNums = [];
  document.getElementById('g24-formula').value = '';
  renderG24Nums();
}

function backspaceFormula() {
  const f    = document.getElementById('g24-formula');
  const last = f.value[f.value.length - 1];
  const num  = parseInt(last);
  if (!isNaN(num)) {
    for (let i = g24.usedNums.length - 1; i >= 0; i--) {
      const idx = g24.usedNums[i];
      if (g24.choices[idx] === num) {
        g24.usedNums.splice(i, 1);
        document.getElementById(`nbtn${idx}`)?.classList.remove('used');
        break;
      }
    }
  }
  f.value = f.value.slice(0, -1);
}

function submit24() {
  const formula = document.getElementById('g24-formula').value.trim();
  if (!formula) return;

  if (!/^[0-9+\-*/() ]+$/.test(formula)) {
    document.getElementById('g24-msg').innerHTML =
      `<div class="msg msg-err">Only use numbers and +, -, *, /, ()</div>`;
    return;
  }

  const usedDigits = formula.replace(/[^0-9]/g, '').split('').map(Number);
  const sortArr    = a => [...a].sort((a, b) => a - b);
  if (sortArr(usedDigits).join() !== sortArr(g24.choices).join()) {
    document.getElementById('g24-msg').innerHTML =
      `<div class="msg msg-err">Use all 4 numbers exactly once!</div>`;
    return;
  }

  let result;
  try { result = eval(formula); }
  catch {
    document.getElementById('g24-msg').innerHTML =
      `<div class="msg msg-err">Invalid expression!</div>`;
    return;
  }

  if (Math.round(result) === 24) {
    incrLevel(currentUser);
    showResult(true, `${formula} = 24. Excellent!`, start24);
  } else {
    reduceLife(currentUser);
    const u = getUser(currentUser);
    showResult(false, `${formula} = ${result}, not 24. Lives left: ${u.lives}`, start24);
  }
}

// ============================
//  GAME 4: CAT FINDER
// ============================
let cf = {};

function startCatFinder(diff) {
  const sizes  = [3, 4, 5, 6];
  const size   = sizes[diff] || 3;
  const total  = size * size;
  const numCats = Math.floor(Math.random() * Math.floor(total / 2)) + 1;
  const avail  = Array.from({ length: total }, (_, i) => i + 1);
  const catCards = [];
  for (let i = 0; i < numCats; i++) {
    const idx = Math.floor(Math.random() * avail.length);
    catCards.push(avail[idx]);
    avail.splice(idx, 1);
  }
  cf = { size, total, catCards, foundCats: [], diff };

  showScreen('screen-cats');
  const u = getUser(currentUser);
  updateHUD('cf-user', null, 'cf-lives', u);
  document.getElementById('cf-memorize-phase').style.display = '';
  document.getElementById('cf-guess-phase').style.display    = 'none';
  document.getElementById('cf-msg').innerHTML = '';
  renderCatGridMem();
  startMemorizeTimer(size * 2);
}

function renderCatGridMem() {
  const grid = document.getElementById('cf-grid-mem');
  grid.style.gridTemplateColumns = `repeat(${cf.size}, 52px)`;
  grid.innerHTML = '';
  for (let card = 1; card <= cf.total; card++) {
    const cell = document.createElement('div');
    cell.className   = 'cat-cell cat-show';
    cell.textContent = cf.catCards.includes(card) ? '🐱' : '';
    if (!cf.catCards.includes(card)) cell.style.background = 'rgba(0,0,0,0.4)';
    grid.appendChild(cell);
  }
}

function startMemorizeTimer(seconds) {
  let t = seconds;
  const bar       = document.getElementById('cf-bar');
  const timerText = document.getElementById('cf-timer-text');
  bar.style.width = '100%';
  timerText.textContent = `${t}s remaining`;

  const interval = setInterval(() => {
    t--;
    bar.style.width       = `${(t / seconds) * 100}%`;
    timerText.textContent = `${t}s remaining`;
    if (t <= 0) {
      clearInterval(interval);
      startCountdown(3, () => {
        document.getElementById('cf-memorize-phase').style.display = 'none';
        document.getElementById('cf-guess-phase').style.display    = '';
        renderCatGridGuess();
      });
    }
  }, 1000);
}

function startCountdown(n, cb) {
  const overlay = document.getElementById('countdown-overlay');
  const numEl   = document.getElementById('countdown-num');
  overlay.classList.add('show');
  let t = n;
  function tick() {
    numEl.textContent = t;
    if (t <= 0) { overlay.classList.remove('show'); cb(); return; }
    t--;
    setTimeout(tick, 1000);
  }
  tick();
}

function renderCatGridGuess() {
  const grid = document.getElementById('cf-grid-guess');
  grid.style.gridTemplateColumns = `repeat(${cf.size}, 52px)`;
  grid.innerHTML = '';
  updateCatProgress();
  for (let card = 1; card <= cf.total; card++) {
    const cell = document.createElement('div');
    cell.className = 'cat-cell';
    if (cf.foundCats.includes(card)) {
      cell.classList.add('correct');
      cell.textContent = '✅';
    } else {
      cell.textContent = card;
    }
    cell.dataset.card = card;
    cell.addEventListener('click', () => selectCatCard(card, cell));
    grid.appendChild(cell);
  }
}

function selectCatCard(card, cell) {
  if (cf.foundCats.includes(card)) return;
  if (cf.catCards.includes(card)) {
    cf.foundCats.push(card);
    cell.classList.add('correct');
    cell.textContent = '✅';
    updateCatProgress();
    if (cf.foundCats.length === cf.catCards.length) {
      incrLevel(currentUser);
      showResult(true,
        `You found all ${cf.catCards.length} cat(s)! Purrfect!`,
        () => startCatFinder(cf.diff));
    }
  } else {
    cell.classList.add('wrong');
    cell.textContent = '❌';
    document.getElementById('cf-msg').innerHTML =
      `<div class="msg msg-err">Wrong card! No cat here.</div>`;
    reduceLife(currentUser);
    const u = getUser(currentUser);
    setTimeout(() => {
      showResult(false,
        `That card had no cat. Lives remaining: ${u.lives}`,
        () => startCatFinder(cf.diff));
    }, 800);
  }
}

function updateCatProgress() {
  document.getElementById('cf-progress').textContent =
    `Found: ${cf.foundCats.length} / ${cf.catCards.length} cats`;
}

// ============================
//  INIT
// ============================
setTimeout(() => showScreen('screen-auth'), 2000);

document.getElementById('login-pwd').addEventListener('keydown', e => {
  if (e.key === 'Enter') doLogin();
});
document.getElementById('reg-pwd').addEventListener('keydown', e => {
  if (e.key === 'Enter') doRegister();
});
