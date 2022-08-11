def rec_sum(n:int)->int:
    if n==0:
        return 0 
    return rec_sum(n-1) + n



print(rec_sum(4))