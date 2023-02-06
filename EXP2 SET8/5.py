def secMostRepeated(seq):

    occ = {}
    for i in range(len(seq)):
        occ[seq[i]] = occ.get(seq[i], 0) + 1

    first_max = -10**8
    sec_max = -10**8

    for it in occ:
        if (occ[it] > first_max):
            sec_max = first_max
            first_max = occ[it]

        elif (occ[it] > sec_max and
              occ[it] != first_max):
            sec_max = occ[it]

    for it in occ:
        if (occ[it] == sec_max):
            return it


seq = [ "bbb", "aaa", "bbb",
            "ddd", "aaa", "aaa" ]
print(secMostRepeated(seq))