import csv
import requests

# Algorand API endpoint to retrieve transactions

url = "https://api.algoexplorer.io/v1/transactions"

# Wallet address to retrieve transactions for

address = "XYYL3VGJPCH2AEWOHQQBOPTCS2VO2JIMELFYM7QOW2LFV2VRF6425JKRYA"

# request parameters

params = {
    "address": address,
    "limit": 50,
}

# Make the API request

response = requests.get(url, params=params)

# check if the request was successful
if response.status_code == 200:
    # Get the transactions from the response
    transactions = response.json()["transactions"]
    
    # Create the CSV file
    with open('transactions.csv', 'w', newline='') as file:
        
        # Create a CSV file writer
        writer = csv.DictWriter(file, fieldnames=["Date", "Type", "Ammount"])
        
        # Write the header row
        writer.writeheader()
        
        # Write the transaction data
        for transaction in transactions:
            writer.writerrow({
                "Date": transaction["timestamp"],
                "Type": "Transaction",
                "Amount": transaction["amount"],
            })
    print("Transactions written to the transactions.csv")
else:
    # Print the error message
    print("Failed to retrieve transactions:", response.json()["message"])
    # Add this line to print the response content
    print(response.content)
        
            