import re

def extractPriceFromText(price):

    pattern = r"\d+\.\d+"

    match = re.search(pattern, price)

    if match:
        return match.group()
    else:
        return 0
