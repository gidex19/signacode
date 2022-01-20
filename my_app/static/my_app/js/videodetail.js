$(document).ready(function(){

    var video = videojs('#videoPlayer');
    console.log(video);
    console.log("it worked");
    forwardBtn = document.getElementById('forwardBtn');
    fastForwardBtn = document.getElementById('fastForwardBtn');
    rewindBtn = document.getElementById('rewindBtn');
    fastRewindBtn = document.getElementById('fastRewindBtn');
    // testBtn = document.getElementById('testBtn');
    playPauseBtn = document.getElementById('playPauseBtn');
    console.log(rewindBtn);
    console.log(forwardBtn);
    // playPauseBtn.addEventListener('click', ()=>{
    //   console.log("play button has just been clicked");
    //   if (video.paused()== true){
    //     video.play();
    //   }
    //   else{
    //     video.pause();
    //   }
    // });
    

    forwardBtn.addEventListener('click', ()=>{

      currentTime = video.currentTime();
      console.log(currentTime);
      currentTime = currentTime + 10;
      console.log(currentTime)
      video.currentTime(currentTime);
      console.log(currentTime)
    });
    fastForwardBtn.addEventListener('click', ()=>{

      currentTime = video.currentTime();
      console.log(currentTime);
      currentTime = currentTime + 30;
      video.currentTime(currentTime);
      });

    rewindBtn.addEventListener('click', ()=>{
      currentTime = video.currentTime();
      console.log(currentTime);
      currentTime = currentTime - 10;
      video.currentTime(currentTime);
    });

    fastRewindBtn.addEventListener('click', ()=>{
      currentTime = video.currentTime();
      console.log(currentTime);
      currentTime = currentTime - 30;
      video.currentTime(currentTime);
    });


})