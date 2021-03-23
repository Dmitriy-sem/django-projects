const slides = document.querySelectorAll(".slider__item"),
      lines = document.querySelectorAll(".slider-lines_item"),
      next = document.querySelector('.arrow2'),
      prev = document.querySelector('.arrow1'),
      wrap = document.querySelector('.slider'),
	  slidesField = document.querySelector('.slider__items'),
	  width = window.getComputedStyle(wrap).width


let slideIndex = 1,
 	offset = 0

slidesField.style.width = 100 * slides.length + '%'
slides.forEach((slide) =>{
	slide.style.width = width
})

function changeLine() {
    if (slideIndex < 1){
        slideIndex = slides.length
    }

    if (slideIndex > slides.length){
        slideIndex = 1
    }
     lines.forEach((item) => {
        item.classList.remove("active_line")
    })

    lines[slideIndex-1].classList.add('active_line')
}

function minusSlide() {
    let localWidth = +width.slice(0, width.length - 2)
	if (offset === 0){
	    slidesField.style.transition = 'transform 0.35s ease'
		offset = localWidth * (slides.length - 1)
	} else {
	    slidesField.style.transition = 'transform 0.6s ease'
		offset -= localWidth
	}

	slidesField.style.transform = `translateX(-${offset}px)`
    slideIndex--
    changeLine()
}

function plusSlide(){
    let localWidth = +width.slice(0, width.length - 2)
	if (offset === localWidth * (slides.length - 1)){
	    slidesField.style.transition = 'transform 0.2s ease'
		offset = 0
	} else {
	    slidesField.style.transition = 'transform 0.6s ease'
		offset += localWidth
	}
	slidesField.style.transform = `translateX(-${offset}px)`
    slideIndex++
    changeLine()

}
changeLine()

/*Accord menu*/
$(function() {
  let Accordion = function(el, multiple) {
    this.el = el || {};
    // more then one submenu open?
    this.multiple = multiple || false;

    let dropdownlink = this.el.find('.dropdownlink');
    dropdownlink.on('click',
                    { el: this.el, multiple: this.multiple },
                    this.dropdown);
  };

  Accordion.prototype.dropdown = function(e) {
    let $el = e.data.el,
        $this = $(this),
        //this is the ul.submenuItems
        $next = $this.next();

    $next.slideToggle();
    $this.parent().toggleClass('open');

    if(!e.data.multiple) {
      //show only one menu at the same time
      $el.find('.submenuItems').not($next).slideUp().parent().removeClass('open');
    }
  }

  let accordion = new Accordion($('.accordion-menu'), false);
})