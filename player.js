function PlayThis(Number){
  document.getElementById('playing').innerHTML=document.getElementById(Number).innerHTML
  document.getElementById('playing').value=Number
  var audio="<audio hidden autoplay src=\"audio/"
  audio+=document.getElementById(Number).innerHTML
  audio+=".mp3\"/>"
  document.getElementById('PLAYER').innerHTML=audio
}
function PlayPause(){
  PlayThis(1)
}
function Prev(){
  var pista = document.getElementById('playing').value
  if(pista > 1){
    pista--
    PlayThis(pista)
  }else if(pista==1){
    PlayThis(3)
  }
}
function Next(){
  var pista = document.getElementById('playing').value
  if(pista < 3){
    pista++
    PlayThis(pista)
  }else if(pista==3){
    PlayThis(1)
  }
}
