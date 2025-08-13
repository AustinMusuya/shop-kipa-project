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

- **Python 3.8+** (if using local venv)
- **Docker & Docker Compose** (if using containerized setup)
- **Git**
- **Virtual Environment** (optional if running with Docker)

---

## Setup Instructions

You can choose **one of two methods** to run Shop-Kipa:

---

### **Method 1 MacOS/Linux — Docker Compose (Recommended )**

1. **Clone the repository**

```bash
git clone https://github.com/AustinMusuya/shop-kipa-project.git
cd shop-kipa-project
```

2. **Create **``** file**

Copy the example and set your credentials:

```bash
cp .env_example .env
```

Example `.env`:

```env
POSTGRESQL_DB=shop_kipa_db
POSTGRESQL_USER=my_user
POSTGRESQL_PASSWORD=my_pass
DB_HOST=db
DB_PORT=5432
```

3. **Build and start containers**

**_a) Start Db container first_**

```bash
docker compose up  -d db
```

**_b) Start web container next_**

```bash
docker compose up  -d web
```

- This starts two containers:
  - **db**: PostgreSQL
  - **web**: Django app

4. **Apply migrations**

**_Run on a new terminal session_**

```bash
docker compose exec web python manage.py migrate
```

5. **Create a superuser**

```bash
docker compose exec web python manage.py createsuperuser
```

6. **Access the application**

- Django dev server: `http://127.0.0.1:8000/`
- Admin panel: `http://127.0.0.1:8000/admin/`

**Tips**

- Use `docker compose down -v` to reset containers and volumes.
- Docker Compose automatically handles database startup order.

---

### **Method 2 — Local Python Virtual Environment**

1. **Clone the repository**

```bash
git clone https://github.com/AustinMusuya/shop-kipa-project.git
cd shop-kipa-project
```

2. **Create a virtual environment**

- On Mac/Linux:

```bash
python3 -m venv venv
source venv/bin/activate
```

- On Windows:

```bash
python -m venv venv
venv\Scripts\activate
```

3. **Install dependencies**

```bash
pip install -r requirements.txt
```

4. **Configure the database**

- For MySQL:

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

- For SQLite (development):

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
```

5. **Apply migrations**

```bash
python manage.py makemigrations
python manage.py migrate
```

6. **Create a superuser**

```bash
python manage.py createsuperuser
```

7. **Run the development server**

```bash
python manage.py runserver
```

Access the app at: `http://127.0.0.1:8000/`

---

## How to Use

### Admin Features

1. Log in at `http://127.0.0.1:8000/admin/` using superuser credentials.
2. Manage:
   - Users: Add, edit, assign roles
   - Products: Update stock and reorder points
   - Suppliers: Track supplier info
   - Sales: Record and view sales details

### Default User Access

- Read-only by default; view inventory, suppliers, and sales.
- Admins can grant extra permissions via the admin panel.

---

## Testing

- Navigate through inventory, suppliers, sales sections.
- Test different user roles by logging in with multiple accounts.

---

## Contributing

1. Fork the repository
2. Create a new feature branch
3. Submit a pull request

---

## License

MIT License
