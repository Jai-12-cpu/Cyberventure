const DB_KEY = "cyberventure_db";
let currentUser = null;

// ---------------- STORAGE ----------------
function loadDB(){
  return JSON.parse(localStorage.getItem(DB_KEY)) || {};
}
function saveDB(db){
  localStorage.setItem(DB_KEY, JSON.stringify(db));
}
function setUser(u,data){
  const db = loadDB();
  db[u]=data;
  saveDB(db);
}
function getUser(u){
  return loadDB()[u];
}

// ---------------- SCREEN ----------------
function showScreen(id){
  document.querySelectorAll(".screen").forEach(s=>s.classList.remove("active"));
  document.getElementById(id).classList.add("active");
}

// ---------------- AUTH ----------------
function showLogin(){
  document.getElementById("auth-login").style.display="";
  document.getElementById("auth-register").style.display="none";
}

function showRegister(){
  document.getElementById("auth-login").style.display="none";
  document.getElementById("auth-register").style.display="";
}

function doRegister(){
  const u=document.getElementById("reg-user").value;
  const p=document.getElementById("reg-pwd").value;
  setUser(u,{pwd:p,lv:1});
  currentUser=u;
  goHub();
}

function doLogin(){
  const u=document.getElementById("login-user").value;
  const p=document.getElementById("login-pwd").value;
  const data=getUser(u);

  if(!data || data.pwd!==p){
    alert("wrong login");
    return;
  }
  currentUser=u;
  goHub();
}

function doLogout(){
  currentUser=null;
  showScreen("screen-auth");
}

// ---------------- HUB ----------------
function goHub(){
  showScreen("screen-hub");
  document.getElementById("hud-user").innerText="USER: "+currentUser;
  document.getElementById("hud-level").innerText="LEVEL 1";
}

function startCurrentLevel(){
  alert("Game starts here (your logic already exists)");
}

// ---------------- INIT ----------------
setTimeout(()=>{
  showScreen("screen-auth");
},1500);
