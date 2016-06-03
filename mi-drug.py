from rbm import *

import get_data,convert

training_data = np.array(get_data.training_data)




#training_data = np.array([[1,1,1,0,0,0],[1,0,1,0,0,0],[1,1,1,0,0,0],[0,0,1,1,1,0], [0,0,1,1,0,0],[0,0,1,1,1,0]])
num_visible = training_data.shape[1]
r = RBM(num_visible = num_visible, num_hidden = 100, learning_rate=0.1)
r.train(training_data,max_epochs=100)
print 'r.weights'
print r.weights
scores = []
for mirna in training_data:
    query = np.array([mirna])
    p_hidden = r.run_visible(query,1)
    p_visible = r.run_hidden(p_hidden,1)
    for i in range(len(mirna)):
        if mirna[i]==1:
            p_visible[0][i]=0
    scores.append(p_visible[0])

results = convert.Rev_Matrix(scores,5)
print len(results)
fpw=open('result.txt','wb')
for line in results:
    fpw.write('\t'.join([str(x) for x in line]))
    fpw.write('\n')
fpw.close()
