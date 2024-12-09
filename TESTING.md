# Ramen Bar - Testing
![Ramen Bar](/documentation/home-page.webp)

Welcome to the testing documentation for the Ramen Bar website. As a student developer, I have dedicated my efforts to creating a high-quality, user-friendly platform for ramen enthusiasts to explore and make reservations. Built using HTML, CSS, Bootstrap, JavaScript, Python, and Django, this project integrates modern web development tools to deliver a seamless experience. This document provides an overview of the testing strategies and methodologies I employed to ensure the functionality, performance, and responsiveness of the site. From verifying design consistency across devices to ensuring smooth reservation workflows and debugging complex interactions, this guide outlines the steps taken to make the Ramen Bar website an enjoyable and reliable platform for every visitor.

Visit the site here: [CURRY LOVERS](https://micmic210.github.io/curry-lovers/index.html)

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

`User Story 1: As a new visitor, I want to learn about Japanese curry so that I can understand its cultural significance and history.`

Goal: To provide a comprehensive overview of Japanese curry, including its origins and cultural importance.

How it is Achieved: 
* The History Page provides detailed content on the origins and cultural background of Japanese curry.
* Clear navigation from the Home Page directs users to the History section, ensuring easy access to information.
* Engaging imagery and well-organized content make it easy for users to absorb the information.

`User Story 2: As a home cook, I want to find easy-to-follow Japanese curry recipes so that I can try making them at home.`

Goal: To offer a variety of user-friendly recipes with clear instructions and ingredient lists.

How it is Achieved:
* The Recipes Page includes multiple recipes, each with step-by-step instructions and ingredient lists.
* Users can filter recipes by ingredients and cooking time, making it easy to find recipes that suit their needs.
* Recipes are presented in a clear, organized format, with high-quality images to guide users through the cooking process.

`User Story 3: As a member, I want to join a community of curry lovers so that I can share my experiences and learn from others.`
	
Goal: To provide a platform where users can connect, share, and engage with others.

How it is Achieved:
* The Memberships Page offers an easy signup process and outlines the benefits of joining the community.
* Members have access to exclusive content and can participate in forums or comment on recipes.
* The site includes features like a Thank-you page to acknowledge new members, reinforcing a sense of community.

- - - 

### Full Testing 

To ensure the Curry Lovers website is fully responsive and functions correctly across various devices, the following devices were used for testing:

Desktop and Laptop
* Windows 10/11 - Google Chrome, Microsoft Edge
* macOS - Safari, Google Chrome

Tablets
* iPad (air, pro) - Safari, Google Chrome

Smartphones
* iPhone (12 Pro, 14 Pro Max) - Safari, Google Chrome
* Samsung Galaxy S series - Google Chrome


The “CURRY LOVERS” website was thoroughly tested across various pages, ensuring that all key features, including navigation, content display, form validation, and error handling, functioned correctly. Below are the detailed test results for each page:

`Home Page`

| Feature| Expected Outcome | Pass/Fail |
| --- | --- | --- |
| Navigation to History and Recipes | Links on the homepage successfully direct users to the history and recipes sections. | PASS |
| Gallery Images | The images in the gallery correctly link to the specific sections of the recipe page. | PASS |
| Header Navigation | The header contains links to the Home, History, Recipes, and Membership pages, all of which work correctly. | PASS |
| Footer Links | The footer contains links to social networks, which correctly redirect to the respective sites. | PASS |

`History Page`

| Feature| Expected Outcome | Pass/Fail |
| --- | --- | --- |
| Content Display | The page correctly displays detailed information about the history of Japanese curry. | PASS |
| Header Navigation | The header navigation links work correctly. | PASS |
| Footer Links | The footer links to social networks work as intended. | PASS |

`Recipe Page`

| Feature| Expected Outcome | Pass/Fail |
| --- | --- | --- |
| Recipe Content Display | The page correctly displays the content of various recipes, including ingredients and preparation steps. | PASS |
| Header Navigation | The header navigation links work correctly. | PASS |
| Footer Links | The footer links to social networks work as intended. | PASS |

`Membership Page`

| Feature| Expected Outcome | Pass/Fail |
| --- | --- | --- |
| Form Validation | The membership form correctly prevents submission when required fields are empty. | PASS |
| Successful Submission | On successful submission, the form redirects to the thank-you page. | PASS |
| Header Navigation | The header navigation links work correctly. | PASS |
| Footer Links | The footer links to social networks work as intended. | PASS |

`Thank-you Page`

| Feature| Expected Outcome | Pass/Fail |
| --- | --- | --- |
| Thank-You Message | The page correctly displays a thank-you message after form submission. | PASS |
| Back Home Button | The “Back Home” button successfully redirects to the homepage. | PASS |
| Header Navigation | The header navigation links work correctly. | PASS |
| Footer Links | The footer links to social networks work as intended. | PASS |

`404 Page`

| Feature| Expected Outcome | Pass/Fail |
| --- | --- | --- |
| Error Handling | The 404 error page displays when navigating to a non-existent page. | PASS |
| Back Home Button | The “Back Home” button successfully redirects to the homepage. | PASS |