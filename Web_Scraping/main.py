import requests
from bs4 import BeautifulSoup
import csv

# Make a request
page = requests.get(
    "https://codedamn-classrooms.github.io/webscraper-python-codedamn-classroom-website/")
# Parse the HTML content of the page using BeautifulSoup
soup = BeautifulSoup(page.content, 'html.parser')

# Create an empty list to store the extracted products
all_products = []

# Extract the product information using BeautifulSoup's select method
products = soup.select('div.thumbnail')
# Loop through each product
for product in products:
    # Extract the name of the product
    name = product.select('h4 > a')[0].text.strip()
    # Extract the description of the product
    description = product.select('p.description')[0].text.strip()
    # Extract the price of the product
    price = product.select('h4.price')[0].text.strip()
    # Extract the reviews of the product
    reviews = product.select('div.ratings')[0].text.strip()
    # Extract the image URL of the product
    image = product.select('img')[0].get('src')

    # Add the product details to the all_products list as a dictionary
    all_products.append({
        "name": name,
        "description": description,
        "price": price,
        "reviews": reviews,
        "image": image
    })

# Get the keys (field names) of the first product in the all_products list
keys = all_products[0].keys()

# Open a CSV file for writing the extracted product information
with open('products.csv', 'w', newline='') as output_file:
    # Create a DictWriter to write the extracted product information to the CSV file
    dict_writer = csv.DictWriter(output_file, keys)
    # Write the header row with the field names
    dict_writer.writeheader()
    # Write the extracted product information to the CSV file
    dict_writer.writerows(all_products)
