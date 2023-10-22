#Module-1 & 2
#1.Write a program that asks your name and then greets you by your name: Examples:

#If you enter Viivi as your name, the program will greet you with Hello, Viivi!.
#If you enter Ahmed as your name, the program will greet you with Hello, Ahmed!.
# Ask the user for their name
name = input("What is your name? ")

# Greet the user by their name
print("Hello, " + name + "!")
#2.Write a program that asks the user for the radius of a circle and the prints out the area of the circle.
# Ask the user for the radius of the circle
radius = float(input("Enter the radius of the circle: "))

# Calculate the area of the circle
area = 3.14159 * (radius ** 2)

# Print the result
print(f"The area of the circle with radius {radius} is {area:.2f}")
#3. Write a program that asks the user for the length and width of a rectangle. The program then prints out the perimeter and area of the rectangle. The perimeter of a rectangle is the sum of the lengths of each four sides.
# Ask the user for the length and width of the rectangle
length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))

# Calculate the perimeter and area of the rectangle
perimeter = 2 * (length + width)
area = length * width

# Print the results
print(f"The perimeter of the rectangle is {perimeter:.2f}")
print(f"The area of the rectangle is {area:.2f}")
#4.Write a program that asks the user for three integer numbers. The program prints out the sum, product, and average of the numbers.
# Ask the user for three integer numbers
num1 = int(input("Enter the first integer: "))
num2 = int(input("Enter the second integer: "))
num3 = int(input("Enter the third integer: "))

# Calculate the sum, product, and average
sum_of_numbers = num1 + num2 + num3
product_of_numbers = num1 * num2 * num3
average = sum_of_numbers / 3

# Print the results
print(f"Sum: {sum_of_numbers}")
print(f"Product: {product_of_numbers}")
print(f"Average: {average:.2f}")
#5. Write a program that asks the user to enter a mass in medieval units: talents (leiviskä), pounds (naula), and lots (luoti). The program converts the input to full kilograms and grams and outputs the result to the user:
#One talent is 20 pounds.
#One pound is 32 lots.
#One lot is 13,3 grams.
# Conversion factors
talent_to_kg = 30.24  # 1 talent is approximately 30.24 kg
pound_to_kg = 0.405  # 1 pound is approximately 0.405 kg
lot_to_g = 17.0145  # 1 lot is approximately 17.0145 g

# Ask the user for the mass in medieval units
talents = float(input("Enter the number of talents: "))
pounds = float(input("Enter the number of pounds: "))
lots = float(input("Enter the number of lots: "))

# Convert to kilograms and grams
mass_kg = (talents * talent_to_kg) + (pounds * pound_to_kg)
mass_g = lots * lot_to_g

# Split mass_kg into whole kilograms and grams
whole_kg = int(mass_kg)
remaining_g = int((mass_kg - whole_kg) * 1000)

# Print the result
print(f"The mass is {whole_kg} kilograms and {remaining_g} grams.")
#Write a program that draws two random combinations of numbers for a combination lock:
#a 3-digit code where each number is between 0 and 9.
#a 4-digit code where each number is between 1 and 6.
import random

# Generate a random 3-digit combination
combination_3_digit = [str(random.randint(0, 9)) for _ in range(3)]
combination_3_digit = ''.join(combination_3_digit)

# Generate a random 4-digit combination
combination_4_digit = [str(random.randint(1, 6)) for _ in range(4)]
combination_4_digit = ''.join(combination_4_digit)

# Print the combinations
print(f"3-Digit Combination: {combination_3_digit}")
print(f"4-Digit Combination: {combination_4_digit}")

# Module - 3
#Write a program that asks a fisher the length of a zander in centimeters. If the zander does not fulfill the size limit, the program instructs to release the fish back into the lake and notifies the user of how many centimeters below the size limit the caught fish was. A zander must be 42 centimeters or longer to meet the size limit.
# Define the size limit for the zander
size_limit = 42  # Minimum size in centimeters

# Ask the fisher for the zander's length
zander_length = float(input("Enter the length of the zander in centimeters: "))

# Check if the zander meets the size limit
if zander_length >= size_limit:
    print("Congratulations! The zander is of legal size.")
else:
    size_difference = size_limit - zander_length
    print(f"The zander is {size_difference:.2f} centimeters below the size limit.")
    print("Please release the fish back into the lake.")
