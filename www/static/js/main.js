console.log("main.js loaded - edit me in www/static/js/main.js");


function searchBar() {
    let searchIcon = document.getElementsByClassName("searchbutton")[0];
    searchIcon.outerHTML = '<input class="searchbar" type="text" placeholder="Search..."></input>';
}

function hambugerMenu(document){
    var newElement = document.createElement('p');
    newElement.textContent = 'Hello, World!';
    document.getElementByID('HBButton').appendChild(newElement);
}

window.onclick = function(event){
    if(!event.target.matches('.dropbtn')){
        var dropdowns = this.document.getElementsByClassName("dropdown-content");
        var i;
        for(i = 0; i < dropdowns.length; i++){
            var openDropdown = downdowns[i];
            if(openDropdown.classList.contains('show')){
                openDropdown.classList.remove('show');
            }
        }
    }
}
