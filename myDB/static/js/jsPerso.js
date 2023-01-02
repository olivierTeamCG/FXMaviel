

function monScript() {
  var userName = document.querySelector('#user-tools strong').innerHTML;
  console.log(document.querySelectorAll('.export_link')[0]);
  if(userName != "fx" && userName != "admin"){
      try{
      document.querySelectorAll('.import_link')[0].remove();
      document.querySelectorAll('.export_link')[0].remove();
      }catch(e){}
  }
  else{
      try{
          if(userName != "admin"){
              document.querySelectorAll('.import_link')[0].remove();
          }
      }catch(e){

      }
  }

  /*if(document.querySelectorAll('.field-image')[0] && document.querySelectorAll('.field-image_tag')[0]){
    document.querySelectorAll('.field-image')[0].innerHTML += document.querySelectorAll('.field-image_tag')[0].innerHTML;
  document.querySelectorAll('.field-image_tag')[0].innerHTML = "";
  }*/
  if(document.querySelectorAll('.file-upload a')){
    //console.log(document.querySelectorAll('.file-upload a')[0].href);
    document.querySelectorAll('.file-upload a')[0].innerHTML = `<img src='${document.querySelectorAll('.file-upload a')[0].href}'>`;
  }

if(document.querySelector('#id_image')){
  document.querySelector('#id_image').onchange = function (e) {
    console.log(e.target.value);

    var url = e.target.value;
    var ext = url.substring(url.lastIndexOf('.') + 1).toLowerCase();
    if (e.target.files && e.target.files[0]&& (ext == "gif" || ext == "png" || ext == "jpeg" || ext == "jpg")) {
      var reader = new FileReader();

      reader.onload = function (e) {
        //$('#img').attr('src', e.target.result);
        console.log(e.target.result);
        //document.querySelector('#id_image').parentNode.innerHTML += `<img src="${e.target.result}">`;
        //document.querySelector('#renderImg').src = e.target.result;
        document.querySelectorAll('.file-upload a img')[0].src = e.target.result;
      }
      reader.readAsDataURL(e.target.files[0]);
    }


  }





}


function htmlDecode(input){
  var e = document.createElement('div');
  e.innerHTML = input;
  return e.childNodes.length === 0 ? "" : e.childNodes[0].nodeValue;
}

//htmlDecode("&lt;img src='myimage.jpg'&gt;"); 
// returns "<img src='myimage.jpg'>"

document.querySelectorAll('.readonly').forEach( function (item){
  item.innerHTML = htmlDecode(item.innerHTML);
  console.log(item.innerHTML);
})



}

if (document.readyState === 'complete') {
  monScript();
} else {
  document.addEventListener('DOMContentLoaded', function() {
    monScript();
  });
}