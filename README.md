# MNK-group-test-assignment

Pandas scripts with merging files, analysing and SQL query.

1. **folder task_1.** Three files named "data.csv, prices.csv, quantity.csv". First file contains list of details of the
   supplier, second - prices, third - quantity in stock.

"data_merge.py" has a pandas library script that process these 3 files by combining them so that in the "result.csv"
file are only lines
with availability and price greater than zero. Positions from the price list is considered correct if all columns have
data.
The result file is in the format (part_number, manufacturer, price, quantity).

"report.py" has a method that provide a report on the number of brands and positions under them in the
format BRAND1 - 5000 rows, etc.

2. **folder task_2.** The file "sample_supplier.csv", contains the another price list.

"sql_query.py" compare the sample file with result file from the task_1 using the written SQL query from "query.txt"
file. The items are considered the same if they have the same part_number and manufacturer.

The comparison are written to the "comparison.csv" which has better prices for the overlapping items. It was also 
reformatted to open in Excel.

3. Repository contains two folders task_1 and task_2:

- The first folder contains all the code for the first task
- The second folder contains TXT files with SQL queries from the second file

NOTICES
!!! to the quantity.csv file was manually added a header 'part_number quantity' !!!