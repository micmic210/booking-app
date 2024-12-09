# Ramen Bar
![Ramen Bar](/documentation/index.webp)

Welcome to Ramen Bar – your ultimate destination for all things ramen! Whether you’re a ramen aficionado or just discovering the joy of this comforting dish, we’re here to share the flavors, culture, and magic of a perfect bowl of ramen.

Join us as we explore mouthwatering recipes, offer expert tips, and connect with fellow ramen enthusiasts who share a passion for this delicious and soulful cuisine. Dive into the rich world of ramen with us and discover your new favorite bowl!

Here's the website: [Ramen Bar](https://ramen-bar-booking-app-8cf486e28254.herokuapp.com/) 


---

## Contents

1. [User Experience](#user-experience)
   - [User Stories](#user-stories)
2. [Design](#design)
   - [Color Scheme](#color-scheme)
   - [Brand Logo and Favicon](#brand-logo-and-favicon)
   - [Typography](#typography)
   - [Imagery](#imagery)
   - [Wireframes](#wireframes)
   - [Features](#features)
3. [Future Implementations](#future-implementations)
4. [Technologies Used](#technologies-used)
   - [Languages Used](#languages-used)
   - [Frameworks, Libraries & Programs Used](#frameworks-libraries--programs-used)
5. [Deployment & Local Development](#deployment--local-development)
   - [Repository Deployment via Heroku](#repository-deployment-via-heroku)
6. [Testing](#testing)
   - [Solved Bugs](#solved-bugs)
7. [Credits](#credits)
   - [Code Used](#code-used)
   - [Content](#content)
   - [Media](#media)
   - [Acknowledgments](#acknowledgments)
8. [Debug History](#debug-history)

---
- - - 

## User Experience
Ramen Bar is crafted to provide an engaging and seamless user experience, making every visit to the site a delightful journey into the world of ramen. The intuitive and visually appealing layout ensures effortless navigation, allowing users to make and manage reservations, cancel bookings, or get in touch with ease. Dive into blogs that celebrate ramen culture, its ties to Japan, and culinary inspiration, all presented with captivating visuals and a clean design. For logged-in users, the experience is elevated with interactive features like the ability to write, edit, and delete comments, as well as express appreciation through LIKE buttons. Ramen Bar combines functionality and aesthetics to create a community-centric platform that’s as warm and inviting as a bowl of ramen.

### User Stories

The Ramen Bar website focuses on providing a user-friendly and engaging experience. Visitors can browse a categorized menu, make and cancel reservations, and contact the restaurant through an intuitive interface. A blog section allows users to explore articles on ramen culture and engage through comments and likes. Registered users benefit from additional features such as comment management and personalization. Admins can efficiently manage menu items, reservations, and blog content via the Django admin panel. These features ensure a seamless and enjoyable experience for both users and administrators.


- - -

## Design
### Color Scheme

The **Ramen Bar** website employs a vibrant and appetizing color scheme designed to stimulate the senses and reflect the lively, flavorful experience of enjoying a bowl of ramen. The warm hues of orange (#F57C00), yellow (#FFC107), and red (#DC3545) dominate the palette, evoking energy, passion, and warmth, which are all integral to the dining experience. These colors not only capture the essence of the ramen culture but also enhance the appetite of visitors. The green (#28A745) offers a fresh contrast, symbolizing the wholesome and balanced ingredients often found in ramen dishes. 

Meanwhile, the cool blue (#17A2B8) adds a calming balance to the vibrant tones, maintaining visual harmony throughout the site. For the blog and text-heavy sections, dim gray (#696969) provides a neutral, easy-to-read foundation that complements the vivid colors without overwhelming the viewer. By incorporating Bootstrap’s default colors, the design achieves both consistency and a modern aesthetic, creating a visually delightful experience that mirrors the essence of Ramen Bar.

![color pallete](/documentation/curry-lovers-palette.webp)

### Brand Logo and Favicon

The Ramen Bar logo is a vibrant and inviting design that reflects the essence of the brand. Featuring a steaming bowl of ramen with chopsticks resting atop, the logo symbolizes the warmth and authenticity of Japanese ramen culture. The intricate details, including the colorful ingredients and dynamic presentation, evoke a sense of appetite and culinary artistry, perfectly aligning with the restaurant's mission.

The favicon, a simple yet bold "RB" in a warm orange and dim gray color scheme, complements the logo while providing a clean and professional representation of the brand in browser tabs and bookmarks. Together, the logo and favicon create a cohesive visual identity, enhancing the brand's recognition and appeal to ramen enthusiasts.

### Typography

The Ramen Bar website features Berkshire Swash for headings, infusing a touch of playfulness and charm into the design. This decorative serif font evokes the warmth and authenticity of a cozy ramen shop, making it the perfect choice for a casual dining experience. The flowing, hand-crafted appearance of Berkshire Swash reflects the artistry behind crafting a perfect bowl of ramen, tying the typography to the site's theme of comfort, culture, and delicious food.

![Berkshire Swash-title](/documentation/poppins-title.webp)

For body text, Open Sans ensures clarity and readability, creating a welcoming and approachable vibe for visitors. Its clean, modern style complements the dynamic Berkshire Swash headings, providing a harmonious balance between tradition and contemporary design. Together, these fonts enhance the inviting and casual feel of the Ramen Bar website, making it easy for users to explore menus, engage with blogs, and immerse themselves in the warm atmosphere of ramen culture.

![Open Sans](/documentation/roboto.webp)

### Imagery

The Ramen Bar website features high-quality images of steaming bowls of ramen, fresh ingredients, and inviting restaurant interiors to immerse users in the warm and flavorful world of ramen. These visuals are carefully chosen to evoke a sense of comfort and satisfaction, showcasing the vibrant colors, textures, and artistry that define this beloved dish. By integrating these enticing images throughout the site, the design not only enhances engagement but also captures the casual and welcoming atmosphere of a ramen bar, making every visitor feel closer to their next delicious meal.

### Wireframes
Here are the wireframes I have prepared to illustrate the user interface design across different devices—mobile, tablet, and desktop—ensuring a consistent and optimized user experience for each screen size.

`The Home Page`
![index](/documentation/index.png)

`The Philosophy Page`
![phylosophy](/documentation/philosophy.png)

`The Menu Page`
![menu](/documentation/menu.png)

`The Reservation Page`
![reservation](/documentation/reservation.png)

`The Contact Page`
![contact](/documentation/contact.png)

`The Blog Page`
![blog](/documentation/blog.png)

### Features 

The Ramen Bar website includes a variety of key pages, each designed to provide a seamless and engaging user experience:

![index](/documentation/index.webp)
* Home Page: Welcomes visitors with vibrant imagery, an overview of the new menu, our three pillars of mission, and quick access to essential features such as reservations and blogs.

![menu](/documentation/menu.webp)
* Menu Page: Displays a categorized list of ramen dishes, starters, and more, complete with descriptions, prices, and photos, allowing users to explore the offerings in detail.

![reservation](/documentation/reservation.webp)
* Reservation Page: Enables users to easily book a table with a simple form, complete with a confirmation message upon successful submission.

![blog](/documentation/blog.webp)
* Blog Page: Features articles on ramen culture, recipes, and the history of ramen, along with options for logged-in users to comment, edit, delete, and like posts.

![contact](/documentation/contact.webp)
* Contact Page: Provides a user-friendly contact form for inquiries, ensuring direct communication with the restaurant.

![cancellation](/documentation/cancellation.png)
* Reservation Cancellation Page: Allows users to cancel their reservations using a reservation number, ensuring flexibility and convenience.

![sign-in](/documentation/sign-in.webp)
![logout](/documentation/)
![sign-up](/documentation/sign-up.png)
* Authentication Pages: Includes login, signup, and account management options, offering secure access to personalized features.

![thank_you](/documentation/thank_you)
* Thank-You Page: Displays a confirmation message after successful actions like form reservations.

## Future Implementations 

The Ramen Bar website will be expanded with the following features to provide users with an even more engaging and comprehensive experience:

1. Newsletter Subscription
A dedicated newsletter feature will allow users to subscribe and receive updates on the latest menu items, blog posts, special events, and promotions directly in their inbox. This will help build a stronger connection with the community and keep users informed about all things Ramen Bar.

2. Blog Categories and Slugs
To enhance blog functionality, we plan to introduce categories and slugs. Users will be able to filter blog posts by topics such as "Ramen Recipes," "Ramen Culture," and "Travel in Japan." Additionally, unique slugs for each post will improve SEO and make it easier to share and access specific articles.

3. Ramen Build-a-Bowl Feature
A custom "Build-a-Bowl" interactive feature will allow users to virtually create their ideal ramen bowl by selecting broth, noodles, toppings, and protein options. This feature will educate users about different ramen components and could potentially integrate with reservations or takeout options in the future.

4. Interactive Map of Ramen Shops in Japan
An interactive map showcasing the best ramen shops in Japan, categorized by region, will be added. This feature will appeal to travel enthusiasts and ramen lovers alike, helping them explore Japan's rich ramen culture.


- - - 

## Technologies Used
### Languages Used

The Ramen Bar website is developed using a modern stack of web technologies to deliver a responsive, interactive, and visually appealing experience:

* HTML5: Used to structure the content and layout of the website, ensuring a semantic, accessible, and user-friendly design.
* CSS3: Employed to style the website with a cohesive color scheme, typography, and layout, creating a visually engaging and professional look.
* JavaScript: Utilized to enhance interactivity and add dynamic elements, such as responsive navigation menus, form validation, and other interactive features.
* Bootstrap: Integrated to streamline the development of a responsive design, ensuring that the website looks great on devices of all sizes and resolutions.
* Python: Powers the backend logic of the application, handling core functionality like data processing, user authentication, and server-side operations.
* Django: A robust framework used to manage the backend infrastructure, including database interactions, user management, and seamless integration of dynamic content.

### Frameworks, Libraries & Programs Used

* Balsamiq: Used to create wireframes, providing a clear visual representation of the site’s layout and structure before development began.
* GitHub: Utilized for version control, storing code, and collaboration during the development process.
* GitPod: The integrated development environment (IDE) used for writing, testing, and debugging code throughout the project.
* Google Fonts: Imported custom fonts, specifically Berkshire Swash and Open Sans, to enhance the site’s typography and visual appeal.
* Google Developer Tools: Leveraged for debugging, testing functionality, and ensuring responsiveness across different screen sizes.
* dbdiagram: Used to design and visualize the database structure, ensuring efficient relationships between tables, such as for reservations, users, menu items, blogs, and comments.
* Cloudinary: Served as the image hosting platform, enabling secure storage and optimization of images for the website.
* Favicon.io: Created the website favicon, adding a professional touch to the browser tab and enhancing brand recognition.
* Am I Responsive?: Verified how the site appears across various devices, showcasing the responsive design and ensuring a consistent user experience.
* Grammarly: Checked spelling and grammar across the site content, ensuring polished and professional text presentation.


- - - 

## Deployment & Local Development
### Repository Deployment via Heroku

To deploy the project live, Heroku was used. Here are the steps:

1. Create a New App

* Log into the Heroku dashboard and click New, then select Create New App from the dropdown menu.
* On the next page, enter the App Name and select a Region, then click Create App.

2. Configure the App Settings
* Navigate to the Settings tab and click Reveal Config Vars.
* Add the following configuration variables:
    * PORT: Set to 8000.
    * CLOUDINARY_URL: For image hosting.
    *DATABASE_URL: For connecting to the Postgres database.

3. Connect to GitHub

* Go to the Deploy tab and select GitHub – Connect to GitHub.
* Search for your repository by name and click Connect once located.

4. Deployment Method

* Choose between:
    * Manual Deployment: Deploy the app manually when ready by clicking the Deploy Branch button.
    * Automatic Deployment: Automatically redeploy the app whenever changes are pushed to the main branch on GitHub.

* Launch the Application
    * Once the build is complete, the app can be launched by clicking the Open App button that appears below the build information or in the top-right corner of the Heroku dashboard.


- - - 

### Updated Testing Section Summary

Here's a concise and polished version of your testing section for the README:

---

## Testing

Comprehensive testing was carried out to ensure the **Ramen Bar** website delivers a reliable and seamless user experience. Both automated and manual testing methods were employed:  

- **Automated Testing**: The HTML and CSS were validated using W3C Validator tools, while JavaScript was tested with JSHint to ensure compatibility and functionality. Lighthouse was used to analyze performance, accessibility, and best practices.  
- **Manual Testing**: All key features were rigorously tested, including reservations, cancellations, contact forms, authentication, and blog functionalities. The site was also tested across multiple devices and browsers to confirm responsiveness and usability.  

For a detailed breakdown of tests performed and results, please refer to [TESTING.md](/TESTING.md).  

### Solved Bugs

1. **Favicon Not Appearing on Deployed Website**  
   - **Issue**: The favicon was not displaying in the browser tab after deployment.  
   - **Fix**: Uploaded a `favicon.ico` file and added versioning to the favicon link to ensure browsers load the updated icon.

2. **ES6 Syntax Compatibility**  
   - **Issue**: The use of `const` triggered compatibility warnings in environments that don’t support ES6.  
   - **Fix**: Replaced the `const` keyword with `var` to ensure compatibility across all JavaScript environments.

--- 

- - - 

## Credits
### Code Used

The Ramen Bar website incorporates code from Code Institute’s Blog project, particularly for the structure and Bootstrap styling of the blog section. These elements were adapted and customized to align with the design and functionality needs of the site, ensuring a seamless and engaging user experience.

### Content


### Media 
This project includes images borrowed from the following sources:

- Photo-ac.com: images used in blog section 
- Unsplash: menu images, other pages

### Acknowledgments  
I would like to extend my heartfelt gratitude to Mr. Jubril Akolade, my mentor from Code Institute, for his invaluable guidance, encouragement, and insightful feedback throughout the development of this project. His expertise and support were instrumental in bringing this website to life.

I would also like to thank the tutors at Code Institute for their patience, assistance, and invaluable advice throughout the learning and development process. Their dedication and support have been essential to my growth as a developer.

A special thanks to my husband and my daughter for their unwavering support, constructive feedback, and encouragement during this journey. Their advice and suggestions greatly contributed to the success of this project.

