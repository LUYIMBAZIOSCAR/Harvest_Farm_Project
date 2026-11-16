# Harvest Farm

Harvest Farm is a Django-based agricultural website for showcasing farm activities, publishing knowledge content, accepting partnership applications, handling farm tour bookings, and managing public contact messages.

## Features

- Responsive marketing site with dedicated pages for Home, About, Knowledge Hub, Gallery, Partnerships, Book a Tour, and Contact
- Dynamic article publishing with categories, search, filtering, and pagination
- Gallery with image and YouTube video support
- Partnership application form with database storage and admin review
- Farm tour booking flow with validation and status tracking
- Contact form with message management
- Configurable farm details and social links through Django Admin
- Deployment-ready Django project setup using WhiteNoise, environment variables, and PostgreSQL-ready configuration

## Local setup

1. Create and activate a virtual environment.
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Copy `.env.example` to `.env` and adjust settings.
4. Run migrations:
   ```bash
   python manage.py migrate
   ```
5. Create a superuser:
   ```bash
   python manage.py createsuperuser
   ```
6. Start the development server:
   ```bash
   python manage.py runserver
   ```

## Production notes

- Set `DEBUG=False` and configure `ALLOWED_HOSTS`.
- Set a secure `DJANGO_SECRET_KEY`.
- Use PostgreSQL values in `.env` if deploying with a database service.
- Collect static files with:
  ```bash
  python manage.py collectstatic --noinput
  ```
- Use `gunicorn` and WhiteNoise for deployment.

## Admin access

After creating a superuser, log in at `/admin/` to manage:

- Farm information
- Articles and categories
- Gallery items and categories
- Partnership applications
- Bookings
- Contact messages
- Social links
