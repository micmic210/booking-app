// Smooth navigation to menu and reservation pages
document.addEventListener("DOMContentLoaded", () => {
  // Go to Menu button
  const goToMenuButton = document.querySelector(".btn-danger");
  if (goToMenuButton) {
    goToMenuButton.addEventListener("click", (event) => {
      event.preventDefault(); 
      window.location.href = goToMenuButton.getAttribute("href"); 
    });
  }

  // Book Table button
  const bookTableButton = document.querySelector(".btn-success");
  if (bookTableButton) {
    bookTableButton.addEventListener("click", (event) => {
      event.preventDefault(); 
      window.location.href = bookTableButton.getAttribute("href"); 
    });
  }
});


// Learn More Button Navigation
document.addEventListener("DOMContentLoaded", () => {
  const learnMoreButton = document.getElementById("learnMoreButton");

  if (learnMoreButton) {
      learnMoreButton.addEventListener("click", () => {
          // Navigate to philosophy.html
          window.location.href = "/philosophy/"; 
      });
  }
});

// Menu Section: Category Filtering
const menuTab = document.querySelector(".menu-tab");

if (menuTab) {
  menuTab.addEventListener("click", (event) => {
    const button = event.target.closest(".menu-btn");
    if (!button) return; 

    const targetId = button.getAttribute("data-target");
    if (!targetId) return;

    // Remove "active" from all buttons
    menuTab.querySelectorAll(".menu-btn").forEach((btn) => btn.classList.remove("active"));
    button.classList.add("active");

    // Show/Hide categories
    const menuCategories = document.querySelectorAll(".menu-category");
    if (targetId === "#all") {
      menuCategories.forEach((category) => category.classList.remove("d-none"));
    } else {
      menuCategories.forEach((category) => category.classList.add("d-none"));
      const targetCategory = document.querySelector(targetId);
      if (targetCategory) targetCategory.classList.remove("d-none");
    }
  });
}

// Set default state
const defaultButton = menuTab?.querySelector(".menu-btn[data-target='#all']");
if (defaultButton) defaultButton.classList.add("active");
const menuCategories = document.querySelectorAll(".menu-category");
menuCategories.forEach((category) => category.classList.remove("d-none"));