#2.Write a program that asks the user to enter the cabin class of a cruise ship and then prints out a written description according to the list below. You must use an if/elif/else structure in your solution.

#LUX: upper-deck cabin with a balcony.
#A: above the car deck, equipped with a window.
#B: windowless cabin above the car deck.
#C: windowless cabin below the car deck.
#If the user enters an invalid cabin class, the program outputs an error message Invalid cabin class.
# Ask the user to enter the cabin class
cabin_class = input("Enter the cabin class (LUX, A, B, C): ")

# Check the cabin class and provide a description
if cabin_class == "LUX":
    description = "Upper-deck cabin with a balcony."
elif cabin_class == "A":
    description = "Above the car deck, equipped with a window."
elif cabin_class == "B":
    description = "Windowless cabin above the car deck."
elif cabin_class == "C":
    description = "Windowless cabin below the car deck."
else:
    description = "Invalid cabin class."

# Print the description
print(description)
#3. Write a program that asks for the biological gender and hemoglobin value (g/l). The program the notifies the user if the hemoglobin value is low, normal or high.

#A normal hemoglobin value for adult females is between 117-155 g/l.
#A normal hemoglobin value for adult males is between 134-167 g/l.
# Ask the user for biological gender and hemoglobin value
gender = input("Enter your biological gender (male/female): ")
hemoglobin_value = float(input("Enter your hemoglobin value (g/l): "))

# Define the normal hemoglobin ranges based on gender
if gender == "female":
    normal_range = (117, 155)
elif gender == "male":
    normal_range = (134, 167)
else:
    print("Invalid gender input. Please enter 'male' or 'female'.")
    exit()

# Check if the hemoglobin value is low, normal, or high
if normal_range[0] <= hemoglobin_value <= normal_range[1]:
    print("Hemoglobin value is within the normal range.")
elif hemoglobin_value < normal_range[0]:
    print("Hemoglobin value is low.")
else:
    print("Hemoglobin value is high.")
#4.Write a program that asks the user to enter a year and notifies the user whether the input year is a leap year. A year is a leap year if it is divisible by four. However, years divisible by 100 are leap years only if they are also divisible by 400.
# Ask the user to enter a year
year = int(input("Enter a year: "))

# Check if it's a leap year
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")
#Module - 4
#1. Write a program that uses a while loop to print out all numbers divisible by three in the range of 1-1000.
number = 1

while number <= 1000:
    if number % 3 == 0:
        print(number)
    number += 1
#2. Write a program that converts inches to centimeters until the user inputs a negative value. Then the program ends.
# Define the conversion factor from inches to centimeters
inches_to_cm = 2.54

while True:
    # Ask the user for input
    inches = float(input("Enter a length in inches (or a negative value to quit): "))

    # Check if the user wants to quit
    if inches < 0:
        print("Program ended.")
        break

    # Convert inches to centimeters and print the result
    centimeters = inches * inches_to_cm
    print(f"{inches} inches is equal to {centimeters:.2f} centimeters")
#3. Write a program that asks the user to enter numbers until they enter an empty string to quit. Finally, the program prints out the smallest and largest number from the numbers it received.
# Initialize variables for the smallest and largest numbers
smallest = None
largest = None

while True:
    user_input = input("Enter a number (or press Enter to quit): ")

    # Check if the user wants to quit
    if user_input == "":
        break

    try:
        number = float(user_input)
    except ValueError:
        print("Invalid input. Please enter a number or press Enter to quit.")
        continue

    if smallest is None or number < smallest:
        smallest = number

    if largest is None or number > largest:
        largest = number

if smallest is not None and largest is not None:
    print(f"Smallest number: {smallest}")
    print(f"Largest number: {largest}")
else:
    print("No valid numbers entered.")
#4. Write a game where the computer draws a random integer between 1 and 10. The user tries to guess the number until they guess the right number. After each guess the program prints out a text: Too high, Too low or Correct. Notice that the computer must not change the number between guesses.
import random

# Generate a random number between 1 and 10
target_number = random.randint(1, 10)

# Initialize a variable to keep track of the number of guesses
attempts = 0

