import sys, os

def Gen_Matrix(input, output, typ):

    table = []
    col = int(typ)*174
    
    for i in range(322):
        table.append(['0',]* col)
    
    data = open(input, 'r')
    for line in data.readlines():
        line = line.strip('\n')
        
        a = line.split('\t')
        
        rna, diseases, types = a
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
        
    f = open(output, 'wb')
    
    for item in table:
    
        newrow = '\t'.join(item)
        
        f.write(newrow+'\n')
    
    f.close
    
def Rev_Matrix(input, output, typ):

    reversed_table = []
    typ = int(typ)
    table = []
    f_in = open(input, 'r')
    for line in f_in.readlines():
        line = line.strip('\n')
        m = line.split('\t')
        table.append(m)
    
    for item in table:
        for i in range(len(item)):
            
            if (i+1) % 5 == 0:
                pass  
            else:
                if item[i] == '1':
                    b = [str(table.index(item)+1), str(((i+1) // 5)+1), str((i+1) % 5),]
                    
                    reversed_table.append(b)
                else:
                    pass  
    
        
    f_out = open(output, 'wb')
    
    for item in reversed_table:
        
        newrow = '\t'.join(item)
        f_out.write(newrow+'\n')
        
    f_out.close

Gen_Matrix('C:\\Users\\KingSky\\Desktop\\raw_data.txt', 'C:\\Users\\KingSky\\Desktop\\newdata.txt', 5)
Rev_Matrix('C:\\Users\\KingSky\\Desktop\\newdata.txt', 'C:\\Users\\KingSky\\Desktop\\output.txt', 5)