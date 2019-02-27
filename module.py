import numpy as np

def get_points():
    rows = int(input("Ingrese la cantidad de puntos que va a ingresar\n"))
    if rows < 2:
        print("Debes ingresar al menos dos puntos")
        exit(1)
    columns = 2
    points = [[0 for x in range(columns)] for y in range(rows)]
    for i in range(0, rows):
        print("Punto %d" % (i + 1))
        points[i][0] = float(input("Ingrese coordenada x\n"))
        points[i][1] = float(input("Ingrese coordenada y\n"))
    return points

def get_y(matrix):
    y = []
    for i in range(len(matrix)):
        y.append(matrix[i][1])
    return y

def get_A(matrix):
    rows = len(matrix)
    columns = 3
    A = np.array([[0 for x in range(columns)] for y in range(rows)])

    for i in range(rows):
        A[i][0] = matrix[i][0] ** 2
        A[i][1] = matrix[i][0]
        A[i][2] = 1
    return A

def calc_line(points):
    line = []
    n = len(points)
    sum_xy = sum_x2 = sum_x = sum_y = 0
    for i in range(n):
        sum_x += points[i][0]
        sum_y += points[i][1]
        sum_x2 += points[i][0] ** 2
        sum_xy += points[i][0] * points[i][1]

    m = (n * sum_xy - sum_x * sum_y) / (n * sum_x2 - (abs(sum_x)**2))
    c = (sum_y * sum_x2 - sum_x * sum_xy) / (n * sum_x2 - (abs(sum_x)**2))
    line.append(m)
    line.append(c)
    return line

def print_line(line):
    print("Solución lineal:\ny = %fx%s%f" % (line[0], "+" if line[1] >= 0 else "", line[1]))

def print_cuadratic(X):
    print("Solución cuadrática:\ny = %fx**2%s%fx%s%f" % (X[0], "+" if X[1] >= 0 else "", X[1],
                                                         "+" if X[2] >= 0 else "", X[2]))
def check_points(matrix):
    different = False
    for i in range(len(matrix)):
        for j in range(i + 1, len(matrix)):
            if matrix[i][0] != matrix[j][0]:
                if matrix[i][1] != matrix[j][1]:
                    different = True

    if not different:
        print("Error, debes ingresar puntos distintos!")
        exit(1)



