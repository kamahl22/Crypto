import requests

# Your Algorand address
algo_address = "H7OMXZEU45Y5UNMPR4EF7ETXZP3X6WAXDAE76OJGZY7BJYFJ4JIJ4M2KPM"

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
     

    transaction_types = []
    sender_addresses = []
    receiver_addresses = []
    #transaction_amounts = []
    for asset_id in asset_ids:
        # API endpoint for ASA transaction information
        api_endpoint = "https://algoindexer.algoexplorerapi.io/v2/accounts/" + algo_address + "/transactions"

        # Make the API request
        response_3 = requests.get(api_endpoint)

        # Check if the API request was successful
        if response_3.status_code == 200:
            # Get the ASA information from the response
            asa_transaction_information = response_3.json()

            # Get the 'name' and 'unit-name'
            asa_transactions = asa_transaction_information.get("transactions", [])
            for transaction in asa_transactions:
                asset_transfer_transaction = transaction.get("asset-transfer-transaction", {})
                transaction_type = asset_transfer_transaction.get("tx-type", "")
                sender_address = asset_transfer_transaction.get("sender", "")
                receiver_address = asset_transfer_transaction.get("receiver", "")
                asset_id = asset_transfer_transaction.get("asset-id", "")

                if transaction_type:
                    transaction_types.append(transaction_type)

                if sender_address:
                    sender_addresses.append(sender_address)

                if receiver_address:
                    receiver_addresses.append(receiver_address)

                if asset_id:
                    asset_ids.append(asset_id)

            print("Transaction Type:", transaction_types)
            print("Sender Address:", sender_address)
            print("Receiver Address:", receiver_address)
            print("Asset ID:", asset_id, " - ", asa_names)


            
            #if asset_id in asa_transactions:
              #  asset_id.append(asset_id, )
            #print(asa_transactions)
            
            #tx-type in transactions

               




else:
    # Print the error message
    print("Failed to retrieve Account Information:", response.json()["message"])
    print(response.content)
    
