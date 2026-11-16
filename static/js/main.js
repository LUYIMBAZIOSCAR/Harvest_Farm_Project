document.addEventListener('DOMContentLoaded', function () {
    const currentYear = document.getElementById('currentYear');
    if (currentYear) {
        currentYear.textContent = new Date().getFullYear();
    }

    const slides = document.querySelectorAll('.hero-slide');
    const dots = document.querySelectorAll('.hero-slider-dots .dot');
    const prevBtn = document.querySelector('.hero-slider-btn.prev');
    const nextBtn = document.querySelector('.hero-slider-btn.next');

    if (!slides.length) return;

    let currentSlide = 0;
    let autoRotate;

    function showSlide(index) {
        currentSlide = (index + slides.length) % slides.length;

        slides.forEach((slide, idx) => {
            slide.classList.toggle('active', idx === currentSlide);
        });

        dots.forEach((dot, idx) => {
            dot.classList.toggle('active', idx === currentSlide);
        });
    }

    function startAutoRotate() {
        clearInterval(autoRotate);
        autoRotate = setInterval(() => {
            showSlide(currentSlide + 1);
        }, 5000);
    }

    prevBtn?.addEventListener('click', () => {
        showSlide(currentSlide - 1);
        startAutoRotate();
    });

    nextBtn?.addEventListener('click', () => {
        showSlide(currentSlide + 1);
        startAutoRotate();
    });

    dots.forEach((dot, index) => {
        dot.addEventListener('click', () => {
            showSlide(index);
            startAutoRotate();
        });
    });

    showSlide(0);
    startAutoRotate();
});
