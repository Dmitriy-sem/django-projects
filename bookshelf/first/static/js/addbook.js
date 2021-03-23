const elem = document.querySelector('.image-input'),
      image = document.querySelector('.image-book'),
      sign = document.querySelector('.add_image')
elem.addEventListener('change', () =>{
    image.src = image.src.replace('book_template', 'white_book')
    sign.innerHTML = 'Выбрать другую картинку'
})
