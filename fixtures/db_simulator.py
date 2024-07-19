import logging

import mysql.connector
import ulid
import random
import datetime

# Database connection
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="wayne_vault"
)

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
cursor = db.cursor()

# Configuration
WALLET_COUNT = 100_000
TRANSACTION_COUNT = 2_000_000
BATCH_SIZE = 100_000

wallet_types = ['Safe', 'Business', 'IPG', 'Commission', 'Settlement']
transaction_types = ['CashIn', 'CashOut', 'Payment', 'PaymentRefund', 'Commission', 'CommissionRefund', 'Unblock']
receipt_types = ['Deposit', 'Withdraw']
receipt_statuses = ['Init', 'Pending', 'Accepted', 'Declined', 'Canceled']


# Generate wallets
def generate_wallets(batch_size):
    logging.info(f'Generating wallets with batch size {batch_size}')
    wallets = []
    for _ in range(batch_size):
        wallet_id = str(ulid.new())
        slug = wallet_id
        wallet_type = random.choice(wallet_types)
        wallets.append((wallet_id, slug, wallet_type))
        logging.info(f"Inserting wallet with ID {wallet_id}")
    return wallets


# Insert wallets into database
def insert_wallets(wallets):
    cursor.executemany(
        "INSERT INTO wallets (id, slug, type) VALUES (%s, %s, %s)",
        wallets
    )
    db.commit()

# Generate transactions
def generate_transactions(batch_size, wallet_ids):
    logging.info(f'Generating transactions with batch size {batch_size}')
    transactions = []
    receipts = []
    invoices = []
    for _ in range(batch_size):
        transaction_id = str(ulid.new())
        transaction_type = random.choice(transaction_types)
        safe = random.randint(0, 1)
        amount = random.randint(1, 10000)
        if random.randint(0, 1):
            source_id = random.choice(wallet_ids)
            target_id = random.choice(wallet_ids)
        safe_source_id = random.choice(wallet_ids)
        safe_target_id = random.choice(wallet_ids)
        invoice_id = str(ulid.new())
        invoices.append((invoice_id, ))

        receipt_id = None
        if transaction_type in ['CashIn', 'CashOut']:
            receipt_id = str(ulid.new())
            receipt_type = random.choice(receipt_types)
            receipt_status = random.choice(receipt_statuses)
            receipts.append((receipt_id, receipt_type, receipt_status))
            logging.info(f"Inserting receipt with ID {receipt_id}")

        transactions.append((transaction_id, transaction_type, safe, amount, source_id, safe_source_id, target_id, safe_target_id, receipt_id, invoice_id))
    return transactions, invoices, receipts


# Insert transactions into database
def insert_transactions(transactions):
    cursor.executemany(
        "INSERT INTO transactions (id, type, safe, amount, source_id, safe_source_id, target_id, safe_target_id, receipt_id, invoice_id) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
        transactions
    )
    db.commit()


# Insert receipts into database
def insert_receipts(receipts):
    cursor.executemany(
        "INSERT INTO receipts (id, type, status) VALUES (%s, %s, %s)",
        receipts
    )
    db.commit()


def insert_invoices(invoices):
    cursor.executemany(
        "INSERT INTO invoices (id) VALUES (%s)",
        invoices
    )
    db.commit()


# Generate and insert data
wallet_ids = []
for _ in range(WALLET_COUNT // BATCH_SIZE):
    wallets = generate_wallets(BATCH_SIZE)
    insert_wallets(wallets)
    wallet_ids.extend([wallet[0] for wallet in wallets])

for _ in range(TRANSACTION_COUNT // BATCH_SIZE):
    transactions, invoices, receipts = generate_transactions(BATCH_SIZE, wallet_ids)
    insert_invoices(invoices)
    if receipts:
        insert_receipts(receipts)
    insert_transactions(transactions)

cursor.close()
db.close()
