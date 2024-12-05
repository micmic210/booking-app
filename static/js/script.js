// Smooth scroll to sections
function scrollToSection(sectionId) {
  const section = document.querySelector(sectionId);
  if (section) {
    section.scrollIntoView({
      behavior: "smooth"
    });

    // Remove active class from all buttons
    document.querySelectorAll(".cta-btn").forEach((btn) => btn.classList.remove("active"));

    // Add active class to the corresponding button
    if (sectionId === "#menu") {
      document.querySelector(".cta-green").classList.add("active");
    } else if (sectionId === "#reservation") {
      document.querySelector(".cta-orange").classList.add("active");
    }
  } else {
    console.error(`Section with ID ${sectionId} not found.`);
  }
}

// Learn More Button Navigation
document.addEventListener("DOMContentLoaded", () => {
  const learnMoreButton = document.getElementById("learnMoreButton");

  if (learnMoreButton) {
      learnMoreButton.addEventListener("click", () => {
          // Navigate to philosophy.html
          window.location.href = "/philosophy/"; // Adjust this path if necessary
      });
  }
});

// Menu Section: Category Filtering
const menuTab = document.querySelector(".menu-tab");

if (menuTab) {
  menuTab.addEventListener("click", (event) => {
    const button = event.target.closest(".menu-btn");
    if (!button) return; // Clicked outside a button

    const targetId = button.getAttribute("data-target");
    if (!targetId) return;

    // Remove "active" from all buttons
    menuTab.querySelectorAll(".menu-btn").forEach((btn) => btn.classList.remove("active"));
    // Add "active" to clicked button
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
