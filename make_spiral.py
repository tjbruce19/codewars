import numpy as np

def spiralize_clever(size):
    # Make a snake
    spiralize = [[1 - min(i,j,size-max(i,j)-1)%2 for j in range(size)] for i in range(size)]
    # for i in range(int(size/2-(size%4==0))):
    #     spiralize[i+1][i] = 1 - spiralize[i+1][i]
    return spiralize


def spiralize(size):
    if size == 2:
        return [[1,1],[0,1]]
    elif size == 1:
        return [[1]]
    elif size == 0:
        return []
    if size%2==0:
        if size%3==0:
            u_array = np.asarray([[1,1],[0,1]])
            for _ in range((size//2)-1):
                shape = u_array.shape
                u_array = np.insert(
                    np.insert(np.insert(np.insert(1 - u_array, shape[0], 1, axis=1), 0, 1, axis=0), shape[0] + 1, 1, axis=0), 0,
                    1, axis=1)
                u_array[1,0] = 0
        else:
            u_array = np.asarray([[1, 1], [1, 1]])
            for _ in range((size // 2) - 1):
                shape = u_array.shape
                u_array = np.insert(
                    np.insert(np.insert(np.insert(1 - u_array, shape[0], 1, axis=1), 0, 1, axis=0), shape[0] + 1, 1,
                              axis=0), 0,
                    1, axis=1)
                u_array[1, 0] = 0
    else:
        u_array = np.asarray([[1]])
        for _ in range((size-1)//2):
            shape = u_array.shape
            u_array = np.insert(
                np.insert(np.insert(np.insert(1 - u_array, shape[0], 1, axis=1), 0, 1, axis=0), shape[0] + 1, 1, axis=0), 0,
                1, axis=1)
            u_array[1,0] = 0
    return u_array.tolist()
# np_d = spiralize(8)
# print(np.asarray(np_d))
# print(spiralize_clever(5))
print(np.asarray(spiralize_clever(10)))