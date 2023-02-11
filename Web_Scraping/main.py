#Importing libraries
import requests
from bs4 import BeautifulSoup
import csv

'''
# Make a GET request to the specified URL
res = requests.get('https://codedamn.com')

# Print the text content of the response
print(res.text)
# Print the HTTP status code of the response
print(res.status_code)  
'''

'''
# Make a request to https://codedamn-classrooms.github.io/webscraper-python-codedamn-classroom-website/
# Store the result in 'res' variable
res = requests.get(
    'https://codedamn-classrooms.github.io/webscraper-python-codedamn-classroom-website/')

# Store the text content of the response
txt = res.text
# Store the HTTP status code of the response
status = res.status_code

# Print the text content and the HTTP status code of the response
print(txt, status)
'''
'''
# Send a GET request to the URL
page = requests.get("https://codedamn.com")

# Create a BeautifulSoup object with the HTML content of the page
soup = BeautifulSoup(page.content, 'html.parser')

# Extract the text of the <title> tag
title = soup.title.text # This line retrieves the text content of the <title> tag

print(title)
'''

'''
page = requests.get(
    "https://codedamn-classrooms.github.io/webscraper-python-codedamn-classroom-website/")
    
# Create a BeautifulSoup object with the HTML content of the page
soup = BeautifulSoup(page.content, 'html.parser')

# Extract title of page
page_title = soup.title.text

# print the result
print(page_title) 
'''
'''
# Make a request
page = requests.get(
    "https://codedamn.com")
soup = BeautifulSoup(page.content, 'html.parser')

# Extract title of page
page_title = soup.title.text

# Extract body of page
page_body = soup.body

# Extract head of page
page_head = soup.head

# print the result
print(page_body, page_head)
'''

'''
# Make a request
page = requests.get(
    "https://codedamn-classrooms.github.io/webscraper-python-codedamn-classroom-website/")
soup = BeautifulSoup(page.content, 'html.parser')

# Extract title of page
page_title = soup.title

# Extract body of page
page_body = soup.body

# Extract head of page
page_head = soup.head

# print the result
print(page_title, page_head)
'''

'''
# Make a request
page = requests.get(
    "https://codedamn-classrooms.github.io/webscraper-python-codedamn-classroom-website/")
soup = BeautifulSoup(page.content, 'html.parser')

# Extract first <h1>(...)</h1> text
first_h1 = soup.select('h1')[0].text
'''
'''
# Make a request
page = requests.get(
    "https://codedamn-classrooms.github.io/webscraper-python-codedamn-classroom-website/")
soup = BeautifulSoup(page.content, 'html.parser')

# Create all_h1_tags as empty list
all_h1_tags = []

# Set all_h1_tags to all h1 tags of the soup
for element in soup.select('h1'):
    all_h1_tags.append(element.text)

# Create seventh_p_text and set it to 7th p element text of the page
seventh_p_text = soup.select('p')[6].text

print(all_h1_tags, seventh_p_text)
'''

'''
# Make a request
page = requests.get(
    "https://codedamn-classrooms.github.io/webscraper-python-codedamn-classroom-website/")
soup = BeautifulSoup(page.content, 'html.parser')

# Create top_items as empty list
top_items = []

# Extract and store in top_items according to instructions on the left
products = soup.select('div.thumbnail')
for elem in products:
    title = elem.select('h4 > a.title')[0].text
    review_label = elem.select('div.ratings')[0].text
    info = {
        "title": title.strip(),
        "review": review_label.strip()
    }
    top_items.append(info)

print(top_items)
'''

'''
# Make a request
page = requests.get(
    "https://codedamn-classrooms.github.io/webscraper-python-codedamn-classroom-website/")
soup = BeautifulSoup(page.content, 'html.parser')

# Create top_items as empty list
image_data = []

# Extract and store in top_items according to instructions on the left
images = soup.select('img')
for image in images:
    src = image.get('src')
    alt = image.get('alt')
    image_data.append({"src": src, "alt": alt})

print(image_data)
'''
'''
# Make a request
page = requests.get(
    "https://codedamn-classrooms.github.io/webscraper-python-codedamn-classroom-website/")
soup = BeautifulSoup(page.content, 'html.parser')

# Create an empty list to store the extracted links
all_links = []

# Extract the 'a' tags from the page using BeautifulSoup's select method
links = soup.select('a')
# Loop through each 'a' tag
for ahref in links:
    # Extract the text from the tag and strip any leading/trailing whitespaces
    text = ahref.text
    text = text.strip() if text is not None else ''

     # Extract the href from the tag and strip any leading/trailing whitespaces
    href = ahref.get('href')
    href = href.strip() if href is not None else ''

    # Append the extracted text and href to the all_links list as a dictionary
    all_links.append({"href": href, "text": text})

# Print the all_links list
print(all_links)
'''

'''
# Make a request
page = requests.get(
    "https://codedamn-classrooms.github.io/webscraper-python-codedamn-classroom-website/")
soup = BeautifulSoup(page.content, 'html.parser')

# Create an empty list to store the extracted products
all_products = []

# Use BeautifulSoup's select method to extract the product information from the page
products = soup.select('div.thumbnail')
# Loop through each product
for product in products:
    # TODO: Work on extracting the product information and storing it in the all_products list
    
        # Find the h4 tag, which contains the product name
    name = product.find('h4').text.strip()

    # Find the next sibling p tag after the h4 tag, which contains the price
    price = product.find('h4').find_next('p').text.strip()

    # Find the p tag with class "description", which contains the product description
    description = product.find('p', class_='description').text.strip()

    # Add the product details to the all_products list as a dictionary
    all_products.append({
        'name': name,
        'price': price,
        'description': description
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

'''

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
