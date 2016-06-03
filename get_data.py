import random,convert

raw_data = []
with open('raw_data.txt') as fp:
    raw_data = [[int(y) for y in x.split('\t')] for x in fp.read().split('\n') if x]


#Split training and test set
point = int( (len(raw_data) * 0.8) // 1)
random.shuffle(raw_data)

training_set = raw_data[:point]
test_set = raw_data[point:]

print len(training_set)
print len(test_set)

training_data = convert.Gen_Matrix(training_set,5)
