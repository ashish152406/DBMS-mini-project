from flask import Flask, render_template
from database import get_db_connection
import os
app = Flask(__name__)
app = Flask(__name__, template_folder='../frontend/templates', static_folder='../frontend/static')
# Homepage
@app.route('/')
def index():
    return render_template('index.html')


# View Patients
@app.route('/patients')
def view_patients():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM patients")
    patients = cursor.fetchall()
    conn.close()
    return render_template('view_patients.html', patients=patients)

# View Doctors
@app.route('/doctors')
def view_doctors():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM doctors")
    doctors = cursor.fetchall()
    conn.close()
    return render_template('view_doctors.html', doctors=doctors)

# View Appointments
@app.route('/appointments')
def view_appointments():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("""
        SELECT a.appointment_id, p.name AS patient_name, d.name AS doctor_name, 
               a.appointment_date, a.appointment_time, a.status
        FROM appointments a
        JOIN patients p ON a.patient_id = p.patient_id
        JOIN doctors d ON a.doctor_id = d.doctor_id
    """)
    appointments = cursor.fetchall()
    conn.close()
    return render_template('view_appointments.html', appointments=appointments)

# View Departments
@app.route('/departments')
def view_departments():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM departments")
    departments = cursor.fetchall()
    conn.close()
    return render_template('view_departments.html', departments=departments)

# View Medicines
@app.route('/medicines')
def view_medicines():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM medicines")
    medicines = cursor.fetchall()
    conn.close()
    return render_template('view_medicines.html', medicines=medicines)

if __name__ == '__main__':
    app.run(debug=True)
