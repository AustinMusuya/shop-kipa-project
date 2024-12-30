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
Prerequisites
Python 3.8+: Ensure Python 3.8 or higher is installed.
MySQL (For production): MySQL is required for production deployment. SQLite can be used for local development.
Virtual Environment: Recommended to isolate dependencies.
Setup Instructions
1. Clone the Repository
bash
Copy code
git clone https://github.com/AustinMusuya/shop-kipa-project.git
cd shop-kipa-project
2. Create a Virtual Environment
bash
Copy code
python3 -m venv venv
source venv/bin/activate   # On Windows use: venv\Scripts\activate
3. Install Dependencies
bash
Copy code
pip install -r requirements.txt
4. Configure the Database
Set up your MySQL database (or use SQLite for development) and update the database configuration in shop_kipa_project/settings.py:

python
Copy code
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'shop_kipa_db',
        'USER': 'your-username',
        'PASSWORD': 'your-password',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
5. Apply Migrations
bash
Copy code
python manage.py migrate
6. Create a Superuser (Admin)
bash
Copy code
python manage.py createsuperuser
7. Run the Development Server
bash
Copy code
python manage.py runserver
The app will be available at http://127.0.0.1:8000/.

How to Use
Admin Features
Log in to the admin panel at http://127.0.0.1:8000/admin/ using the superuser credentials.
Manage:
Users: Add, edit, and assign roles.
Products: Add new inventory items, update stock levels, and set reorder points.
Suppliers: Track supplier details and associated products.
Sales: Record and view sales details.
Default User Access
Default users have read-only access. They can view:
Product inventory.
Supplier information.
Sales history.
Admins can grant additional permissions via the admin panel.

Testing
To ensure the app is functioning correctly:

Navigate to various sections (inventory, suppliers, sales) via the admin panel or frontend views.
Test user roles by logging in with accounts that have different permission levels.
Contributing
If you'd like to contribute to Shop-Kipa:

Fork the repository.
Create a new feature branch.
Submit a pull request.
License
This project is licensed under the MIT License.

For any issues or feedback, feel free to reach out!