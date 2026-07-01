# ROOTS-AI

A Django (backend) + Vue 3/Vite (frontend) project.

- `backend/` — Django project settings, URLs, WSGI/ASGI entrypoints
- `core/`, `api/` — Django apps
- `frontend/` — Vue 3 + Vite single-page app

## Prerequisites

- Python 3.10+
- Node.js `^22.18.0` or `>=24.12.0` (see `frontend/package.json`)

## Backend setup (Django)

1. Create and activate a virtual environment:

   ```sh
   python3 -m venv venv
   source venv/bin/activate   # Windows: venv\Scripts\activate
   ```

2. Install dependencies:

   ```sh
   pip install -r requirements.txt
   ```

3. Apply migrations:

   ```sh
   python manage.py migrate
   ```

4. (Optional) Create an admin user:

   ```sh
   python manage.py createsuperuser
   ```

5. Run the dev server:

   ```sh
   python manage.py runserver
   ```

   The API will be available at `http://127.0.0.1:8000/api/`, and the admin site at `http://127.0.0.1:8000/admin/`.

## Frontend setup (Vue 3 + Vite)

1. Install dependencies:

   ```sh
   cd frontend
   npm install
   ```

2. Run the dev server:

   ```sh
   npm run dev
   ```

   The app will be available at `http://localhost:5173` (default Vite port).

3. Build for production:

   ```sh
   npm run build
   ```

## Running both together

Run the backend (`python manage.py runserver`, port 8000) and frontend (`npm run dev`, port 5173) in separate terminals. CORS is fully open in `backend/settings.py` (`CORS_ALLOW_ALL_ORIGINS = True`), so the frontend can call the Django API during development without extra configuration.

## Notes

- `DEBUG = True` and `SECRET_KEY` is a placeholder in `backend/settings.py` — replace both before deploying.
- The database is SQLite (`db.sqlite3`), created automatically on first migrate.
