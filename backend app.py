from flask import Flask, render_template, request, redirect
import mysql.connector

app = Flask(__name__)

# MySQL connection
db = mysql.connector.connect(
    host="localhost",
    user="empuser",
    password="emp@123",
    database="employee_db"
)
cursor = db.cursor()

# ---------------- DASHBOARD ----------------
@app.route("/dashboard")
def dashboard():
    user = request.args.get("user", "admin")
    role = request.args.get("role", "ADMIN")

    cursor.execute("SELECT * FROM employees")
    employees = cursor.fetchall()

    return render_template(
        "dashboard.html",
        user=user,
        role=role,
        employees=employees
    )

# ---------------- ADD EMPLOYEE ----------------
@app.route("/add_employee", methods=["POST"])
def add_employee():
    user = request.args.get("user")
    role = request.args.get("role")

    if role != "ADMIN":
        return "Access Denied"

    name = request.form["name"]
    department = request.form["department"]
    email = request.form["email"]
    salary = request.form["salary"]
    status = request.form["status"]

    cursor.execute("SELECT COUNT(*) FROM employees")
    count = cursor.fetchone()[0] + 1

    emp_code = f"EMP-{department[:2].upper()}-{count:03d}"

    cursor.execute(
        """
        INSERT INTO employees
        (emp_code, name, department, email, salary, status)
        VALUES (%s, %s, %s, %s, %s, %s)
        """,
        (emp_code, name, department, email, salary, status)
    )
    db.commit()

    return redirect(f"/dashboard?user={user}&role={role}")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
