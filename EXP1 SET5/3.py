"""
Management of a car company, planning to give incentives for their employee based on the year of
experience. If the employee Service is 3 years then he will get Rs. 30,000 as incentives, if the
employee Service is 2 years then he will get Rs. 20,000 as incentives and if the employee Service is 1
years then he will get Rs. 10,000 as incentives.
The employee id consist of 5 digits, first two digit indicates the joining year and next three digit
indicates roll number.

Input:
Employee id: 20407
Output:
incentives: Rs. 10,000
"""

emp_id = str(input("Enter the Employee id:- "))

yrs = int(emp_id[0]+emp_id[1])
this_year = 21
worked_yrs = this_year-yrs
# print(worked_yrs)
print("Incentive :- ₹", worked_yrs*10000)