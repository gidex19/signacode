
$(document).ready(function(){
    // $(".img-one").hide();
    $(".card-text").each(function(i){
      len=$(this).text().length;
      if(len>60)
      {
        $(this).text($(this).text().substr(0,80)+'...');
      }
    });  
    
    const darkModeToggle = document.querySelector('input');
    let lightMode = localStorage.getItem('lightMode');
    console.log(lightMode);
    const enableLightMode = () => {
      $(".img-two").hide();
      $(".img-one").show();
      document.body.classList.add("light-theme");
      lightMode = 'enabled';
      localStorage.setItem('lightMode', 'enabled');
  
    };
  
    const disableLightMode = () => {
      $(".img-one").hide();
      $(".img-two").show();
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
            console.log(lightMode);
            // console.log("yes darkmode worked");
          }
          else{
            disableLightMode();
            console.log(lightMode);
            // console.log("not working")
          }
          // document.body.classList.toggle('dark-theme');
          // console.log("its working");
        });  
          
  })
  
  
  