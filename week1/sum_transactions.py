import csv
with open('sample_transactions.csv', mode='r') as file:
    csvReader = csv.reader(file)
    min = None
    max = None
    total = 0
    count = 0
    for lines in csvReader:
        try:
             amount = float(lines[2])
        except:
            print(f"Skipping invalid data cell: {lines[2]}")     
            continue

        print(f"Current line: {lines}")
        total += amount
        count += 1
        if min is None or amount < min:
            min = amount
        if max is None or amount > max:
            max = amount
    
    average = total / count if count > 0 else 0

    print(f"Total: {total}, Count: {count}, Min: {min}, Max: {max}, Average: {average}")