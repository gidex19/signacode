
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
  let darkMode = localStorage.getItem('darkMode');
  console.log(darkMode);
  const enableDarkMode = () => {
    $(".img-one").hide();
    $(".img-two").show();
    document.body.classList.add("dark-theme");
    localStorage.setItem('darkMode', 'enabled');

  };

  const disableDarkMode = () => {
    $(".img-two").hide();
    $(".img-one").show();
    document.body.classList.remove("dark-theme");
    localStorage.setItem('darkMode', null);
  };

  if (darkMode === "enabled"){
    enableDarkMode();
  }
  else{
    disableDarkMode();
  }


    

      darkModeToggle.addEventListener('click', () => {
        // $(".img-two").hide();
        // $(".img-one").show();
        // enableDarkMode();
        console.log(darkMode);
        darkMode = localStorage.getItem('darkMode');
        if (darkMode !== "enabled"){
          enableDarkMode();
          // console.log("yes darkmode worked");
        }
        else{
          disableDarkMode();
          // console.log("not working")
        }
        // document.body.classList.toggle('dark-theme');
        // console.log("its working");
      });  
        
})


