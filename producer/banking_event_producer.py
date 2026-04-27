import json
import random
import time
from datetime import datetime, timezone
from azure.eventhub import EventHubProducerClient, EventData

# Replace with your NEW connection string (after rotating key)
CONNECTION_STR = ""
# Your Event Hub name
EVENT_HUB_NAME = "banking-transactions"

# Sample master data
customers = ["CUST101", "CUST102", "CUST103", "CUST104", "CUST105"]
accounts = ["ACC101", "ACC102", "ACC103", "ACC104", "ACC105"]
locations = ["Toronto", "Mississauga", "Brampton", "Vancouver", "Calgary"]
merchant_categories = ["Grocery", "Fuel", "Online", "Travel", "Crypto", "Restaurant"]
transaction_types = ["DEBIT", "CREDIT", "TRANSFER"]

# Create Event Hub Producer
producer = EventHubProducerClient.from_connection_string(
    conn_str=CONNECTION_STR,
    eventhub_name=EVENT_HUB_NAME
)

print("Sending banking transactions to Event Hub...\n")

try:
    while True:
        amount = round(random.uniform(10, 8000), 2)

        transaction = {
            "transaction_id": f"TXN{random.randint(100000, 999999)}",
            "account_id": random.choice(accounts),
            "customer_id": random.choice(customers),
            "transaction_type": random.choice(transaction_types),
            "amount": amount,
            "currency": "CAD",
            "merchant_category": random.choice(merchant_categories),
            "location": random.choice(locations),
            "device_id": f"DEV{random.randint(100, 999)}",
            "event_time": datetime.now(timezone.utc).isoformat(),
            "is_high_value": amount >= 5000
        }

        # Send event (BEST PRACTICE)
        event_data = EventData(json.dumps(transaction))
        producer.send_batch([event_data])

        # 🖨️ Print confirmation
        print(f"Sent: {transaction['transaction_id']} | Amount: {amount}")

        # ⏳ Wait 2 seconds
        time.sleep(2)

except KeyboardInterrupt:
    print("\nStopped sending events.")

finally:
    producer.close()
