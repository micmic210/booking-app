document.addEventListener('DOMContentLoaded', () => {
  const likeButton = document.getElementById('likeButton');

  if (likeButton) {
      likeButton.addEventListener('click', function () {
          const blogId = likeButton.getAttribute('data-id');

          // Send an AJAX request to the server
          fetch(`/blog/like/${blogId}/`, {
              method: 'POST',
              headers: {
                  'Content-Type': 'application/json',
                  'X-CSRFToken': getCSRFToken(),
              },
              body: JSON.stringify({})
          })
          .then(response => response.json())
          .then(data => {
              if (data.liked !== undefined) {
                  // Update the like count and button text
                  const likesCount = document.getElementById('likesCount');
                  likesCount.textContent = data.likes_count;

                  likeButton.disabled = true;
                  likeButton.innerHTML = `<i class="fa fa-thumbs-up"></i> ${data.liked ? 'Liked' : 'Like'}`;
              } else if (data.error) {
                  alert(data.error);
              }
          })
          .catch(error => console.error('Error:', error));
      });
  }
});

function getCSRFToken() {
  const cookies = document.cookie.split(';');
  for (let cookie of cookies) {
      const [key, value] = cookie.trim().split('=');
      if (key === 'csrftoken') {
          return decodeURIComponent(value);
      }
  }
  return '';
}

/**
* Show the edit form for a specific comment.
*/
function showEditForm(commentId) {
  const editForm = document.getElementById(`edit-form-${commentId}`);
  if (editForm) {
      editForm.classList.remove('d-none'); // Show the form
  } else {
      console.error(`Edit form with ID edit-form-${commentId} not found.`);
  }
}

/**
* Hide the edit form for a specific comment.
*/
function hideEditForm(commentId) {
  const editForm = document.getElementById(`edit-form-${commentId}`);
  if (editForm) {
      editForm.classList.add('d-none'); // Hide the form
  } else {
      console.error(`Edit form with ID edit-form-${commentId} not found.`);
  }
}

/**
* Confirm delete action using SweetAlert2.
*/
function confirmDelete(blogId, commentId) {
  Swal.fire({
      title: 'Are you sure?',
      text: "Do you really want to delete this comment?",
      icon: 'warning',
      showCancelButton: true,
      confirmButtonColor: '#d33',
      cancelButtonColor: '#3085d6',
      confirmButtonText: 'Yes, delete it!'
  }).then((result) => {
      if (result.isConfirmed) {
          const deleteUrl = `/blog/${blogId}/comment/${commentId}/delete/`;
          window.location.href = deleteUrl;
      }
  });
}
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
