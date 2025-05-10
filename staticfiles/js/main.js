window.addEventListener("scroll", function () {
    let navbar = document.querySelector(".navbar");
    let navLinks = this.document.querySelectorAll(".nav-item a");
    if (window.scrollY > 50) {
        navbar.classList.add("scrolled");

        navLinks.forEach(function (link) {
            link.style.color = "black";
            link.style.textShadow = "none";
        });

    } else {
        navbar.classList.remove("scrolled");

        navLinks.forEach(function (link) {
            link.style.color = "white";
            link.style.textShadow = "0 0 5px black";
        });

    }
});
// const carousel = document.getElementById('carouselExampleFade');

//     // Function to handle playing/pausing videos
//     function handleVideoPlayback() {
//         const videos = carousel.querySelectorAll('video');

//         videos.forEach(video => {
//             const isActive = video.closest('.carousel-item').classList.contains('active');

//             if (isActive) {
//                 video.currentTime = 0;  // Reset video to start
//                 video.play().catch(error => console.log("Video play failed:", error));
//             } else {
//                 video.pause();
//             }
//         });
//     }

//     // Handle when the carousel slides
//     carousel.addEventListener('slid.bs.carousel', handleVideoPlayback);

//     // Play the first video when the page loads
//     window.addEventListener('load', handleVideoPlayback);


const carousel = document.querySelector('#carouselExampleFade');
carousel.addEventListener('slide.bs.carousel', function () {
    // Remove the active animations instantly when slide starts changing
    document.querySelectorAll('.custom-caption').forEach(caption => {
        caption.style.opacity = '0';
    });
});

carousel.addEventListener('slid.bs.carousel', function () {
    // After slide finishes, allow captions to animate again
    const activeItem = document.querySelector('.carousel-item.active .custom-caption');
    if (activeItem) {
        activeItem.style.opacity = '1';
    }
});