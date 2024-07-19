import asyncio
import logging
import random
import ulid
from aiomysql import connect

# Logging setup
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Database connection parameters
host = "localhost"
user = "root"
password = ""
database = "wayne_vault"

# Configuration
WALLET_COUNT = 1000000
TRANSACTION_COUNT = 20000000
BATCH_SIZE = 10000000

wallet_types = ['Safe', 'Business', 'IPG', 'Commission', 'Settlement']
transaction_types = ['CashIn', 'CashOut', 'Payment', 'PaymentRefund', 'Commission', 'CommissionRefund', 'Unblock']
receipt_types = ['Deposit', 'Withdraw']
receipt_statuses = ['Init', 'Pending', 'Accepted', 'Declined', 'Canceled']

async def generate_wallets(batch_size):
    logging.info(f'Generating wallets with batch size {batch_size}')
    wallets = []
    for _ in range(batch_size):
        wallet_id = str(ulid.new())
        slug = wallet_id
        wallet_type = random.choice(wallet_types)
        wallets.append((wallet_id, slug, wallet_type))
        logging.info(f"Inserting wallet with ID {wallet_id}")
    return wallets

async def insert_wallets(conn, wallets):
    async with conn.cursor() as cur:
        await cur.executemany(
            "INSERT INTO wallets (id, slug, type) VALUES (%s, %s, %s)",
            wallets
        )
        await conn.commit()

async def generate_transactions(batch_size, wallet_ids):
    logging.info(f'Generating transactions with batch size {batch_size}')
    transactions = []
    receipts = []
    for _ in range(batch_size):
        # Transaction generation logic remains the same
        pass  # Placeholder for transaction generation logic

    return transactions, receipts

async def insert_transactions(conn, transactions):
    async with conn.cursor() as cur:
        await cur.executemany(
            "INSERT INTO transactions (id, type, safe, amount, source_id, safe_source_id, target_id, safe_target_id, receipt_id, invoice_id) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
            transactions
        )
        await conn.commit()

async def insert_receipts(conn, receipts):
    async with conn.cursor() as cur:
        await cur.executemany(
            "INSERT INTO receipts (id, type, status) VALUES (%s, %s, %s)",
            receipts
        )
        await conn.commit()

async def main():
    async with connect(host=host, user=user, password=password, db=database) as conn:
        wallet_ids = []
        for _ in range(WALLET_COUNT // BATCH_SIZE):
            wallets = await generate_wallets(BATCH_SIZE)
            await insert_wallets(conn, wallets)
            wallet_ids.extend([wallet[0] for wallet in wallets])

        for _ in range(TRANSACTION_COUNT // BATCH_SIZE):
            transactions, receipts = await generate_transactions(BATCH_SIZE, wallet_ids)
            await insert_transactions(conn, transactions)
            if receipts:
                await insert_receipts(conn, receipts)

if __name__ == "__main__":
    asyncio.run(main())
