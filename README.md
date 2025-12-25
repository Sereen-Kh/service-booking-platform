# Service Booking Platform

A modern, full-stack platform for booking and managing services, built with FastAPI, React, PostgreSQL, and Docker.

---

## 🚀 Tech Stack

**Frontend:**

- React 19 (Vite)
- CSS Modules (custom, can use Tailwind/Chakra/Material UI)

**Backend:**

- FastAPI (Python 3.13)
- SQLAlchemy (async)
- Pydantic v2
- Alembic (migrations)
- JWT Authentication (OAuth2)

**Database & Cache:**

- PostgreSQL 15
- Redis 7

**DevOps:**

- Docker & Docker Compose
- Uvicorn (ASGI server)

---

## 📦 Features

- User authentication (JWT, OAuth2)
- Role-based access (Customer, Provider, Admin)
- Service discovery & search
- Booking & scheduling
- Provider dashboard
- Admin dashboard
- Responsive frontend UI

---

## 🛠️ Getting Started

1. **Clone the repo:**
   ```sh
   git clone <repo-url>
   cd booking-platform
   ```
2. **Start backend services:**
   ```sh
   docker compose up -d
   ```
3. **Backend (FastAPI):**
   ```sh
   cd backend
   python -m venv .venv
   source .venv/bin/activate
   pip install -r requirements.txt
   uvicorn app.main:app --reload
   ```
4. **Frontend (React):**
   ```sh
   cd frontend
   npm install
   npm run dev
   ```

---

## 📚 API Documentation

- Interactive docs: [http://localhost:8000/docs](http://localhost:8000/docs)

---

## 🤝 Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss what you would like to change.

---

## 📄 License

[MIT](LICENSE)
