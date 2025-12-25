# Employee Management System using AWS EC2 (Ubuntu) & MySQL

A full-stack **Employee Management System** deployed on **AWS EC2 using Ubuntu**, built with **Python (Flask)** and **MySQL**.  
The application supports **role-based access**, **employee lifecycle management**, and a **modern web interface**.

---

## 📌 Project Overview

Managing employee records manually is inefficient and error-prone.  
This project provides a **cloud-based web application** to manage employee details such as:

- Employee information
- Role-based login (Admin / HR / Viewer)
- Employee status (Active / On Leave / Resigned)
- Secure SQL-based data storage

The system is hosted on **AWS EC2 (Ubuntu AMI)** and verified using real SQL queries.

---

## 🚀 Features

- 🔐 Login Authentication (Admin / HR / Viewer)
- 👥 Add and View Employees
- 🔄 Employee Status Management (Active, On Leave, Resigned)
- 🛂 Role-Based Access Control
- 🗄️ MySQL Database Integration
- 🎨 Modern, colorful UI using HTML & CSS
- ☁️ Deployed on AWS EC2 (Ubuntu)

---

## 🧱 System Architecture



User Browser
↓
Flask Web Application
↓
AWS EC2 (Ubuntu)
↓
MySQL Database


---

## 🛠️ Technologies Used

- **AWS EC2** – Cloud server
- **Ubuntu 22.04** – Operating System
- **Python 3** – Backend language
- **Flask** – Web framework
- **MySQL** – Relational database
- **HTML & CSS** – Frontend
- **Linux Commands** – Server management

---

## 📁 Repository Structure



employee-management-system-aws/
│
├── app.py
├── requirements.txt
├── README.md
│
├── templates/
│ ├── login.html
│ └── dashboard.html
│
├── sql/
│ ├── database.sql
│ └── sample_queries.sql
│
├── docs/
│ ├── Project_Report_Siva.docx
│ ├── Project_Report_Siva.pdf
│ ├── SQL_Commands_Siva.docx
│ └── Code_Document_Siva.docx
│
├── screenshots/
│ ├── login_page.png
│ ├── dashboard_page.png
│ ├── add_employee.png
│ └── sql_output.png
│
└── .gitignore


---

## ⚙️ Installation & Setup (Step-by-Step)

### 1️⃣ Launch EC2 (Ubuntu AMI)
- Create EC2 instance using **Ubuntu 22.04**
- Open ports: `22`, `5000`, `3306`

---

### 2️⃣ Connect to EC2
```bash
ssh -i key.pem ubuntu@<EC2_PUBLIC_IP>

3️⃣ Install System Packages
sudo apt update && sudo apt upgrade -y
sudo apt install python3 python3-pip python3-venv python3-full mysql-server -y

4️⃣ Create Virtual Environment
python3 -m venv venv
source venv/bin/activate

5️⃣ Install Python Libraries
pip install flask mysql-connector-python

6️⃣ MySQL Setup
sudo mysql

CREATE DATABASE employee_db;
USE employee_db;

CREATE TABLE employees (
  id INT AUTO_INCREMENT PRIMARY KEY,
  emp_code VARCHAR(30),
  name VARCHAR(100),
  department VARCHAR(50),
  email VARCHAR(100),
  salary INT,
  status VARCHAR(20)
);

CREATE TABLE users (
  username VARCHAR(50) PRIMARY KEY,
  password VARCHAR(100),
  role VARCHAR(20)
);

INSERT INTO users VALUES
('admin','admin123','ADMIN'),
('hr','hr123','HR'),
('viewer','view123','VIEWER');

CREATE USER 'empuser'@'localhost' IDENTIFIED BY 'emp@123';
GRANT ALL PRIVILEGES ON employee_db.* TO 'empuser'@'localhost';
FLUSH PRIVILEGES;

7️⃣ Run Application
python app.py


Open in browser:

http://<EC2_PUBLIC_IP>:5000

🔐 Login Credentials (Sample)
Username	Password	Role
admin	admin123	ADMIN
hr	hr123	HR
viewer	view123	VIEWER
📊 Sample SQL Queries
SELECT * FROM employees;
SELECT * FROM employees WHERE status='On Leave';
UPDATE employees SET status='Resigned' WHERE emp_code='EMP-IT-001';
SELECT COUNT(*) FROM employees;
