# Track It

### Description
Track It is a simple web application that helps users track their income and expenses. By inputting financial data, users can visualize their spending habits with a dynamic pie chart, giving them clear insights into their financial health.

### Video Demo
Check out [Video Demo](https://youtu.be/g5mTiwfEye0).

## Features
* **Track Income and Expenses:** Input both income and expenses and categorize them for easy tracking.
* **Data Visualization:** View your financial breakdown in a pie chart, clearly showing the relationship between income and expenses.
* **Categorization:** Assign categories to expenses such as salary, rent, investment, and side-hustle to get detailed insights.

## Pages
### Index Page
The Index Page displays a table with user information, generated after the user submits data through the Add Page.

![Index Page](/Images/Index%20page.png)

### Add Page
The Add Page allows users to input their financial data through a form. The form includes:
- **Amount:** Input the amount of money for income or expenses.
- **Type:** Choose between Income and Expense.
- **Category:** Select from categories like salary, rent, investment, or side-hustle.

![Add Page](/Images/Add%20page.png)

### Dashboard Page
On the Dashboard Page, a pie chart is generated based on the submitted data, visually displaying the relationship between income and expenses.

![Dashboard Page](/Images/Dashboard%20page.png)

## Database Setup
Track It uses SQLAlchemy to manage the database, which stores user income and expense data. Below is a snapshot of the database structure.

![Database](/Images/Database.png)

## Built With
* **Python**
* **JavaScript**
* **Chart.js** (for data visualization)
* **Flask** (Python web framework)
  - **Flask-SQLAlchemy** (for managing the SQLite database)
  - **Flask-WTF** (for handling forms)
* **HTML/CSS/Bootstrap** (for frontend styling and responsiveness)

## Getting Started

### Prerequisites
To run this project locally, you will need the following:

- **Python 3.x**
- **Flask**
- **Flask-SQLAlchemy**
- **Flask-WTF**

### Installation
1. Clone the repository:
    ```bash
    git clone https://github.com/your-username/track-it.git
    cd track-it
    ```

2. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Run the Flask app:
    ```bash
    flask run
    ```

4. Open your browser and navigate to `http://127.0.0.1:5000`.

## Reference Documentation

* [Flask WTF-Forms Documentation](https://flask-wtf.readthedocs.io/en/stable/)
* [Stack Overflow](https://stackoverflow.com/)
* [Bootstrap Documentation](https://getbootstrap.com/docs/)
* [Chart.js Documentation](https://www.chartjs.org/docs/)
* [W3Schools](https://www.w3schools.com/)
