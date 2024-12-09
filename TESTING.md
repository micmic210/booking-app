# Ramen Bar - Testing
![Ramen Bar](/documentation/home-page.webp)

Welcome to the testing documentation for the Ramen Bar website. As a student developer, I have dedicated my efforts to creating a high-quality, user-friendly platform for ramen enthusiasts to explore and make reservations. Built using HTML, CSS, Bootstrap, JavaScript, Python, and Django, this project integrates modern web development tools to deliver a seamless experience. This document provides an overview of the testing strategies and methodologies I employed to ensure the functionality, performance, and responsiveness of the site. From verifying design consistency across devices to ensuring smooth reservation workflows and debugging complex interactions, this guide outlines the steps taken to make the Ramen Bar website an enjoyable and reliable platform for every visitor.

Visit the site here: [RAMEN BARS](https://micmic210.github.io/curry-lovers/index.html)

- - - 

## Contents
* [Automated Testing](#automated-testing)
	* [W3C Validator](#w3c-validator)
	* [JavaScript Validator](#javascript-validator)
	* [Lighthouse](#lighthouse)
* [Manual Testing](#manual-testing)
	* [Testing User Stories](#testing-user-stories)
	* [Full Testing](#full-testing)

- - -

## Automated Testing

### W3C Validator 

[W3C Validator](https://validator.w3.org/):
All HTML and CSS files for the Ramen Bar website were tested using the W3C Validator tools, and no errors were found. Below is a list of the validated files:

HTML Files: 
![html](/documentation/html.webp)
* index.html: Passed validation with no errors.
* phylosophy.html: Passed validation with no errors.
* menu.html: Passed validation with no errors.
* reservation.html: Passed validation with no errors.
* confirmation.html: Passed validation with no errors.
* cancellation.html: Passed validation with no errors.
* contact.html: Passed validation with no errors.
* thank_you.html: Passed validation with no errors.
* blog.html: Passed validation with no errors.
* blog_detail.html: Passed validation with no errors.
* sign-in.html: Passed validation with no errors.
* logout.html: Passed validation with no errors.
* sign-up.html: Passed validation with no errors.
* 404.html: Passed validation with no errors.

CSS File:
![css](/documentation/cl-css.webp)
* style.css: Passed validation with no errors.

### JavaScript Validator 
![jshint](https://jshint.com/) was used to validate the JavaScript.
* Metrics: 
There is only one function in this file.
It takes one argument.
This function contains 7 statements.
Cyclomatic complexity number for this function is 4.
Passed validation with no errors or warnings.
![javascript.js](/documentation/jshint-result.webp)

- - - 

### Lighthouse

Below are the Lighthouse test results for the Ramen Lovers website, showcasing key performance metrics and areas of optimization.

### Mobile Results
![index.html](/documentation/index-mobile.webp)


### Desktop Results
![index.html](/documentation/index-desktop.webp)

- - - 

### Manual Testing
#### Testing User Stories

### User Stories

The Ramen Bar website focuses on providing a user-friendly and engaging experience. Visitors can browse a categorized menu, make and cancel reservations, and contact the restaurant through an intuitive interface. A blog section allows users to explore articles on ramen culture and engage through comments and likes. Registered users benefit from additional features such as comment management and personalization. Admins can efficiently manage menu items, reservations, and blog content via the Django admin panel. These features ensure a seamless and enjoyable experience for both users and administrators.


#### 1. User-Friendly Frontend Design
As a user, I want the website to have a visually appealing and intuitive design so that I can easily navigate and interact with it.

* Each page has a consistent design theme.
* Clear and intuitive navigation menus are provided.
* Reservation and contact forms are visually appealing and easy to use.

#### 2. Menu Display
As a customer, I want to view the menu online, so that I can see the available dishes and their details.

* Menu items are displayed by categories (e.g., Ramen, Starters).
* Each menu item includes a name, description, price, and photo.
* An "All Menu" button allows customers to view all items across categories.

#### 3. Reservation Functionality
As a customer, I want to reserve a table online, so that I can secure a spot in the restaurant without waiting.

* Customers can fill out a reservation form with fields for name, email, phone number, date, time, and number of guests.
* Upon successful form submission, a confirmation message is displayed.
* Reservations are recorded in the database and accessible via the admin panel.

#### 4. Reservation Cancellation
As a user, I want to cancel my reservation using my reservation number online so that I can modify my plans without contacting support.

* The website has a "Cancel Reservation" option, accessible from the homepage.
* Users must enter their reservation number for cancellation.
The system validates the entered reservation number against existing records.
* If the reservation number is valid, the user sees the cancel button.
Upon successful cancellation, the system displays a confirmation message.
* If the reservation number is invalid, an error message informs the user.

#### 5. Blog Feature
As a user, I want to read blog posts, leave comments, and like posts so that I can engage more deeply with the site.

* Users can view the latest blog posts on a blog list page.
* Users can read detailed blog posts on a blog detail page.
* Logged-in users can leave comments and like posts.
* Blog posts and comments can be managed through the admin panel.

#### 6. Contact Form Functionality
As a customer, I want to send inquiries through a contact form, so that I can communicate directly with the restaurant.

* The contact form includes fields for name, email, and message.
Upon submission, the message is sent to the admin email.
* A "Thank You" page is displayed after successful submission.
* Errors in form submission display appropriate messages.

#### 7. Authentication
As a user, I want to create an account to manage my personal information.

* Users can sign up with a username, email, and password.
* Logged-in users can write, edit, and delete their own comments.
* Logged-in users can use the LIKE button.
* Admin users can manage accounts through the Django admin panel.

#### 8. Menu Management
As a restaurant manager, I want to add, edit, or delete menu items, so that I can keep the menu up-to-date.

* Admin users can log in to the Django admin panel.
* Menu items can be added, edited, or deleted from the database via the admin panel.
* Menu items include fields for name, description, price, category, and photo upload.
* Changes to the menu are immediately reflected on the website.


---

### ADMIN

| TEST | OUTCOME | PASS/FAIL |
|:---:|:---:|:---:|
| Create Menu Item | Menu item successfully created and displayed in the correct category | Pass |
| Edit Menu Item | Menu item successfully updated, and changes reflected on the site | Pass |
| Delete Menu Item | Menu item successfully removed from the site | Pass |
| Create Blog Post | Blog post successfully created and displayed on the blog page | Pass |
| Edit Blog Post | Blog post successfully updated, and changes reflected on the site | Pass |
| Delete Blog Post | Blog post successfully deleted | Pass |
| Manage User Comments | Comments successfully approved, edited, or deleted as needed | Pass |
| Access Reservations | Admin can view and manage all reservations in the Django admin panel | Pass |

---

### USER

| TEST | OUTCOME | PASS/FAIL |
|:---:|:---:|:---:|
| Create Account | Account successfully created and user redirected to the homepage | Pass |
| Login | Login successful, and user redirected to their dashboard | Pass |
| Logout | Logout successful, and user redirected to the homepage | Pass |
| Make a Reservation | Reservation successfully made, and confirmation message displayed | Pass |
| Cancel Reservation | Reservation successfully canceled using the reservation number, and confirmation message displayed | Pass |
| Submit Contact Form | Contact form submitted successfully, and user redirected to a "Thank You" page | Pass |
| Read Blog Posts | Blog post content displayed correctly | Pass |
| Add Comment under Blog Post | Comment added successfully and displayed beneath the blog post | Pass |
| Edit Comment | Logged-in user successfully updated their comment | Pass |
| Delete Comment | Logged-in user successfully deleted their comment | Pass |
| Like Blog Post | "Like" successfully registered, and the count updated | Pass |

Here’s a refined debug history section that selects and organizes 10 good debugging instances based on complexity, relevance, and impact:

---

## Debug History

### 1. **Cloudinary Configuration Error**
- **Issue**: A typo in the `CLOUDINARY_URL` environment variable caused a startup failure with the error:  
  ```
  ValueError: Invalid CLOUDINARY_URL scheme. Expecting to start with 'cloudinary://'
  ```
- **Solution**:
  - Corrected the `CLOUDINARY_URL` in `env.py` to the proper format:
    ```
    cloudinary://API_KEY:API_SECRET@CLOUD_NAME
    ```
  - Restarted the server to verify the fix.
- **Outcome**: The issue was resolved, and media uploads functioned correctly.

---

### 2. **Static Files Configuration Error**
- **Issue**: Running `collectstatic` resulted in:
  ```
  django.core.exceptions.ImproperlyConfigured: You're using the staticfiles app without having set the STATIC_ROOT setting to a filesystem path.
  ```
- **Solution**:
  - Updated `settings.py` to include:
    ```python
    STATIC_URL = 'static/'
    STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
    STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
    ```
  - Created necessary directories and ran `collectstatic`.
- **Outcome**: Static files were successfully collected, and the site rendered correctly.

---

### 3. **CSRF Verification Error**
- **Issue**: Deployed site displayed a `403 Forbidden` error due to failed CSRF verification.
- **Solution**:
  - Added `CSRF_TRUSTED_ORIGINS` in `settings.py` for the deployment domain.
  - Configured the CSRF variable in Heroku:
    ```
    heroku config:set CSRF_TRUSTED_ORIGINS=https://<your-app>.herokuapp.com
    ```
- **Outcome**: Fixed the issue, and forms now work on the live site.

---

### 4. **Menu Item Image Upload Failure**
- **Issue**: Menu images failed to upload due to missing Cloudinary configuration.
- **Solution**:
  - Updated the `menu/models.py` to include:
    ```python
    from cloudinary.models import CloudinaryField
    image = CloudinaryField('image', folder='menu_images/')
    ```
  - Ran migrations to apply changes.
- **Outcome**: Images successfully uploaded and displayed on the menu page.

---

### 5. **Reservation Form Not Displayed**
- **Issue**: The reservation form was not rendering on `reservation.html` due to a missing context variable in the view.
- **Solution**:
  - Fixed the view to include:
    ```python
    def reservation(request):
        form = ReservationForm()
        return render(request, 'reservation.html', {'form': form})
    ```
- **Outcome**: The reservation form displayed correctly.

---

### 6. **LIKE Button Count Not Updating**
- **Issue**: The LIKE button did not update the count dynamically.
- **Solution**:
  - Implemented AJAX to update the LIKE count without reloading the page:
    ```javascript
    $('#likeButton').click(function() {
        $.ajax({
            url: '/like-post/',
            method: 'POST',
            data: { post_id: postId },
            success: function(response) {
                $('#likeCount').text(response.likes);
            }
        });
    });
    ```
- **Outcome**: The LIKE button now updates in real-time.

---

### 7. **Pagination Not Displaying Properly**
- **Issue**: Pagination links for the blog posts were broken due to an incorrect URL pattern.
- **Solution**:
  - Fixed the `urls.py` to include:
    ```python
    path('blog/', BlogListView.as_view(), name='blog'),
    ```
  - Added `paginator` logic in the template.
- **Outcome**: Pagination displayed and functioned correctly.

---

### 8. **Edit Comment Not Saving**
- **Issue**: Edited comments were not being saved due to a missing form `action` attribute in the HTML.
- **Solution**:
  - Updated the comment edit form in `blog_detail.html` to include:
    ```html
    <form action="{% url 'edit_comment' comment.id %}" method="POST">
    ```
- **Outcome**: Edited comments now save as expected.

---

### 9. **Heroku Deployment Failure**
- **Issue**: Deployment failed with the error:
  ```
  ModuleNotFoundError: No module named 'gunicorn'
  ```
- **Solution**:
  - Added `gunicorn` to `requirements.txt` and redeployed:
    ```
    pip install gunicorn
    pip freeze > requirements.txt
    git add requirements.txt
    git commit -m "Add gunicorn"
    git push heroku main
    ```
- **Outcome**: Deployment succeeded.

---

### 10. **404 Error for Contact Page**
- **Issue**: Accessing the contact page resulted in a 404 error due to a missing entry in `urls.py`.
- **Solution**:
  - Added the contact view to `urls.py`:
    ```python
    path('contact/', ContactView.as_view(), name='contact'),
    ```
- **Outcome**: The contact page loaded successfully.

---

### Key Learnings
- Ensure environment variables are accurately configured.
- Use AJAX for dynamic UI updates.
- Always test URL patterns and context variables in views.
- Deploy incrementally to catch issues early.

--- 

This format is ready for copy-pasting into your **TESTING.md** and showcases your debugging skills clearly and professionally.
---
