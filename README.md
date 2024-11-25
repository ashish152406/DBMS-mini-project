# DBMS-mini-project
Hospital Management System
Project Overview
The Hospital Management System (HMS) is a web-based application developed using Flask (Python framework) and MySQL database to manage hospital operations. It allows users to view and manage hospital-related information such as patients, doctors, appointments, departments, and medicines.
### 1. Clone the Repository
Clone this repository to your local machine:
git clone <repository_url>
cd hospital-management-system
Features
Patient Management: View and manage patient details.
Doctor Management: View and manage doctor profiles.
Appointment Scheduling: Schedule and manage patient appointments.
Department Management: View and manage hospital departments.
Medicine Management: View and manage available medicines.

Technologies Used
Frontend: HTML, CSS, JavaScript
Backend: Python (Flask)
Database: MySQL
Icon Library: FontAwesome (for icons)
Version Control: Git

Prerequisites
Before running this project, ensure you have the following installed:
Python 3.x
MySQL Database
Flask
pip (Python package manager)
You can install the necessary Python libraries using:

bash
Copy code
pip install -r requirements.txt
Installation

bash
cd hospital_management_system
Set up the MySQL database:

Create a database named hospital_db in MySQL:

sql
Copy code
CREATE DATABASE hospital_db;
Run the SQL commands to create the necessary tables (as provided in your previous setup).

Set up the Flask environment:

Install Flask and other required Python libraries:

bash:
pip install flask flask-mysqldb
Set up the Flask app in the backend/app.py file and configure the MySQL connection in config.py.

Run the Flask Application:

Run the Flask app:

bash
python backend/app.py
Access the application at http://127.0.0.1:5000/ in your web browser.


hospital_management_system/
│
├── backend/
│   ├── app.py               # Flask application
│   ├── config.py            # Configuration for database and app settings
│   └── database.py          # MySQL connection settings
│
├── frontend/
│   ├── templates/           # HTML files
│   │   ├── index.html       # Homepage
│   │   ├── view_patients.html
│   │   ├── view_doctors.html
│   │   ├── view_appointments.html
│   │   ├── view_departments.html
│   │   ├── view_medicines.html
│   └── static/              # Static files (CSS, JS)
│       ├── styles.css       # Main styles
│
├── requirements.txt         # Python dependencies
└── README.md                # Project description
