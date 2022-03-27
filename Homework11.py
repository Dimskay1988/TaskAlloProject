class geometric_progression:
    @staticmethod
    def geoprog(i, d):
        while True:
            yield i
            i *= d

iter = geometric_progression
iter = iter.geoprog(1, 2)
print(next(iter))
print(next(iter))
print(next(iter))
print(next(iter))
print(next(iter))
print(next(iter))
print(next(iter))
print(next(iter))
print(next(iter))
print(next(iter))