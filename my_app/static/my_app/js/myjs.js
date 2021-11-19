
$(document).ready(function(){
    $(".card-text").each(function(i){
        len=$(this).text().length;
        if(len>60)
        {
          $(this).text($(this).text().substr(0,80)+'...');
        }
      });  
})


