$(document).ready(function(){
  $("label.l-for-open-menu-btn").click(function(){
    $("label.l-for-open-menu-btn").css({
        'display': 'none',
        'opacity': '0',
        'transition': 'opacity 0.5s linear',
        'z-index': '0',
    });
      
    $("label.l-for-close-menu-btn").css({
        'display': 'flex',
        'opacity': '1',
        'transition': 'opacity 0.5s linear',
        'z-index': '1',
    });
  });
    
  $("label.l-for-close-menu-btn").click(function(){
    $("label.l-for-close-menu-btn").css({
        'display': 'none',
        'opacity': '0',
        'transition': 'opacity 0.5s linear',
        'z-index': '0',
    });
      
    $("label.l-for-open-menu-btn").css({
        'display': 'flex',
        'opacity': '1',
        'transition': 'opacity 0.5s linear',
        'z-index': '1',
    });
  });
    
  
    
  $("#radiobtn1").click(function(){
    $("div.row-for-main-navigation").css({
        'transform': 'translateX(0)',
        'transition': 'transform 0.5s linear',
    });
  });
    
  $("#radiobtn2").click(function(){
    $("div.row-for-main-navigation").css({
        'transform': 'translateX(100%)',
        'transition': 'transform 0.45s linear',
    });
  });
});