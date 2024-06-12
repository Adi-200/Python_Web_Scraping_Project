## Overview
Grocery Stores In New York Web Scraping project involves the extraction of detailed information about grocery stores in New York City from the Yellow Pages website using web scraping techniques. The primary objective is to gather structured data including store names, types, addresses, and contact numbers. The extracted data is then cleaned 
and organized for further analysis or use in other applications.

## Objective
* To extract structured information about grocery stores from the Yellow Pages.
* To clean and format the extracted data for usability.
* To provide a structured dataset that can be used for various analytical or business purposes.

## Outline
From this site, we have extracted the following information:
1. Store Name
2. Store Type
3. Street Address
4. Locality
5. Contact No
   
## Key Features

### Web Scraping Implementation:
* HTML Content Fetching: Uses the requests library to send HTTP requests and retrieve HTML content from the Yellow Pages.
* HTML Parsing: Utilizes BeautifulSoup to parse the retrieved HTML content, allowing for easy navigation and data extraction from the document object model (DOM).

### Data Extraction:
* Store Names: Extracts the names of grocery stores using specific CSS selectors to target relevant HTML elements.
* Store Types: Captures the categories or types of grocery stores, applying regular expressions to ensure correct spacing and text formatting.
* Street Addresses: Extracts the street addresses of the stores, cleanses the data using regular expressions to standardize the format.
* Locality: Gathers information about the locality or neighbourhood where each store is located.
* Contact Numbers: Extracts phone numbers and filters them using regular expressions, particularly focusing on identifying numbers that meet specific criteria, such as starting with a particular digit.

### Data Cleaning and Validation:
* Regular Expressions: Implements regex patterns to clean and validate the extracted data, ensuring consistency and removing unnecessary whitespace or formatting issues.
* Consistent Data Formatting: Ensures all extracted information is uniformly formatted for ease of analysis and integration into other systems.
  
### Data Organization:
* Pandas Data Frame: Structures the cleaned data into a Pandas Data Frame, which facilitates easy manipulation, analysis, and exporting of the data to various formats.

## Skills
* Python
  

