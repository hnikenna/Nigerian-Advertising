var myVar;
document.addEventListener('DOMContentLoaded', function() {
    document.getElementById('adblock-warning').style.display = "none";
});

function loader() {
//    console.log('PathName:', window.location.pathname)
    if(window.location.pathname === '/') {

//        myVar = setTimeout(showPage, 2000);
        showPage()

    }else{

        showPage()

    }
}

function showPage() {
  document.getElementById("loader").style.display = "none";
  document.getElementById("body").style.display = "block";
}
