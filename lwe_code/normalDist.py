import math,random

## calculating the discrete normal distribution with the help of continuous uniform distribution
def dist(ksd,b):
    mean = 0

    # PDF of normal distribution
    def pdf(x):
        return math.exp(-0.5*(float(x/ksd))**2)/(float(ksd)*math.sqrt(2*math.pi))

    # To discretise continous normal disbribution:
    total_pdf=0
    for i in range(int(-ksd), int(ksd)+1,1):
        total_pdf= total_pdf + pdf(i)

    # Basic insertion sort with an add-on: also returns a list that represent the change in order that can help revert back to original list after sorting. 
    # Eg if list is ["a","c","b"], then sorted list is ["a","b","c"] and the order than can help to revert to the original list is [0,2,1].
    def insertSort(arr):
        order=[i for i in range(len(arr))]
        for i in range(1, len(arr)):
            key = arr[i]
            j = i-1
            while j >= 0 and key < arr[j] :
                    arr[j + 1] = arr[j]
                    order[j+1] = order[j]
                    j -= 1
            arr[j+1] = key
            order[j+1] = i
        return arr,order

    # sort a list with respect to a given list.
    # Eg. when ["a","c","b"] is sorted by the order list [0,2,1]. the output will be ["a","b","c"].
    def sortByOrder(arr,order):
        sortedArr=[0]*len(arr)
        for i in range(len(arr)):
            sortedArr[i] = arr[order[i]]
        return sortedArr

    # generate events and their respective probabilities in new array
    xValue=[]
    xProb=[]
    for i in range(int(-ksd), int(ksd)+1,1):
        xValue.append(i)
        xProb.append(pdf(i)/total_pdf)

    # sorting events and their respective probabilities in ascending order
    sortedxProb,sortedOrder = insertSort(xProb)
    sortedxValue = sortByOrder(xValue,sortedOrder)

    depositeArr =[]
    for i in range(b):
        u = random.uniform(0, 1)
        lowerlimit = 0
        for j in range(len(xValue)):
            if lowerlimit<u<lowerlimit + sortedxProb[j]:
                break
            else:
                lowerlimit = lowerlimit + sortedxProb[j]
        depositeArr.append(sortedxValue[j])

    return depositeArr
