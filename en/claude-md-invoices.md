## invoices.py (legacy code)
- Tests: `python3 -m unittest tests.test_invoices` (characterization: they pin the real behavior).
- Contract that does NOT change without warning: total() returns an int for an empty list and no VIP.
- Pending: total() modifies its input list (decide whether that's a bug).
- One change per commit; behavior changes always with the test changed first.
