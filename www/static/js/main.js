console.log("main.js loaded - edit me in www/static/js/main.js");


// toggle light vs dark mode
function switchBgMode() {

}


// activate search function
function searchBar() {
    let searchIcon = document.getElementsByClassName("searchbutton")[0];
    searchIcon.outerHTML = '<input class="searchbar" type="text" placeholder="Search..."></input>';
}


// W3 schools support code adapted to our neccesities on how to work our way through the hamburger menu. 
function dropdownMenu() {
    document.getElementById("myDropdown").classList.toggle("show");
}

window.onclick = function(event) {
    if (!event.target.matches('.dropbtn')) {
        let dropdowns = document.getElementsByClassName("dropdown-content");
        for (let i = 0; i < dropdowns.length; i++) {
            var openDropdown = dropdowns[i];
            if (openDropdown.classList.contains('show')) {
                openDropdown.classList.remove('show');
            }
        }
    }
}



// W3 Schools also provided the implementation for this.
// Claude helped us to add the first line of code 
//"When this specific event happens on this object, run this function." 
document.addEventListener("DOMContentLoaded", function () {
  var acc = document.getElementsByClassName("accordion");

  for (var i = 0; i < acc.length; i++) {
    acc[i].addEventListener("click", function () {
      this.classList.toggle("active");

      var panel = this.nextElementSibling;
      if (panel.style.maxHeight) {
        panel.style.maxHeight = null;
      } else {
        panel.style.maxHeight = panel.scrollHeight + "px";
      }
    });
  }
});