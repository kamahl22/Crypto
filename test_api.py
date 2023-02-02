import requests
import json
import datetime

# Your Algorand address
algo_address = "XYYL3VGJPCH2AEWOHQQBOPTCS2VO2JIMELFYM7QOW2LFV2VRF6425JKRYA"

# Convert "current-round", "from-round" and "to-round" dates to Algorand rounds
current_date = datetime.datetime.now()
current_round = int(current_date.timestamp() * 1000 / 100)
from_round = int(current_date.timestamp() * 1000 / 100)
start_date = datetime.datetime(2022, 1, 1)
end_date = datetime.datetime(2022, 12, 31)
from_round = int(start_date.timestamp() * 1000 / 100)
to_round = int(end_date.timestamp() * 1000 / 100)

# API endpoint for getting wallet information
api_endpoint = "https://algoindexer.algoexplorerapi.io/v2/accounts/" + algo_address

# Make the API request
response = requests.get(api_endpoint)

# Check if the API request was successful
if response.status_code == 200:
    # Get the account information from the response
    account_information = response.json()
    
    # Get the 'asset-id' value in the "account" field of the response
    assets = account_information.get("account", {}).get("assets", [])

    # Extract the asset-id from the account information
    asset_ids = []
    for asset in assets:
        asset_id = asset.get("asset-id")
        if asset_id:
            asset_ids.append(asset_id)
            
    print("Asset IDs:", asset_ids)
    
    asa_names = []
    asa_unit_names = []
    for asset_id in asset_ids:
        # API endpoint for ASA information
        api_endpoint = "https://algoindexer.algoexplorerapi.io/v2/assets/" + str(asset_id)
    
        # Make the API request
        response_2 = requests.get(api_endpoint)
    
        # Check if the API request was successful
        if response_2.status_code == 200:
            # Get the ASA information from the response
            asa_information = response_2.json()
            
            # Get the 'name' and 'unit-name'
            asa_name = asa_information.get("asset", {}).get("params", {}).get("name", "")
            asa_unit_name = asa_information.get("asset", {}).get("params", {}).get("unit-name", "")
            
            if asa_name:
                asa_names.append(asa_name)
                
            if asa_unit_name:
                asa_unit_names.append(asa_unit_name)
                
    print("ASA Names:", asa_names)
    print("ASA Unit Names:", asa_unit_names)
     

    transaction_type = []
    sender_address = []
    receiver_address = []
    #transaction_amounts = []
    for asset_id in asset_ids:
        # API endpoint for ASA transaction information
        api_endpoint = "https://algoindexer.algoexplorerapi.io/v2/accounts/" + algo_address + "/transactions?from-round=1234567&to-round=9876543"
    
        # Make the API request
        response_3 = requests.get(api_endpoint)
        
        # Check if the API request was successful
        if response_3.status_code == 200:
            # Get the ASA information from the response
            asa_transaction_information = response_3.json()
            
            current_round = asa_transaction_information.get("current-round", None)
            timestamp = current_round * 100 / 1000
            timestamp = datetime.datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S')

            # Add the timestamp to each transaction
            next_token = asa_transaction_information.get("next-token", None)
            transactions = asa_transaction_information.get("transactions", {})
            #print(transactions)
            for transaction in transactions:
                asset_transfer_transaction = transaction.get("asset-transfer-transaction", {})
                #print(asset_transfer_transaction)
                tx_type = transaction.get("tx-type", "")
                sender = transaction.get("sender", "")
                receiver = asset_transfer_transaction.get("receiver", "")
                amount = asset_transfer_transaction.get("amount", 0)
                id = transaction.get("id", "")
                transaction_asset_id = asset_transfer_transaction.get("asset-id", None)
                if transaction_asset_id in asset_ids:
                    index = asset_ids.index(transaction_asset_id)
                    #asa_name = asa_names[index]
                    #asa_unit_name = asa_unit_names[index]
                    current_timestamp = datetime.time()
                    current_datetime = datetime.datetime.now()
                    current_date_formatted = current_datetime.strftime("%d-%m-%Y")
                    
                    #if start_date <= current_datetime <= end_date:
                    print("Transaction Date:", current_date_formatted)
                    print("Asset IDs:", transaction_asset_id)
                    print("ASA Name:", asa_name)
                    print("ASA Unit Name:", asa_unit_name)
                    
                    from_timestamp = from_round * 100 / 1000
                    from_datetime = datetime.datetime.fromtimestamp(from_timestamp)
                    from_date_formatted = from_datetime.strftime("%d-%m-%Y")

                    to_timestamp = to_round * 100 / 1000
                    to_datetime = datetime.datetime.fromtimestamp(to_timestamp)
                    to_date_formatted = to_datetime.strftime("%d-%m-%Y")

                    print("From date:", from_date_formatted)
                    print("To date:", to_date_formatted)
                    print("Transaction Type:", tx_type)
                    print("Sender:", sender)
                    print("Receiver:", receiver)
                    print("Amount:", amount)
                    print("ID:", id)
                    print() 
else:
    # Print the error message
    print("Failed to retrieve Account Information:", response.json()["message"])
    print(response.content)
    
