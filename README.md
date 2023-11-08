# Hungary Used Car Price Analysis

## Project Overview
This repository hosts a data analysis project that investigates the regional price disparities in used car listings on the Hungarian website Hasznaltauto.hu. The analysis focuses on understanding market trends and testing the hypothesis that cars are listed for higher prices outside of Budapest.

## Features
- Web scraping with Python using `requests` and `BeautifulSoup`
- Data analysis and visualization
- Price comparison across different regions

## Prerequisites
Libraries, tools, or frameworks that need to be installed to run the project:
- Python
- BeautifulSoup4
- pandas
- matplotlib

## Repository Structure

  01.Brand_and_model_determination.py: Identifies popular car brands and models with the most listings.
  02.Extracting_URLS_into_txt.py: Extracts listing URLs and saves them to a text file for further processing.
  03.ad_urls.txt: Contains the extracted URLs from which the data is scraped.
  04.From_URL_Models_data_to_CSV.py: Scrapes data from each URL and stores it in a CSV file.
  05.car_data_extracted_from_urls.csv: The initial dataset extracted from the listings.
  06.Data__date_format_transformation.py: Transforms date formats within the dataset for consistency.
  07.Modified_car_data.csv: The dataset after date format transformation.
  08.Data_exploration_and_cleaning.py: Explores the data for insights and performs necessary cleaning.
  09.CLEAN_DATA.csv: The cleaned dataset ready for analysis.
  10.Data_visualization.py: Visualizes the findings using various data visualization techniques.

## Data
The data used in this project is sourced from public car listings, with the focus on providing a transparent and replicable analysis of the used car market in Hungary.

## Contributing
Contributions to this project are welcome. Please refer to the contributing guidelines for more details.
