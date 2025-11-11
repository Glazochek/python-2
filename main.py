n = int(input())


def tree_1():
    for i in range(1, n + 1):
        print(i * "*")


print("\n")


def tree_2():
    for i in range(1, n + 1):
        print(" ".join(i * ["*"]))


print("\n")


def tree_3():
    for i in range(n, 0, -1):
        print(" ".join(i * ["*"]))


print("\n")


def tree_4():
    for i in range(1, n + 1):
        print(" " * ((n - i) * 2) + " ".join(i * ["*"]))


print("\n")


def tree_5():
    for i in range(1, n + 1):
        print(" " * (n - i) + " ".join(i * ["*"]))


print("\n")


def tree_6():
    for i in range(1, n + 1):
        if i == n:
            print(" " * (n - i) + " ".join(i * ["*"]))
        else:
            print(" " * (n - i) + " ".join(["*" if (o == 1 or o == i) else " " for o in range(1, i + 1)]))


print("\n")
