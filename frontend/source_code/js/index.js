document.addEventListener("DOMContentLoaded", function () {
    const slider = document.querySelector(".slider");
    const prevBtn = document.querySelector(".prev-btn");
    const nextBtn = document.querySelector(".next-btn");
  
    let currentIndex = 1; // Set the initial index to 1 (Slide 2)
  
    function showSlide(index) {
      const translateValue = -index * 95 + "%";
      slider.style.transform = "translateX(" + translateValue + ")";
  
      // Show/hide buttons based on the current index
      prevBtn.style.display = index === 0 ? "none" : "block";
      nextBtn.style.display = index === 2 ? "none" : "block";
    }
  
    function nextSlide() {
      currentIndex = (currentIndex + 1) % 3;
      showSlide(currentIndex);
    }
  
    function prevSlide() {
      currentIndex = (currentIndex - 1 + 3) % 3;
      showSlide(currentIndex);
    }
  
    // Initial setup to show Slide 2
    showSlide(currentIndex);
  
    nextBtn.addEventListener("click", nextSlide);
    prevBtn.addEventListener("click", prevSlide);
  
    setInterval(nextSlide, 5000);
  });
  
