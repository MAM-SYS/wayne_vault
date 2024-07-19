

SELECT
    '01J2KT0AF49ABF0HNDKZ6DAZ7Q' as wallet_id,
    COALESCE(SUM(CASE
                 WHEN target_id = '01J2KT0AF49ABF0HNDKZ6DAZ7Q' THEN amount
                 WHEN source_id = '01J2KT0AF49ABF0HNDKZ6DAZ7Q' THEN -amount
                 ELSE 0
             END), 0) AS available_amount,
    COALESCE(SUM(CASE
                 WHEN safe_target_id = '01J2KT0AF49ABF0HNDKZ6DAZ7Q' THEN amount
                 WHEN safe_source_id = '01J2KT0AF49ABF0HNDKZ6DAZ7Q' THEN -amount
                 ELSE 0
             END), 0) AS blocked_amount
FROM
    transactions
WHERE (transactions.target_id = '01J2KT0AF49ABF0HNDKZ6DAZ7Q' OR transactions.source_id = '01J2KT0AF49ABF0HNDKZ6DAZ7Q' OR transactions.safe_target_id = '01J2KT0AF49ABF0HNDKZ6DAZ7Q' OR transactions.safe_source_id = '01J2KT0AF49ABF0HNDKZ6DAZ7Q')