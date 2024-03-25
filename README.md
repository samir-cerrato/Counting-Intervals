# Counting-Intervals
Getting familiar with Divide-and-Conquer algorithms pt.2 

2 Task 2: Counting intervals

2.1 Problem description

In this task, your input includes a list of n intervals [x, y) where x is the starting point and y is the
ending point. Given a list of n query points, for each query q, you need to report the number of intervals
containing q. In other words, you will return the number of intervals [x, y) such that x ≤q < y. To
simplify the task, there are no duplicates of starting and ending points among all n intervals. The
values x, y, q are floats with maximum 4 decimal places.
Your input will start with the value of n, continuing with n intervals, and n queries. For each interval,
float coordinates x and y are separated by one space.
For each query q, you should output an integer (from 0 to n) that counts the number of intervals
containing q. Given an array counter for n queries, a Python script to output should be:

for x in counter:

print(x)

Sample Input 1:

4

1 3

2 5

7 8

9 10

2

4

8

9

Sample Output 1:

2

1

0

1

Note that Sample Input 1 is an example for getting the output. Your test cases are like the Sample
Input 2.

Sample Input 2:

4

1.2345 2.3456

1.1234 2.2345

2.4567 3.1234

1.0001 3.2345

2.1234

3.1234

4.1234

1.1231

Sample Output 2:

3

1

0

1
