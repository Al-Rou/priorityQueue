class MaxPQ:
    def __init__(self, capacity):
        self.pq = []*(capacity+1)
        self.N = 0

    def isEmpty(self):
        return self.N == 0

    def size(self):
        return self.N

    def insert(self, x):
        self.N += 1
        self.pq[self.N] = x
        self.swim(self.N)

    def swim(self, k):
        while k > 1 and self.pq[k//2] < self.pq[k]:
            self.exch(self.pq, k, k//2)
            k = k//2

    def sink(self, k):
        while 2*k <= self.N:
            j = 2*k
            if j < self.N and self.pq[j] < self.pq[j+1]:
                j += 1
            if not self.pq[k] < self.pq[j]:
                break
            self.exch(self.pq, k, j)
            k = j

    def delMax(self):
        max = self.pq[1]
        self.exch(self.pq, 1, self.N)
        self.N -= 1
        self.sink(1)
        self.pq[self.N + 1] = None
        return max

    def exch(a, i, j):
        aux = a[i]
        a[i] = a[j]
        a[j] = aux
