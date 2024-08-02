# 0x00. Personal data

## Back-end

## Authentification

![PERSONAL](https://private-user-images.githubusercontent.com/125453474/302913548-8bf68917-255c-4b6e-867f-e27671a54223.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3MjI1MDQxODQsIm5iZiI6MTcyMjUwMzg4NCwicGF0aCI6Ii8xMjU0NTM0NzQvMzAyOTEzNTQ4LThiZjY4OTE3LTI1NWMtNGI2ZS04NjdmLWUyNzY3MWE1NDIyMy5wbmc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjQwODAxJTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI0MDgwMVQwOTE4MDRaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT0wNDcyYTM4OTc2NzA0OGEzYTdhZjFkODlkZmQwMDM1Njg0ZDk3MDUyMmQzMmEwZDk2MzVmZjEzOTc0ODcyODJlJlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCZhY3Rvcl9pZD0wJmtleV9pZD0wJnJlcG9faWQ9MCJ9.U5E3xpJjIlanQtvarETu7vJO5p1ddu7jbkEL0XOghWI)


## Resources

__Read or watch:__

- [What Is PII, non-PII, and Personal Data?](https://piwik.pro/blog/what-is-pii-personal-data/)
- [logging documentation](https://docs.python.org/3/library/logging.html)
- [bcrypt package](https://github.com/pyca/bcrypt/)
- [Logging to Files, Setting Levels, and Formatting](https://www.youtube.com/watch?v=-ARI4Cz-awo)

## Learning Objectives

At the end of this project, you are expected to be able to [explain to anyone](https://fs.blog/feynman-learning-technique/), without the help of Google:

  - Examples of Personally Identifiable Information (PII)
  - How to implement a log filter that will obfuscate PII fields
  - How to encrypt a password and check the validity of an input password
  - How to authenticate to a database using environment variables

## Requirements

  - All your files will be interpreted/compiled on Ubuntu 18.04 LTS using `python3` (version 3.7)
  - All your files should end with a new line
  - The first line of all your files should be exactly `#!/usr/bin/env python3`
  - A `README.md` file, at the root of the folder of the project, is mandatory
  - Your code should use the `pycodestyle` style (version 2.5)
  - All your files must be executable
  - The length of your files will be tested using `wc`
  - All your modules should have a documentation (`python3 -c 'print(__import__("my_module").__doc__)'`)
  - All your classes should have a documentation (`python3 -c 'print(__import__("my_module").MyClass.__doc__)'`)
  - All your functions (inside and outside a class) should have a documentation (`python3 -c 'print(__import__("my_module").my_function.__doc__)' and python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'`)
  - A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified)
  - All your functions should be type annotated

# Tasks 📃

## 0. Regex-ing

Write a function called `filter_datum` that returns the log message obfuscated:

Arguments:
    - `fields`: a list of strings representing all fields to obfuscate
    - `redaction`: a string representing by what the field will be obfuscated
    - `message`: a string representing the log line
    - `separator`: a string representing by which character is separating all fields in the log line (`message`)
- The function should use a regex to replace occurrences of certain field values.
- `filter_datum` should be less than 5 lines long and use `re.sub` to perform the substitution with a single regex.

      bob@dylan:~$ cat 0-main.py
      #!/usr/bin/env python3
      """
      Main file
      """

      filter_datum = __import__('filtered_logger').filter_datum

      fields = ["password", "date_of_birth"]
      messages = ["name=egg;email=eggmin@eggsample.com;password=eggcellent;date_of_birth=12/12/1986;", "name=bob;email=bob@dylan.com;password=bobbycool;date_of_birth=03/04/1993;"]

      for message in messages:
          print(filter_datum(fields, 'xxx', message, ';'))

      bob@dylan:~$
      bob@dylan:~$ ./0-main.py
        name=egg;email=eggmin@eggsample.com;password=xxx;date_of_birth=xxx;
      name=bob;email=bob@dylan.com;password=xxx;date_of_birth=xxx;
      bob@dylan:~$
