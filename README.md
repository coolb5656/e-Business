# E - Business
Submission for 2022 FBLA E - Business Competition
---


# Folder Structure

```
├── src
│   ├── admin
│   │   ├── admin.py --handles all admin only views
│   ├── api
│   │   ├── api.py --handles all backend, never seen by user
│   ├── db
│   │   ├── models.py -- outlines database table structure
│   ├── user
│   │   ├── customer.py -- handles all non admin views
│   ├── forms
│   │   ├── auth.py -- handles all login/signup views
│   │   ├── shop.py -- handles all shopping views(cart, checkout)
│   ├── views
│   │   ├── main.py -- handles all non-specific views (homepage, contact, etc...)
│   │   ├── shop.py -- handles all shop-specific views (items browsing, item view, etc...)
│   ├── static
│   ├── templates
│   ├── __init__.py -- sets up application
├── Procfile -- for heroku hosting
├── requirements.txt -- for required packages
├── wsgi -- for setting up wsgi server for gunicorn
└── .gitignore
```