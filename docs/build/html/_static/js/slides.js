var elem = document.querySelector(".carousel-container");
new Flickity(elem, {
    cellAlign: "right",
    contain: true,
    initialIndex: 2,
    pageDots: false,
    wrapAround: true,
    draggable: true,
    prevNextButtons: true,
    pauseAutoPlayOnHover: false
});
