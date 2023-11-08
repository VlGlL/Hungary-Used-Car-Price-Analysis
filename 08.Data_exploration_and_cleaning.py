import pandas as pd

# After having a snap of the data it became clear that, it needs to be cleaned:
# there are invalid locations and missing information.


# Define the clean_location function before its usage
def clean_location(location, seller_location):
    # Remove the "," at the end of the location if present
    if location.endswith(','):
        location = location[:-1]
    # Replace location with seller location if the condition is met
    keywords = ["A", "Erste", "Autók", "Telefonon", "AutoLab", "BK", "K", "M8",
                "PMCBurly", "Opticar", "Silver", "Kocsiguru", "MB", "CARNET-INVEST", "Spiler", "Nesztor", "Mobil",
                "Tazo", ""]
    if location in keywords:
        location = seller_location
    # Replacing Érd - Parkváros with 'Érd'
    if location == 'Érd - Parkváros':
        return 'Érd'
    # Correcting Kaposvár
    if location == 'Kaposvárp':
        return 'Kaposvár'
    return location


# Load the data
file_path = 'Modified_car_data.csv'
car_data = pd.read_csv(file_path)

# Remove "Térkép" from the end of strings in the 'Location' column
car_data['Location'] = car_data['Location'].str.replace(r'Térkép$', '', regex=True)

# Apply the function to the 'Location' column
car_data['Location'] = car_data.apply(lambda x: clean_location(x['Location'], x['Seller Location']), axis=1)

# Sorting the dataset by 'Year' in ascending order
car_data = car_data.sort_values(by='Year')

# Cleaning the 'Price' column by removing ' Ft' and converting to an integer
car_data['Price'] = car_data['Price'].str.replace(' Ft', '').str.replace('.', '', regex=False).astype(int)

# Number of unique locations and seller locations
num_unique_locations = car_data['Location'].nunique()
num_unique_seller_locations = car_data['Seller Location'].nunique()
print(f"Number of different locations: {num_unique_locations}")
print(f"Number of different seller locations: {num_unique_seller_locations}")

# Get and print unique values from both columns
unique_locations = car_data['Location'].unique()
unique_seller_locations = car_data['Seller Location'].unique()
print(f"Unique locations: {unique_locations}")
print(f"Unique seller locations: {unique_seller_locations}")

# Checking for zero values in 'Price' and 'Year' columns
zero_price_count = (car_data['Price'] == 0).sum()
zero_year_count = (car_data['Year'].isnull()).sum()
print(f"Number of zero values in the Price column: {zero_price_count}")
print(f"Number of zero values in the Year column: {zero_year_count}")

# Save the fully cleaned data to a new CSV file
final_file_path = 'CLEAN_DATA.csv'  # Replace with the full path if needed
car_data.to_csv(final_file_path, index=False)
