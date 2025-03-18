import unittest
from timemasterx.core import TimeMasterX

class TestTimeMasterX(unittest.TestCase):
    def test_now(self):
        tm = TimeMasterX()
        self.assertIsInstance(tm.now(), str)

    def test_add_time(self):
        tm = TimeMasterX("2025-03-18 12:00:00")
        self.assertEqual(tm.add_time(hours=1), "2025-03-18 13:00:00")

if __name__ == "__main__":
    unittest.main()
