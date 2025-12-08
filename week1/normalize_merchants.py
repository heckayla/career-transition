import csv
import re


def normalize_merchant_text(merchant):
    merchant = merchant.strip().lower()
    merchant = re.sub('[*]', ' ', merchant)
    merchant = re.sub('[0-9#]', '', merchant)  # Remove numbers and special characters
    merchant = re.sub('.com.*', '', merchant)  # Remove .com and any pages after
    merchant = re.sub('receipt|online|order|ride|food|meal|retail|purchase|digital|trip', '', merchant)
    merchant = re.sub('mn|minneapolis', '', merchant) # Remove place names
    merchant = re.sub(' +', ' ', merchant)  # Replace multiple spaces with single space
    return merchant

def match_merchant(m_text, m_list):
    for merchant in m_list:  
        for alias in merchant[1]:
            if alias in m_text:
                return merchant[0]
    print(f"No match found for merchant text: {m_text}")
    return "Unknown Merchant"

known_merchants = [
    ('Amazon', ['amazon', 'amzn', 'amazn', 'amz']),
    ('Walmart', ['walmart', 'wmt', 'wal-mart', 'wal mart']),
    ('Starbucks', ['starbucks', 'sbx', 'starbux', 'starbcks', 'starbk']),
    ('Target', ['target', 'tgt', 'trgt', 'tar']),
    ('DoorDash', ['doordash', 'door dash', 'ddash', 'drdsh', 'dd', 'dasher', 'drd', 'dordsh']),
    ('Uber', ['uber', 'ubr', ]),
]

with open('messy_50row_merchants.csv', mode='r') as file:
    csvReader = csv.reader(file)
    normalized_lines = []

    line_count = 0
    for line in csvReader:
        if line_count > 0:
            try:
                normalized_text = normalize_merchant_text(line[1])
                normalized_merchant = match_merchant(normalized_text, known_merchants)
                
                print(f"Merchant:  {normalized_merchant}")
                normalized_lines.append([line[0], normalized_merchant, line[2]])
            except IndexError:
                print(f"Skipping invalid line: {line}")
                continue
        else:
            normalized_lines.append(line)  # Keep header as is
        line_count += 1

    with open('normalized_50row_merchants.csv', mode="w", newline='\n') as output_file:
        csvWriter = csv.writer(output_file)
        csvWriter.writerows(normalized_lines)
        


