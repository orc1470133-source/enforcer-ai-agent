import unittest
from simulator import simulate
from marketplace import draft_offer, generate_research_report

class OfflineTests(unittest.TestCase):
    def test_flat_prices_preserve_cash(self):
        result = simulate([100.0] * 30)
        self.assertEqual(result["final_equity"], 1000.0)
        self.assertEqual(result["trades"], [])
    def test_invalid_prices(self):
        with self.assertRaises(ValueError):
            simulate([0] * 30)
    def test_no_negative_cash_or_leverage(self):
        result = simulate([100 + (i % 20) * 2 for i in range(100)])
        self.assertGreaterEqual(result["final_equity"], 0)
        self.assertEqual(result["mode"], "offline_simulation")
    def test_marketplace_never_publishes(self):
        self.assertEqual(draft_offer()["publication_status"], "DRAFT_NOT_PUBLISHED")
    def test_research_demo(self):
        self.assertEqual(generate_research_report("BTC", [100, 110], "demo")["change_pct"], 10)
    def test_no_unsupported_symbols(self):
        with self.assertRaises(ValueError):
            generate_research_report("DOGE", [1, 2], "demo")

if __name__ == "__main__":
    unittest.main()
