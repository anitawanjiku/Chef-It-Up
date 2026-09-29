console.log("main.js loaded - edit me in www/static/js/main.js");

/*async function getData() {
  const url ="/initial_route"
  try {
    const response = await fetch(url);
    if (!response.ok) {
      throw new Error(`Response status: ${response.status}`);
  }
  needs a catch
}
} */


// toggle light vs dark mode
function switchBgMode() {
  let bodyColor = document.querySelector("body");
  if (bodyColor.className === "light-mode") {
    bodyColor.className = "dark-mode";
    img => img.src = "static/img/darkremylogo";
  }
  else {bodyColor.className = "light-mode"};
  img => img.src = "static/img/lightremylogo.png";
}

//--------------------------------------------------------------------------------------------------------------------------
// activate search function
function searchBar() {
    let searchIcon = document.getElementsByClassName("searchbutton")[0];
    searchIcon.outerHTML = '<input class="searchbar" type="text" placeholder="Search..."></input>';
}

//--------------------------------------------------------------------------------------------------------------------------
// This is for the hamburguer menu in the navigation bar. The dropdown would help us get into any part of the webpage. 
// W3 schools support code adapted to our neccesities on how to work our way through the hamburger menu. 
function dropdownMenu(x) {
    document.getElementById("myDropdown").classList.toggle("show");
    x.classList.toggle("change");
}

window.onclick = function(event) {
    if (!event.target.matches('.dropbtn')) {
        let dropdowns = document.getElementsByClassName("dropdown-content");
        for (let i = 0; i < dropdowns.length; i++) {
            var openDropdown = downdowns[i];
            if (openDropdown.classList.contains('show')) {
                openDropdown.classList.remove('show');
            }
        }
    }
}

//--------------------------------------------------------------------------------------------------------------------------
// W3 Schools also provided the implementation for this. This is for the accordion, the accordion in the about section, which 
// would help us 
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

//--------------------------------------------------------------------------------------------------------------------------
//function myFunction(x) {
  //x.classList.toggle("change");
//}