while True:
    # Ask the user to guess the number
    user_guess = int(input("Guess the number (between 1 and 10): "))
    attempts += 1

    if user_guess < target_number:
        print("Too low.")
    elif user_guess > target_number:
        print("Too high.")
    else:
        print(f"Correct! You guessed the number in {attempts} attempts.")
        break
# 5. Write a program that asks the user for a username and password. If either or both are incorrect, the program ask the user to enter the username and password again. This continues until the login information is correct or wrong credentials have been entered five times. If the information is correct, the program prints out Welcome. After five failed attempts the program prints out Access denied. The correct username is python and password rules.
# Define the correct username and password
correct_username = "python"
correct_password = "rules"

# Initialize the number of login attempts
attempts = 0

# Use a while loop to allow multiple login attempts
while attempts < 5:
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    if username == correct_username and password == correct_password:
        print("Welcome")
        break
    else:
        print("Incorrect username or password. Please try again.")
        attempts += 1

if attempts >= 5:
    print("Access denied. You've reached the maximum number of login attempts.")
#6. Implement an algorithm for calculating an approximation for the value of pi (π). Let's assume that A is a unit circle. A unit circle has the radius of one and it is centered at the origin (0,0). Smallest possible square B is drawn around the unit circle so that circle A is completely inside the square. The corners of the square are now (-1,-1), (1, -1), (1, 1), and (-1, 1). If a large number of random points are scattered inside the square, the fraction of points that fall inside the circle A correlates with the fraction of the area of circle A compared to the area of square B: πr^2/4 = π*1^2/4 = π/4. This can be used as a simple method for calculating an approximation of the value of pi: Let's generate a large number of random points, such as one million, inside square B. Let N be the total number of random points. Each point inside the square is tested for whether it resides inside circle A. Let n be the total number of points that fall inside circle A. Now we have n/N≈π/4, and from that we get π≈4n/N. Write a program that asks the user how many random points to generate, and then calculates the approximate value of pi using the method explained above. At the end, the program prints out the approximation of pi to the user. (Notice that it is easy to test if a point falls inside circle A by testing if it fulfills the inequation x^2+y^2<1.).
import random

# Ask the user for the number of random points to generate
num_points = int(input("Enter the number of random points to generate: "))

# Initialize the count of points inside the circle
points_inside_circle = 0

# Generate random points and check if they are inside the circle
for _ in range(num_points):
    x = random.uniform(-1, 1)  # Random x-coordinate between -1 and 1
    y = random.uniform(-1, 1)  # Random y-coordinate between -1 and 1
    if x**2 + y**2 < 1:  # Check if the point is inside the circle
        points_inside_circle += 1

# Calculate the approximate value of pi
approx_pi = 4 * points_inside_circle / num_points

# Print the approximation of pi
print(f"Approximation of pi: {approx_pi}")
# Module - 5
#1. Write a program that asks the user how many dice to roll. The program rolls all the dice once and prints out the sum of the numbers. Use a for loop.
import random

# Ask the user how many dice to roll
num_dice = int(input("Enter the number of dice to roll: "))

# Initialize a variable to keep track of the sum
total_sum = 0

# Roll the dice and calculate the sum
for _ in range(num_dice):
    roll = random.randint(1, 6)  # Simulate rolling a 6-sided die
    total_sum += roll

# Print the sum of the dice rolls
print(f"Sum of {num_dice} dice rolls: {total_sum}")
#2. Write a program that asks the user to enter numbers until they input an empty string to quit. At the end, the program prints out the five greatest numbers sorted in descending order. Hint: You can reverse the order of sorted list items by using the sort method with the reverse=True argument.
# Initialize an empty list to store numbers
numbers = []

# Input numbers from the user until an empty string is entered
while True:
    user_input = input("Enter a number (or press Enter to quit): ")

    if user_input == "":
        break

    try:
        number = float(user_input)
        numbers.append(number)
    except ValueError:
        print("Invalid input. Please enter a number or press Enter to quit.")

# Check if there are any numbers to sort
if numbers:
    # Sort the list of numbers in descending order
    numbers.sort(reverse=True)

    # Print the top five numbers in descending order or all of them if there are less than five
    print("The five greatest numbers in descending order:")
    for num in numbers[:5]:
        print(num)
else:
    print("No valid numbers entered.")
#3. Write a program that asks the user for an integer and tells if the number is a prime number. Prime numbers are number that are only divisible by one or the number itself.

