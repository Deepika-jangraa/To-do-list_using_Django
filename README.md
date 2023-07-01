# To-do-list_using_Django
Django Todo List
Django Todo List is a web application that allows users to manage and organize their tasks. Users can create, update, and delete tasks, mark tasks as completed, and filter tasks based on different criteria.

Features
User registration and authentication system for secure access to the application.
Create, update, and delete tasks.
Mark tasks as completed or pending.
Filter tasks based on completion status, priority, or due date.
User-friendly interface with intuitive task management.
Technologies Used
Django: High-level Python web framework for building robust web applications.
Python: Programming language used for the backend logic and data manipulation.
HTML/CSS: Front-end technologies for creating the user interface and styling the application.
SQLite: Lightweight relational database used for storing task data.
Bootstrap: Front-end framework for responsive and visually appealing design

Setup
Ensure you have Python and Django installed on your machine.
Clone this repository or download the source code to your local machine.
Open a terminal and navigate to the project folder.
Create a virtual environment to isolate project dependencies (optional but recommended).
Install the required packages and dependencies by running pip install -r requirements.txt.
Apply database migrations by running python manage.py migrate.
Start the Django development server with python manage.py runserver.
Open your web browser and visit http://localhost:8000 to access the application.
Usage
Register a new user account or log in with existing credentials.
Once logged in, you will be redirected to the Todo List dashboard.
Use the form at the top to create a new task by entering the task details and clicking "Add Task".
Existing tasks will be displayed below the form.
To mark a task as completed, click the checkbox next to the task.
To update a task, click the "Edit" button and modify the task details.
To delete a task, click the "Delete" button.
Use the filter options at the top to filter tasks based on completion status, priority, or due date.

File Structure
manage.py: Django management script for running development server, database migrations, and other commands.
todoapp/: Main Django project directory.
settings.py: Configuration file for Django project settings, including database connection and installed apps.
urls.py: URL configuration for the project, including routes to different views and templates.
views.py: Contains the logic and functions for handling HTTP requests and rendering templates.
models.py: Defines the database models for tasks and users.
templates/: Contains HTML templates for rendering the user interface.
static/: Directory for static files such as CSS stylesheets, JavaScript files, and images.
License
This project is licensed under the Deepika-jangraa License.

Feel free to modify and adapt the code for your needs. Happy task management!
