# career transition
This repository shows the output of my plan to dust off my scripting skills as I prepare for a career shift back to the tech industry, specifically targeting roles in the Implementation family. The repo is organized into different projects and learning exercises I've undertaken in this endeavor.

## Contents of Specific Folders

### week1
Contains the initial scripts I put together to refresh my skills in parsing CSV files for relatively-realistic use cases in accounting. Also contains CSV inputs and CSV outputs for those files.

- `sum_transactions.py`: Takes a CSV list of transactions as input, and prints the sum of their amounts, the count of transactions, the min amount, the max amount, and the average amount.
- `filter_large_transactions.py`: Takes a CSV list of transactions as input, and returns as output only the transactions from that list whose amounts are greater than 100.
- `normalize_merchants.py`: Takes a CSV list of transactions as input, and returns a CSV list of the same transactions with their merchant names normalized. Currently only supports a specific set of merchants (Amazon, Walmart, Target, Starbucks, DoorDash, Uber), but could be extended relatively easily.
