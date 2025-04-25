# Habit Tracker API

## 📌 Description

**Habit Tracker API** — это минималистичное, но масштабируемое приложение для отслеживания привычек.

Пользователи могут:
- ✅ Создавать привычки
- 🗓 Логировать выполнение привычек по датам
- 📊 Смотреть статистику выполнений

📢 Проект реализован в виде REST API и полностью покрыт тестами.


## 🐍 Stack

- Python 3
- FastAPI
- SQLAlchemy
- SQLite
- Pydantic v2
- Pytest


## 💾 Installation  
1. 📂 **Clone the repository:**  
```bash
 git clone https://github.com/suchkovdaniil/HabitTracker.git
```
2. 📁 **Navigate to the 'IstoriiBot' folder and then to 'src':**  
```bash
 cd HabitTracker
```
3. 🌟 **Create and activate a virtual environment:**  
```bash
 python3 -m venv venv
 source venv/bin/activate
```
4. 📦 **Install the requirements from requirements.txt:**  
```bash
 pip install -r requirements.txt
```
5. 🚀 **Run the server:**
```bash
 uvicorn app.main:app --reload
 ```
6. 🌐 **Open:**:
```
 http://127.0.0.1:8000/docs
 ```