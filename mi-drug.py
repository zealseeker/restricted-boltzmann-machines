from rbm import *

training_data = np.array([[1,1,1,0,0,0],[1,0,1,0,0,0],[1,1,1,0,0,0],[0,0,1,1,1,0], [0,0,1,1,0,0],[0,0,1,1,1,0]])
num_visible = training_data.shape[1]
r = RBM(num_visible = num_visible, num_hidden = 2, learning_rate=0.1)
r.train(training_data,max_epochs=1000)
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
    scores.append(p_visible)
