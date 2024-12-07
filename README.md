# Student Management API

## Project Overview
This is a simple Student Management application built with FastAPI (backend), HTML, and JavaScript (frontend). The application allows users to perform CRUD (Create, Read, Update, Delete) operations on student records.

## Features
- View all students
- Add new students
- Update existing student information
- Delete students

## Technology Stack
- Backend: FastAPI (Python)
- Frontend: HTML, JavaScript
- API Type: RESTful

## Prerequisites
- Python 3.7+
- pip
- FastAPI
- Uvicorn

## Installation

### Backend Setup
1. Clone the repository
```bash
git clone https://github.com/AhemdMahmoud/Fastapi_Workshop.git
cd student-management-project
```

2. Create a virtual environment (optional but recommended)
```bash
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
```

3. Install dependencies
```bash
pip install fastapi uvicorn
```

### Running the Application
1. Start the FastAPI server
```bash
uvicorn students:app --reload
```

2. Open the `index.html` file in your web browser

## API Endpoints
- `GET /students`: Retrieve all students
- `POST /students`: Add a new student
- `PUT /students/{student_id}`: Update an existing student
- `DELETE /students/{student_id}`: Delete a student

## Student Model
```python
class Student:
    id: int
    name: str
    grad: int
```

## Potential Improvements
- Add database integration
- Implement more robust error handling
- Add input validation
- Create a more sophisticated frontend


## Contributing
Contributions are welcome! Please feel free to submit a Pull Request.
