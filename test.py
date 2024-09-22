import sqlite3
from tkinter import Tk
from PIL import Image
import requests
from io import BytesIO

#connect to the database
conn = sqlite3.connect(r'C:\Users\colto\Desktop\Bartending\Bartending-App\Drinks.db')
c = conn.cursor()

#Get user input for multiple ingredient
ingredients_input = input("Enter each ingredient seperated by a comma: ").lower()
ingredients = [ing.strip() for ing in ingredients_input.split(',')]

# Dynamically construct the SQL query to search for all ingredients
query = """
SELECT column2, column7, column10,column11,column12,column13,column14,column15,column16,column17,column18, column19, column20,column21,column22,column23,column24,column25,column26,column27,column28
FROM Drinks
WHERE """ + " OR ".join(
    [f"(column10 LIKE ? OR column11 LIKE ? OR column12 LIKE ? OR column13 LIKE ? OR column14 LIKE ? OR column15 LIKE ? OR column16 LIKE ? OR column17 LIKE ? OR column18 LIKE ?)"
    for _ in ingredients])

#prepare the parameters (for each ingredient, we need 9 placeholders)
params = []
for ingredient in ingredients:
    params.extend(['%' + ingredient  + '%'] * 9)

#execture the query with the parameters
c.execute(query, params)

#Fetch all matching results
drinks = c.fetchall()

#Check if any drinks were found
if drinks:
    print("Drinks that include", ingredient + ":")
    for recipe in drinks:
        drink_name = recipe[0]        
        image_path = recipe[1] #This should be the file path from column7
        gredients = recipe[2:10]
        instructions = recipe[11] #This should output the instructions
        measures = recipe[12:20] #this should hopefully output all the measurements

        print(f"\n{drink_name}") #print the drink name
        print(gredients)
        print(measures)
        print(instructions)

        #try to open image and display it
        if image_path.startswith('http://') or image_path.startswith('https://'):
            try:
                response = requests.get(image_path)
                img = Image.open(BytesIO(response.content))  # Open the image from the downloaded content
                img.show()  # Display the image
            except Exception as e:
                print(f"Could not open image for {drink_name}: {e}")
        else:
            # If the image path is a local file, try to open it
            try:
                img = Image.open(image_path)  # Open the image using its file path
                img.show()  # This will display the image
            except Exception as e:
                print(f"Could not open image for {drink_name}: {e}")
else:
    print("No recipe or shit broken idk")

#close the connection
conn.close()
