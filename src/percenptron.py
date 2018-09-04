#感知机学习
import random
import numpy as np
import matplotlib.pyplot as plt
class Data:
    def __init__(self, x, y):
        self.x = x
        self.y = y
class Perceptron:
    def __init__(self, w0, b0, data, eta):
        self.w0, self.b0, self.data, self.eta = w0, b0, data, eta
        self.w = w0
        self.b = b0
        self.data_size = len(x)
    def func_filter(self, vals):
        sum_ = np.sum(np.multiply(vals.x, self.w))
        if vals.y * (sum_ + self.b) <= 0:
            return True
        else:
            return False
    def train(self):
        error_data = list(filter(self.func_filter, self.data))
        while len(error_data) > 0:
            index = 0#random.randrange(0, len(error_data))
            sum_ = np.sum(np.multiply(error_data[index].x, self.w))
            if error_data[index].y * (sum_ + self.b) <= 0:
                self.w = self.w + self.eta * error_data[index].y * error_data[index].x
                self.b = self.b + self.eta * error_data[index].y
            error_data = list(filter(self.func_filter, self.data))
        return self.w, self.b
        
        
x = np.array([[3, 3], [4, 3], [1, 1], [2, 2], [2, 3]])
y = np.array([1, 1, -1, -1, -1])
data = []
x_samples = [i[0] for i in x]
y_samples = [i[1] for i in x]
for i in range(len(x)):
    d = Data(x[i], y[i])
    data.append(d)
w0, b0, eta = np.array([1, 1]), 0, 1
perceptron = Perceptron(w0, b0, data, eta)
w, b = perceptron.train()

for i in range(len(x_samples)):
    color_ = 'green' if y[i] > 0 else 'red'
    plt.scatter(x_samples[i], y_samples[i], color=color_)

#w为法向量
k = -w[0]/w[1]
x_line = np.arange(0, 6, 1)
y_line = np.multiply(k, x_line)-b

plt.plot(x_line, y_line)

plt.show()
