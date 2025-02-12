# For Importing the MySQL connector module to interact with the database
import mysql.connector

# Connect to the MySQL database
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="test"
)

# Creating a function to get all individual polling units information
def individual_polling_unit(polling_unit_id):
    # Create a cursor object which allows the execute SQL queries
    mycursor = mydb.cursor()

    # Define the SQL query to select all columns from the 'announced_pu_results' table where 'polling_unit_uniqueid' matches a given value
    quercy = "SELECT * FROM announced_pu_results WHERE polling_unit_uniqueid = %s"

    # Execute the SQL query with the given parameter 'ans'
    mycursor.execute(quercy, (polling_unit_id,))

    # Fetch all the results from the executed query
    myresult = mycursor.fetchall()

    # Loop through each result row
    for row in myresult:
        # Create a dictionary mapping column names to their respective values in the current row
        colandval = dict(zip(mycursor.column_names, row))
        # Loop through each column in the row and print the column name and its value
        for col, detail in colandval.items():
            print(col, ' = ', detail)
        # Print a new line after each row
        print('\n')

# Create an input to get polling_unit_id from the user
polling_unit_id = input('Enter the id of the polling unit you will like to make enquiry of : ')
# To call the function individual_polling_unit
individual_polling_unit(polling_unit_id)