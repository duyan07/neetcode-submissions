# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def merge(self, arr, l, r):
        i = 0
        j = 0
        k = 0
        
        while i < len(l) and j < len(r):
            if l[i].key < r[j].key:
                arr[k] = l[i]
                i += 1
            elif l[i].key > r[j].key:
                arr[k] = r[j]
                j += 1
            else:
                arr[k] = l[i]
                arr[k + 1] = r[j]
                i += 1
                j += 1
                k += 1
            k += 1

        while i < len(l):
            arr[k] = l[i]
            i += 1
            k += 1
        while j < len(r):
            arr[k] = r[j]
            j += 1
            k += 1
        
        return arr

    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:
        if len(pairs) <= 1:
            return pairs

        m = len(pairs) // 2
        l = self.mergeSort(pairs[:m])
        r = self.mergeSort(pairs[m:])

        pairs = self.merge(pairs, l, r)

        return pairs