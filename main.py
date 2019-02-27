from module import *

matrix = np.array(get_points())
check_points(matrix)
line = calc_line(matrix)
Y = np.array(get_y(matrix))
A = get_A(matrix)
AT = A.transpose()
a = np.dot(AT, A)
b = np.dot(AT, Y)
X = np.linalg.solve(a, b)
print("\n")
print_line(line)
print("\n")
print_cuadratic(X)

