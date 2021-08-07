import matplotlib.pyplot as plt

def collatz(n):
    arr = []
    while(n != 1):
        if(n%2 == 0):
            n = n/2
        else:
            n = (3*n) + 1
        arr.append(n)
    return arr

def curve(arr):
    x_axis = [x for x in range(len(arr))]
    y_axis = [y for y in arr]

    plt.plot(x_axis, y_axis)
    plt.show()

if __name__ == "__main__":
    n = int(input("Enter n: "))
    arr = collatz(n)
    curve(arr)

