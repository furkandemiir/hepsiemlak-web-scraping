# hepsiemlak-web-scraping
 This project focuses on developing a Python application to scrape rental apartment data from Hepsiemlak.com for properties in İzmir, Buca. The data collected includes details such as listing date, description, neighborhood, floor level, building age, room count, size, furnished status, natural gas availability, and rental price. The scraped data is automatically saved into an Excel file. To ensure comprehensive data collection, pagination or scrolling is handled programmatically, and at least 500 listings are collected.

### *Technologies and Methods Used*
BeautifulSoup:
BeautifulSoup is a popular Python library used for web scraping tasks. It parses HTML and XML documents, enabling efficient data extraction. In this project, it was employed to retrieve detailed information from rental listings on Hepsiemlak.com.

### *Installation and Usage*:

!pip install beautifulsoup4

import requests

from bs4 import BeautifulSoup

### Implementation Steps
Project Planning:
Identified the key data points to collect: listing date, description, neighborhood, floor level, building age, room count, size, furnished status, natural gas availability, and rental price. Selected target pages based on these requirements.

Library Setup:
Installed the required libraries, BeautifulSoup and Requests, using the following command:

!pip install beautifulsoup4

Initial URL Request:
Sent a GET request to the target webpage, specifying a user-agent header to mimic a real browser request and avoid access restrictions.

url = "https://www.hepsiemlak.com/buca-kiralik"

response = requests.get(url, headers={"user-agent": "Mozilla/5.0"})

HTML Parsing:
Parsed the HTML content of the webpage using BeautifulSoup and analyzed its structure to identify the tags and classes containing the required data.

soup = BeautifulSoup(response.content, 'html.parser')

Data Extraction:
Extracted the listing details using specific HTML tags and classes. Loops and conditional checks were implemented to ensure all relevant information was captured.

listings = soup.find_all('div', class_='listing-detail')
for listing in listings:
    price = listing.find('span', class_='price').text
    room_count = listing.find('span', class_='room-count').text
    
Navigating Detail Pages:
Accessed individual listing detail pages using the href links provided on the main page. Adjusted relative URLs using the requests.compat.urljoin() function.

Data Cleaning and Handling Missing Values:
Addressed missing or inconsistent data by filling gaps with None to ensure uniformity.

Exporting to Excel:
Converted the cleaned data into a pandas DataFrame and saved it to an Excel file for further analysis and use.

![image](https://github.com/user-attachments/assets/d01d2055-815e-48f0-993b-aae1966b44ba)
