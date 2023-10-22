from random import randint


def sorting(array):
    new_array = [0 for _ in range(len(array))]
    for j in array:
        count_smaller_numb = 0
        for i in array:
            if j > i:
                count_smaller_numb += 1
        new_array[count_smaller_numb] = j
    return new_array


def create_array():
    register_numbs = []
    array = []
    for _ in range(15):
        while True:
            x = randint(0, 100)
            if x in register_numbs:
                pass
            else:
                array.append(x)
                register_numbs.append(x)
                break
    return array


my_array = create_array()
res = sorting(my_array)
print('The array before entering the function: ' + str(my_array))
print('The array after entering the function:  ' + str(res))

