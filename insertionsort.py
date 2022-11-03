list = [4, 3, 10, 33, 4, 5, 6, 7, 8, 16]


def insertion_sort(list):
    for i in range(1, len(list)):
        current_num = list[i]
        p = i-1
        while p >= 0 and list[p] > current_num:
            list[p+1] = list[p]
            p -= 1

        list[p+1] = current_num
        print(list)
     
    

insertion_sort(list)