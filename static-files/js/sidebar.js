let background = document.getElementById('background');
let sidebar = document.getElementById('sidebar');
let openHamburgerMenu = document.getElementById('openHamburgerMenu');
let closeHamburgerMenu = document.getElementById('closeHamburgerMenu');


openHamburgerMenu.onclick = () => {
   background.style.display = 'block';
   sidebar.style.display = 'block';
};

closeHamburgerMenu.onclick = () => {
   sidebar.style.display = 'none';
   background.style.display = 'none';
};
