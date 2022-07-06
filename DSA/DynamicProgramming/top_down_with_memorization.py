"""
    Top Down with Memorization
    Solve the bigger problem by recursively finding the solution to smaller subproblems. Whenever we solve a sub-problem, we cache its 
    result so that we don't end up solving it repeatedly it's called multiple times. This technique of storing the results of already solved subproblems 
    is called memoization
"""

def fibMemo(n, memo):
    if n == 1:
        return 0
    if n == 2:
        return 1
    if not n in memo:
        memo[n] = fibMemo(n-1, memo) + fibMemo(n-2, memo)
        print(memo)
    return memo[n]


myDict ={}
print(fibMemo(6, myDict))