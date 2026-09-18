function hambugerMenu(document){
    var newElement = document.createElement('p');
    newElement.textContent = 'Hello, World!';
    document.getElementByID('HBButton').appendChild(newElement);
}