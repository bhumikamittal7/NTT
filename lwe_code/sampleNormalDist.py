import math,random
import matplotlib.pyplot as plt

mean = 0
ksd=25
## calculating the discrete normal distribution with the help of continuous uniform distribution
def dist(ksd,b):

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

    # sort a list with respect to a given index list.
    # Eg. when ["a","c","b"] is sorted by the order list [0,2,1]. the output will be ["a","b","c"].
    def sortByOrder(arr,order):
        sortedArr=[0]*len(arr)
        for i in range(len(arr)):
            sortedArr[i] = arr[order[i]]
        return sortedArr

    # generates events and their respective probabilities in new array
    xValue=[]
    xProb=[]
    for i in range(int(-ksd), int(ksd)+1,1):
        xValue.append(i)
        xProb.append(pdf(i)/total_pdf)

    # sorting events and their respective probabilities in ascending order
    sortedxProb,sortedOrder = insertSort(xProb)
    sortedxValue = sortByOrder(xValue,sortedOrder)

    countArr =[0]*len(xValue)
    for i in range(b):
        u = random.uniform(0, 1)
        lowerlimit = 0
        for j in range(len(xValue)):
            if lowerlimit<u<lowerlimit + sortedxProb[j]:
                break
            else:
                lowerlimit = lowerlimit + sortedxProb[j]
        countArr[j]=countArr[j]+1

    # reverting the ascending ordered events and probabilities into their original order
    finalxValue,finalOrder = insertSort(sortedxValue)
    finalcountArr = sortByOrder(countArr,finalOrder)

    #plotting bar graph
    plt.bar(finalxValue, finalcountArr)
    plt.show()

    # for k in range(len(countArr)): 
    #     print(finalxValue[k],'appears', finalcountArr[k],'times.')

dist(ksd,100000)