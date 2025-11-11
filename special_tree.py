ls = list(range(1, 8))

while len(ls) > 0:
    print((7-len(ls))*" " + " ".join(list(map(str, ls))))
    del ls[0]

ls.append(7)
i = 1
while len(ls) < 7:
    ls.append(7-i)
    ls.sort()
    i += 1
    print((7-len(ls))*" " + " ".join(list(map(str, ls))))


# 1 2 3 4 5 6 7
#  2 3 4 5 6 7
#   3 4 5 6 7
#    4 5 6 7
#     5 6 7
#      6 7
#       7
#      6 7
#     5 6 7
#    4 5 6 7
#   3 4 5 6 7
#  2 3 4 5 6 7
# 1 2 3 4 5 6 7

