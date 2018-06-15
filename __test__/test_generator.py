def squares(n=10):
    # results = []
    for i in range(n+1):
        yield i**2
    #     results.append(i**2)
    # return results

for x in squares(10):
    print(x)