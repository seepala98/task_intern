# task_intern

Shell script task


Statement:
You have to write a script (bash/python/ruby) which will take an input file (PFA sample) and a input date formatted in yyyyMMdd format, e.g.:
$ bash task.sh 20180601 1530947027582.csv

This should output a file named <input_file_name>_out.csv, e.g. 1530947027582_out.csv

The description of output file and input contents is given below:
Input: 
This file contains multiple lines of sections and data. The line containing section won't have any comma (,) in the line. You can find all sections by:
$ grep -v , 1530947027582.csv


In our sample input, there are 4 sections: bids, impression, wins, click. These will be different in the actual test data. Lets call number of sections n.

The file begins with a starting section. Each section is immediately followed by multiple lines of data for that section. A section ends when another section line is encountered. 
e.g. In our sample input, the stating section is "bids" (line no 1). The next section is "impression" (line 1759). All lines from Line 2 - 1758 contains data for bids section. 

The data itself is a two-column csv. 
1st column is unix epoch timestamp in milliseconds. => let's call this column timestamp
2nd column is a number (integer/float etc. => you have to account for these two number formats here) => let's call this value
e.g. 1526986800000,101119 => timestamp = 1526986800000, value = 101119

The value column might be empty for some rows. Please handle this condition.

Output:
The output csv should look like a pivot table. 
Output csv file should have 25 rows, 1st row is for header, and next 24 rows are for each hour of the input date.
It should have n + 1 columns. (number of sections + 1)
1st column should contain the hour-level timestamp (as mentioned in line above) in unix epoch timestamp in milliseconds format.
Next n columns should have sum of values for that hour as they appear in the original csv. 
So, if a data point is for 1:25 pm in input file, the value of that data point should be added to 2:00 pm row of output csv.

a sample output row might look like:
hour	bids	impression	wins	click
1527795000000	2846825	61441	142436	1881
1527798600000	4381325	86220	195040	3092
...
...

and so on.
