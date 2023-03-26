import numpy as np

grid = np.zeros((4, 4))
head = [1, 1]

print(grid)
print(head)

grid[*head] = 2

print(grid)

head += np.array([1, 0])

print(head)
print(type(head))


grid[*head] = 2

print(grid)
