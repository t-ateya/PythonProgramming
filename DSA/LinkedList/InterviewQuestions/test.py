def sum():
    list1 = [6,1, 7]
    list2 = [2, 9, 5]
    index1 = len(list1) -1
    
    tot = []
    carry = 0
    while index1 >=0:
        s = list1[index1] + list2[index1] + carry
        if s >10:
            carry =1
            s = s %10   
            print(carry)

        tot.append(s)
        index1 -=1
        

    #tot.reverse()
    return tot

#print(sum())
print(abs(-2))