#For example, 13 is a prime number as it can only be divided by 1 or 13 so that the result is an integer.
#On the other hand, 21 is not a prime number as it is divisible by 3 and 7.
# Ask the user for an integer
num = int(input("Enter an integer: "))

# Check if the number is a prime number
if num < 2:
    is_prime = False
else:
    is_prime = True
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            is_prime = False
            break

# Print the result
if is_prime:
    print(f"{num} is a prime number.")
else:
    print(f"{num} is not a prime number.")
#4. Write a program that asks the user to enter the names of five cities one by on (use a for loop for reading the names) and stores them into a list structure. Finally, the program prints out the names of the cities one by one, one city per line, in the same order they were read as input. Use a for loop for asking the names and a for/in loop to iterate through the list.
# Initialize an empty list to store city names
cities = []

# Use a for loop to read the names of five cities
for i in range(5):
    city_name = input(f"Enter the name of city {i + 1}: ")
    cities.append(city_name)

# Use a for/in loop to print the city names
print("Cities you entered:")
for city in cities:
    print(city)
# Module - 6
#1.Write a function that returns a random dice roll between 1 and 6. The function should not have any parameters. Write a main program that rolls the dice until the result is 6. The main program should print out the result of each roll.
import random

# Define a function to simulate a dice roll
def roll_dice():
    return random.randint(1, 6)

# Main program to roll the dice until the result is 6
rolls = 0
while True:
    result = roll_dice()
    print(f"Roll {rolls + 1}: {result}")
    rolls += 1

    if result == 6:
        break

print(f"Congratulations! It took {rolls} rolls to get a 6.")
#2. Modify the function above so that it gets the number of sides on the dice as a parameter. With the modified function you can for example roll a 21-sided role-playing dice. The difference to the last exercise is that the dice rolling in the main program continues until the program gets the maximum number on the dice, which is asked from the user at the beginning.
import random

# Define a function to simulate a dice roll with a specified number of sides
def roll_dice(sides):
    return random.randint(1, sides)

# Ask the user for the number of sides and the maximum number on the dice
num_sides = int(input("Enter the number of sides on the dice: "))
max_number = int(input("Enter the maximum number on the dice: "))

# Main program to roll the dice until the maximum number is reached
rolls = 0
while True:
    result = roll_dice(num_sides)
    print(f"Roll {rolls + 1}: {result}")
    rolls += 1

    if result == max_number:
        break

print(f"Congratulations! It took {rolls} rolls to get a {max_number}.")
#3.Write a function that gets the quantity of gasoline in American gallons and returns the number converted to litres. Write a main program that asks for a volume in gallons from the user and converts the value to liters. The conversion must be done by using the function. Conversions continue until the user inputs a negative value.
# Define a function to convert American gallons to liters
def gallons_to_liters(gallons):
    liters = gallons * 3.78541
    return liters

# Main program
while True:
    # Ask the user for the quantity of gasoline in American gallons
    gallons = float(input("Enter the quantity of gasoline in American gallons (or a negative value to quit): "))

    if gallons < 0:
        print("Program ended.")
        break

    # Convert the input from gallons to liters using the function
    liters = gallons_to_liters(gallons)
    print(f"{gallons} gallons is equal to {liters:.2f} liters")
#4. Write a function that gets a list of integers as a parameter. The function returns the sum of all the numbers in the list. For testing, write a main program where you create a list, call the function, and print out the value it returned.
# Define a function to calculate the sum of integers in a list
def sum_of_list(numbers):
    return sum(numbers)

# Main program for testing
if __name__ == "__main__":
    # Create a list of integers
    integer_list = [5, 10, 15, 20, 25]

    # Call the function and print the result
    result = sum_of_list(integer_list)
    print(f"The sum of the list is: {result}")
#5. Write a function that gets a list of integers as a parameter. The function returns a second list that is otherwise the same as the original list except that all uneven numbers have been removed. For testing, write a main program where you create a list, call the function, and then print out both the original as well as the cut-down list.
# Define a function to filter out odd numbers from a list
def remove_odd_numbers(numbers):
    even_numbers = [x for x in numbers if x % 2 == 0]
    return even_numbers

