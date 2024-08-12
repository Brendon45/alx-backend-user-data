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

__Repo__:

  - GitHub repository: `alx-backend-user-data`
  - Directory: `0x03-user_authentication_service`
  - File: `user.py`

## 1. create user

In this task, you will complete the `DB` class provided below to implement the `add_user` method.

    """DB module
    """
    from sqlalchemy import create_engine
    from sqlalchemy.ext.declarative import declarative_base
    from sqlalchemy.orm import sessionmaker
    from sqlalchemy.orm.session import Session

    from user import Base


    class DB:
        """DB class
        """

        def __init__(self) -> None:
            """Initialize a new DB instance
            """
            self._engine = create_engine("sqlite:///a.db", echo=True)
            Base.metadata.drop_all(self._engine)
            Base.metadata.create_all(self._engine)
            self.__session = None

            @property
            def _session(self) -> Session:
            """Memoized session object
            """
            if self.__session is None:
                DBSession = sessionmaker(bind=self._engine)
                self.__session = DBSession()
            return self.__session

Note that `DB._session` is a private property and hence should NEVER be used from outside the `DB` class.

Implement the `add_user` method, which has two required string arguments: `email` and `hashed_password`, and returns a `User` object. The method should save the user to the database. No validations are required at this stage.

    bob@dylan:~$ cat 1-main.py
    #!/usr/bin/env python3
    """
    Main file
    """

    from db import DB
    from user import User

    my_db = DB()

    user_1 = my_db.add_user("test@test.com", "SuperHashedPwd")
    print(user_1.id)

    user_2 = my_db.add_user("test1@test.com", "SuperHashedPwd1")
    print(user_2.id)

    bob@dylan:~$ python3 1-main.py
    1
    2
    bob@dylan:~$

__Repo:__

  - GitHub repository: `alx-backend-user-data`
  - Directory: `0x03-user_authentication_service`
  - File: `db.py`

## 2. Find user

In this task you will implement the `DB.find_user_by` method. This method takes in arbitrary keyword arguments and returns the first row found in the `users` table as filtered by the method’s input arguments. No validation of input arguments required at this point.

Make sure that SQLAlchemy’s `NoResultFound` and `InvalidRequestError` are raised when no results are found, or when wrong query arguments are passed, respectively.

Warning:

  - `NoResultFound` has been moved from `sqlalchemy.orm.exc` to `sqlalchemy.exc` between the version 1.3.x and 1.4.x of SQLAchemy - please make sure you are importing it from `sqlalchemy.orm.exc`

        bob@dylan:~$ cat 2-main.py
        #!/usr/bin/env python3
        """
        Main file
        """
        from db import DB
        from user import User

        from sqlalchemy.exc import InvalidRequestError
        from sqlalchemy.orm.exc import NoResultFound


        my_db = DB()

        user = my_db.add_user("test@test.com", "PwdHashed")
        print(user.id)

        find_user = my_db.find_user_by(email="test@test.com")
        print(find_user.id)

        try:
          find_user = my_db.find_user_by(email="test2@test.com")
          print(find_user.id)
        except NoResultFound:
            print("Not found")

        try:
            find_user = my_db.find_user_by(no_email="test@test.com")
            print(find_user.id)
        except InvalidRequestError:
           print("Invalid")        

        bob@dylan:~$ python3 2-main.py
        1
        1
        Not found
        Invalid
        bob@dylan:~$

__Repo:__

  - GitHub repository: `alx-backend-user-data`
  - Directory: `0x03-user_authentication_service`
  - File: `db.py`

## 3. update user

In this task, you will implement the `DB.update_user` method that takes as argument a required `user_id` integer and arbitrary keyword arguments, and returns `None`.

The method will use `find_user_by` to locate the user to update, then will update the user’s attributes as passed in the method’s arguments then commit changes to the database.

If an argument that does not correspond to a user attribute is passed, raise a `ValueError`.

    bob@dylan:~$ cat main.py
    #!/usr/bin/env python3
    """
    Main file
    """
    from db import DB
    from user import User

    from sqlalchemy.exc import InvalidRequestError
    from sqlalchemy.orm.exc import NoResultFound


    my_db = DB()

    email = 'test@test.com'
    hashed_password = "hashedPwd"

    user = my_db.add_user(email, hashed_password)
    print(user.id)

    try:
        my_db.update_user(user.id, hashed_password='NewPwd')
        print("Password updated")
    except ValueError:
        print("Error")

    bob@dylan:~$ python3 main.py
    1
    Password updated
    bob@dylan:~$ 

__Repo:__

  - GitHub repository: `alx-backend-user-data`
  - Directory: `0x03-user_authentication_service`
  - File: `db.py`

## 4. Hash password

In this task you will define a `_hash_password` method that takes in a `password` string arguments and returns bytes.

The returned bytes is a salted hash of the input password, hashed with `bcrypt.hashpw`.

    bob@dylan:~$ cat main.py
    #!/usr/bin/env python3
    """
    Main file
    """
    from auth import _hash_password

    print(_hash_password("Hello Holberton"))

    bob@dylan:~$ python3 main.py
    b'$2b$12$eUDdeuBtrD41c8dXvzh95ehsWYCCAi4VH1JbESzgbgZT.eMMzi.G2'
    bob@dylan:~$

__Repo__:

  - GitHub repository: `alx-backend-user-data`
  - Directory: `0x03-user_authentication_service`
  - File: `auth.py`

## 
