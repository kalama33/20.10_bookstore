import timeit  # Importa el módulo timeit para medir el tiempo de ejecución
import matplotlib.pyplot as plt

def time_it(N):
    setup_queue = f"from collections import deque; dq=deque(range({N}, 0, -1))"  # Configura un deque con elementos en orden inverso
    fifo_queue = "dq.appendleft(None); dq.pop()"  # Operación de eliminar un elemento del extremo izquierdo del deque (FIFO)

    queue_time = timeit.repeat(setup=setup_queue, stmt=fifo_queue, repeat=10, number=1000)  # Mide el tiempo de ejecución de la operación de la cola

    queue_mean = sum(queue_time) / len(queue_time)  # Calcula el tiempo promedio

    setup_list = f"num = list(range({N}, 0, -1))"  # Crea una lista con elementos en orden inverso
    fifo_list = "num.append(None); num.pop(0)"  # Operación de eliminar un elemento del frente de la lista (FIFO)

    list_time = timeit.repeat(setup=setup_list, stmt=fifo_list, repeat=3, number=1000)  # Mide el tiempo de ejecución de la operación de la lista

    list_mean = sum(list_time) / len(list_time)  # Calcula el tiempo promedio

    return queue_mean, list_mean  # Devuelve los tiempos promedio de la cola y la lista


X = [10, 100, 1000, 10000, 100000]  # Tamaños de entrada
Y_queue = [time_it(num)[0] for num in X]  # Calcula los tiempos promedio de la cola para cada tamaño de entrada
Y_list = [time_it(num)[1] for num in X]  # Calcula los tiempos promedio de la lista para cada tamaño de entrada

print(Y_queue)  # Imprime los tiempos promedio de la cola
print()
print(Y_list)  # Imprime los tiempos promedio de la lista

# Comparison Plot
plt.plot(X, Y_queue, label='Queue')
plt.plot(X, Y_list, label='List')
plt.xlabel('Input Size')
plt.ylabel('Average Time (seconds)')
plt.title('Comparison of Execution Time: Queue vs List')
plt.legend()
plt.show()
