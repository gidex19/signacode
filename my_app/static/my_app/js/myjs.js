
$(document).ready(function(){
  // $(".img-one").hide();
  $(".card-text").each(function(i){
    len=$(this).text().length;
    if(len>60)
    {
      $(this).text($(this).text().substr(0,80)+'...');
    }
  });  


//   $('#autoWidth').lightSlider({
//     autoWidth:true,
//     loop:true,
//     onSliderLoad: function() {
//         $('#autoWidth').removeClass('cS-hidden');
//     } 
// });  
  
  

  const darkModeToggle = document.querySelector('input');
  let lightMode = localStorage.getItem('lightMode');
  // console.log(lightMode);
  const enableLightMode = () => {
    $(".img-two").hide();
    $(".img-one").show();
    $(".logo2").hide();
    $(".logo").show();
    $(".collage-grid-dark").hide();
    $(".collage-grid-light").show();

    document.body.classList.add("light-theme");
    lightMode = 'enabled';
    localStorage.setItem('lightMode', 'enabled');

  };

  const disableLightMode = () => {
    $(".img-one").hide();
    $(".img-two").show();
    $(".logo").hide();
    $(".logo2").show();
    $(".collage-grid-dark").show();
    $(".collage-grid-light").hide();
    document.body.classList.remove("light-theme");
    lightMode = null;
    localStorage.setItem('lightMode', null);
  };

  if (lightMode === "enabled"){
    enableLightMode();
  }
  else{
    disableLightMode();
  }


    

      darkModeToggle.addEventListener('click', () => {
        // $(".img-two").hide();
        // $(".img-one").show();
        // enableDarkMode();
        
        lightMode = localStorage.getItem('lightMode');
        if (lightMode !== "enabled"){
          enableLightMode();
          // console.log(lightMode);
          // console.log("yes darkmode worked");
        }
        else{
          disableLightMode();
          // console.log(lightMode);
          // console.log("not working")
        }
        // document.body.classList.toggle('dark-theme');
        // console.log("its working");
      });
      
      // code for the video player starts here

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




      // code for video player ends here
        
})


