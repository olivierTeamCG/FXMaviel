function monScript() {
    var userName = document.querySelector('#user-tools strong').innerHTML;
    console.log(document.querySelectorAll('.export_link')[0]);
    if(userName != "fx" && userName != "admin"){
        document.querySelectorAll('.import_link')[0].remove();
        document.querySelectorAll('.export_link')[0].remove();
    }
    else{
        if(userName != "admin"){
            document.querySelectorAll('.import_link')[0].remove();
        }
    }

    alert("coucou");
    if(document.querySelectorAll('.field-image_tag')){
      document.querySelectorAll('.field-image')[0].innerHTML += document.querySelectorAll('.field-image_tag')[0].innerHTML;
    }


  }
  
  if (document.readyState === 'complete') {
    monScript();
  } else {
    document.addEventListener('DOMContentLoaded', function() {
      monScript();
    });
  }