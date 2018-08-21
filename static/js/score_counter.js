

 var timeleft = 10;
var scoreCounter = setInterval(function(){
   timeleft --;
  if(timeleft >= 0){
    document.getElementById("progressBar").value = timeleft;
    document.getElementById("score_getter").value = timeleft;
    document.getElementById("countdown").innerHTML = timeleft;
  }
  if(timeleft < 0)
    clearInterval(scoreCounter);
},1000);

