screenWidth = screen.width
facebookIcon = document.querySelector("#face")

if (Number(screenWidth) <= 550) {
    facebookIcon.classList.remove("fa-3x")
    facebookIcon.classList.add("fa-2x")
}
