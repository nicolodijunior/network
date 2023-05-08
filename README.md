# README

This is a social network project for CS50 Web programming course. The project is developed using Django, HTML, CSS, and JavaScript.

#### Project Description

The social network allows registered users to create posts, follow other users, and like posts. Below are the requirements and features of the project:

    Create new text-based posts.
    Display all posts from all users with the most recent posts first.
    Display the profile page of a user with the number of followers and followed users and all posts for that user, in reverse chronological order. The profile page should also allow users to follow or unfollow other users.
    Display posts made by the users that the current user follows.
    Implement pagination to display only 10 posts per page.
    Allow users to edit their posts using JavaScript.
    Ensure that it is not possible for a user to perform actions that are not allowed.

#### How to run the project

    0. Install Django
    run pip3 install Django in your terminal to install Django (you’ll also have to install pip)
    
    1. Clone the repository
    git clone https://github.com/<username>/cs50w-network.git

    2. Navigate to the project directory
    cd cs50w-network

    3. Create database tables
    python manage.py makemigrations
    python manage.py migrate
    
    4. Run the server
    python manage.py runserver

    5. Open the application 
    In a browser, visit http://127.0.0.1:8000/

#### File structure

The project has a file structure similar to the Django Project structure:

    network/: This directory contains the code for the social network application.
    network/static/: This directory contains the static files for the project, such as CSS and JavaScript files.
    network/templates/: This directory contains the HTML templates for the project.
    network/forms.py: This file contains the forms used in the project.
    network/models.py: This file contains the models for the project.
    network/tests.py: This file contains the tests for the project.
    network/urls.py: This file contains the URL routing for the project.
    network/views.py: This file contains the views for the project.
    project4/settings.py: This file contains the project settings.
    project4/urls.py: This file contains the URL routing for the project.
    requirements.txt: This file contains the required Python packages for the project.

#### Additional notes

    This was my frist project using javascript, django and css grid and flex. The project is developed using Django v3.2.8 and Python v3.9.7.
