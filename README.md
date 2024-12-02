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


