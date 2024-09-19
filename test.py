import sqlite3
from tkinter import Tk
from PIL import Image
import requests
from io import BytesIO

#connect to the database
conn = sqlite3.connect(r'C:\Program Files\SQLiteStudio\Drinks.db')
c = conn.cursor()

#Get user input for the ingredient
ingredient = input("Enter and ingredient: ").lower()

#SQL query to select both the recipe name (column2) and the image file path (column7)
query = """
SELECT column2, column7
FROM Drinks
WHERE column10 LIKE ?
   OR column11 LIKE ?
   OR column12 LIKE ?
   OR column13 LIKE ?
   OR column14 LIKE ?
   OR column15 LIKE ?
   OR column16 LIKE ?
   OR column17 LIKE ?
   OR column18 LIKE ?
"""

#Parameters for the query (searching for the ingredient in multiple columns)
params = ('%' + ingredient  + '%',) * 9
c.execute(query, params)

#Fetch all matching results
drinks = c.fetchall()

#Check if any drinks were found
if drinks:
    print("Drinks that include", ingredient + ":")
    for recipe in drinks:
        drink_name = recipe[0]
        image_path = recipe[1] #This should be the file path from column7
        
        print(drink_name) #print the drink name

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
