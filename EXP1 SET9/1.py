"""
1. Friend of three are going for the weight loss challenge. The winner will get exciting prizes from
other two.
input:
Challenge day:
friend1-63
friend2-47
friend3-39
one month later:
friend1-59
friend2-44
friend3-42

output:
Winner is: friend1

"""
friend1 = int (input("friend1 :- "))
friend2 = int (input("friend2 :- "))
friend3 = int (input("friend3 :-" ))

if min(friend3,friend1,friend2) == friend1:
    print("Friend 1 wins")
elif min(friend3,friend1,friend2) == friend2:
    print("Friend 2 wins")
elif min(friend3,friend1,friend2) == friend3:
    print("Friend 3 wins")


