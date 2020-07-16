# Day14 scope

class Difference:
    def __init__(self, arr):
        self.__elements = arr

        self.maximumDifference = 0

    def computeDifference(self):
        max_val = []
        for n in self.__elements:
            max_val.append(max(list(map(lambda x: abs(n - x), self.__elements))))

        self.maximumDifference = max(max_val)


# End of Difference class

_ = input()
arr = [int(e) for e in input().split(' ')]

d = Difference(arr)
d.computeDifference()

print(d.maximumDifference)
