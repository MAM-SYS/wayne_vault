BEGIN transaction;
INSERT INTO wallets (id, slug, TYPE)
		values("01J2KSPK2TG2B1486MFXZ0GMR2", "Commission", "Commission"),
		      ("01J2KST02T7N145WM993KQ6WF4", "IPG", "IPG"),
		      ("01J2KT0AF49ABF0HNDKZ6DAZ7Q", "+989397314927", "Business"),
		      ("01J2KT8K60HRG2142CM34SK83S", "+989163322747", "Business"),
INSERT INTO invoices (id)
		values("01J2KT0CTKCB1S1EMHP2C9MQ6N");
INSERT INTO receipts (id, TYPE, status, meta)
		values("01J2KTC8RHHB5C17V2TC2N49SK", "Deposit", "Accepted", NULL);
INSERT INTO transactions (id, TYPE, safe, amount, source_id, safe_source_id, target_id, safe_target_id, receipt_id, invoice_id)
		values("01J2KSP96M95JXP5H7PH7QWHFB", "CashIn", FALSE, 50000, "01J2KST02T7N145WM993KQ6WF4", null, "01J2KT0AF49ABF0HNDKZ6DAZ7Q", null, "01J2KTC8RHHB5C17V2TC2N49SK", "01J2KT0CTKCB1S1EMHP2C9MQ6N"),
		      ("01J2KW4D0S91TBDJJN3KVD4G0V", "Commission", FALSE, 5000, "01J2KT0AF49ABF0HNDKZ6DAZ7Q", null, "01J2KSPK2TG2B1486MFXZ0GMR2", null, NULL, "01J2KT0CTKCB1S1EMHP2C9MQ6N"),
		      ("01J2KV28ETBZ71J89D01N8DFYS", "Payment", TRUE, 45000, "01J2KT0AF49ABF0HNDKZ6DAZ7Q", null, null, "01J2KT8K60HRG2142CM34SK83S", NULL, "01J2KT0CTKCB1S1EMHP2C9MQ6N"),
		      ("01J2X9Z4W7N7VPXNK2HW9S835A", "PaymentRefund", TRUE, 45000, null, "01J2KT8K60HRG2142CM34SK83S", null, "01J2KT0AF49ABF0HNDKZ6DAZ7Q", NULL, "01J2KT0CTKCB1S1EMHP2C9MQ6N"),
		      ("01J3517692X32CPK15K0TEQW1C", "Unblock", TRUE, 45000, null, "01J2KT0AF49ABF0HNDKZ6DAZ7Q", "01J2KT0AF49ABF0HNDKZ6DAZ7Q", null, NULL, "01J2KT0CTKCB1S1EMHP2C9MQ6N");
COMMIT;
