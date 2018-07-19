var timeleft = 11;
var scoreCounter = setInterval(function(){
   timeleft --;
  if(timeleft >= 0){
    document.getElementById("progressBar").value = timeleft;
    document.getElementById("countdown").value = timeleft;
  }
  if(timeleft < 0)
    clearInterval(downloadTimer);
},1000);


function get_my_points(){
    {{ score }}
  document.getElementById("score").innerHTML = timeleft;
   clearTimeout(scoreCounter);
   document.getElementById("info").style.display = "inline";
}