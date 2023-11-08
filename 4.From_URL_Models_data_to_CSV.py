import requests
from bs4 import BeautifulSoup
import csv
import re


def parse_ad(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Check if the request was successful
    except requests.RequestException as e:
        print(f"An error occurred: {e}")
        return None

    soup = BeautifulSoup(response.content, 'html.parser')

    # Extracting the information
    try:
        year = soup.find('strong', {'class': 'adview__year'}).text.strip()
        mileage = soup.find('strong', {'class': 'adview__mileage'}).text.strip()
        price = soup.find('div', {'class': 'ListingPagePrice-secondary adview_main-price'}).text.strip()
        model = soup.find('div', {'class': 'col-xs-28 alcim'}).text.strip()

        # Extracting additional information
        doors = soup.find('td', text='Ajtók száma:').find_next('td').text.strip()
        color = soup.find('td', text='Szín:').find_next('td').text.strip()
        ac_type = soup.find('td', text='Klíma fajtája:').find_next('td').text.strip()
        fuel_type = soup.find('td', text='Üzemanyag:').find_next('td').text.strip()
        power = soup.find('td', text='Teljesítmény:').find_next('td').text.strip()
        location = soup.find('span', {'class': 'contact-button-text'}).text.strip().split()[0]
        total_weight = soup.find('td', text='Teljes tömeg:').find_next('td').text.strip()
        gear_shift = soup.find('td', text='Sebességváltó:').find_next('td').text.strip()

        # Extracting Seller Location information from description
        description = soup.find('meta', {'name': 'description'})['content']
        seller_location_match = re.search(r'\(Eladó címe: (.*?)\)', description)
        seller_location = seller_location_match.group(1) if seller_location_match else None

    except AttributeError as e:
        print(f"An error occurred while parsing: {e}")
        return None

    # Clean up mileage, price, and other text data by removing unwanted characters
    mileage = mileage.replace('\xa0', '').replace('km', '').strip()
    price = price.replace('\xa0', '').replace('Ft', '').strip()
    power_kw, power_le = power.replace('\xa0', '').split(',')
    power_kw = power_kw.strip().split()[0]  # Extracting only the numeric part for kW
    power_le = power_le.strip().split()[0]  # Extracting only the numeric part and appending ' LE' for LE
    total_weight = total_weight.replace('\xa0', '').replace(' kg', '') + ' KG'

    # Creating a dictionary to hold the information
    ad_info = {
        'Year': year,
        'Mileage': f'{mileage} km',  # Add 'km' back to mileage after cleaning
        'Price': f'{price} Ft',  # Add 'Ft' back to price after cleaning
        'Model': model,
        'Number of Doors': doors,
        'Color': color,
        'Air Condition Type': ac_type,
        'Fuel Type': fuel_type,
        'Horse Power': f'{power_kw} kW, {power_le}',
        'Location': location,
        'Seller Location': seller_location,
        'Total Weight': total_weight,
        'Gear Shift': gear_shift
    }

    return ad_info


def write_to_csv(data, filename):
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=data[0].keys())
        writer.writeheader()
        for row in data:
            writer.writerow(row)


# Read URLs from a file
with open('ad_urls.txt', 'r') as file:
    urls = [line.strip() for line in file]

# Parsing each URL
data = []
for url in urls:
    info = parse_ad(url)
    if info:
        data.append(info)
    else:
        print(f"Failed to parse information from {url}")

# Writing data to CSV
if data:
    write_to_csv(data, '5.car_data_extracted_from_urls.csv')
else:
    print("No data to write.")
