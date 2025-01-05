#Time: 2 mins 12 secs
def printStairs(n):
    for row in range(1, n + 1):
        spaces = n - row
        print(spaces * " ", "*" * row)

printStairs(6)