import unittest
import subprocess
import sys
from tools.paired_summary import summarize

class SummaryTests(unittest.TestCase):
    def test_fixed_broken_and_direction(self):
        rows = [{'baseline_error':'1','candidate_error':'0'}, {'baseline_error':'1','candidate_error':'0'}, {'baseline_error':'0','candidate_error':'1'}]
        n, fixed, broken, mean = summarize(rows)
        self.assertEqual((n, fixed, broken), (3, 2, 1))
        self.assertAlmostEqual(mean, 1/3)

    def test_invalid_and_empty(self):
        for rows in ([], [{'baseline_error':'2','candidate_error':'0'}], [{}, {}]):
            with self.assertRaises(ValueError):
                summarize(rows)

    def test_cli_is_descriptive_only(self):
        result = subprocess.run([sys.executable, 'tools/paired_summary.py', 'examples/pairs.csv'], capture_output=True, text=True, check=True)
        self.assertNotIn('interval', result.stdout.lower())
        self.assertIn('descriptive', result.stdout.lower())

    def test_identical(self):
        self.assertEqual(summarize([{'baseline_error':'0','candidate_error':'0'}]*2), (2,0,0,0))

if __name__ == '__main__':
    unittest.main()
