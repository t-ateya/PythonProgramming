
"""
    Bottom Up with Tabulation
    Tabulation is the opposite of top-down approach and avoids recursion. I this approach, we solve the problem "bottom-up" (i.e by solving all the related sub
    problems first). This is done by filling up a table. Based on the results in the table, the solution to the top/original problem is then computed.
"""

def fibonacciTable(n):
    tb = [0, 1]
    for i in range(2, n+1):
        tb.append(tb[i-1] + tb[i-2])
    return tb[n-1]

print(fibonacciTable(6))