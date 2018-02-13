#!/usr/bin/env python3
# coding: utf-8

# In[2]:


import argparse
from FEC_individual_contribution_processor import FECIndividualContributionProcessor


# In[ ]:

# PERCENTILE_FILE_PATH = '../input/percentile.txt'
# ITCONT_FILE_PATH = '../input/itcont.txt'
# OUTPUT_FILE_PATH = '../output/repeat_donors.txt'

# In[ ]:

def main():
    parser = argparse.ArgumentParser(description='parse input files and output file')
    parser.add_argument('individual_contribution', help='Input Contribution File')
    parser.add_argument('required_percentile', help='Input Percentile File')
    parser.add_argument('output_donor', help='Output Result File')
    args = parser.parse_args()

    with open(args.required_percentile, 'r') as f_percentile:
        percentile = int(f_percentile.read().strip())

    if not percentile:
        print('no content')
    

    processor = FECIndividualContributionProcessor(percentile)

    with open (args.individual_contribution,'r') as f_cont, open(args.output_donor, 'w') as f_donor:
        for line in f_cont:
            record = processor.process(line.strip())
            if record:
                f_donor.write(record + '\n')
                
if __name__ == '__main__':
    main()

