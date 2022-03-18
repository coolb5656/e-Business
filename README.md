# E - Business
Submission for 2022 FBLA E - Business Competition
---


# Folder Structure

```
app
├── db
│   ├── __init__.py
│   ├── models.py
├── db.sqlite
├── __init__.py
├── routes
│   ├── admin
│   │   ├── admin.py
│   │   ├── __init__.py
│   ├── api
│   │   ├── api.py
│   │   ├── __init__.py
│   ├── club
│   │   ├── __init__.py
│   ├── forms
│   │   ├── auth.py
│   │   ├── __init__.py
│   ├── __init__.py
│   ├── shop
│   │   ├── __init__.py
│   │   └── shop.py
│   ├── student
│   │   ├── __init__.py
│   │   └── student.py
│   └── views
│       ├── __init__.py
│       ├── main.py
├── static
│   ├── all.css
│   ├── css
│   │   ├── style.css
│   │   └── themes
│   │       └── tequila.css
│   ├── gen
│   │   ├── app.js
│   │   └── style.css
│   ├── img
│   │   ├── favicon.ico
│   │   ├── logo_mobile.png
│   │   └── logo.png
│   ├── js
│   │   └── app.js
│   ├── placeholder
│   │   ├── item.jpg
│   │   └── profile.jpg
│   ├── scss
│   │   └── bootstrap.scss
│   └── upload
└── templates
    ├── admin
    │   ├── base.html
    │   └── dashboard.html
    ├── auth
    │   ├── admin
    │   │   └── dashboard.html
    │   ├── club
    │   │   └── signup.html
    │   ├── customer
    │   │   └── dashboard.html
    │   ├── login.html
    │   └── signup.html
    ├── base.html
    ├── club
    │   ├── add
    │   │   └── item.html
    │   ├── items.html
    │   ├── orders.html
    │   ├── reports
    │   │   ├── item.html
    │   │   └── order.html
    │   └── settings.html
    ├── macros.html.j2
    ├── main
    │   └── index.html
    ├── shop
    │   ├── browse_item.html
    │   ├── browse_items.html
    │   ├── cart.html
    │   └── checkout.html
    └── student
        ├── base.html
        └── dashboard.html
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