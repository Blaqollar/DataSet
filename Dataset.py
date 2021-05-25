#Machine Learning Train and Test
#Measuring the accuracy of your model


#DataSet (100 customers and their shopping habits) Representation x = no of min y = amount of money spent
import numpy
import matplotlib.pyplot as plt
numpy.random.seed(2)

x = numpy.random.normal(3, 1, 100)
y = numpy.random.normal(150, 40, 100) / x

plt.scatter(x, y)
plt.show()

# Split into train/test

train_x = x[:80]
train_y = y[:80]

test_x = x[80:]
test_y = y[80:]

#display same graph with the training set

plt.scatter(train_x, train_y)
plt.show()

#display same graph with the testing as well

plt.scatter(test_x, test_y)
plt.show()

#draw a line through data plot depending what it looks like using plot() of the matplotlib module

import numpy
import matplotlib.pyplot as plt
numpy.random.seed(2)

x = numpy.random.normal(3, 1, 100)
y = numpy.random.normal(150, 40, 100) / x

train_x = x[:80]
train_y = y[:80]

test_x = x[80:]
test_y = y[80:]

mymodel = numpy.poly1d(numpy.polyfit(train_x, train_y, 4))

myline = numpy.linspace(0, 6, 100)

plt.scatter(train_x, train_y)
plt.plot(myline, mymodel(myline))
plt.show()

# Use R-squared in sklearn module to measure relationship btwn x and y axis

import numpy
from sklearn.metrics import r2_score
numpy.random.seed(2)
x = numpy.random.normal(3, 1, 100)
y = numpy.random.normal(150, 40, 100) / x
train_x = x[:80]
train_y = y[:80]
test_x = x[80:]
test_y = y[80:]
mymodel = numpy.poly1d(numpy.polyfit(train_x, train_y, 4))
r2 = r2_score(train_y, mymodel(train_x))
print(r2)


# Now the model has been trained - You'll have  to test as well with R2

import numpy
from sklearn.metrics import r2_score
numpy.random.seed(2)

x = numpy.random.normal(3, 1, 100)
y = numpy.random.normal(150, 40, 100) / x

train_x = x[:80]
train_y = y[:80]

test_x = x[80:]
test_y = y[80:]

mymodel = numpy.poly1d(numpy.polyfit(train_x, train_y, 4))

r2 = r2_score(test_y, mymodel(test_x))

print(r2)

#Now model is ok cause it fits the testing as well - we can now use it to predict future values


