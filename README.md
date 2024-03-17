# <p style="text-align: center;">Elvira Espinoxa Ahumada</p>


![Logo]()

[Click here to view the live web application]()



## Index - Table of Content

- [User Experience (UX)](#user-experience-ux)
- [Design](#design)
- [Technologies Used](#technologies-used)
- [Features](#features)
- [Testing](#testing)
- [Deployment](#deployment)
- [Credits](#credits)

## User Experience (UX)

The site’s users want to play an online game that has elements of chance.
The site’s goal is to provide a challenging game with increasing levels of difficulty to entertain online users. 

### Project Goals

#### Agile Methodology

#### User stories 

### First time user

### Registered user

### Admin user

## Design

### Wireframes
Were created using Balsamiq. The sections below show individual wireframes for different devices:

- Desktop layout

![img]()

- Tablet layout

![img]()

- Smartphone layout

![img]()

### Database Scheme

### CRUD
CRUD functionality was implemented in both booking courses and commenting where:

- Create: An authenticated user can create a booking or leaving a comment.

- Read: A user can read the course information and comments .

- Update: An authenticated user can edit and update their own booked courses or comments.

- Delete: An authenticated user can delete their own booked courses or comments.

### Data Models


#### Allauth User Model
The User model was built using Django's Allauth library

## Technologies Used

### Languages

- [HTML](https://en.wikipedia.org/wiki/HTML5) - used for the main site content.
- [CSS](https://en.wikipedia.org/wiki/CSS) - used for the main site design and layout.
- [Python](https://en.wikipedia.org/wiki/Python_(programming_language)) - used as the back-end programming language.
- [JavaScript](https://en.wikipedia.org/wiki/JavaScript) - used for user interaction on the site for automatically closing 
Django Messages and to handle the notification dropdown and notification delete functions.   

## Frameworks, Libraries and  Tools

- [Am I Responsive](https://ui.dev/amiresponsive) - Used to verify responsiveness of website on different devices.

- [Bootstrap v5.3.2](https://getbootstrap.com/) - Used to help with the responsiveness of the site and to aid the coding of some of the layout

- [Balsamiq](https://balsamiq.com/) - Used to create the wireframes during the design process

- [Cloudinary](https://cloudinary.com/) - Used for online static file storage.

- [Django](https://www.djangoproject.com/)- Used as the Python framework for the site.

- [ElephantSQL](https://www.elephantsql.com/) - Used as the Postgres database.

- [Favicon.io](https://favicon.io/) - Used to create and add the favicon to the browser tab

- [Font Awesome](https://fontawesome.com/) - Used to add icons to the site for aesthetic and UX purposes.

- [GitHub](https://github.com/) - Used to store the project code after being created in GitPod 

- [Gitpod](https://www.gitpod.io/) - Used to create, edit & preview the project's code

- [Google Fonts](https://fonts.google.com/) - Used to import the 'xxxxxxxxxxxx' and 'xxxxxxxxxxxxxxx' fonts into the style. 
css file which are used on all pages of the project.

- [Heroku](https://dashboard.heroku.com/)- Used for hosting the deployed back-end site.

- [PostgreSQL](https://www.postgresql.org/) - Used as the relational database management.

- [Markdown Builder by Tim Nelson](xxxxxxxxxxxxx) - Used to help generate the Markdown files.

- [W3C](https://www.w3.org/) - Used for HTML & CSS Validation.

- [WAVE](https://wave.webaim.org/) - Used for Accessibility evaluation.

## Features
(Part of the base html)

### Nav Menu

![]()

### Footer

![]()

---------------

### Sign Up Page

![]()

### Login Page

![]()

### About section

![]()

### Services section

![]()


### Book and appointment

![]()

### List of user's appointments

![]()

### Edit appointments

![]()

### Delete appointments

![]()

### List of the latest reviews


![]()

### Pagination


![]()

### Add a review


![]()

### Edit reviews


 ![]()

### Delete reviews


![]()

### Log Out


![]()

### Admin Panel


![]()


## Feature Features
This is definitely a project I want to revisit in the future and add some extra features to......................................................

## Testing

### Validator testing

The website was tested using the tools made available by the World Wide Web Consortium, also known as "W3C".

The two tools used were the Markup Validation Service and the CSS Validation Service. Both tools were used to test the website by URL and also by direct input, with the results shown below.

No errors were returned for all HTML or CSS across all tests. Some warnings were displayed.

- HTML Validation by Direct Input
     
- CSS Validation by Direct Input

- JavaScript


### Manual testing

The site was tested manually across a range of devices to ensure all links and styling work correctly and to ensure responsiveness across a range of devices. All features on the page were tested, to ensure functionality was not impacted in any way. 

### Browser Compatibility

Testing was carried out on multiple browsers such as Google Chrome, Microsoft Edge, Mozilla Firefox, Brave,  Safari and Opera. Testing was carried out on an Apple iPhone, Apple iPhone 13, Samsung Galaxy S20 FE, Samsung Galaxy A51 and Apple iPad Pro.

### Lighthouse Testing

A test in all pages was ran using Lighthouse within Google Chrome to verify performance and accessibility standards were met and to ensure best practices were followed.
The full report can be viewed [here]().

#### Homepage

![]()

#### About / Services page

![]()

#### Book and appointment page

![]()

#### Reviews page

### Bugs Fixed

![]()

## Deployment 
This project was deployed using Github and Heroku.
The live deployed application can be found deployed on [Heroku](Add link herexxxxxxxxxxxxxxxx).

## Local Deployment
This project can be cloned or forked in order to make a local copy on your own system.

#### Forking the GitHub Repository
You can fork the repository by following these steps:

1. Go to the GitHub repository
2. Click on Fork button in upper right hand corner

#### Cloning the GitHub Repository

You can clone the repository to use locally by following these steps:

1. Navigate to the GitHub Repository you want to clone
2. Click on the code drop down button
3. lick on HTTPS
4. Copy the repository link to the clipboard
5. Open your IDE of choice (git must be installed for the next steps)
6. Type git clone copied-git-url into the IDE terminal

The project will now be cloned locally for you to use.

### ElephantSQL Database
This project uses ElephantSQL for the PostgreSQL Database.

To obtain your own Postgres Database, sign-up with your GitHub account, then follow these steps:

Click Create New Instance to start a new database.
Provide a name (this is commonly the name of the project: tribe).
Select the Tiny Turtle (Free) plan.
You can leave the Tags blank.
Select the Region and Data Center closest to you.
Once created, click on the new database name, where you can view the database URL and Password.

### Cloudinary API
This project uses the Cloudinary API to store media assets online, due to the fact that Heroku doesn't persist this type of data.

To obtain your own Cloudinary API key, create an account and log in.

1. For Primary interest, you can choose Programmable Media for image and video API.
2. Optional: edit your assigned cloud name to something more memorable.
3. On your Cloudinary Dashboard, you can copy your API Environment Variable.
4. Be sure to remove the CLOUDINARY_URL= as part of the API value; this is the key.

#### How to run the project locally 
Once the project is cloned or forked, in order to run it locally, you'll need to follow these steps:

1. Install any applicable packages found within the requirements.txt file.
pip3 install -r requirements.txt. 

If you have your own packages that have been installed, then the requirements file needs updated using:
pip3 freeze --local > requirements.txt

2. Create a new file called env.py in the main directory.
3. Add the DATABASE_URL value and your chosen SECRET_KEY and the Cloudinary URL to env.py file.

Sample env.py file:(Add picture xxxxxxxxxxxxxxxxxx)

4. Comment out the default database configuration.
5. Add the Cloudinary and all the rest of libraries you need to the list of installed apps in settings.py
6. Add the STATIC files settings - the url, storage path, directory path, root path, media url and default file storage path.
7. Link the file to the templates directory in Heroku.
8. Change the templates directory to TEMPLATES_DIR
9. Add Heroku to the ALLOWED_HOSTS list the format ['app_name.heroku.com', 'localhost']
10. Save all files and make necessary migrations. 
python3 manage.py makemigrations
11. Migrate the data to the database:
 python3 manage.py migrate
12. Create a superuser: 
python3 manage.py createsuperuser

Everything should be ready now, so run the Django app again: 
python3 manage.py runserver

### Heroku Deployment
This project uses Heroku, a platform as a service (PaaS) that enables developers to build, run, and operate applications entirely in the cloud.

Deployment steps are as follows, after account setup:
Make sure DEBUG = False in the settings.py

Heroku needs two additional files in order to deploy properly.

Create a new file in the main directory called Procfile (do not use any extension for the name of this file)
The Procfile can be created with the following command:

echo web: gunicorn app_name.wsgi > Procfile
replace app_name with the name of your primary Django app name; the folder where settings.py is located

1. Select New in the top-right corner of your Heroku Dashboard, and select Create new app from the dropdown menu.
2. Your app name must be unique, and then choose a region closest to you (EU or USA), and finally, select Create App.
3. From the new app Settings, click Reveal Config Vars, and set your environment variables.
(Add table with keys!!)


Go to the deploy tab on Heroku and connect to GitHub, then to the required repository. 

Scroll to the bottom of the deploy page and either click Enable Automatic Deploys for automatic deploys or Deploy Branch to deploy manually. Manually deployed branches will need re-deploying each time the GitHub repository is updated.
Click 'Open App' to view the deployed live site.

The project should now be connected and deployed to Heroku!

## Credits

### Acknowledgements

- The whole team at Code Institute for their teaching and support.
