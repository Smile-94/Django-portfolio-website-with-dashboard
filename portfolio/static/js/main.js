
// -------------------------js code for about section-------------
let tabLinks=document.getElementsByClassName('tab-link');
let tabContents=document.getElementsByClassName('tab-content');

function opentab(tabName){
    for(tabLink of tabLinks){
        tabLink.classList.remove('active');
    }
    for(tabContent of tabContents){
        tabContent.classList.remove('active-tab');
    }
    event.currentTarget.classList.add('active')
    document.getElementById(tabName).classList.add('active-tab')
}

// ----------------side menu---------------
let sideMenu=document.getElementById('sideMenu');

function openMenu(){
    sideMenu.style.right="0"
}
function closeMenu(){
    sideMenu.style.right="-200px"
}