# Main program for testing
if __name__ == "__main":
    # Create a list of integers
    integer_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    # Call the function and get the cut-down list
    cut_down_list = remove_odd_numbers(integer_list)

    # Print the original and cut-down lists
    print("Original list:", integer_list)
    print("Cut-down list (even numbers only):", cut_down_list)
# 6. Write a function that receives two parameters: the diameter of a round pizza in centimeters and the price of the pizza in euros. The function calculates and returns the unit price of the pizza per square meter. The main program asks the user to enter the diameter and price of two pizzas and tells the user which pizza provides better value for money (which of them has a lower unit price). You must use the function you wrote for calculating the unit prices.
import math

# Define a function to calculate the unit price per square meter
def unit_price(diameter, price):
    radius = diameter / 2
    area = math.pi * (radius ** 2)
    unit_price = price / area
    return unit_price

# Main program
if __name__ == "__main__":
    # Ask the user for the details of the first pizza
    diameter1 = float(input("Enter the diameter of the first pizza (in centimeters): "))
    price1 = float(input("Enter the price of the first pizza (in euros): "))

    # Calculate the unit price of the first pizza
    unit_price1 = unit_price(diameter1, price1)

    # Ask the user for the details of the second pizza
    diameter2 = float(input("Enter the diameter of the second pizza (in centimeters): "))
    price2 = float(input("Enter the price of the second pizza (in euros): "))

    # Calculate the unit price of the second pizza
    unit_price2 = unit_price(diameter2, price2)

    # Determine which pizza provides better value for money
    if unit_price1 < unit_price2:
        print("The first pizza provides better value for money.")
    elif unit_price2 < unit_price1:
        print("The second pizza provides better value for money.")
    else:
        print("Both pizzas have the same unit price.")
# Module-7
#1. Write a program that asks the user for a number of a month and then prints out the corresponding season (spring, summer, autumn, winter). Save the seasons as strings into a tuple in your program. We can define each season to last three months, December being the first month of winter.
# Define a tuple of seasons
seasons = ("Winter", "Spring", "Summer", "Autumn", "Winter")

# Ask the user for a number of a month (1-12)
month_number = int(input("Enter the number of a month (1-12): "))

# Check if the input is within the valid range
if 1 <= month_number <= 12:
    # Determine the season based on the month
    season_index = (month_number - 1) // 3
    season = seasons[season_index]
    print(f"The season for month {month_number} is {season}.")
else:
    print("Invalid input. Please enter a number between 1 and 12.")
#2. Write a program that asks the user to enter names until he/she enters an empty string. After each name is read the program either prints out New name or Existing name depending on whether the name was entered for the first time. Finally, the program lists out the input names one by one, one below another in any order. Use the set data structure to store the names.
# Initialize an empty set to store names
names_set = set()

# Collect names from the user until an empty string is entered
while True:
    name = input("Enter a name (or press Enter to finish): ")

    if name == "":
        break

    if name in names_set:
        print("Existing name")
    else:
        print("New name")
        names_set.add(name)

# List the entered names one by one
print("Entered names:")
for name in names_set:
    print(name)
#3. Write a program for fetching and storing airport data. The program asks the user if they want to enter a new airport, fetch the information of an existing airport or quit. If the user chooses to enter a new airport, the program asks the user to enter the ICAO code and name of the airport. If the user chooses to fetch airport information instead, the program asks for the ICAO code of the airport and prints out the corresponding name. If the user chooses to quit, the program execution ends. The user can choose a new option as many times they want until they choose to quit. (The ICAO code is an identifier that is unique to each airport. For example, the ICAO code of Helsinki-Vantaa Airport is EFHK. You can easily find the ICAO codes of different airports online.)
# Initialize an empty dictionary to store airport data
airport_data = {}

while True:
    # Ask the user for the desired action
    print("Options:")
    print("1. Enter a new airport")
    print("2. Fetch airport information")
    print("3. Quit")
    choice = input("Enter your choice (1/2/3): ")

    if choice == "1":
        # Enter a new airport
        icao = input("Enter the ICAO code of the airport: ")
        name = input("Enter the name of the airport: ")
        airport_data[icao] = name
        print("New airport information saved.")
    elif choice == "2":
        # Fetch airport information
        icao = input("Enter the ICAO code of the airport: ")
        if icao in airport_data:
            print(f"The name of the airport with ICAO code {icao} is {airport_data[icao]}.")
        else:
            print(f"Airport with ICAO code {icao} not found.")
    elif choice == "3":
        # Quit the program
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please select 1, 2, or 3.")
# MOdule - 8
#1. Write a program that asks the user to enter the ICAO code of an airport. The program fetches and prints out the corresponding airport name and location (town) from the airport database used on this course. The ICAO codes are stored in the ident column of the airport table.
import sqlite3

