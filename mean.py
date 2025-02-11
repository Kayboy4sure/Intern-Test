from bs4 import BeautifulSoup
import statistics
import psycopg2
import random

#create a function to fetch data
def get_data():
    dataget = {}
    url = "python_class_question.html"
    soup = BeautifulSoup(open(url).read())
    td = soup.find_all('td')

    for text in range(0, len(td), 2):
        dataget[td[text].text] = td[text+1].text.split(', ')
    return dataget

dataget = get_data()

mean_table = {}

#create a loop to get colors with the number of times they appear store in dic.
for day in dataget:
    for color in dataget[day]:
        if color in mean_table:
            mean_table[color] += 1
        else:
            mean_table[color] = 1


print ('The mean value for the colors is ', statistics.mean(mean_table.values()))

value = max(mean_table.values())

#create a loop to determine key that belong to the value
for item in mean_table:
    if mean_table[item] == value:
        value = item

print ('The most worn color throughout the week is ', value)

color_list = []
for data in dataget.values():
    color_list += data

print ('The median color is ', statistics.median(color_list))

print ('The variance of the colors is', statistics.variance(mean_table.values()))

print ('The probability that the color red could be choose is ', mean_table['RED']/sum(mean_table.values()))

data = list(mean_table.items())

conn = psycopg2.connect(database = "color_table", 
                        user = "username", 
                        host= "localhost",
                        password = "password",
                        port = "5432")

cur = conn.cursor()

cur.execute("""CREATE TABLE color_list(
            id SERIAL PRIMARY KEY,
            color VARCHAR (255) UNIQUE NOT NULL,
            frequency INTEGER NOT NULL,
            """)

# inserting values into color list table
for d in data:
    cur.execute("INSERT INTO color_list(id, color, frequency) VALUES (%s, %s)", d)

conn.commit()

conn.close()

# create a function to generation 4 random digit and convert it to integer
def get_random_int():
    number = ''
    for num in range(4):
        random_num = random.randint(0, 1)
        number += str(random_num)
    return (int(number, 2))

print('Program that generates  random 4 digits number of 0s and 1s and convert the generated number to base 10 => ', get_random_int())

#create a function generate fibonacci list and sum them up
def fibonacci():
    fibonacci_list = [0, 1]
    sum_of_list = fibonacci_list[0] + fibonacci_list[1]
    for number in range(2, 50):
        next_number = fibonacci_list[number-1]+fibonacci_list[number-2]
        fibonacci_list.append(next_number)
        sum_of_list += next_number
    return sum_of_list

print('Program that sum the first 50 fibonacci sequence => ', fibonacci())
