# 🚚 TransitOps – Smart Fleet Management System

## 📌 Overview

TransitOps is a web-based Fleet Management System developed using **Flask** to help logistics companies efficiently manage their daily operations.

The system provides a centralized platform to manage vehicles, drivers, trips, maintenance records, fuel logs, operational expenses, and business reports through an intuitive dashboard.

---

## ✨ Features

- 🔐 User Authentication (Login & Registration)
- 🚚 Vehicle Management
- 👨‍✈️ Driver Management
- 🛣️ Trip Management
- 🔧 Maintenance Management
- ⛽ Fuel Log Management
- 💰 Expense Tracking
- 📊 Reports & Dashboard
- 📈 Fleet Statistics
- 💾 SQLite Database Integration
- 🎨 Responsive Bootstrap UI

---

## 🛠️ Tech Stack

### Backend
- Flask
- SQLAlchemy
- Flask-Login

### Frontend
- HTML
- CSS
- Bootstrap 5
- Jinja2 Templates

### Database
- SQLite

---

## 📂 Project Structure

```
TransitOps/
│
├── app/
│   ├── auth/
│   ├── dashboard/
│   ├── drivers/
│   ├── vehicles/
│   ├── trips/
│   ├── maintenance/
│   ├── fuel/
│   ├── expenses/
│   ├── reports/
│   ├── models/
│   ├── templates/
│   └── static/
│
├── instance/
├── migrations/
├── config.py
├── run.py
├── requirements.txt
└── README.md
```

---

## 🚀 Installation

Clone the repository:

```bash
git clone https://github.com/harini25102-eng/odoo_hackathon_project
```

Go to the project directory:

```bash
cd TransitOps
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate the virtual environment.

### macOS / Linux

```bash
source venv/bin/activate
```

### Windows

```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
python run.py
```

Open your browser:

```
http://127.0.0.1:5000
```

---

## 📊 Modules

- Dashboard
- Vehicles
- Drivers
- Trips
- Maintenance
- Fuel
- Expenses
- Reports

---

## 🔮 Future Enhancements

- GPS-based Live Vehicle Tracking
- Route Optimization
- Predictive Maintenance
- Role-Based Access Control
- Export Reports to PDF & Excel
- Email Notifications
- Business Analytics & AI Recommendations

---

## 👥 Team

Developed as part of a Hackathon project.

---

## 📄 License

This project is developed for educational and hackathon purposes.