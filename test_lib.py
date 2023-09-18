import unittest
import pandas as pd
from io import StringIO
from contextlib import redirect_stdout
from lib import perform_data_analysis  # Assuming 'lib.py' contains the function

class TestLib(unittest.TestCase):
    def test_perform_data_analysis_print_output(self):
        # Create a StringIO object to capture printed output
        printed_output = StringIO()

        # Redirect stdout to capture the printed output
        with redirect_stdout(printed_output):
            perform_data_analysis()

        # Get the captured printed output as a string
        printed_output_str = printed_output.getvalue()

        # Define the expected statistical summary as a string
        expected_output = """\
count    1.360000e+02
mean     6.671887e+05
std      8.847868e+05
min      1.794153e+04
25%      1.587478e+05
50%      3.960815e+05
75%      9.327925e+05
max      6.165102e+06
Name: total_at_risk, dtype: float64
"""

        # Assert that the captured printed output matches the expected output
        self.assertEqual(printed_output_str, expected_output)

if __name__ == '__main__':
    unittest.main()

