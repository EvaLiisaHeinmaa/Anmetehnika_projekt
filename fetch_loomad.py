#Võimalik Pythoni kood

import requests
import pandas as pd

# Define the API endpoint and parameters
api_url = "https://avaandmed.eesti.ee/api/3/action/datastore_search"
resource_id = "your_resource_id_here"  # Replace with the actual resource ID

# Set up parameters for the API request
params = {
    "resource_id": resource_id,
    "limit": 1000  # Adjust as needed
}

# Make the API request
response = requests.get(api_url, params=params)

# Check if the request was successful
if response.status_code == 200:
    data = response.json()
    records = data["result"]["records"]
    
    # Convert records to a pandas DataFrame
    df = pd.DataFrame.from_records(records)
    
    # Display the first few rows of the DataFrame
    print(df.head())
else:
    print(f"Failed to fetch data. Status code: {response.status_code}")
