const slideList = document.querySelector('.slide_list');  // Slide parent dom
const slideContents = document.querySelectorAll('.slide_content');  // each slide dom
const slideBtnNext = document.querySelector('.slide_btn_next'); // next button
const slideBtnPrev = document.querySelector('.slide_btn_prev'); // prev button
const pagination = document.querySelector('.slide_pagination');
const slideLen = slideContents.length;  // slide length
const slideWidth = 1000; // slide width
const slideSpeed = 300; // slide speed
const startNum = 0; // initial slide index (0 ~ 4)
const star = document.querySelectorAll('.star'); // each star dom
const slideBox = document.querySelector('.slide_box'); // Slide Box
const navbarHeight = document.querySelector(".navbar").offsetHeight; // navbar height
const slidesHeight = document.querySelector(".slide01").offsetHeight * 4; // slides height sum
const searchLocation = document.querySelector("#search").offsetTop; // Search location
const searchMove = document.querySelector("#move1"); // fitSearch location button
const fitLocation = document.querySelector("#fitSearch").offsetTop; // fitSearch location
const fitMove = document.querySelector("#move2"); // fitSearch location button

slideList.style.width = slideWidth * (slideLen + 2) + "px";

// Copy first and last slide
let firstChild = slideList.firstElementChild;
let lastChild = slideList.lastElementChild;
let clonedFirst = firstChild.cloneNode(true);
let clonedLast = lastChild.cloneNode(true);
    
// Add copied Slides
slideList.appendChild(clonedFirst);
slideList.insertBefore(clonedLast, slideList.firstElementChild);
    
// Add pagination dynamically
let pageChild = '';
for (var i = 0; i < slideLen; i++) {
    pageChild += '<li class="dot';
    pageChild += (i === startNum) ? ' dot_active' : '';
    pageChild += '" data-index="' + i + '"><a href="#"></a></li>';
}
pagination.innerHTML = pageChild;
const pageDots = document.querySelectorAll('.dot'); // each dot from pagination
    
slideList.style.transform = "translate3d(-" + (slideWidth * (startNum + 1)) + "px, 0px, 0px)";
    
let curIndex = startNum; // current slide index (except copied slide)
let curSlide = slideContents[curIndex]; // current slide dom
curSlide.classList.add('slide_active');
    
/** Next Button Event */
function nextPageDo() {
    if (curIndex <= slideLen - 1) {
        slideList.style.transition = slideSpeed + "ms";
        slideList.style.transform = "translate3d(-" + (slideWidth * (curIndex + 2)) + "px, 0px, 0px)";
    }
    if (curIndex === slideLen - 1) {
        setTimeout(function() {
            slideList.style.transition = "0ms";
            slideList.style.transform = "translate3d(-" + slideWidth + "px, 0px, 0px)";
        }, slideSpeed);
        curIndex = -1;
    }
    curSlide.classList.remove('slide_active');
    pageDots[(curIndex === -1) ? slideLen - 1 : curIndex].classList.remove('dot_active');
    curSlide = slideContents[++curIndex];
    curSlide.classList.add('slide_active');
    pageDots[curIndex].classList.add('dot_active');
}

slideBtnNext.addEventListener('click', function() {
    nextPageDo();
});
    

/** Prev Button Event */
slideBtnPrev.addEventListener('click', function() {
    if (curIndex >= 0) {
        slideList.style.transition = slideSpeed + "ms";
        slideList.style.transform = "translate3d(-" + (slideWidth * curIndex) + "px, 0px, 0px)";
    }
    if (curIndex === 0) {
        setTimeout(function() {
            slideList.style.transition = "0ms";
            slideList.style.transform = "translate3d(-" + (slideWidth * slideLen) + "px, 0px, 0px)";
        }, slideSpeed);
        curIndex = slideLen;
    }
    curSlide.classList.remove('slide_active');
    pageDots[(curIndex === slideLen) ? 0 : curIndex].classList.remove('dot_active');
    curSlide = slideContents[--curIndex];
    curSlide.classList.add('slide_active');
    pageDots[curIndex].classList.add('dot_active');
});
    
/** Pagination Button Event */
let curDot;
Array.prototype.forEach.call(pageDots, function (dot, i) {
    dot.addEventListener('click', function (e) {
        e.preventDefault();
        curDot = document.querySelector('.dot_active');
        curDot.classList.remove('dot_active');
              
        curDot = this;
        this.classList.add('dot_active');
    
        curSlide.classList.remove('slide_active');
        curIndex = Number(this.getAttribute('data-index'));
        curSlide = slideContents[curIndex];
        curSlide.classList.add('slide_active');
        slideList.style.transition = slideSpeed + "ms";
        slideList.style.transform = "translate3d(-" + (slideWidth * (curIndex + 1)) + "px, 0px, 0px)";
    });
});

// setInterval next slide
let interval = setInterval(function() {
    nextPageDo();
}, 4500);

slideBox.addEventListener('mouseover', function() {
    star[curIndex].style.display = "inline-flex";
});

slideBox.addEventListener('mouseout', function() {
    star[curIndex].style.display = "none";
});

// search button
searchMove.addEventListener('click', function() {
    window.scrollTo({top: searchLocation - navbarHeight - slidesHeight, behavior: 'smooth'});
})
// fitSearch button
fitMove.addEventListener('click', function() {
    window.scrollTo({top: fitLocation - navbarHeight - slidesHeight, behavior: 'smooth'});
})








// test
const testbtn = document.getElementById("test");

testbtn.addEventListener('click', function() {
    console.log('클릭됨');
    console.log(fitLocation);
});