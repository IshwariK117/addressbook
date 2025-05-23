
# 📒 Address Book Application

## 📌 Project Overview
This project is an **Address Book** application that allows users to:
- Create a new contact with **multiple addresses**
- **Edit** and **Delete** existing contacts
- Validations on **Email**, **Phone Number**, and **PIN Code**

---

## ✅ Current Status
- ✅ **Frontend:** Fully functional using **Bootstrap**. Users can create and view contacts.
- ⚙️ **Backend:** FastAPI setup complete. Basic API routes are created. CRUD operations & validations are **partially implemented**.
- 🗃️ **Database:** **PostgreSQL** selected. Integration and migrations are **in progress**.


### 🖼️ UI Views

<img src="ss1 (3).png" alt="Address Book UI" width="400"/>
<img src="ss1 (1).png" alt="Address Book UI" width="400"/>
<img src="ss1 (2).png" alt="Address Book UI" width="400"/>



## 🛠️ Technology Stack

| Layer       | Technology         |
|-------------|--------------------|
| Backend     | Python FastAPI     |
| Frontend    | Bootstrap 5        |
| Database    | PostgreSQL         |
| AI Tool     | Cursor AI          |



## 💾 Database Justification

We selected **PostgreSQL** because it is:
- Highly reliable and handles **relational data** efficiently.
- Excellent for managing **multiple addresses per contact** via relational tables.
- Supports complex queries, **advanced data types** (like JSON, arrays), and better indexing.


## 🚀 How to Run the Project

### 🔧 Backend

1. **Install dependencies**:
   ```bash 
   pip install fastapi uvicorn psycopg2-binary pydantic
``
2. **Set up PostgreSQL DB**:

   * Create a database in PostgreSQL.
   * Update DB connection settings in your backend code (e.g., in `config.py` or `.env`).

3. **Run FastAPI server**:

   ```bash
   uvicorn main:app --reload
   ```

---

## 🤖 AI Tools Used

* **Cursor AI** was used for smart code completions, error detection, and faster development.

---
```bash
addressbook-app/
├── frontend/
│   ├── index.html              # Main contact list page
│   ├── create_contact.html     # Add new contact page
│   └── edit_contact.html       # Edit contact page
├── app/
│   ├── main.py                 # FastAPI application entry point
│   ├── database.py             # Database configuration (SQLAlchemy)
│   ├── models.py               # SQLAlchemy models
│   ├── schemas.py              # Pydantic models for request/response validation
│   ├── crud.py                 # CRUD operations for database
│   └── routers/
│       └── contact.py          # API routes for contact management
└── requirements.txt            # Python dependencies
