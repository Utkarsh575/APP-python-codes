"""
Units 0-100 - Rs.0
Units 101-200 - Rs.1.00
Units 201-300 - Rs. 2.00
Units 301 - more - Rs. 3.00

Input:
Previous reading: 5897
Current reading: 6121

Output:
Bill amount: 148
"""

prev_reading = int(input("Enter  the Previous Meter Reading :- "))
curr_reading = int(input("Enter  the Current Meter Reading :- "))

total_reading =curr_reading - prev_reading 
bill_amt=0

for i in range(0,total_reading+1,1):
    if i >=0 and i <=100:
        bill_amt+=0;
    elif i >=101 and i <= 200:
        bill_amt+=1;
    elif i>=201 and i <=300 :
        bill_amt+=2
    elif i>=301 :
        bill_amt+=3

print("Your Bill Amount for ", total_reading , " is :- ₹", bill_amt);

