import random 


def yates_shuffle(lists):
    for index in range(len(lists)-1):
        #random number b/w and current index
        random_index = random.randint(0, index + 1)
        # swap index with random number at the index like bubble sort
        lists[index], lists[random_index] = lists[random_index], lists[index]

    return lists


l = [1, 3, 4, 5, 9, 22, 23, 30, 44, 45, 47, 50, 52]

if __name__ == '__main__':
    print(yates_shuffle(l))