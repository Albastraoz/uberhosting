## Uber hosting.

After the 3th milestoneproject with Flask I helped some friends with finding a decent hosting provider.
This gave me the idea to create a hosting providers website which I can build out into a fully functional platform later.
The goal is to have the option to buy and choose a hosting service and find information (news items) about what has changes.
So far the website has a good look and is ready to use while there is still a wide area to explore and include into the project.

To get admin access to the website use the following login:
username: admin
password: admin123

Hosted on [Heroku](https://uber-hosting.herokuapp.com/)
Repository on [GitHub](https://github.com/Albastraoz/uberhosting)

## UX

![Responsive Views of website](/static/images/responsive.jpg)

### Users 
Expected users of the website are people who want to host their website somewhere.

### User Stories
1. Companies with websites who have big databases
2. User looking for a place to host their smaller ecommerce website or portfolio
3. Owner of website to post news and look for order information
4. Contact support to find out more about hosting

### Design
![Website Logo - Uber](/static/images/logo.png)
- Colour scheme is green with black which gives a more darker feeling which is easy to read but still stands out.
    - Main green colour:   ![#10DE0C](https://placehold.it/15/#10DE0C/000000?text=+) `#10DE0C`
    - Black has been used as other main color to give a more darker 'nerdy' look.
    - Grey and white colours have been used to create visible difference
- [Custom designed logo](/static/images/logo.png) created using the following font: 
    - font-family: 'Rubik Mono One Regular';
- Roboto and Krona One font used throughout the website
    - font-family: 'Roboto', sans-serif; - All text.
    - font-family: 'Bowlby One SC', cursive; - Only h1 titles.

### Mockups
The website consists of several pages each with a unique section of information:
- [Homepage](https://www.figma.com/file/MwkIV0SytxIA0Z10rodsq4/Uber-Hosting?node-id=0%3A1)   

## Features

Features planned, implemented and outlined for later development 

### Planned Features
- Documentation - ReadMe File & Mockups
- Website content
- Contact form
- Colour Scheme
- Custom Logo
- SQL database
    - CRUD for news posts
    - Editable user profiles
    - Order lists
    - CRUD news items (admin)
- Bootstrap - HTML, CSS Framework
    - Grid System - Columns and Rows
    - Icons
- User register/login database
    - Password reset
    - Profile information
- News posts
- Chat function
- Customisation function for packages
- Packages system to sell package hosting deals
- Stripe API
- CMS system for content (admin)
- Responsive design - Mobile First
- Accesibility
- Git - Version Control System
- GitHub - Remote Repository
- Deployed - Hosted on Heroku

### Existing Features
- Documentation - ReadMe File & Mockups
- Website content
- Contact form
- Colour Scheme
- Custom Logo
- SQL database
    - CRUD for news posts
    - Editable user profiles
    - Order lists
    - CRUD news items (admin)
- Bootstrap - HTML, CSS Framework
    - Grid System - Columns and Rows
    - Icons
- User register/login database
    - Password reset
    - Profile information
- News posts
- Packages system to sell package hosting deals
- Stripe API
- Responsive design - Mobile First
- Accesibility
- Git - Version Control System
- GitHub - Remote Repository
- Deployed - Hosted on Heroku

### Features Left to Implement
- CMS system for content (admin)
- Chat function
- Customisation function for packages

## Technologies Used

This project makes use of:
- [HTML](https://developer.mozilla.org/en-US/docs/Web/HTML)
    - HTML for basic strucutre
- [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
    - CSS for Styling
- [Bootstrap](https://getbootstrap.com/)
    - HTML and CSS Framework from **Bootstrap**
- [Javascript](https://www.w3schools.com/jsref/)
    - JavaScript for game application
- [jQuery](https://jquery.com/)
    - The project uses JQuery to simplify DOM manipulation
- [Visual Studio Code](https://code.visualstudio.com/)
    - Changed to local workspace where I used VS Code as editor
- [Python](https://www.python.org/)
    - Project runs on Python
- [Django](https://www.djangoproject.com/)
    - Django framework is used for website functionality
- [AtlasMongoDB](https://www.postgresql.org/)
    - A PostgreSQL database is used to store information
- [Google Chrome](https://www.google.com/chrome/)
    - Used for browser and dev tools
- [Mozilla Firefox](https://www.mozilla.org/en-US/firefox/new)
    - Used for browser and dev tools
- [Google](https://www.google.com/)
    - **Google** was used for research.
- [Git](https://git-scm.com/)
    - **Git** used for Version Control
- [GitHub](https://github.com/)
    - Repository hosted on **GitHub**
- [Heroku](https://www.heroku.com)
    - Website hosted on **Heroku**
- [Am I Responsive](http://ami.responsivedesign.is)
    - Testing responsiveness of the website

## Testing

The website was tested by users, Chrome/Firefox dev tools and for errors on W3.

### User experience testing 
Preview was send regularly to people within my social circle and asked for testing.

1. Sending website location to specific users over messaging.
2. Write down feedback.
3. Search for possible fixes.
4. If possible implement solution to error or improve product.

### Dev tools
- Everything has been tested and works correctly except for some minor bugs.

### Coding error testing
After complete product start to addres coding errors:

1. Go to W3's validation websites [HTML](https://validator.w3.org) or [CSS](https://jigsaw.w3.org/css-validator/).
2. Fill in URL of every specific page and look for errors.
3. Locate errors and solve accordingly.
4. After all errors are solved go back to step 1 and continue untill no errors are shown.

## Deployment

The project is hosted on [Heroku](https://uber-hosting.herokuapp.com/)
 
To deploy your own version of the website:
- Have git installed
- Visit the [repository]([GitHub](https://github.com/Albastraoz/uberhosting))
- Click 'Clone or download' and copy the code for http
- Open your chosen IDE (Cloud9, VS Code, etc.)
- Open a terminal in your root directory
- Type 'git clone ' followed by the code taken from github repository
    - ```git clone https://github.com/Albastraoz/uberhosting.git```
- Install all dependencies from the requirements.txt file
- When this completes you have your own version of the website
    - Feel free to make any changes to it
- The website can be run by opening one of the HTML files within a web browser
- Visit the link provided
- Your website with any made changes will appear
- Saved changes to the website will appear here after refreshing the page

The benefits of hosting your website on Heroku through Github is that any pushed changes to your project will automatically update the website. Development branches can be created and merged to the master when complete.

It may take a moment for changes to appear on the hosted website.

## Credits

### Content
The text on the website has been written myself or copied and edited from:  
- [Wikipedia](https://www.wikipedia.org/)

All icons are imported from Fontawesome:
- [Fontawesome](http://www.fontawesome.com/)

Fonts are imported from Google fonts:
- [Google Fonts](https://fonts.google.com/)

### Media
The images for the website are copyright free and taken from:
- [Wikipedia](https://www.wikipedia.org/)
- [Pexels](https://www.pexels.com/)
- [Needpix](https://www.needpix.com/)
- [Flickr](https://www.flickr.com/)

All images direct location:
- [intro.jpg](https://www.needpix.com/photo/619074/planet-earth-globe-space-world-continents-blue-light)
- [datacenter.jpg](https://commons.wikimedia.org/wiki/File:Wikimedia_Foundation_Servers-8055_35.jpg)
- [aboutus.jpg](https://www.pexels.com/photo/analysis-brainstorming-business-business-group-466733/)
- [contact.jpg](https://www.flickr.com/photos/ervins_strauhmanis/14562090039)
- [newspaper.jpg](https://www.pexels.com/photo/folded-newspapers-158651/)

### Acknowledgements
Thank you to the following for inspiration, motivation and the direction I needed:

- Seun Owonikoko    @seun_mentor
- Yung-Chin Huang
- Code Institute
- Pretty Printed - great tutorials
- Google - your best friend
