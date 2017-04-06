from math import sqrt, pi, exp
import numpy as np
import matplotlib.pyplot as plt

m = 2.0e3    # kg
C = 20.0e3  # N.s/m
v0 = 10.0    # m/s

x = []
t = []

for k in np.arange(55000, 100001, 5000):
	C_c = 2 * sqrt(m*k)
	w_n = sqrt(k/m)
	zeta = C / C_c
	w_d = w_n * sqrt(1 - zeta**2)

	t_max = pi / (2.0 * w_d)
	x_max = v0 / w_d * exp(-zeta * w_n * t_max)

	t.append(t_max)
	x.append(x_max)

	print 'k: ', k
	print 'w_n: ', w_n
	print 'C_c: ', C_c
	print 'zeta: ', zeta
	print 'w_d: ', w_d
	print 't_max: ', t_max
	print 'x_max: ', x_max
	print

k = [i for i in np.arange(55000, 100001, 5000)]

plt.plot(k, x)
plt.plot(k, t)
plt.xlim(min(k), max(k))
plt.yticks(np.arange(0.0, 1.0, 0.1))
plt.grid(True)
plt.legend(['x', 't'], loc='lower right')
plt.xlabel('Spring Stiffness, K (N/m)')
plt.title('Maximum Displacment (meters) and Corresponding Time (sec)')
plt.show()



