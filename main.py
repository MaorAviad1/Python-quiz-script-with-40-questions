#Python quiz script with 40 questions

import sys

questions = [
    {
        "question": "1. What Python library is commonly used for connecting with MySQL?",
        "options": ["A. mysqlclient", "B. PyMySQL", "C. psycopg2", "D. sqlite3"],
        "answer": "B"
    },
    {
        "question": "2. How do you establish a connection to a MySQL database?",
        "options": ["A. pymysql.connect()", "B. pymysql.open()", "C. pymysql.connection()", "D. pymysql.start()"],
        "answer": "A"
    },
    {
        "question": "3. What is the purpose of the cursor object in Python-MySQL interaction?",
        "options": ["A. Managing transactions", "B. Executing SQL queries", "C. Connecting to the database",
                    "D. Handling errors"],
        "answer": "B"
    },
    {
        "question": "4. How do you execute an SQL query using a cursor object?",
        "options": ["A. cursor.execute()", "B. cursor.run()", "C. cursor.sql()", "D. cursor.query()"],
        "answer": "A"
    },
    {
        "question": "5. Which method is used to fetch all the rows from the result set?",
        "options": ["A. fetchall()", "B. fetchone()", "C. fetch()", "D. get()"],
        "answer": "A"
    },
    {
        "question": "6. How do you close a MySQL connection?",
        "options": ["A. connection.end()", "B. connection.terminate()", "C. connection.finish()",
                    "D. connection.close()"],
        "answer": "D"
    },
    {
        "question": "7. Which method is used to commit the current transaction?",
        "options": ["A. commit()", "B. save()", "C. store()", "D. apply()"],
        "answer": "A"
    },
    {
        "question": "8. What is the purpose of the rollback() method?",
        "options": ["A. To revert changes in case of errors", "B. To close the database connection",
                    "C. To execute an SQL query", "D. To create a new table"],
        "answer": "A"
    },
    {
        "question": "9. Which SQL statement is used to insert data into a table?",
        "options": ["A. INSERT", "B. ADD", "C. CREATE", "D. APPEND"],
        "answer": "A"
    },
    {
        "question": "10. What is the correct syntax to create a database in MySQL?",
        "options": ["A. CREATE DATABASE database_name", "B. CREATE DATABASE database_name;",
                    "C. CREATE DATABASE database-name;", "D. CREATE database_name;"],
        "answer": "B"
    },
    {
        "question": "11. Which function is used to create a DataFrame in Pandas?",
        "options": ["A. pandas.DataFrame()", "B. pandas.Create()", "C. pandas.Data()", "D. pandas.Table()"],
        "answer": "A"
    },
    {
        "question": "12. How do you read a CSV file using Pandas?",
        "options": ["A. pd.read_csv()", "B. pd.read()", "C. pd.csv()", "D. pd.read_table()"],
        "answer": "A"
    },
    {
        "question": "13. Which function is used to filter DataFrame rows based on a condition?",
        "options": ["A. filter()", "B. select()", "C. where()", "D. query()"],
        "answer": "D"
    },
    {
        "question": "14. How can you access a specific row in a DataFrame using the index label?",
        "options": ["A. df.loc[]", "B. df.iloc[]", "C. df.at[]", "D. df.ix[]"],
        "answer": "A"
    },
    {
        "question": "15. What does the Pandas function 'groupby()' do?",
        "options": ["A. Sorts data", "B. Groups data by a column", "C. Filters data", "D. Splits data into chunks"],
        "answer": "B"
    },
    {
        "question": "16. How do you merge two DataFrames in Pandas?",
        "options": ["A. pd.join()", "B. pd.concat()", "C. pd.merge()", "D. pd.combine()"],
        "answer": "C"
    },
    {
        "question": "17. Which method is used to drop a column from a DataFrame?",
        "options": ["A. drop_column()", "B. drop()", "C. remove_column()", "D. delete_column()"],
        "answer": "B"
    },
    {
        "question": "18. How do you apply a custom function to a DataFrame column?",
        "options": ["A. apply()", "B. map()", "C. transform()", "D. change()"],
        "answer": "A"
    },
    {
        "question": "19. Which method is used to calculate the mean of a column in a DataFrame?",
        "options": ["A. mean()", "B. average()", "C. median()", "D. mode()"],
        "answer": "A"
    },
    {
        "question": "20. How do you rename a column in a DataFrame?",
        "options": ["A. df.columns.rename()", "B. df.rename(columns={})", "C. df.rename_column()", "D. df.change_column()"],
        "answer": "B"
    },
    {
        "question": "21. What is the primary purpose of the Django framework?",
        "options": ["A. Data analysis", "B. Web development", "C. Desktop applications", "D. Machine learning"],
        "answer": "B"
    },
    {
        "question": "22. Which command is used to create a new Django project?",
        "options": ["A. django-startproject", "B. django-admin startproject", "C. django-createproject", "D. django-initproject"],
        "answer": "B"
    },
    {
        "question": "23. In Django, what is a 'view' responsible for?",
        "options": ["A. Defining the database schema", "B. Processing HTTP requests", "C. Handling URL routing", "D. Displaying static files"],
        "answer": "B"
    },
    {
        "question": "24. How do you create a new Django app within a project?",
        "options": ["A. python manage.py createapp app_name", "B. python manage.py startapp app_name", "C. django-admin createapp app_name", "D. django-admin startapp app_name"],
        "answer": "B"
    },
    {
        "question": "25. What is the purpose of Django's 'models'?",
        "options": ["A. To define the structure of the database", "B. To process HTTP requests", "C. To manage URL routing", "D. To display static files"],
        "answer": "A"
    },
    {
        "question": "26. What is the Django's ORM (Object-Relational Mapping) used for?",
        "options": ["A. Interacting with databases using Python objects", "B. Generating HTML templates", "C. Managing HTTP requests", "D. Configuring URL routing"],
        "answer": "A"
    },
    {
        "question": "27. How do you run the development server in a Django project?",
        "options": ["A. python manage.py devserver", "B. python manage.py runserver", "C. django-admin runserver", "D. django-admin startserver"],
        "answer": "B"
    },
    {
        "question": "28. In Django, what is the purpose of the 'urls.py' file?",
        "options": ["A. Managing the database", "B. Handling HTTP requests", "C. Defining URL patterns and routing", "D. Rendering HTML templates"],
        "answer": "C"
    },
    {
        "question": "29. Which method is used to include another app's URLs in the main 'urls.py' file?",
        "options": ["A. include()", "B. append()", "C. extend()", "D. insert()"],
        "answer": "A"
    },
    {
        "question": "30. What is the purpose of Django's 'TemplateView'?",
        "options": ["A. To render a static HTML template", "B. To manage URL routing", "C. To handle form submissions", "D. To define the database schema"],
        "answer": "A"
    },
    {
        "question": "31. How do you import the NumPy library in a Python script?",
        "options": ["A. import numpy", "B. import np", "C. import numpy as np", "D. import num"],
        "answer": "C"
    },
    {
        "question": "32. Which function is used to create a NumPy array?",
        "options": ["A. numpy.array()", "B. numpy.create()", "C. numpy.ndarray()", "D. numpy.arr()"],
        "answer": "A"
    },
    {
        "question": "33. What is the main advantage of using NumPy arrays over Python lists?",
        "options": ["A. Faster operations", "B. Smaller file size", "C. Easier syntax", "D. More data types"],
        "answer": "A"
    },
    {
        "question": "34. How do you create an array of evenly spaced values between a range using NumPy?",
        "options": ["A. np.linspace()", "B. np.arange()", "C. np.range()", "D. np.space()"],
        "answer": "A"
    },
    {
        "question": "35. How do you create a 3x3 identity matrix using NumPy?",
        "options": ["A. np.identity(3)", "B. np.eye(3)", "C. np.ones((3, 3))", "D. np.zeros((3, 3))"],
        "answer": "B"
    },
    {
        "question": "36. How do you perform element-wise addition of two NumPy arrays?",
        "options": ["A. np.add()", "B. np.sum()", "C. np.concatenate()", "D. np.append()"],
        "answer": "A"
    },
    {
        "question": "37. What is the purpose of the 'shape' attribute in a NumPy array?",
        "options": ["A. To determine the data type", "B. To calculate the sum of elements", "C. To get the dimensions of the array", "D. To find the maximum value"],
        "answer": "C"
    },
    {
        "question": "38. How do you calculate the dot product of two NumPy arrays?",
        "options": ["A. np.dot()", "B. np.cross()", "C. np.multiply()", "D. np.product()"],
        "answer": "A"
    },
    {
        "question": "39. How do you transpose a NumPy array?",
        "options": ["A. np.transpose()", "B. array.T", "C. array.transpose()", "D. Both A and B"],
        "answer": "D"
    },
    {
        "question": "40. How do you calculate the mean of a NumPy array?",
        "options": ["A. np.mean()", "B. np.average()", "C. np.median()", "D. np.mode()"],
        "answer": "A"
    },
]


def main():
    score = 0

    for question in questions:
        print(question["question"])
        for option in question["options"]:
            print(option)

        user_answer = input("Enter the correct option (A, B, C, or D): ").upper()

        while user_answer not in ["A", "B", "C", "D"]:
            print("Please enter a valid option (A, B, C, or D).")
            user_answer = input("Enter the correct option (A, B, C, or D): ").upper()

        if user_answer == question["answer"]:
            score += 1
            print("Correct!")
        else:
            print("Wrong answer.")
        print("\n")

    print(f"Your final score is {score} out of {len(questions)}")

if __name__ == "__main__":
    main()