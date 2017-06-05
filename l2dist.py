import numpy as np


def ecld2loops(test, train):
    number_test = test.shape[0]
    number_train = train.shape[0]
    dists = np.zeros((number_test, number_train))

    for i in xrange(number_test):
      for j in xrange(number_train):
           dists[i,j] =  np.sqrt( np.sum((test[i,:]- train[j,:])**2) )

    return dists


def ecld1loops(test, train):
    number_test = test.shape[0]
    number_train = train.shape[0]
    dists = np.zeros((number_test, number_train))

    for i in xrange(number_test):
            #dists[i,:] = np.sum( ( train - X[i,:]) ** 2, axis = 1)
            #axis = 1 : colums wise
            dists[i,:] = np.sqrt( np.sum( ( train - test[i,:]) ** 2, axis = 1  ) )
    return dists


def ecld0loops(test, train):
    number_test = test.shape[0]
    number_train = train.shape[0]
    dists = np.zeros((number_test, number_train))

    xydiff = test[:, :, None] - train[:, :, None].T

    dists = np.sqrt( (xydiff**2).sum(1) )

    return dists





train = np.array([[1,2,3],
                 [3,2,1],
                 [5,6,7],
                 [1,2,3],
                 [1,1,1]])


test = np.array([[0,0,0],
                 [2,2,2]])



dist = np.zeros((len(test),len(train)))
print("euclidean distance three ways")


print("test")
print(test)

print("train")
print(train)

print("2 loops")
print(ecld2loops(test, train))

print("1 loop")
print(ecld1loops(test, train))

print("none loops")
print(ecld0loops(test, train))
