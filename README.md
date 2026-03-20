

# 📝 Task Manager Web Application

A simple and efficient **Task Manager Web Application** built using **Python, Django, HTML, CSS, and JavaScript**. This application helps users manage their daily tasks with features like task creation, status tracking, deadline management, and user authentication.

---

## 🚀 Features

* ✅ User Registration & Login Authentication
* 🏠 Clean and informative Home Page
* ➕ Add Tasks with Title, Description, and Deadline
* 📅 Date Picker (Calendar) for selecting task deadlines
* 🔄 Task Status Management:

  * Pending
  * In Progress
  * Completed
* ✏️ Update Task Status dynamically
* 🗂️ Tasks sorted based on nearest deadline (priority-based display)
* 🌗 Light/Dark Theme Toggle
* 🧭 Smooth Navigation between pages
* 📱 Responsive and user-friendly UI

---

## 🛠️ Tech Stack

### 👨‍💻 Frontend

* HTML5
* CSS3
* JavaScript

### ⚙️ Backend

* Python
* Django

### 🗄️ Database

* MySQL

### 🔧 Tools & Platforms

* Git (Version Control)
* GitHub (Repository Hosting)

---

## 📂 Project Structure

```task-manager/
├── backend/
│   ├── backend/
│   │   ├── settings.py
│   │   ├── urls.py
│   │   └── wsgi.py
│   ├── users/
│   │   ├── models.py
│   │   ├── views.py
│   │   ├── serializers.py
│   │   ├── urls.py
│   │   └── admin.py
│   ├── tasks/
│   │   ├── models.py
│   │   ├── views.py
│   │   ├── serializers.py
│   │   ├── urls.py
│   │   ├── permissions.py
│   │   └── admin.py
│   └── manage.py
├── frontend/
│   ├── index.html          (Home page)
│   ├── login.html          (Login page)
│   ├── register.html       (Register page)
│   └── dashboard.html      (Dashboard with all features)
├── README.md
├── gitignore
```

---

## ⚙️ Installation & Setup

### 🔹 1. Clone the Repository

```bash
git clone https://github.com/Pradesha3112/Task-Manager.git
cd My-Task-Manager
```

---

### 🔹 2. Create Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate   # For Windows
```

---

### 🔹 3. Install Dependencies

```bash
pip install django
```

---

### 🔹 4. Run Migrations

```bash
python manage.py migrate
```

---

### 🔹 5. Start Server

```bash
python manage.py runserver
```

---

### 🔹 6. Open in Browser

```
http://127.0.0.1:8000/
```

---

## 🔐 Authentication Flow

1. User registers with basic details
2. Logs into the system
3. Redirected to dashboard
4. Can manage tasks securely

---

## 📌 How It Works

1. User logs in or registers
2. Adds tasks with deadline using calendar
3. Tasks are displayed in order of nearest deadline
4. User can update task status anytime
5. Theme can be switched between light and dark

---

## 🎯 Future Enhancements

* 🔔 Notifications & reminders
* 📊 Task analytics dashboard
* ☁️ Deployment (AWS / Vercel / Render)
* 📱 Mobile responsiveness improvements
* 🧠 AI-based task suggestions

---

## 🤝 Contributing

Contributions are welcome! Feel free to fork this repository and submit a pull request.

---

## 📧 Contact

**Name:** Pradesha S
**Email:** [aaa@gmail.com](mailto:pradesha3112@gmail.com)

---

## ⭐ Acknowledgements

* Django Documentation
* Open-source community
* GitHub for version control

---
