import pandas as pd

# Load the data from the file
file_path = '5.car_data_extracted_from_urls.csv'
car_data = pd.read_csv(file_path)


# Define a function to transform the year format if needed
def transform_year(year):
    # Check if the year is in the format 'YYYY'
    if len(str(year)) == 4:
        # Transform it to 'YYYY-01'
        return f"{year}-01"
    else:
        # If the year is in 'YYYY/MM' format, convert it to 'YYYY-MM'
        parts = str(year).split('/')
        if len(parts) == 2 and parts[1].isdigit():
            return f"{parts[0]}-{int(parts[1]):02d}"
        else:
            # If the format is not recognized, return the original string
            return year


# Apply the function to the 'Year' column
car_data['Year'] = car_data['Year'].apply(transform_year)

# Save the modified data to a new CSV file
new_file_path = 'Modified_car_data.csv'  # Replace with your desired file path
car_data.to_csv(new_file_path, index=False)
