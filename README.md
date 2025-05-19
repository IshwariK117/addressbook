# Address Book Application

## Project Overview
This project is an Address Book application where users can create contacts with multiple addresses. The application supports adding, editing, and deleting contacts with validations on email, phone number, and pin code.

---

## Current Status
- **Frontend:** Fully functional using Bootstrap. User can create and view contacts.
- **Backend:** Initial FastAPI setup completed. Basic API routes created but CRUD operations and validations are partially implemented.
- **Database:** PostgreSQL chosen but integration and migrations are in progress.

---

## Technology Stack

- **Backend:** Python FastAPI  
- **Frontend:** Bootstrap 5  
- **Database:** PostgreSQL  
- **Cursor AI**
---

## Justification for Database Choice
We chose PostgreSQL because it is reliable and works very well with relational data, which fits perfectly for storing contacts and multiple addresses. It handles complex queries easily and keeps data safe and consistent (ACID compliance).

Compared to MySQL, PostgreSQL offers:
- Better support for advanced data types like JSON and arrays.
- More powerful and flexible indexing options.
- Full support for complex transactions and concurrency control.


---

## How to Run

### Backend
1. Install dependencies:
```bash
pip install fastapi uvicorn psycopg2-binary pydantic
```

2.Set up PostgreSQL database and update the connection details in your backend code.

3.Run the FastAPI server:
```bash
uvicorn main:app --reload
```

AI Tools Used
Cursor AI was used for code autocompletion and assistance during development.

Screenshots 
<img src="assets/addressbook_ui.png" alt="Address Book UI" width="400"/>

