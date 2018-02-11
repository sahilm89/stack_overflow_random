from sklearn import linear_model
import csv
import numpy as np
import matplotlib.pyplot as plt

def process_chunk(chuk):

    training_set_feature_list = []
    training_set_label_list = []
    test_set_feature_list = []
    test_set_label_list = []
    count = 1
    # to divide into training & test
    chuk = map(lambda x: x[2:], chuk)
    chunk = np.array(chuk,dtype = np.float)
    ########## Testing dataset ########################################
    test_set_feature_list = chunk[30:,3:5]
    test_set_label_list = chunk[30:,2]

    ########## Training dataset ########################################
    training_set_feature_list = chunk[:30,3:5]
    training_set_label_list = chunk[:30, 2]

    # Create linear regression object
    regr = linear_model.LinearRegression()
    # Train the model using the training sets
    regr.fit(training_set_feature_list, training_set_label_list)

    predictedTestSet = regr.predict(test_set_feature_list)

     # The coefficients
    print 'Coefficients: {}'.format(regr.coef_)
    # The mean square error
    print 'Residual sum of squares: %.2f' % np.mean(predictedTestSet - test_set_label_list) ** 2
    # Explained variance score: 1 is perfect prediction
    print 'Variance score: %.2f' % regr.score( test_set_feature_list, test_set_label_list)
    X = [x for (y,x) in sorted(zip(test_set_label_list, predictedTestSet))]
    Y = [y for (y,x) in sorted(zip(test_set_label_list, predictedTestSet))]
    plt.plot(range(len(X)),X , 'r.', label='predicted')    
    plt.plot(range(len(Y)),Y , 'g-',label='test_set')    
    plt.legend()
    plt.show()
    return predictedTestSet


# Load and parse the data
file_read = open('file1.csv', 'r')

reader = csv.reader(file_read)

chunk, chunksize = [], 12

for i, line in enumerate(reader):
    if ( i > 0):
        chunk.append(line)

predictedSet = process_chunk(chunk)
print predictedSet
