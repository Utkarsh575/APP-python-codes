initial_tuple = [('b', 100), ('c', 200), ('c', 45),
             ('d', 876), ('e', 75)]
 
print("initial_list", str(initial_tuple))

result = [i for i in initial_tuple if i[1] <= 100]

print("Resultant tuple list: ", str(result))