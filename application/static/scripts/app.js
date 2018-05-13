function addElementlog () {
  var newDiv = document.createElement("div"); 
  newDiv.innerHTML +='<div id="popup"><div><form action = "/login" method = "post"><h1>Login</h1><label>Username</label><br><input type="text" name="notendanafn"><br><label>Password</label><br><input type="password" name="lykilord"><br></form></div><div><input type="submit" value="Login"/></div><div><p id="close" onClick="closePopup()">CLOSE</p</div>';   
  var currentDiv = document.getElementById("main_container"); 
  document.body.insertBefore(newDiv, currentDiv); 
}

function addElementsign () {
  var newDiv = document.createElement("div"); 
  newDiv.innerHTML +='<div id="popup"><div><form><h1>Signup</h1><div><label>Username</label><br><input type="text" name="notendanafn"></div><br><div><label>Password</label><br><input type="password" name="lykilord"></div><br><div><label>Confirm password</label><br><input type="password" name="lykilord"></div></form><div id="close" onClick="closePopup()"><strong>Signup</strong></div></div><div><p id="close" onClick="closePopup()">CLOSE</p</div>';   
  var currentDiv = document.getElementById("main_container"); 
  document.body.insertBefore(newDiv, currentDiv); 
}

function uppl(){
	document.getElementById("user").innerHTML +='<div id="lo" >Login</div>';
	document.getElementById("user").innerHTML +='<div id="si">Signup</div>';
};

uppl();

document.body.style.background = '#353333';

var si = document.getElementById("si");
var lo = document.getElementById("lo");
var co = document.getElementById("close");


si.onclick = function(){
  addElementsign();
  openPopup();
}

lo.onclick = function(){
  addElementlog();
  openPopup();
}

function openPopup() {
  var el = document.getElementById('popup');
  el.style.display = 'block';
}

function closePopup() {
  var el = document.getElementById('popup');
  var del = document.getElementById("popup"); 
  del.remove()
  el.style.display = 'none';
}
