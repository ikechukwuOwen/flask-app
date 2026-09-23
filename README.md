# Lolipop

Lolipop is a Flask web application with user authentication, profiles, and group management.

## Features

- User registration and login
- Password hashing
- Remember-me login
- User profiles
- Create and join groups
- Group invitation codes
- SQLite for local development
- PostgreSQL support for deployment

## Requirements

- Python
- Git

## Local setup

Clone the repository and move into the project folder:

```powershell
git clone https://github.com/ikechukwuOwen/flask-app.git
cd flask-app
```

Create and activate the virtual environment:

```powershell
python -m venv lolipop
.\lolipop\Scripts\Activate.ps1
```

Install the dependencies:

```powershell
pip install -r requirements.txt
```

## Database setup

Apply the database migrations:

```powershell
flask --app app db upgrade
```

If you create or change a model, generate and apply a new migration:

```powershell
flask --app app db migrate -m "Describe the database change"
flask --app app db upgrade
```

## Run locally

Start the development server:

```powershell
flask --app app run --debug
```

Open the app at:

```text
http://127.0.0.1:5000
```

## Project structure

```text
flask-app/
├── app.py
├── forms.py
├── models.py
├── routes.py
├── requirements.txt
├── Procfile
├── migrations/
├── static/
└── templates/
```

## Heroku deployment

Set the production secret key:

```powershell
heroku config:set SECRET_KEY="your-secret-key" --app lolipop-app
```

Deploy the app:

```powershell
git add .
git commit -m "Update application"
git push heroku main
```

Apply migrations on Heroku:

```powershell
heroku run flask db upgrade --app lolipop-app
```

View the deployed app:

```powershell
heroku open --app lolipop-app
```

View Heroku logs:

```powershell
heroku logs --tail --app lolipop-app
```

## Security

Do not commit secrets, local databases, or the virtual environment. These should remain ignored:

```text
.env
instance/
*.db
lolipop/
```
