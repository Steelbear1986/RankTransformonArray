class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        s = set(arr)
        l = list(sorted(s))
        arr2 = {l[i]: i + 1 for i in range(len(l))}

        for i in range(len(arr)):
            arr[i] = arr2[arr[i]]
        return arr
