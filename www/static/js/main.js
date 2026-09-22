console.log("main.js loaded - edit me in www/static/js/main.js");


function searchBar() {
    let searchIcon = document.getElementsByClassName("searchbutton")[0];
    searchIcon.outerHTML = '<input class="searchbar" type="text" placeholder="Search..."></input>';
}

// W3 schools support code adapted to our neccesities on how to work our way through the hamburger menu. 
function dropdownMenu(){
    document.getElementById("myDropdown").classList.toggle("show");
}

window.onclick = function(event){
    if(!event.target.matches('.dropbtn')){
        let dropdowns = this.document.getElementsByClassName("dropdown-content");
        let i;
        for(i = 0; i < dropdowns.length; i++){
            var openDropdown = downdowns[i];
            if(openDropdown.classList.contains('show')){
                openDropdown.classList.remove('show');
            }
        }
    }
}

var acc = document.getElementsByClassName("accordion");
var i;

for (i = 0; i < acc.length; i++) {
  acc[i].addEventListener("click", function() {
    /* Toggle between adding and removing the "active" class,
    to highlight the button that controls the panel */
    this.classList.toggle("active");

    /* Toggle between hiding and showing the active panel */
    var panel = this.nextElementSibling;
    if (panel.style.display === "block") {
      panel.style.display = "none";
    } else {
      panel.style.display = "block";
    }
  });
}