# Task Manager API - Setup Guide

This document provides step-by-step instructions to set up and run the Django Task Manager API locally.

## Prerequisites

Before starting, ensure you have these installed:
- Python 3.8+ (https://www.python.org/downloads/)
- Git (https://git-scm.com/downloads)
- pip (Python package manager)
## Quick Setup


1. Clone repository:
```bash
git clone https://github.com/Mukhtyarkhan/AAK--Test/tree/main/taskmanager.git
cd taskmanager


2. Create and activate virtual environment:
python -m venv venv
# Windows:
venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate

3. Install dependencies:
pip install -r requirements.txt


4. Configure database (SQLite used by default):
python manage.py migrate

5. Create admin user:
python manage.py createsuperuser


6. Run server:
python manage.py runserver

