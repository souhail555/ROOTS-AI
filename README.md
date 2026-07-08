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
   (Set-ExecutionPolicy -Scope Process -ExecutionPolicy RemoteSigned) & venv/bin/activate   # Windows: venv\Scripts\activate
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

   The API will be available at `http://127.0.0.1:8010/api/`, and the admin site at `http://127.0.0.1:8010/admin/`.

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

Run the backend (`python manage.py runserver`, port 8010) and frontend (`npm run dev`, port 5173) in separate terminals. CORS is fully open in `backend/settings.py` (`CORS_ALLOW_ALL_ORIGINS = True`), and the frontend also uses Vite proxy for `/api` during development.

### One-command startup (Windows)

From the project root, run:

```bat
start-dev.cmd
```

This opens two terminals automatically:

- Backend terminal: runs migrations and starts Django on `127.0.0.1:8010`
- Frontend terminal: starts Vite on `127.0.0.1:5173`

## Notes

- `DEBUG = True` and `SECRET_KEY` is a placeholder in `backend/settings.py` — replace both before deploying.
- The database is SQLite (`db.sqlite3`), created automatically on first migrate.

## Environment Variables (Optional)

The project now supports environment-based configuration. If you do not set any variables, behavior stays exactly the same as current local defaults.

- `DJANGO_SECRET_KEY` (default: `django-insecure-change-me`)
- `DJANGO_DEBUG` (default: `True`)
- `DJANGO_ALLOWED_HOSTS` (comma-separated, default: empty)
- `DJANGO_CORS_ALLOW_ALL_ORIGINS` (default: `True`)
- `ROOTS_ADMIN_USERNAMES` (comma-separated, default: `Admin,admin`)
- `ROOTS_ADMIN_EMAIL` (default: `souhail.aidi6@gmail.com`)
- `ROOTS_ADMIN_PASSWORD` (default: `Admin#12345`)

Example (PowerShell):

```powershell
$env:DJANGO_DEBUG="True"
$env:DJANGO_ALLOWED_HOSTS="127.0.0.1,localhost"
```

## Admin and Access Control

- Django Admin now includes richer list/search/filter views for Users, Projects, and Cars.
- Regular users can access only their own projects and cars.
- Admin users (`role=admin`, `is_staff`, or `is_superuser`) can access all projects and cars.

## Seed / Demo Data

Run this command to create deterministic demo users, projects, and cars:

```sh
python manage.py seed_demo_data
```

Optional parameters:

```sh
python manage.py seed_demo_data --users 3 --projects-per-user 2 --cars-per-project 2 --password Demo#12345
```

## Safe Data Migration Helpers

Use these helpers before/after schema changes to check and repair ownership consistency:

```sh
python manage.py migration_precheck
python manage.py migration_precheck --fail-on-issues
python manage.py migration_repair_ownership --dry-run
python manage.py migration_repair_ownership --apply
```
