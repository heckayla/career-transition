import csv

with open('sample_filter_large_transactions.csv', mode='r') as file:
    csvReader = csv.reader(file)
    large_transactions = [] # Only catch transactions larger than 100
    for lines in csvReader:
        try:
             amount = float(lines[2])
        except ValueError: #Header detected
            large_transactions.append(lines)
            continue
        except:
            print(f"Unexpected line error. Skipping invalid line: {lines}")     
            continue

        if amount > 100:
            large_transactions.append(lines)

    with open('filtered_transactions_output.csv', mode="w", newline='\n') as output_file:
        csvWriter = csv.writer(output_file)
        csvWriter.writerows(large_transactions)