import requests
from bs4 import BeautifulSoup


def get_ad_urls(base_url, num_pages):
    ad_urls = []

    for page_num in range(1, num_pages + 1):
        # Assume the page URLs follow a predictable pattern with page number
        page_url = f"{base_url}/page/{page_num}"
        try:
            response = requests.get(page_url)
            response.raise_for_status()
        except requests.RequestException as e:
            print(f"An error occurred: {e}")
            continue  # Skip to the next page if an error occurs

        soup = BeautifulSoup(response.content, 'html.parser')
        ad_elements = soup.find_all('h3')  # Assuming each ad is listed within an <h3> element

        for ad_element in ad_elements:
            ad_link = ad_element.find('a')
            if ad_link:
                ad_url = ad_link['href']
                ad_urls.append(ad_url)

    return ad_urls


# Base URL of the listing pages
base_url = 'https://www.hasznaltauto.hu/talalatilista/PCOG2VG3R3RDADH5S56ADV4ZTXYLQKZUJAVTJUSK6NNHTKBJEEL2GJFNAYIP7P' \
           'SOLOMKNYVJ22YR3W6HY4CTS74T24QKOMZJGRCKZSBL3BRCGVUMJWSQQF5UNDHFAR3KUGCRIYHSYBWY6H4UF4YWE2FAQRYBDKZPHHUR62' \
           'IYG3QAXK24PJSCFBIYPPQHX2CZJKA3KL5SXTWTGR2KPPKOPKQOJQWI5YDN3W7CHRNU7W7EUUMBA63VGYCUPAJDAS4TQIQ7PRGHGW75BI' \
           'ZZMCSCP3RXFG4D6CRKMKGMLPOMTALFVQZRYLYY545APOPIBCO2STKGHUYHGYMHQCG6Q7SWSPEG3LCJAGUYOMRZGSO3ZKX7CET6A6776Y' \
           'MOBF5CPC772A3WVBZBMPXOG4HW4Q7FLCL5HMZ25PFLIMSPWV4F7DQ4SUSU4Q3GLZ36NGZT4N63T2F4THILCXLL5S2RVZNCWE6RO4M5ZH' \
           'AFV6QVAZMKMXDJOLMBRE7SVUMY33A7GLAXVWDTHIR22XQYQZREDNWHQDYQOOPB5YEAE6WRVXUL5GB3RZU6QUOKHNTDFVTK4TEM3RP42R' \
           'YA5YGNLY25GADE4FGFBLSFEXSVU72FMEKKJY5XXFXMLFT47EZ557WELMQXTW6RJKY3DM6PEAK5QW7PM4O4LDXMXT4EL5QFLEJOLC5RM7' \
           'UGVQGQNTCQD2BFSNDIF6SFHUY4OVWQSTUHNUQ4E4ENDRGCCXBURNPA74MXWRO5VK7PNTTYZISBDWJUEQQBL4DLFJCUYPKKYYNHIZYEI6' \
           '2KWWZ5PWSDJQBL22DS45TOQYZGGCOENDJW4TUEBHVKEH7NV7KY7AJIOKC7QA3MUZVDUY7QGV2DO7DFB3GJK5QOZIGPLNDTEK75B7WWVC' \
           '3O2DWO2PZGE6RYG'

# Number of listing pages to scrape
num_pages = 24

# Get the ad URLs
ad_urls = get_ad_urls(base_url, num_pages)

# Output the ad URLs to a text file
with open('ad_urls.txt', 'w') as file:
    for ad_url in ad_urls:
        file.write(f"{ad_url}\n")
