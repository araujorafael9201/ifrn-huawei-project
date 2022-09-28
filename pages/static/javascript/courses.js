/* BUTTONS */
button01 = document.querySelector("#title-01")
button02 = document.querySelector("#title-02")
button03 = document.querySelector("#title-03")
button04 = document.querySelector("#title-04")

/* SECTIONS */
section01 = document.querySelector(".section-01")
section02 = document.querySelector(".section-02")
section03 = document.querySelector(".section-03")
section04 = document.querySelector(".section-04")

/* FUNCTIONS */
button02.addEventListener("click", () => {
    button02.classList.add("act-ive")
    button01.classList.remove("act-ive")
    button03.classList.remove("act-ive")
    button04.classList.remove("act-ive")
    
    section02.style.display = "block"
    section01.style.display = "none"
    section03.style.display = "none"
    section04.style.display = "none"
})

button01.addEventListener("click", () => {
    button01.classList.add("act-ive")
    button02.classList.remove("act-ive")
    button03.classList.remove("act-ive")
    button04.classList.remove("act-ive")
    
    section01.style.display = "block"
    section02.style.display = "none"
    section03.style.display = "none"
    section04.style.display = "none"
})

button03.addEventListener("click", () => {
    button03.classList.add("act-ive")
    button02.classList.remove("act-ive")
    button01.classList.remove("act-ive")
    button04.classList.remove("act-ive")
    
    section03.style.display = "block"
    section02.style.display = "none"
    section01.style.display = "none"
    section04.style.display = "none"
})

button04.addEventListener("click", () => {
    button04.classList.add("act-ive")
    button02.classList.remove("act-ive")
    button03.classList.remove("act-ive")
    button01.classList.remove("act-ive")
    
    section04.style.display = "block"
    section02.style.display = "none"
    section03.style.display = "none"
    section01.style.display = "none"
})