"""
5. Examination was conducted for 100 students. There are totally 2 set of question papers (50 QP in
each set). The time the proctor distributed the question papers, it is the usual routine that some
students will choose the QP that covers their known question and the students indulge in exchanging
the question paper mutually. To avoid this situation, proctor sets the simple rule like, all the even
register number students will take set A QP and all the ODD register number students will take set B
QP (Assuming Reg No ranges from RA2011003010001 - RA2011003010100)

input: RA2011003010009
output: set B
"""

reg_no=str(input("Enter the registration no:- "))

if(int(reg_no[-1])%2==0):
    print("SET A")
else:
    print("SET B")
