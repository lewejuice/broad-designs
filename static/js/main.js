// Javascript for Toasts
var toastElList = [].slice.call(document.querySelectorAll('.toast'));
var toastList = toastElList.map(function(toastEl) {
    return new bootstrap.Toast(toastEl);
});

function hideToast() {
    $('.toast').each(function() {
        this.style.setProperty('opacity', '0', 'important');
    });
}

// Service Icon switch bar from design to code
$('#btnradio1').click(function() {
    $('#design-service-icons').css("display", "block");
    $('#code-service-icons').css("display", "none");
});
$('#btnradio3').click(function() {
    $('#design-service-icons').css("display", "none");
    $('#code-service-icons').css("display", "block");
});

// Design/Code fade homescreen function

const left = document.querySelector(".left");
const right = document.querySelector(".right");
const container = document.querySelector(".dc-container");

left.addEventListener("mouseenter", () => {
    container.classList.add("hover-left");
});

left.addEventListener("mouseleave", () => {
    container.classList.remove("hover-left");
});

right.addEventListener("mouseenter", () => {
    container.classList.add("hover-right");
});

right.addEventListener("mouseleave", () => {
    container.classList.remove("hover-right");
});

// Start of Tawk.to Script
var Tawk_API = Tawk_API || {},
    Tawk_LoadStart = new Date();
(function() {
    var s1 = document.createElement("script"),
        s0 = document.getElementsByTagName("script")[0];
    s1.async = true;
    s1.src = 'https://embed.tawk.to/605214e7067c2605c0b972b8/1f10a3afb';
    s1.charset = 'UTF-8';
    s1.setAttribute('crossorigin', '*');
    s0.parentNode.insertBefore(s1, s0);
})();
// End of Tawk.to Script