"""
    Dynamic Programming (DP) is an algorithmic technique for solving an optimization problem by breaking it down into 
    simpler subproblems and utilizing the fact that optimal the optimal solution to the overall problem depends upon the optimal solution to its subproblems

    Properties of DP:
    1. Optimal Structure:
        - If any problem's overall optimal solution can be structured from the optimal solutions of its subproblem, then this problem has optimal substructure

        Example: Fib(n)  = Fib(n-1) + Fib(n-2)

    2. Overlapping Subproblem:
        Subproblems are smaller versions of the original problem. Any problem has overlapping sub-problem if finding its solution involves solving the same
        sub problem multiple times.
"""