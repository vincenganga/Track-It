# Project Title: Track It

#### Description:

In this project, I present to you Track It, a simple web application that lets you track your money expenditure by taking in your income as well as your expense and presents the data in a pie chart.

## Link
#### Video Demo:  https://youtu.be/g5mTiwfEye0

## Introduction
* Index Page:
  For the index page, you will find a table layout where the user infomation will be presented after inputting the data at the add page.
  ![Index Page](/Images/Index%20page.png)

* Add Page:
  In the add page, there will be a form page which the user will be required to fill out. The form includes an input field of Amount, where the user will input the amount of money they want to be generated. It will also include a Type section which the user can choose between Income and Expense. Lastly there will be a Category section where the user can choose between salary, rent, investment and side-hustle.
  ![Add Page](/Images/Add%20page.png)

* Dashboard Page:
  In the dashboard page, the user information which is generated after submission will display a pie chart will show the users relationship between Income and Expenses.
  ![Dashboard Page](/Images/Dashboard%20page.png)

## SQLAlchemy and SQLite3
I need a table in the database for Income and Expenses hence decided to make one with SQLAlchemy:
![Database](/Images/Database.png)

## Built With

- Python
- JavaScript
- Chart.js
- Flask, Flask-SQLAlchemy, Flask WTF
- HTML
- CSS
- Bootstrap

* Used Flask web framework based in Python, necessary for flask-sqlalchemy to manage SQL database with sqlite and flask-wtf to upload files and forms extensions

## Reference:

* Flask WTF-Forms Documentation
* Stack Overflow
* Bootstrap
* Chart.js documentation
* W3School
