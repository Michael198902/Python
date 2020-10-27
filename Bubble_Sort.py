def bubblesort(dataset):
    for i in range(len(dataset)-1,0,-1): #O(n^2) performance due to the nested for loop
        for j in range(i):
            if dataset[i] > dataset[j+1]:
                temp = dataset[j]
                dataset[j] = dataset[j+1]
                dataset[j+1] = temp
    
    
        print("current state: ", dataset) 
        
        #current state:  [20, 8, 19, 6, 23, 56, 41, 49, 87, 53]
        #current state:  [8, 19, 6, 23, 56, 41, 49, 20, 87, 53]
        #current state:  [19, 6, 8, 23, 56, 41, 49, 20, 87, 53]
        #current state:  [6, 8, 23, 19, 41, 56, 49, 20, 87, 53]
        #current state:  [8, 23, 19, 41, 6, 56, 49, 20, 87, 53]
        #current state:  [8, 23, 19, 41, 6, 56, 49, 20, 87, 53]
        #current state:  [23, 19, 8, 41, 6, 56, 49, 20, 87, 53]
        #current state:  [23, 19, 8, 41, 6, 56, 49, 20, 87, 53]
        #current state:  [23, 19, 8, 41, 6, 56, 49, 20, 87, 53]
        #Result:  [23, 19, 8, 41, 6, 56, 49, 20, 87, 53]



def main():
    list1 = [6, 20, 8, 19, 56, 23, 87, 41, 49, 53]
    list2 = [5, 3, 4, 67, 82, 22, 24, 44, 56]
    bubblesort(list1)
    bubblesort(list2)
    print("Result: ", list1)
    print("result for the second list:", list2)


if __name__ == "__main__":
    main()
