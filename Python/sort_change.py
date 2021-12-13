count_list = []

for i in range(100):
    count_list.append(i)

count_index = 0
for i in count_list:
    size = len(str(i))
    if size == 1:
        temp = '{:0<2d}'.format(i)
    else:
        temp = '{:0<3d}'.format(i)
    count_list[count_index] = temp
    count_index += 1

count_list.sort()

count_index = 0
for i in count_list:
    size = len(i)
    if size == 2:
        temp = i[:1]
    else:
        temp = i[:2]
    count_list[count_index] = temp
    count_index += 1

num_list = list(map(int, count_list))

print(num_list)