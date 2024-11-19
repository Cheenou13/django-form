# Parking Logs Application

A Django-based application that allows users to log encounters with parking checkers and view the history of parking tickets by day and region.

---

## Features

- **Log Tickets**: Users can log parking ticket details, including date/time, street address, and region.
- **View Ticket History**: Users can filter and view tickets by region and day of the week.
- **Responsive Design**: Optimized for mobile devices.

---

## Project Structure
project/ ├── parking_logs/ # Main Django app │ ├── templates/ # HTML templates │ ├── models/ # Models for the database │ ├── views/ # Views for the application │ ├── static/ # Static files (CSS, JavaScript) │ └── style.css # Main stylesheet ├── db.sqlite3 # SQLite database file ├── manage.py # Django's management script ├── static/ # Project-wide static folder └── README.md

# Project documentation

---

## Prerequisites

Before running the project, ensure you have the following installed:

- **Python** (>= 3.8)
- **Django** (>= 5.0.1)
- A virtual environment tool (optional but recommended)

---

## Setup Instructions

### 1. Clone the Repository

```bash
git clone <repository-url>
cd project-directory
```


### 2. Create a Virtual Environment
## Linux/macOS:

```bash
python -m venv venv
source venv/bin/activate
```

## Windows:

```bash
python -m venv venv
venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Apply Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Run the Server

```bash
python manage.py runserver
```

## The server will be available at: http://127.0.0.1:8000/

