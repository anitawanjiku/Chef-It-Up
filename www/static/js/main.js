console.log("main.js loaded - edit me in www/static/js/main.js");


//-------------------------------------------------------------------------------------------------------------
// JSON + AJAX to display backend ingredient of week
/* Followed the MDN doc getData function */
async function getData() {
  const url = "/initial_route";
  try {
    const response = await fetch(url);
    if (!response.ok) {
      throw new Error(`Response status: ${response.status}`);
    }
    const ingredient = await response.text() // Read the response body
    document.querySelector(".ingredient").textContent = ingredient; // Update the DOM

  } catch (error) {
    console.error("Failed to fetch ingredient:", error);
  }
}

getData()


//-------------------------------------------------------------------------------------------------------------------------
// toggle light vs dark mode
function applyTheme(theme) {
  document.body.className = theme + "-mode";

  // keep the switch in sync (checked = dark)
  var box = document.getElementById("switch");
  if (box) box.checked = (theme === "dark");
}

function switchBgMode() {
  var next = document.body.classList.contains("dark-mode") ? "light" : "dark";
  applyTheme(next);
  try { localStorage.setItem("theme", next); } catch (e) {}
}

// On every page load, restore the saved theme
document.addEventListener("DOMContentLoaded", function () {
  var saved = null;
  try { saved = localStorage.getItem("theme"); } catch (e) {}
  applyTheme(saved || "light");
});


//--------------------------------------------------------------------------------------------------------------------------
// activate search function
document.addEventListener('DOMContentLoaded', () => {
  const search = document.querySelector('.search');
  const searchInput = search.querySelector('.searchbar');

  // open
  search.querySelector('.searchbutton').addEventListener('click', () => {
      search.classList.add('open');
      searchInput.focus();
  });

  // close when clicking outside
  document.addEventListener('click', (e) => {
    if (!search.contains(e.target) && !searchInput.value) {
          search.classList.remove('open');
      }
  });

  // Escape closes it
  document.addEventListener('keydown', (e) => {
      if (e.key === 'Escape') search.classList.remove('open');
  });
});


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
