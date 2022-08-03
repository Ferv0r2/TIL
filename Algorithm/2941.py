data = input()

criteria = ["c=", "c-", "dz=", "d-", "d-", "lj", "nj", "s=", "z="]

for i in criteria:
    data = data.replace(i, " ")

print(len(data))