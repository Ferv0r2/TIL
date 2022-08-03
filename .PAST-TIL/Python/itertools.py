import itertools, numpy as np

num_list = np.full((2, 3), 2)
print("num_list : ",num_list)

new_list = list(itertools.chain.from_iterable(num_list))
print("new_list_1 : ", new_list)

new_list = list(itertools.chain(*num_list))
print("new_list_2 : ",new_list)