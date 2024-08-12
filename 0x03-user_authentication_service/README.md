# 0x03. User authentication service

## Back-end

## Authentification

![SERVICE](https://private-user-images.githubusercontent.com/125453474/305865349-fc7f0d9b-deab-423e-97ec-75f38b0690b2.jpg?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3MjM0NzgyNTcsIm5iZiI6MTcyMzQ3Nzk1NywicGF0aCI6Ii8xMjU0NTM0NzQvMzA1ODY1MzQ5LWZjN2YwZDliLWRlYWItNDIzZS05N2VjLTc1ZjM4YjA2OTBiMi5qcGc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjQwODEyJTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI0MDgxMlQxNTUyMzdaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT1jOGFlOWEwYzUwNWIyZjhmODEwZGM1MzdlMTVlOGIzNTk2OTZkOWE2YTIwNjIxYmM3MTQxODAzZTY0MTU1M2ZmJlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCZhY3Rvcl9pZD0wJmtleV9pZD0wJnJlcG9faWQ9MCJ9.1pOxPuIFtGOA0S6tJAlrdSiTyBVs5eGeCQGwbopC6l4)

In the industry, you should __not__ implement your own authentication system and use a module or framework that doing it for you (like in Python-Flask: [Flask-User](https://flask-user.readthedocs.io/en/latest/)). Here, for the learning purpose, we will walk through each step of this mechanism to understand it by doing.

## Resources

__Read or watch__:

  - [Flask documentation](https://flask.palletsprojects.com/en/1.1.x/quickstart/)
  - [Requests module](https://requests.kennethreitz.org/en/latest/user/quickstart/)
  - [HTTP status codes](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html)

## Learning Objectives

At the end of this project, you are expected to be able to [explain to anyone](https://fs.blog/feynman-learning-technique/), __without the help of Google__:

  - How to declare API routes in a Flask app
  - How to get and set cookies
  - How to retrieve request form data
  - How to return various HTTP status codes

## Requirements

- Allowed editors: `vi`, `vim`, `emacs`
- All your files will be interpreted/compiled on Ubuntu 18.04 LTS using `python3` (version 3.7)
- All your files should end with a new line
- The first line of all your files should be exactly `#!/usr/bin/env python3`
- A `README.md` file, at the root of the folder of the project, is mandatory
- Your code should use the `pycodestyle` style (version 2.5)
- You should use `SQLAlchemy` 1.3.x
- All your files must be executable
- The length of your files will be tested using `wc`
- All your modules should have a documentation (`python3 -c 'print(__import__("my_module").__doc__)'`)
- All your classes should have a documentation (`python3 -c 'print(__import__("my_module").MyClass.__doc__)'`)
- All your functions (inside and outside a class) should have a documentation (`python3 -c 'print(__import__("my_module").my_function.__doc__)'` and `python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)')`
- A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified)
- All your functions should be type annotated
- The flask app should only interact with `Auth` and never with `DB` directly.
- Only public methods of `Auth` and `DB` should be used outside these classes

## Setup

You will need to install __bcrypt__

    pip3 install bcrypt

# Tasks 📃

In this task you will create a SQLAlchemy model named `User` for a database table named `users` (by using the [mapping declaration](https://docs.sqlalchemy.org/en/13/orm/tutorial.html#declare-a-mapping) of SQLAlchemy).

The model will have the following attributes:

  - `id`, the integer primary key
  - `email`, a non-nullable string
  - `hashed_password`, a non-nullable string
  - `session_id`, a nullable string
  - `reset_token`, a nullable string

bob@dylan:~$ cat 0-main.py
#!/usr/bin/env python3
"""
Main file
"""
from user import User

print(User.__tablename__)

for column in User.__table__.columns:
    print("{}: {}".format(column, column.type))

bob@dylan:~$ python3 0-main.py
users
users.id: INTEGER
users.email: VARCHAR(250)
users.hashed_password: VARCHAR(250)
users.session_id: VARCHAR(250)
users.reset_token: VARCHAR(250)
bob@dylan:~$


