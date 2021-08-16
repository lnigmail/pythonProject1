

def sum_identicle(x, y, z):
    sum = x + y + z

    if x == y == z:
        sum = sum * 3
    return sum


print(sum_identicle(1, 2, 3))
print(sum_identicle(3, 3, 3))
