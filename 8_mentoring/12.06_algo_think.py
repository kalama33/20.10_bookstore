import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 100, 2000)
y = np.exp(x)

fig, ax = plt.subplots(figsize=(5,3.5))
ax.set_xscale('log')
ax.plot(x,y)
plt.tight_layout()
plt.show()

fig, ax = plt.subplots(figsize=(5,3.5))
ax.set_yscale('log')
ax.plot(x,y)
plt.tight_layout()
plt.show()

#log scaling


fig, ax = plt.subplots(figsize=(5,3.5))
ax.set_xscale('log')
ax.set_yscale('log')
ax.plot(x,y)
plt.tight_layout()
plt.show()