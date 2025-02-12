# For Importing the MySQL connector module to interact with the database
import mysql.connector

# Connect to the MySQL database
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="test"
)

# Creating a function to get sum of all parties result
def sum_of_party_result():
    # Create a cursor object using the connection to the database
    mycursor = mydb.cursor()

    # Define the SQL query to select all columns from the 'announced_pu_results' table
    quercy = "SELECT * FROM announced_pu_results"

    # Execute the SQL query
    mycursor.execute(quercy)

    # Fetch all the rows from the executed query
    myresult = mycursor.fetchall()

    # Initialize an empty dictionary to store the party names and their results
    total_party_result = {}

    # Loop through each row in the result set
    for row in myresult:
        # Create a dictionary mapping column names to their respective values in the current row
        colandval = dict(zip(mycursor.column_names, row))
        
        # Iterate through each column and its corresponding value in the row dictionary
        for column, detail in colandval.items():
            # Check if the column is party_abbreviation
            if column == 'party_abbreviation':
                # If the party abbreviation already exists in the total results dictionary
                if detail in total_party_result:
                    # Add the current party score to the existing total for that party
                    total_party_result[detail] += colandval['party_score']
                else:
                    # Initialize the total party score for the new party abbreviation
                    total_party_result[detail] = colandval['party_score']
            
    # Return the dictionary containing the total results for each party
    return total_party_result

# Call the function to set the data of the sum of result of individual parties 
parties_result = sum_of_party_result()

# Loop through the result
for party, result in parties_result.items():
    # display each parties name and their score
    print (party, ' the result is ', result)