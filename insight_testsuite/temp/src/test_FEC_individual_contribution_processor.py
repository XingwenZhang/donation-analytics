import unittest
from FEC_individual_contribution_processor import FECIndividualContributionProcessor

class TestFEC(unittest.TestCase):
    def test_init(self):
        processor = FECIndividualContributionProcessor(30)
        self.assertEqual(processor.percentile, 30)
        self.assertTrue(isinstance(processor.target_percentile, dict))
        self.assertTrue(isinstance(processor.repeat_donors, dict))

    
    def test_process(self):
        record1 = '''C00384516|N|M2|P|201702039042410894|15|IND|SABOURIN, JOE|LOOKOUT MOUNTAIN|GA|028956146|UNUM|SVP, CORPORATE COMMUNICATIONS|2016|484||PR2283904845050|1147350||P/R DEDUCTION ($192.00 BI-WEEKLY)|4020820171370029339'''
        record2 = '''C00384516|N|M2|P|201702039042410894|15|IND|SABOURIN, JOE|LOOKOUT MOUNTAIN|GA|028956146|UNUM|SVP, CORPORATE COMMUNICATIONS|01312015|384||PR2283904845050|1147350||P/R DEDUCTION ($192.00 BI-WEEKLY)|4020820171370029339'''
        record3 = '''C00384516|N|M2|P|201702039042410893|15|IND|SABOURIN, JOE|LOOKOUT MOUNTAIN|GA|028956146|UNUM|SVP, CORPORATE COMMUNICATIONS|01312017|230||PR1890575345050|1147350||P/R DEDUCTION ($115.00 BI-WEEKLY)|4020820171370029335'''

        processor = FECIndividualContributionProcessor(30)
        self.assertTrue(not processor.process(record1))
        self.assertTrue(not processor.process(record2))
        self.assertEqual(processor.process(record3), 'C00384516|02895|2017|230|230|1')

if __name__ == '__main__':
    unittest.main()