# Create an in-memory SQLite database and a cursor
conn = sqlite3.connect(":memory:")
cursor = conn.cursor()

# Create a table to store airport data
cursor.execute("CREATE TABLE airport (icao TEXT, name TEXT, location TEXT)")
conn.commit()
#2. Write a program that asks the user to enter the area code (for example FI) and prints out the airports located in that country ordered by airport type. For example, Finland has 65 small airports, 15 helicopter airports and so on.
# Sample airport data organized by country code and airport type
airport_data = {
    "FI": {
        "Small Airport": ["Airport1", "Airport2", "Airport3"],
        "Helicopter Airport": ["Heliport1", "Heliport2"],
        # Add more airport types as needed
    },
    "US": {
        "Small Airport": ["SmallAirport1", "SmallAirport2"],
        "Large Airport": ["LargeAirport1", "LargeAirport2"],
    },
    # Add more countries as needed
}

# Function to fetch and print airports by country and airport type
def fetch_airports_by_country(country_code):
    if country_code in airport_data:
        print(f"Airports in {country_code}:")
        country_airports = airport_data[country_code]
        for airport_type, airports in sorted(country_airports.items()):
            print(f"{airport_type}: {', '.join(airports)}")
    else:
        print(f"No airports found for country code {country_code}.")

# Main program
while True:
    country_code = input("Enter a country code (e.g., FI) or 'quit' to exit: ").upper()

    if country_code == 'QUIT':
        break

    fetch_airports_by_country(country_code)
#3 Write a program that asks the user to enter the ICAO codes of two airports. The program prints out the distance between the two airports in kilometers. The calculation is based on the airport coordinates fetched from the database. Calculate the distance using the geopy library: https://geopy.readthedocs.io/en/stable/. Install the library by selecting View / Tool Windows / Python Packages in your PyCharm IDE, write geopy into the search field and finish the installation.

from geopy.distance import geodesic

# Dictionary of airport coordinates (for demonstration)
airport_coordinates = {
    "EFHK": (60.317222, 24.963333),  # Example coordinates for Helsinki-Vantaa Airport (EFHK)
    "EGLL": (51.469722, -0.447778),  # Example coordinates for Heathrow Airport (EGLL)
}

# Function to calculate the distance between two airports
def calculate_distance(icao1, icao2):
    if icao1 in airport_coordinates and icao2 in airport_coordinates:
        coord1 = airport_coordinates[icao1]
        coord2 = airport_coordinates[icao2]
        distance = geodesic(coord1, coord2).kilometers
        return distance
    else:
        return None

# Main program
icao1 = input("Enter the ICAO code of the first airport: ").upper()
icao2 = input("Enter the ICAO code of the second airport: ").upper()

distance = calculate_distance(icao1, icao2)

if distance is not None:
    print(f"The distance between {icao1} and {icao2} is approximately {distance:.2f} kilometers.")
else:
    print("ICAO codes not found in the database.")


# Insert sample data into the airport table
cursor.executemany([
    ('EFHK', 'Helsinki-Vantaa Airport', 'Helsinki'),
    ('EGLL', 'Heathrow Airport', 'London'),
    ('KLAX', 'Los Angeles International Airport', 'Los Angeles'),
    # Add more data as needed
])
conn.commit()

# Function to fetch airport data based on ICAO code
def fetch_airport_info(icao_code):
    cursor.execute("SELECT name, location FROM airport WHERE icao = ?", (icao_code,))
    result = cursor.fetchone()
    return result

# Main program
while True:
    icao = input("Enter the ICAO code of an airport (or 'quit' to exit): ")

    if icao == 'quit':
        break

    result = fetch_airport_info(icao)

    if result is not None:
        name, location = result
        print(f"ICAO: {icao}, Name: {name}, Location: {location}")
    else:
        print("Airport not found.")

# Close the database connection
conn.close()



