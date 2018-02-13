import unittest
from streaming_percentile import StreamingPercentile 

class TestStreamingPercentile(unittest.TestCase):
    def test_push(self):
        sp = StreamingPercentile(50)
        sp.push(1)
        sp.push(2)
        self.assertEqual(sp.percentile_value, 1)
        self.assertEqual(sp.total_amount, 3)
        self.assertEqual(sp.total_counts, 2)

if __name__ == '__main__':
    unittest.main()