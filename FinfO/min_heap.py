import heapq


class KthSmallest:
    min_heap = []

    def __init__(self, k: int) -> None:
        heapq.heapify(self.min_heap)
        heapq.heappush(self.min_heap, k)

    def add(self, num: int) -> None:
        heapq.heappush(self.min_heap, num)

    def getKthSmallest(self) -> int:
        return heapq.nsmallest(1, self.min_heap)[0]

if __name__ == '__main__':
    import random

    kth_smallest = KthSmallest(3)
    for _ in range(15):
        kth_smallest.add(random.randint(1, 60))
    print(kth_smallest.getKthSmallest())
