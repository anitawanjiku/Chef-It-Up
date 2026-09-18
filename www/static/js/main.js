console.log("main.js loaded - edit me in www/static/js/main.js");





function searchBar() {
    let searchIcon = document.getElementsByClassName("searchbutton")[0]
    searchIcon.outerHTML = '<input class="searchbar" type="text" placeholder="Search..."></input>'
}