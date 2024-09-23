import random
import pandas as pd

def generate_and_store_transactions_data_to_s3(event, context):
    df = pd.DataFrame(columns=['transaction_id', 'customer_id', 'product_id', 'quantity', 'price', 
                               'transaction_date', 'payment_type'])    
    for i in range(50):
        transaction_id = "TXN" + str(random.randint(10000000, 99999999))
        customer_id = "C" + str(random.randint(1, 9))
        product_id = random.choice(['P1', 'P2', 'P3', 'P4'])
        quantity = random.randint(1,5)
        price = price = round(random.uniform(10, 1000), 2)
        transaction_date = event['date']
        payment_type = random.choice(['Completed', 'Canceled', 'Payment Pending'])
        df.loc[i] = [transaction_id, customer_id, product_id, quantity, price, 
                               transaction_date, payment_type]

    event_str = event['date'].split("-")
    year = event_str[0]
    month = event_str[1]
    day = event_str[2]
    df.to_csv(f"s3://m3c1-assignment/transactions_data/year={year}/month={month}/day={day}/transactions_{event['date']}.csv", index=False)


# if __name__ == "__main__":
#     generate_and_store_transactions_data_to_s3({"date":"2024-09-23"},2)

    
