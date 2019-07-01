# App Awards

#### In this application you can showcase you projects to be viewed and voted for

#### By **Munge Kevin Oroko**

## Description
This is an application that allows users to showcase their projects. Other users can view all the projects posted, vote on them based on the design, usability and the content. Users are also able to view each others profile details and even search for specific projects.

## BDD Specifications
| User Requirements                  | Input                                                                                                                         | Output                                                                                                         |
|------------------------------------|-------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Sign up/Login                      | To create a new account click the sign up link and fill the form details To login click the login button and fill the details | If login is successful user is navigated to the home page                                                      |
| To add a newproject                | click the submit project tab on the navbar and submit your new project details.                                               | You will be navigated to a page where you can submit a new project.                                            |
| To Review a project                | Click on the review project button.                                                                                           | You will be navigated to a page with the project details where you can post your review.                       |
| To create a profile                | On the navbar click the profile tab and create new profile                                                                    | New profile for the user will be created                                                                       |
| To edit profile                    | On the profile page click the edit profile button, make the changes and submit                                                | Profile will be edited                                                                                         |
| To see all of your posted projects | Navigate to the profile page and all the details and project posts will be displayed.                                         | All the user's profile details will be displayed.                                                              |
| To view Users details              | Navigate to the project whose user you would like to see and click on their name.                                             | You will be redirected to a page with all the users details including their contact information.               |
| To search for a specific project   | input the project's name in the search bar on the navigation bar                                                              | You will be redirected to the projects with a matching name. click on the project you wish to view details of. |
| To view other all projects posted. | Navigate to the home page to view them all                                                                                    | All project posts will be displayed                                                                            |
| To log out                         | click the profile icon and then the logout link                                                                               | You will be logged out                                                                                         |

## Setup/Installation Requirements
* Ensure you have Installed Python3.6
* Clone the App-Awards Repository
* Create and Activate your virtual environment - `python3.6 -m venv --without-pip virtual` && `source virtual/bin/activate`
* Install dependencies - `pip install -r requirements.txt`
* Create a Database - `psql` then `CREATE DATABASE database name`
* Run Migrations - `python3.6 manage.py makemigrations database name` then `python3.6 manage.py migrate`
* Run the App - `python3.6 manage.py runserver`
* Application should open on `localhost:8000` 

## Known Bugs
There are currently no known bugs.

## Technologies Used
* Python 3.6
* Bootstrap
* Heroku
* HTML
* CSS
* Django

## Support and contact details
For more information, questions, or help using the program, get in touch with me on +254 707 280118 or email: orokomunge@gmail.com.

### License
MIT
Copyright (c) 2019 **Munge Kevin Oroko**
  