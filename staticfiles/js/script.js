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
