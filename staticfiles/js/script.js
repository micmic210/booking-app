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

// Validation Function
function validateForm() {
  const form = document.forms["reservation-form"]; 
  const name = form["name"];
  const email = form["email"];
  const phone = form["phone"];
  const date = form["reservation_date"];
  const time = form["reservation_time"];
  const guests = form["guests"];

  // Name validation
  if (name.value.trim() === "" || name.value.trim() === "Jon Doe") {
      alert("Please enter your full name.");
      name.focus();
      return false;
  }

  // Email validation
  if (email.value.trim() === "") {
      alert("Please enter your email address.");
      email.focus();
      return false;
  }
  const emailPattern = /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/;
  if (!emailPattern.test(email.value.trim())) {
      alert("Please enter a valid email address in the format: example@domain.com.");
      email.focus();
      return false;
  }

  // Phone validation
  if (phone.value.trim() === "" || phone.value.trim() === "0000-0000-0000") {
      alert("Please enter your phone number.");
      phone.focus();
      return false;
  }
  if (!/^\d+$/.test(phone.value.trim())) {
      alert("Please enter a valid phone number containing only digits.");
      phone.focus();
      return false;
  }
  if (phone.value.trim().length < 10) {
      alert("Phone number must be at least 10 digits.");
      phone.focus();
      return false;
  }

  // Reservation date validation
  const today = new Date();
  const selectedDate = new Date(date.value);

  if (date.value.trim() === "") {
      alert("Please select a reservation date.");
      date.focus();
      return false;
  }
  if (selectedDate < today.setHours(0, 0, 0, 0)) {
      alert("Reservation date cannot be in the past.");
      date.focus();
      return false;
  }

  // Reservation time validation
  if (time.value.trim() === "") {
      alert("Please select a reservation time.");
      time.focus();
      return false;
  }

  // Guests validation
  if (guests.value.trim() === "" || parseInt(guests.value.trim()) <= 0) {
      alert("Please enter the number of guests.");
      guests.focus();
      return false;
  }

  return true; // Form is valid
}

