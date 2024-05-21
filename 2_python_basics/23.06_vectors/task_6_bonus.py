import numpy as np
import matplotlib.pyplot as plt

"""In this example, the RotationalMatrix2D class takes an angle phi as input. 
The construct_matrix method constructs the 2D rotational matrix based 
on the given angle. The apply_rotation method applies the rotation matrix 
to a 2D vector by performing a dot product between the matrix and the vector. 
The visualize_rotation method uses matplotlib to visualize the original vector 
and the rotated vector using quiver plots.

By creating an instance of the RotationalMatrix2D class with a given phi, 
you can apply the rotation to a 2D vector using the apply_rotation method 
and obtain the rotated vector. Additionally, you can use the visualize_rotation 
method to visualize the original and rotated vectors using matplotlib."""

class RotationalMatrix2D:
    def __init__(self, phi):
        self.phi = phi

    def construct_matrix(self):
        theta = np.radians(self.phi)
        cos_phi = np.cos(theta)
        sin_phi = np.sin(theta)
        return np.array([[cos_phi, -sin_phi], [sin_phi, cos_phi]])

    def apply_rotation(self, vector):
        matrix = self.construct_matrix()
        return np.dot(matrix, vector)

    def visualize_rotation(self, vector):
        rotated_vector = self.apply_rotation(vector)
        origin = np.array([0, 0])
        plt.quiver(*origin, *vector, angles='xy', scale_units='xy', scale=1, color='blue', label='Original Vector')
        plt.quiver(*origin, *rotated_vector, angles='xy', scale_units='xy', scale=1, color='red', label='Rotated Vector')
        plt.xlim(-5, 5)
        plt.ylim(-5, 5)
        plt.xlabel('X')
        plt.ylabel('Y')
        plt.legend()
        plt.grid(True)
        plt.show()

# Example usage
phi = 45  # Angle in degrees
vector = np.array([1, 2])

rotational_matrix = RotationalMatrix2D(phi)
rotated_vector = rotational_matrix.apply_rotation(vector)
print("Rotated Vector:", rotated_vector)

rotational_matrix.visualize_rotation(vector)
