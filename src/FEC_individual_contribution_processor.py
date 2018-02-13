
# coding: utf-8

# In[33]:
import datetime
from collections import namedtuple
from decimal import Decimal, ROUND_HALF_UP

from streaming_percentile import StreamingPercentile


# In[35]:

Donor = namedtuple('Donor',['name', 'zip'])
DonationTarget = namedtuple('DonationTarget', ['recipient', 'zip', 'year'])
RecordLine = namedtuple('RecordLine', 
                    ['recipient', 'No2', 'No3', 'No4', 'No5', 'No6', 'No7', 
                     'name', 'No9', 'No10', 'zip', 'No12', 'No13', 'date',
                     'amount', 'other', 'No17', 'No18', 'No19', 'No20', 'No21'])

RECORD_LENGTH = 21
VALID_ZIP_LENGTH = 5

def get_date(string_date):
    try:
        date_of_transaction = datetime.datetime.strptime(string_date, "%m%d%Y")
        return date_of_transaction
    except:
        return None

def convert_str_to_int_or_float(string_amount):
    '''
    Convert string to int or float according to its original value
    reference: https://stackoverflow.com/questions/379906/parse-string-to-float-or-int
    '''
    try:
        return int(string_amount)
    except ValueError:
        return float(string_amount)
# In[37]:

# test = namedtuple('test',['p1','p2'])
# b = [1,2]
# c = test(*b)

# res = get_date('03212018')
# print(res.year)

# res = string_to_date('03212017')
# print(res)


# In[ ]:

class FECIndividualContributionProcessor(object):
    '''
    Process the whole contribution file line by line
    '''
    def __init__(self, percentile):
        self.percentile = percentile
        self.target_percentile = dict() # Hashmap for lookup, key:value -> DonationTarget : cur_percentile
        self.repeat_donors = dict() # Hashmap for lookup, key:value -> Donor : minimum donation year    
    
    def is_repeat_donor(self, donor, cur_year):
        if donor in self.repeat_donors:
            if cur_year > self.repeat_donors[donor]:
                return True
        
        # Update or insert the min year and return false
        self.repeat_donors[donor] = cur_year
        return False
    
    def format_output(self, donation_target, year):
        '''
        recipient|zip|year|percentile|total_amount|total_number_of_donors
        '''

        percentile_val = str(Decimal(self.target_percentile[donation_target].percentile_value).quantize(0, ROUND_HALF_UP))
        total_donation_amount = str(self.target_percentile[donation_target].total_amount)
        total_number_of_donors = str(self.target_percentile[donation_target].total_counts)
        year = str(year)
        return '|'.join([donation_target.recipient, donation_target.zip[:VALID_ZIP_LENGTH], year, percentile_val, total_donation_amount, total_number_of_donors])
        
    def process(self, record):
        if not record:
            return None
        
        record = record.split('|')
        if len(record) != RECORD_LENGTH:
            return None
        
        record = RecordLine(*record)
        
        date_of_transaction = get_date(record.date)
        
        # Check validation
        if record.other or (not date_of_transaction) or len(record.zip) < VALID_ZIP_LENGTH or (not record.name) or (not record.recipient) or (not record.amount):
            return None
        
        # record.zip = record.zip[:VALID_ZIP_LENGTH]
        
        donor = Donor(record.name, record.zip[:VALID_ZIP_LENGTH])
        
        if not self.is_repeat_donor(donor, date_of_transaction.year):
            return None
        
        donation_target = DonationTarget(record.recipient, record.zip[:VALID_ZIP_LENGTH], date_of_transaction.year)
        if donation_target not in self.target_percentile:
            self.target_percentile[donation_target] = StreamingPercentile(self.percentile)
        self.target_percentile[donation_target].push(convert_str_to_int_or_float(record.amount))
        
        return self.format_output(donation_target, date_of_transaction.year)
            

