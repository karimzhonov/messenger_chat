const leftBarsBtn = document.querySelector('.left-bars-button')
const menu = document.querySelector('.menu')
const discussions = document.querySelector('.discussions')
const leftSiteBack = document.querySelector('.left-site-back')
const chat = document.querySelector('.chat')

const nav_items = document.querySelectorAll('.menu .items .item')
const page_href = window.location.href

nav_items.forEach(point => {
    const a_href = point.querySelector('a').href
    if (a_href === page_href){
        point.classList.add('item-active')
    }
})

// leftBarsBtn.addEventListener('click', ()=>{
//     menu.classList.remove('left-bars-button-active')
//     discussions.classList.remove('left-bars-button-active')
//     chat.classList.add('left-bars-button-active')
// })
//
// leftSiteBack.addEventListener('click', ()=>{
//     menu.classList.add('left-bars-button-active')
//     discussions.classList.add('left-bars-button-active')
//     chat.classList.remove('left-bars-button-active')
// })
