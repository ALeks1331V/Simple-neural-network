import numpy as np
import matplotlib.pyplot as plt


def activate_func(x) :
 return np.heaviside(x, 0)


def forward(X):
 w1 = np.array([[2, -1, -1], [0.5, -1, 0.5]])
 w2 = np.array([-1, 1])
 y1 = np.dot(w1, X)
 z1 = activate_func(y1)
 y2 = np.dot(w2, z1)
 out = activate_func(y2)
 return out


N = 300
x1 = np.random.random(N)
x2 = np.random.random(N)
x3 = [1]*N
x_in = np.array([x1, x2, x3]) 
result = forward(x_in)
print(result) 


for i in range(N):
 if result[i] == 1:
  plt.scatter(x1[i], x2[i], c="green")
 else:
  plt.scatter(x1[i], x2[i], c="red")
x1 = [0.5, 1]
y1 = [0, 1]

x2 = [0, 1]
y2 = [0.5, 1]

# Построение графика
plt.plot(x1, y1, label="Линия от (0.2, 0) до (1, 1)")
plt.plot(x2, y2, label="Линия от (0.2, 0) до (1, 1)")

plt.show()