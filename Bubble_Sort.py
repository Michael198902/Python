def bubblesort(dataset):
    for i in range(len(dataset)-1,0,-1): #O(n^2) performance due to the nested for loop
        for j in range(i):
            if dataset[i] > dataset[j+1]:
                temp = dataset[j]
                dataset[j] = dataset[j+1]
                dataset[j+1] = temp
    
    
        print("current state: ", dataset)



def main():
    list1 = [6, 20, 8, 19, 56, 23, 87, 41, 49, 53]
    bubblesort(list1)
    print("Result: ", list1)


if __name__ == "__main__":
    main()