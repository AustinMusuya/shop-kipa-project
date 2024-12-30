Shop-Kipa Project
Shop-Kipa is a Django-based Inventory Management System designed for shopkeepers to manage their inventory, sales, and suppliers efficiently. It allows administrators to add users, assign roles, and grant permissions, while general users have read-only access by default.

Features
User Management:

Admin users can create new users and assign roles.
Default users have view-only access but can be granted additional permissions.
Inventory Management:

Manage a catalog of products with details like name, category, stock, and reorder levels.
Supplier Management:

Track supplier details and their provided goods.
Sales Tracking:

Record and track sales by product, date, and customer details.
Permission System:

Fine-grained permission system with read-only by default for new users.

Setup Instructions
Prerequisites
Python 3.8+
Make sure Python 3.8 or later is installed on your machine.

MySQL (For production deployment)
You can install MySQL locally or use an external service.

Virtual Environment (Recommended)
Use a virtual environment to manage dependencies and keep your project isolated from other Python projects.

Steps to Set Up the Project
Clone the Repository

Clone the repository to your local machine:

git clone https://github.com/AustinMusuya/shop-kipa-project.git
cd shop-kipa-project

Create a Virtual Environment

Create & activate a Virtual Environment

 python3 -m venv venv
 source venv/bin/activate   # On Windows use: venv\Scripts\activate
Install Dependancies

Install the required Python packages:

 pip install -r requirements.txt
Configure the Database

Set up your MySQL database (or SQLite for development). Update the DATABASES configuration in event_project/settings.py with the correct credentials.

DATABASES = { 'default': { 'ENGINE': 'django.db.backends.mysql', 'NAME': 'shop_kipa_db', 'USER': 'your-username', 'PASSWORD': 'your-password', 'HOST': 'localhost', 'PORT': '3306', } }

Apply Migrations

Run the migrations to set up the database schema:

 python manage.py migrate

Create a Superuser (Admin)

Create a superuser to manage the app via Django admin:

 python manage.py createsuperuser

Run the Development Server

Start the Django development server to test the API:

 python manage.py runserver

 The App should now be running at http://127.0.0.1:8000/.

Testing the API

To test the API, use tools like Rest Client, Postman or CURL, or navigate to the API endpoints. For example:

GET /api/events/list-event - List all events GET /api/events/ - get details for a specific event GET /api/events/upcoming - list upcoming events POST /api/users/register/- Register a new user POST /api/users/login/ - Log in to the API (using token-based authentication) POST /api/events/create-event - Create a new event