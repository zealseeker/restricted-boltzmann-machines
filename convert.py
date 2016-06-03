import sys, os

def Gen_Matrix(input, typ):

    table = []
    col = int(typ)*174

    for i in range(322):
        table.append([0,]* col)


    for item in input:

        rna, diseases, types = item
        x= int(rna)-1
        y=((int(diseases)-1)*typ+int(types))-1
        table[int(rna)-1][((int(diseases)-1)*typ+int(types))-1] = 1


    for i in table:
        j = 5
        while j <= col:
            sums = ( int(i[j-2]) + int(i[j-3]) + int(i[j-4])
                + int(i[j-5]) )
            if sums > 0:
                i[j-1] = 1
            else:
                i[j-1] = 0
            j += 5

    return table

def Rev_Matrix(input, typ):

    reversed_table = []
    typ = int(typ)
    table = input

    for j,item in enumerate(table):
        for i in range(len(item)):

            if (i+1) % 5 == 0:
                pass
            else:
                if item[i] != 0:
                    b = [j+1, ((i+1) // 5)+1, (i+1) % 5,item[i]]
                    reversed_table.append(b)
                else:
                    pass

    return reversed_table
