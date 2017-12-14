"""
Will print colors parsed from Google Material Design color page
"""

import requests
import bs4

soup = bs4.BeautifulSoup(
    requests.get('https://material.io/guidelines/style/color.html#color-color-palette').text,
    'html.parser'
)
blocks = soup.select('#color-color-palette > div > div > div > section > div')
kolors = {}
for block in blocks[:-2]:
    group = block.select_one('span.group')
    color_name = group.text
    numbers, hexs = [], []
    numbers.append(color_name.upper().replace(' ', '_'))
    # hexs.append(group.parent['style'].replace('background-color: ', '')[:-1])
    subcolors = block.select('div.details')
    hexs.append(subcolors[0].select_one('span.hex').text)
    for line in subcolors[1:]:
        col_num = line.select_one('span.shade').text
        col_hex = line.select_one('span.hex').text
        numbers.append(color_name.upper().replace(' ', '_') + col_num)
        hexs.append(col_hex)

    # print(color_name)
    kolors['# ' + color_name] = list(zip(numbers, hexs))


for k, v in kolors.items():
    print()
    print(k)
    for col, hex in v:
        print('{} = hex2rgb(\'{}\')'.format(col, hex))