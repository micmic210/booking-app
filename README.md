![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

Welcome Michiko Inoue,

This is the Code Institute student template for Gitpod. We have preinstalled all of the tools you need to get started. It's perfectly ok to use this template as the basis for your project submissions.

You can safely delete this README.md file or change it for your own project. Please do read it at least once, though! It contains some important information about Gitpod and the extensions we use. Some of this information has been updated since the video content was created. The last update to this file was: **June 18, 2024**

## Gitpod Reminders

To run a frontend (HTML, CSS, Javascript only) application in Gitpod, in the terminal, type:

`python3 -m http.server`

A blue button should appear to click: _Make Public_,

Another blue button should appear to click: _Open Browser_.

To run a backend Python file, type `python3 app.py` if your Python file is named `app.py`, of course.

A blue button should appear to click: _Make Public_,

Another blue button should appear to click: _Open Browser_.

By Default, Gitpod gives you superuser security privileges. Therefore, you do not need to use the `sudo` (superuser do) command in the bash terminal in any of the lessons.

To log into the Heroku toolbelt CLI:

1. Log in to your Heroku account and go to *Account Settings* in the menu under your avatar.
2. Scroll down to the *API Key* and click *Reveal*
3. Copy the key
4. In Gitpod, from the terminal, run `heroku_config`
5. Paste in your API key when asked

You can now use the `heroku` CLI program - try running `heroku apps` to confirm it works. This API key is unique and private to you, so do not share it. If you accidentally make it public, you can create a new one with _Regenerate API Key_.

### Connecting your Mongo database

- **Connect to Mongo CLI on a IDE**
- navigate to your MongoDB Clusters Sandbox
- click **"Connect"** button
- select **"Connect with the MongoDB shell"**
- select **"I have the mongo shell installed"**
- choose **mongosh (2.0 or later)** for : **"Select your mongo shell version"**
- choose option: **"Run your connection string in your command line"**
- in the terminal, paste the copied code `mongo "mongodb+srv://<CLUSTER-NAME>.mongodb.net/<DBname>" --apiVersion 1 --username <USERNAME>`
  - replace all `<angle-bracket>` keys with your own data
- enter password _(will not echo **\*\*\*\*** on screen)_

------

## Release History

We continually tweak and adjust this template to help give you the best experience. Here is the version history:

**June 18, 2024,** Add Mongo back into template

**June 14, 2024,** Temporarily remove Mongo until the key issue is resolved

**May 28 2024:** Fix Mongo and Links installs

**April 26 2024:** Update node version to 16

**September 20 2023:** Update Python version to 3.9.17.

**September 1 2021:** Remove `PGHOSTADDR` environment variable.

**July 19 2021:** Remove `font_fix` script now that the terminal font issue is fixed.

**July 2 2021:** Remove extensions that are not available in Open VSX.

**June 30 2021:** Combined the P4 and P5 templates into one file, added the uptime script. See the FAQ at the end of this file.

**June 10 2021:** Added: `font_fix` script and alias to fix the Terminal font issue

**May 10 2021:** Added `heroku_config` script to allow Heroku API key to be stored as an environment variable.

**April 7 2021:** Upgraded the template for VS Code instead of Theia.

**October 21 2020:** Versions of the HTMLHint, Prettier, Bootstrap4 CDN and Auto Close extensions updated. The Python extension needs to stay the same version for now.

**October 08 2020:** Additional large Gitpod files (`core.mongo*` and `core.python*`) are now hidden in the Explorer, and have been added to the `.gitignore` by default.

**September 22 2020:** Gitpod occasionally creates large `core.Microsoft` files. These are now hidden in the Explorer. A `.gitignore` file has been created to make sure these files will not be committed, along with other common files.

**April 16 2020:** The template now automatically installs MySQL instead of relying on the Gitpod MySQL image. The message about a Python linter not being installed has been dealt with, and the set-up files are now hidden in the Gitpod file explorer.

**April 13 2020:** Added the _Prettier_ code beautifier extension instead of the code formatter built-in to Gitpod.

**February 2020:** The initialisation files now _do not_ auto-delete. They will remain in your project. You can safely ignore them. They just make sure that your workspace is configured correctly each time you open it. It will also prevent the Gitpod configuration popup from appearing.

**December 2019:** Added Eventyret's Bootstrap 4 extension. Type `!bscdn` in a HTML file to add the Bootstrap boilerplate. Check out the <a href="https://github.com/Eventyret/vscode-bcdn" target="_blank">README.md file at the official repo</a> for more options.

------

## FAQ about the uptime script

**Why have you added this script?**

It will help us to calculate how many running workspaces there are at any one time, which greatly helps us with cost and capacity planning. It will help us decide on the future direction of our cloud-based IDE strategy.

Debug Section

### **Debug Log**

#### **1. Cloudinary Configuration Error**
- **Issue**: A typo in the `CLOUDINARY_URL` environment variable caused the following error during startup:
  ```
  ValueError: Invalid CLOUDINARY_URL scheme. Expecting to start with 'cloudinary://'
  ```
- **Solution**:
  1. Corrected the `CLOUDINARY_URL` in the `env.py` file.
     - Correct format: `cloudinary://API_KEY:API_SECRET@CLOUD_NAME`
  2. Restarted the server to verify the fix.

---

#### **2. Static Files Configuration Error**
- **Issue**: The `STATICFILES` directory was not found, resulting in the following error when running `collectstatic`:
  ```
  django.core.exceptions.ImproperlyConfigured: You're using the staticfiles app without having set the STATIC_ROOT setting to a filesystem path.
  ```
- **Solution**:
  1. Added the following settings in `settings.py`:
     ```python
     STATIC_URL = 'static/'
     STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
     STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
     ```
  2. Created the necessary directories:
     ```bash
     mkdir static staticfiles
     ```
  3. Ran `python manage.py collectstatic` to resolve the issue.

---

#### **3. CSRF Verification Error**
- **Issue**: After deploying to Heroku, the following error occurred:
  ```
  Forbidden (403) CSRF verification failed. Request aborted.
  ```
- **Solution**:
  1. Added `CSRF_TRUSTED_ORIGINS` to `settings.py`:
     ```python
     CSRF_TRUSTED_ORIGINS = [
         "https://<your-app-name>.herokuapp.com",
         "https://*.codeanyapp.com",
     ]
     ```
  2. Set the environment variable on Heroku:
     ```bash
     heroku config:set CSRF_TRUSTED_ORIGINS=https://<your-app-name>.herokuapp.com
     ```
  3. Restarted the server to confirm the fix.

---

#### **4. allauth Middleware Error**
- **Issue**: The `allauth.account.middleware.AccountMiddleware` was not added to `MIDDLEWARE`, leading to the following error:
  ```
  django.core.exceptions.ImproperlyConfigured: allauth.account.middleware.AccountMiddleware must be added to settings.MIDDLEWARE
  ```
- **Solution**:
  1. Added the middleware to `settings.py`:
     ```python
     'allauth.account.middleware.AccountMiddleware',
     ```
  2. Applied migrations using:
     ```bash
     python manage.py migrate
     ```

---

#### **5. Reservation Form Not Displayed**
- **Issue**: The `reservation.html` template did not display the form. Debugging revealed that the form was not correctly passed from the `reservation` view.
- **Solution**:
  1. Fixed the `reservation` view in `reservation/views.py`:
     ```python
     def reservation(request):
         if request.method == 'POST':
             form = ReservationForm(request.POST)
             if form.is_valid():
                 reservation = form.save()
                 return redirect('confirmation', reservation_number=reservation.reservation_number)
         else:
             form = ReservationForm()
         return render(request, 'reservation/reservation.html', {'form': form})
     ```
  2. Ensured the form code was properly added to the template.

---

#### **6. Cloudinary Configuration for Menu Management**
- **Issue**: Menu images were not being uploaded due to missing Cloudinary configuration.
- **Solution**:
  1. Updated the `menu/models.py` to include the Cloudinary field:
     ```python
     from cloudinary.models import CloudinaryField

     class Menu(models.Model):
         name = models.CharField(max_length=100)
         description = models.TextField(blank=True, null=True)
         price = models.DecimalField(max_digits=6, decimal_places=2)
         category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='ramen')
         image = CloudinaryField('image', folder="menu_images/")
         is_available = models.BooleanField(default=True)
         created_at = models.DateTimeField(auto_now_add=True)

         def __str__(self):
             return self.name
     ```
  2. Ran migrations:
     ```bash
     python manage.py makemigrations
     python manage.py migrate
     ```

---

### **Key Learnings and Reflections**
1. **Accuracy with Environment Variables**: Typos in `env.py` led to errors. Always verify environment variables before deployment.
2. **Static Files Management**: Reinforced understanding of Django's static files handling.
3. **Prioritizing Error Resolution**: Addressing errors sequentially simplified debugging.
4. **Code Reusability**: Leveraging prior project code significantly improved efficiency.

Based on the screenshot, I understand you are referring to a Markdown style that includes **code blocks** for commands and descriptions, often displayed in "boxes." Below is the updated debugging history formatted in a style consistent with your screenshot:

---

## Debugging History for Blog Features

### 1. **Comment Editing and Deletion Issues**

#### Problem
- The modal for confirming comment edits appeared at the wrong timing.
- Editing functionality sometimes did not save changes correctly.
- Inline editing forms occasionally displayed rendering errors.

#### Solution
```bash
# Fixed the timing of the modal appearance
- Adjusted the `confirmSaveChanges` JavaScript function to ensure the modal appears after clicking the "Submit" button in the edit form.
- Correctly mapped the `comment_form` instance to the respective comment in the template (`blog_detail.html`).
- Updated inline form rendering logic with unique ID management to avoid conflicts.
```

---

### 2. **Incorrect Button States**

#### Problem
- Both "Edit" and "Delete" buttons displayed inconsistently styled buttons.
- Buttons sometimes appeared for unauthorized users or in duplicate.

#### Solution
```bash
# Updated button logic and styling
- Rewrote the conditional rendering logic in `blog_detail.html` to restrict button display to comment authors only.
- Standardized button styles using Bootstrap 4 classes.
```

---

### 3. **LIKE Button Implementation**

#### Problem
- The LIKE functionality allowed unliking, which was against the specification.
- Button styles and text were inconsistent with the desired design.
- AJAX requests failed occasionally due to missing CSRF tokens.

#### Solution
```bash
# Added CSRF token dynamically and restricted unliking
- Restricted "unlike" by disabling the LIKE button after it is clicked.
- Added `Font Awesome` thumbs-up icons for the LIKE button.
- Enhanced `views.py` to handle already liked posts and provide proper JSON responses.
- Integrated CSRF tokens dynamically into AJAX headers.
```

---

### 4. **Rendering Errors in JavaScript and HTML**

#### Problem
- JavaScript syntax errors caused runtime failures in confirmation modals.
- Variables in `confirmSaveChanges` and `confirmDelete` functions were not properly scoped or referenced.

#### Solution
```bash
# Fixed JavaScript syntax errors
- Corrected syntax and used template literals for dynamic ID references.
- Added error handling and console logging for debugging missing elements.
```

---

### 5. **Comments Misaligned with Post Content**

#### Problem
- Comment submission boxes were not aligned properly with the layout.
- Headers for "Edit Comment" and "Leave a Comment" were inconsistent.

#### Solution
```bash
# Updated layout and styling for comments
- Adjusted the `blog_detail.html` layout using the Bootstrap 4 grid system to align comments to the right sidebar.
- Standardized headers to user-friendly text like "Leave a Comment" and "Edit Your Comment."
```

---

### 6. **Miscellaneous Fixes**

```bash
- Removed redundant code for comment approval since it was not required for the current setup.
- Added tooltips and improved button descriptions for accessibility.
- Improved error messages in `views.py` to be more user-friendly.
```

---

### **Code Highlights**

#### Improved `views.py`
```python
# Enhanced error handling for comment_edit and comment_delete
if comment.author != request.user:
    messages.error(request, "You are not authorized to edit this comment.")
    return redirect('blog_detail', id=blog.id)
```

#### Enhanced `blog_detail.html`
```html
<!-- LIKE Button -->
<button id="likeButton" 
        class="btn btn-primary" 
        data-id="{{ blog.id }}" 
        {% if user in blog.likes.all %} disabled {% endif %}>
    <i class="fa {% if user in blog.likes.all %}fa-thumbs-up{% else %}fa-thumbs-o-up{% endif %}"></i>
    {% if user in blog.likes.all %}Liked{% else %}Like{% endif %}
</button>
```

Great to hear that it worked! Below is a summary of the debugging process, including the issues you faced and how you fixed them:

Debug History and Issue Fixes

1. Issue: Embedded Git repository (booking-app)

	•	Problem: During the process of trying to push changes to GitHub, you encountered an issue with an embedded Git repository (booking-app) that had been accidentally added inside your current repository.
	•	Error Message:

hint: You've added another git repository inside your current repository.
hint: Clones of the outer repository will not contain the contents of
hint: the embedded repository and will not know how to obtain it.


	•	Solution:
	•	You identified that the booking-app folder had been added to version control by mistake as an embedded Git repository.
	•	To resolve this, you had to remove the booking-app directory from Git’s staging area using:

git rm --cached -r booking-app


	•	This removed the embedded repository from being tracked by Git.

2. Issue: Merge Conflict during Rebase

	•	Problem: When you tried to pull the latest changes from the remote repository with git pull --rebase, you encountered a merge conflict in settings.py.
	•	Error Message:

error: could not apply 12b939d... Fix: Remove embedded repository booking-app from version control


	•	Solution:
	•	The conflict was resolved by manually editing settings.py to ensure that both sets of changes were properly integrated.
	•	After resolving the conflict, you marked the file as resolved by staging it using:

git add my_project/settings.py


	•	You continued the rebase process with:

git rebase --continue


	•	This successfully resolved the conflict and completed the rebase.

3. Issue: Commit Message and Editor Confusion

	•	Problem: While trying to continue the rebase, you were stuck in an editor screen (most likely Nano or another editor), where the commit message was unclear. You were unable to close the editor and complete the rebase process.
	•	Solution:
	•	You identified that the editor was asking you to confirm the commit message for the rebase.
	•	After closing the editor (by pressing Ctrl+X in Nano, or following the instructions for the editor in use), the rebase was continued.
	•	This allowed the rebase to finish and commit the changes successfully.

4. Issue: File Removal and Cleanup

	•	Problem: Some files (such as templates/account/login.html, templates/account/logout.html, and templates/account/signup.html) were deleted as part of the fixes to clean up the repository.
	•	Solution:
	•	The files were properly removed and staged for commit, and the cleanup process was confirmed with:

git status



5. Issue: Pushing Changes to Remote Repository

	•	Problem: After completing the rebase, you couldn’t push the changes to the remote repository because of a conflict between your local and remote branches.
	•	Solution:
	•	You used the following command to rebase and incorporate any changes from the remote repository:

git pull origin main --rebase


	•	After resolving the conflicts and ensuring everything was updated, you successfully pushed the changes to the remote repository using:

git push origin main



