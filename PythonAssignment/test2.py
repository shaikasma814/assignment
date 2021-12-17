x = 987
y = 87654
z = 9876543
def Largest_Number(x, y, z):
    if (x >= y) and (x >= z):
        largest = x

    elif (y >= z) and (y >= x):
        largest = y

    else:
        largest = z
    return largest

print(Largest_Number(x, y, z))