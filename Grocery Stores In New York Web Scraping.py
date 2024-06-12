# Setting Up Web Scraping Environment
import requests
from bs4 import BeautifulSoup
import re

# Fetch the webpage content
page = requests.get("https://www.yellowpages.com/new-york-ny/grocery-stores")

# Parse the webpage content using BeautifulSoup
soup = BeautifulSoup(page.content,'html.parser') 

def clean_text(text):
    # Remove extra spaces, line breaks, and tabs
    text = re.sub(r'\s+', ' ', text).strip()
    return text

# Extract store names

Shop_name_tags = soup.select(".business-name")
Shop_name = [clean_text(i.get_text()) for i in Shop_name_tags]
print(Shop_name[:30])


len(Shop_name[:30])

#Extract store type

Shop_types = soup.select(".categories")
Shop_type = []
for i in Shop_types:
    Shop_type.append(clean_text(i.get_text()))
print(Shop_type[:30])

len(Shop_type[:30])

#Extract street address

address = soup.select(".street-address")
Street_address = []
for i in address:
    Street_address.append(clean_text(i.get_text()))
print(Street_address)

len(Street_address)

#Extract locality

locality = soup.select(".locality")
locality
Locality_add = []
for i in locality:
    Locality_add.append(clean_text(i.get_text()))
print(Locality_add)

len(Locality_add)

#Extract Phone Number

phone = soup.select(".phones.phone.primary")
Phone_number= []
for i in phone:
    Phone_number.append(clean_text(i.get_text()))
print(Phone_number)

len(Phone_number)

#Extract Phone number where local part starts with '5'

phone_numbers = [
    '(212) 255-2106', '(212) 722-9156', '(212) 349-6555', '(212) 689-9192', '(212) 977-1710',
    '(212) 308-6922', '(888) 828-9465', '(212) 874-9506', '(212) 222-6500', '(212) 374-9474',
    '(212) 925-3898', '(212) 925-2111', '(212) 514-5220', '(212) 463-7059', '(212) 229-0301',
    '(212) 588-5888', '(212) 580-6312', '(212) 426-6081', '(212) 360-7608', '(212) 663-2263',
    '(646) 964-4633', '(212) 410-1640', '(212) 349-8010', '(212) 304-1858', '(212) 233-0808',
    '(212) 608-3863', '(917) 261-4530', '(212) 260-0100', '(646) 225-9300', '(212) 420-1600'
]

# Regular expression to match phone numbers where the local part starts with '5'

pattern = re.compile(r'\(\d{3}\) 5\d{2}-\d{4}')

# Filter phone numbers that match the pattern
numbers_starting_with_5 = [number for number in phone_numbers if pattern.match(number)]

print(numbers_starting_with_5)

# DataFrame Creation

import pandas as pd
# Creating a DataFrame with grocery store details
df = pd.DataFrame({"Store Name":Shop_name[:30],"Store Type":Shop_type[:30],"Street Address":Street_address,"Locality":Locality_add,"Contact No":Phone_number})
# Displaying the DataFrame
df

# Save the DataFrame to a CSV file
df.to_csv("Grocery Stores In NewYork.csv",index = False)

# Load the DataFrame from the CSV file
df = pd.read_csv("Grocery Stores In NewYork.csv")

# Display the first few rows of the DataFrame
df.head()

# Display the last few rows of the DataFrame
df.tail()

# Generate descriptive statistics for numerical columns in the DataFrame
df.describe()

# Provide a concise summary of the DataFrame
df.info()
