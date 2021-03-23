/*Form Image*/
document.getElementById('id_avatar').addEventListener('change', function(){
      if( this.value ){
        document.getElementById('file').click()
      }
});

/*Tabs*/
function openTab(tab, n) {
    const tabcontent = document.querySelectorAll('.tabcontent'),
          tablinks = document.querySelectorAll('.tablinks')

    tabcontent.forEach(item => item.style.display = 'none')
    tablinks.forEach(item => item.classList.remove('active'))


    tabcontent[n].style.display = 'block'
    tab.classList.add('active')
}

const tabInfo = document.querySelector('.tab_info'),
      tabComments = document.querySelector('.tab_comments')

tabInfo.addEventListener('click', () =>{
    openTab(tabInfo, 0)
})

tabComments.addEventListener('click', () =>{
    openTab(tabInfo, 1)
})

document.querySelector('#defaultOpen').click()

/*Form Info*/
const link = document.querySelector('#change_link'),
      formInfo = document.querySelector('#form_info')

link.addEventListener('click', () =>{
    formInfo.style.display = 'block'
    link.style.display = 'none'
})