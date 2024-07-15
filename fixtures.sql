-- fixtures
INSERT INTO wallets (id, type)
		values
		("01J2KSPK2TG2B1486MFXZ0GMR2", "Commission"),
		("01J2KST02T7N145WM993KQ6WF4", "IPG"),
		("01J2KT8K60HRG2142CM34SK83S", "Safe"),
		("01J2KT0AF49ABF0HNDKZ6DAZ7Q", "Business"),
		("01J2KT0B2SFW465290CCCD4V0G", "Business")
		;
-- ----------------------------------------
-- ----------------------------------------
-- ----------------------------------------
-- ----------------------------------------
-- ----------------------------------------
insert into invoices (id, safe_id)
values
("01J2KT0CTKCB1S1EMHP2C9MQ6N", "01J2KT8K60HRG2142CM34SK83S");

-- ----------------------------------------
-- ----------------------------------------
-- ----------------------------------------
-- ----------------------------------------
-- ----------------------------------------

insert into receipts (id, type, status, meta)
values
("01J2KTC8RHHB5C17V2TC2N49SK", "Deposit", "Accepted", null);

-- ----------------------------------------
-- ----------------------------------------
-- ----------------------------------------
-- ----------------------------------------
-- ----------------------------------------

INSERT INTO transactions (id, TYPE, amount, source_id, safe_id, target_id, receipt_id, invoice_id)
		values
-- 		("01J2KSP96M95JXP5H7PH7QWHFB", "CashIn", 50000, "01J2KST02T7N145WM993KQ6WF4", null, "01J2KT0AF49ABF0HNDKZ6DAZ7Q", "01J2KTC8RHHB5C17V2TC2N49SK", "01J2KT0CTKCB1S1EMHP2C9MQ6N"),
		("01J2KW4D0S91TBDJJN3KVD4G0V", "Commission", 5000, "01J2KT0AF49ABF0HNDKZ6DAZ7Q", null, "01J2KSPK2TG2B1486MFXZ0GMR2", null, "01J2KT0CTKCB1S1EMHP2C9MQ6N"),
-- 		("01J2KV28ETBZ71J89D01N8DFYS", "Payment", 45000, "01J2KT0AF49ABF0HNDKZ6DAZ7Q", "01J2KT8K60HRG2142CM34SK83S", "01J2KT0B2SFW465290CCCD4V0G", null, "01J2KT0CTKCB1S1EMHP2C9MQ6N");