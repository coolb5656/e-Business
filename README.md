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
│   │   ├── auth
│   │   │   ├── admin
│   │   │   │   └── dashboard.html
│   │   │   ├── customer
│   │   │   │   └── dashboard.html
│   │   │   ├── login.html
│   │   │   └── signup.html
│   │   ├── base.html
│   │   ├── main
│   │   │   └── index.html
│   │   └── shop
│   │       ├── browse_item.html
│   │       ├── browse_items.html
│   │       └── cart.html
│   ├── __init__.py -- sets up application
├── Procfile -- for heroku hosting
├── requirements.txt -- for required packages
├── wsgi -- for setting up wsgi server for gunicorn
└── .gitignore
```

Views:

1. auth
   1. login
   2. signup
   3. admin
      1. dashboard
   4. customer
      1. dashboard
2. main
   1. index.html
   2. contact
   3. about
3. shop
   1. browse items
   2. individual item
   3. cart
   4. checkout
   
Database Tables:
1. User
   1. uname
   2. email
   3. pwd
   4. profile pic
   5. address
   6. phone num
2. item
   1. name
   2. categories FK
   3. price
   4. description
   5. img
   6. stock
3. cart
   1. User FK
   2. item FK
4. category
   1. name