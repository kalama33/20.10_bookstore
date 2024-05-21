import matplotlib.pyplot as plt
import math

# Valores de X
x = [1, 2, 3, 4]

# Calcular los valores de Y para cada función
y_log = [math.log(val) for val in x]
y_linear = x
y_xlogx = [val * math.log(val) for val in x]
y_square = [val**2 for val in x]
y_exp = [math.exp(val) for val in x]
y_factorial = [math.factorial(val) for val in x]

# Almacenar todos los valores de Y en una lista
y_values = [y_log, y_linear, y_xlogx, y_square, y_exp, y_factorial]

# Etiquetas de las funciones
function_labels = ['log(x)', 'x', 'x * log(x)', 'x^2', 'e^x', 'x!']

# Configurar el gráfico
plt.figure()

# Generar el gráfico para cada función
for y, label in zip(y_values, function_labels):
    plt.plot(x, y, label=label)

# Etiquetas de los ejes y título del gráfico
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Gráfico de funciones')

# Mostrar la leyenda
plt.legend()

# Mostrar el gráfico
plt.show()