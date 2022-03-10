import heapq

def solve(a, n):
    heapq.heapify(a)
    #print(a)
    res = 0
    min1 = heapq.heappop(a)
    for i in range(n - 1):
        min2 = heapq.heappop(a)
        summa = min1 + min2
        res += summa / 20
        min1 = heapq.heappushpop(a, summa)
        #print(summa)
    print("%.2f" % res)