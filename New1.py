import sys, os

def Gen_Matrix(input, typ):

    table = []
    col = int(typ)*174
    
    for i in range(322):
        table.append(['0',]* col)
    
    
    for item in input:
        
        rna, diseases, types = item 
        x= int(rna)-1
        y=((int(diseases)-1)*typ+int(types))-1
        table[int(rna)-1][((int(diseases)-1)*typ+int(types))-1] = '1'
    
            
    for i in table:
        j = 5 
        while j <= col:
            sums = ( int(i[j-2]) + int(i[j-3]) + int(i[j-4]) 
                + int(i[j-5]) )
            if sums > 0:
                i[j-1] = '1'
            else:
                i[j-1] = '0'
            j += 5
    
    def ite1(table):
        for sublist in table:
            for element in sublist:
                yield element 
                
    for num in ite(table):
        num = int(num)
        
    return table 
    
def Rev_Matrix(input, typ):

    reversed_table = []
    typ = int(typ)
    table = input    
    
    for item in table:
        for i in range(len(item)):
            
            if (i+1) % 5 == 0:
                pass  
            else:
                if item[i] == '1':
                    b = [str(table.index(item)+1), str(((i+1) // 5)+1), 
                        str((i+1) % 5),]
                    
                    reversed_table.append(b)
                else:
                    pass  
    
    
    def ite2(reversed_table):
        for sublist in reversed_table:
            for element in sublist:
                yield element 
                
    for num in ite2(reversed_table):
        num = int(num)
    
    return reversed_table

