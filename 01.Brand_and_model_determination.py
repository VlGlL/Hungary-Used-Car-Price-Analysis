# Regional Price Disparities in Used Car Listings on Hasznaltauto.hu - Hungary

# Hypothesis: People are selling the same car on the website "https://www.hasznaltauto.hu/ - in Hungary
# with similar or identical features for more money outside of Budapest

import re
import requests
from bs4 import BeautifulSoup

# We first want to find out, which brand(s) we should choose. e g Audi / Mercedes
# I opted for those that have the highest number of active advertisements
# so the more chance we have the same cars with identical features outside of Budapest.

# to determine which brand to choose
# URL to fetch content from

url = "https://www.hasznaltauto.hu/talalatilista/PCOHKVG3R3RDADH5S56AD56ZBGH3WQULWRBCHLJUV6KQCU2CFZDESWQNED7H3HNWYM2" \
      "B35VJS2ORZ6Y4T4KOJ5CV32BBYT5E2AILCJFPMCB3KWDSNYWELOFCIVZYCKSSSONESAJGH64OT4SH4X3RQMOUWCDXAFOLVUOHKIBVU4G7RQR" \
      "KS5AEMUUIMECT56UVXEKFR6JCXO3XSVSI24PP3ONLAMJYWE3YLM2TQUUMTPXYWFBFPBYDWBKGQUTQOJUJFEMHET3K3RZYWHWNCERT2KN7JLA7" \
      "GUKQCFRSYPW3ORDUMIQTQ5LHBCTQQJXGRJT3MAPCZV32J5OW57GI6VUPPE47SSMZHR2QTEMFEDZGGBXZX7IYN3RGP4EHF74VRJO7MTYS76S25" \
      "UYPIVLPGV6DWXR4XF33KR7KSOMHBMFLIISPWR4F7DTMSUSU4TLPWHWCUIAXQX3PGL3CZEAKFPPV4VFOLQURHUPXGXSJCLLYBWCWVUFGTSPC2UU" \
      "UWSST2GWTKW5D47B6VJZRKTTIAZ7MFGQXATYYTUY6SXGGSLFCKY226LQDMIYQ63HYDC2R2ITFUUGIUZ5N7CYYBO2ATF3QAY7AJRISYQOO4VG3" \
      "LT5CUGXOJOENE4UZ5NHRGTC5GNU6UV4NNRTTWG6HHQHKDTIZL2BL76GWOXWL34KCHMHZJALWY5ALANHJLQMA35F4ZCJVGZUK7JGT7DOOB5U7" \
      "GXZU5USPYJBMZPGPBAKMEVPTAPJP37BCTGBA52RDWMFGPUNAR3EV3IMAVUAT33DBFJ7ASTXV2PWGU3MUQXA5DCHWTTTMSORUB46XT75KZFO6U" \
      "7UNYXBXAHQML6J2GI3ZFIZRIXRKMOQLWYBIB3SEWMBWTPUKL7NT6GX6AK33N534BSX5UJOWLUPVA2576A7EYW2J6"

# Fetch the content from the URL
response = requests.get(url)
content = response.content

# Parse the content using BeautifulSoup
soup = BeautifulSoup(content, 'html.parser')

# List to store brands and their numbers
brands_numbers = []

# Extract the desired information
for option in soup.find_all('option'):
    match = re.match(r"([A-Z]+) \((\d+)\)", option.get_text())
    if match:
        brand, number = match.groups()
        brands_numbers.append((brand, int(number)))

# Sort the list based on the numbers in descending order
sorted_brands = sorted(brands_numbers, key=lambda x: x[1], reverse=True)

# Print the top 3 brands with the highest numbers
for brand, number in sorted_brands[:3]:
    print(f"{brand} {number}")

# output: 13 Oct 2023 - VOLKSWAGEN 9623 / BMW 8490 / FORD 8322
# Choosing models - based on number of advertisements

# Source data that contains the model names and available numbers
source = '''Mindegy</option>\n<option value="4598">B-MAX (67)</option>\n<option value="520">BRONCO (4)</option>\n
<option value="1949">C-MAX (523)</option>\n<option value="521">CAPRI (4)</option>\n<option value="522">CONNECT
 (35)</option>\n<option value="523">CONSUL (1)</option>\n<option value="525">COUGAR (2)</option>\n<option value="526">
 COURIER (14)</option>\n<option value="527">CROWN VICTORIA (6)</option>\n<option value="20028">ECOSPORT (87)</option>\n
 <option value="530">EDGE (30)</option>\n<option value="13243">EGY\xc3\x89B (1)</option>\n<option value="532">ESCAPE (1)
 </option>\n<option value="533">ESCORT (51)</option>\n<option value="534">EXCURSION (3)</option>\n<option value="535">
 EXPEDITION (1)</option>\n<option value="536">EXPLORER (47)</option>\n<optgroup label="F SERIES">\n<option value="1967">
 F SERIES (48)</option>\n<option class="multiselect-subitem" value="8687">F 100 (2)</option>\n
 <option class="multiselect-subitem" value="8688">F 150 (32)</option>\n<option class="multiselect-subitem" value="8689">
 F 250 (9)</option>\n<option class="multiselect-subitem" value="8690">F 350 (4)</option>\n</optgroup>\n
 <optgroup label="FIESTA">\n<option value="540">FIESTA (843)</option>\n<option class="multiselect-subitem" value="7622">
 FIESTA COURIER (1)</option>\n</optgroup>\n<option value="1926">FLEX (2)</option>\n<optgroup label="FOCUS">\n
 <option value="541">FOCUS (2397)</option>\n<option class="multiselect-subitem" value="7727">FOCUS C-MAX (101)</option>
 \n</optgroup>\n<option value="543">FUSION (146)</option>\n<option value="1800">GALAXIE (2)</option>\n
 <option value="544">GALAXY (256)</option>\n<option value="545">GRANADA (2)</option>\n<optgroup label="KA">\n
 <option value="547">KA (105)</option>\n<option class="multiselect-subitem" value="7840">STREETKA (7)</option>\n
 </optgroup>\n<option value="25610">KA+ (3)</option>\n<option value="548">KUGA (717)</option>\n<option value="2007">LTD 
 (1)</option>\n<option value="549">MAVERICK (9)</option>\n<option value="550">MONDEO (1106)</option>\n
 <option value="551">MUSTANG (369)</option>\n<option value="552">ORION (3)</option>\n<option value="554">PROBE (1)
 </option>\n<option value="555">PUMA (215)</option>\n<option value="556">RANGER (190)</option>\n<option value="558">
 S-MAX (402)</option>\n<option value="559">SCORPIO (2)</option>\n<option value="560">SIERRA (10)</option>\n<option value
 ="561">TAUNUS (7)</option>\n<option value="562">TAURUS (1)</option>\n<option value="564">THUNDERBIRD (9)</option>\n
 <option value="11230">TOURNEO (114)</option>\n<option value="565">TRANSIT (483)</option>\n<option value="11231">VIGNALE
  (1)</option>\n<option value="566">WINDSTAR (1)'''

soup = BeautifulSoup(source, 'html.parser')
options = soup.find_all('option')

data = []

for option in options:
    text = option.get_text()
    if '(' in text:
        model, count = text.split(' (')
        count = count.strip(')')
        data.append((model, int(count)))

# Convert list of lists to list of tuples, remove duplicates, and sort
unique_data = list(set(data))
sorted_unique_data = sorted(unique_data, key=lambda x: x[1], reverse=True)

# Print the sorted data
for model, count in sorted_unique_data:
    print(f"Model: {model}, Count: {count}")

# Based on the output - we will choose the model Focus
