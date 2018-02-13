### Running Environment

Python3



### Command

in the **root** directory to run the **project**:

```bash
bash run.sh
```

in the **root** directory to run the **unit test**:

```bash
cd src
bash run_unittest.sh
```



### Assumption

I discard the record line which contain negative donation amount.

For example, in 2015-2016 individual donation dataset, the file itcont_2016_10151005_20150726.txt's 1906th line contains:

```python
C00195065|N|Q1|P|15970348749|15|IND|MITCHELL, KEVIN|DALLAS|TX|75251|SHOWBIZ CINEMAS|CHIEF EXECUTIVE OFFICER|03062015|-2300||0093019|1003390|||4042020151242038316
```

Where the amount is **-2300**, a negative value. I think the donation should be a positive value, so I discard the record line which contains negative amount value.



### Method

##### Streaming Percentile

I use two **heaps** to compute the streaming percentile, one **max heap** and one **min heap**. 

If the percentile's value is **val**, and it is **k**th number in the sorted sequence. Then the max heap store all number smaller than **val**, and then adjust the max heap to keep its size exactly **k**.  Min heap store the rest numbers. 

Finally, update the percentile value. 



##### Repeat Donors and Specific Donation Target

Specific donor is the combination of name and zip code. Donation target is the combination of recipient, zip code and year.

I use **namedtuple** to store them, then insert into **dict** to make use of hast table to speed up.



##### Record Processing

In order to **avoid** the **hard code** of location, e.g recipient is line[0], I use **namedtuple** to access the property.

For example: 

```python
RecordLine = namedtuple('RecordLine', ['recipient', 'No2', 'No3', 'No4', 'No5','No6', 'No7', 'name', 'No9', 'No10', 'zip', 'No12', 'No13', 'date', 'amount', 'other', 'No17', 'No18', 'No19', 'No20', 'No21'])

recipient_id = RecordLine(record).recipient
```



##### Round up

Use **Decimal** and **ROUND_HALF_UP** to achieve 0.5 or more round to 1.



### Reference

1. https://cs.stackexchange.com/questions/57542/find-pth-percentile-of-a-stream-of-numbers
2. https://www.geeksforgeeks.org/median-of-stream-of-running-integers-using-stl/
3. https://stackoverflow.com/questions/2501457/what-do-i-use-for-a-max-heap-implementation-in-python

