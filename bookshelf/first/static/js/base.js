let drop = document.getElementById('dropdown');
let content = document.getElementById('dropdown-content');
let angle = document.getElementsByClassName('fa-angle-down')[0];

if (drop){
    drop.addEventListener("click", function () {
    content.classList.toggle('active');
    angle.classList.toggle('anim');
})
}
