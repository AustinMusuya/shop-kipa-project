
# Shop-Kipa Project

**Shop-Kipa** is a Django-based Inventory Management System designed for shopkeepers to manage their inventory, sales, and suppliers efficiently. It allows administrators to add users, assign roles, and grant permissions, while general users have read-only access by default.

## Features

### 1. **User Management**
   - Admin users can create new users and assign roles.  
   - Default users have view-only access but can be granted additional permissions.

### 2. **Inventory Management**
   - Manage a catalog of products with details like name, category, stock, and reorder levels.

### 3. **Supplier Management**
   - Track supplier details and their provided goods.

### 4. **Sales Tracking**
   - Record and track sales by product, date, and customer details.

### 5. **Permission System**
   - Fine-grained permission system with read-only by default for new users.

## Prerequisites

- **Python 3.8+**: Ensure Python 3.8 or higher is installed.
- **MySQL (For production)**: MySQL is required for production deployment. SQLite can be used for local development.
- **Git**: Recommended for version control. (You can install from the official git website)
- **Virtual Environment**: Recommended to isolate dependencies.

## Setup Instructions

### 1. Clone the Repository

Clone the repository to your local machine:

Terminal

```bash
git clone https://github.com/AustinMusuya/shop-kipa-project.git
cd shop-kipa-project
```

### 2. Create a Virtual Environment

Create and activate a virtual environment:

Terminal

```bash
# On Mac or Linux use: 
python3 -m venv venv
source venv/bin/activate   

# On Windows use: 
python -m venv venv
venv/Scripts/activate
```

### 3. Install Dependencies

Install the required Python packages:

Terminal

```bash
pip install -r requirements.txt
```

### 4. Configure the Database

Set up your MySQL database or SQLite for development and update the database configuration in 
`shop_kipa_project/settings.py`:


For MySQL Database settings:

```python
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
```
OR

For SQLite Database settings:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
```

### 5. Apply Migrations

Run the migrations to set up the database schema:

Terminal

```bash
python manage.py migrate
```

### 6. Create a Superuser (Admin)

Create a superuser to manage the app via Django admin:

Terminal

```bash
python manage.py createsuperuser
```

### 7. Run the Development Server

Start the Django development server to test the app:

Terminal

```bash
python manage.py runserver
```

The app will be available at `http://127.0.0.1:8000/`.

## How to Use

### Admin Features

1. **Log in** to the admin panel at `http://127.0.0.1:8000/admin/` using the superuser credentials.  
2. **Manage**:
   - **Users**: Add, edit, and assign roles.  
   - **Products**: Add new inventory items, update stock levels, and set reorder points.  
   - **Suppliers**: Track supplier details and associated products.  
   - **Sales**: Record and view sales details.

### Default User Access

- Default users have read-only access. They can view:
  - Product inventory
  - Supplier information
  - Sales history

- Admins can grant additional permissions via the admin panel.

## Testing

To ensure the app is functioning correctly:

- Navigate to various sections (inventory, suppliers, sales) via the admin panel or frontend views.
- Test user roles by logging in with accounts that have different permission levels.

## Contributing

If you'd like to contribute to **Shop-Kipa**:

1. Fork the repository.
2. Create a new feature branch.
3. Submit a pull request.

## License

This project is licensed under the MIT License.

For any issues or feedback, feel free to reach out!