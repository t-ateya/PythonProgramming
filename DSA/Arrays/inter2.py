#Write a program to find all pairs of integers whose sum is equal to a given number
#e.g input array [2, 6, 3, 9, 11] and target  9 => [6,3]

from msilib.schema import ListBox


def find_pairs(my_list, target):
    """Finds all pairs of integers whose sum is equal to a given target number"""
    for i in range(len(my_list)):
        for j in range(i+1, len(my_list)):
            if my_list[i] == my_list[j]: continue  #skip if pairs are equal
            
            elif my_list[i] + my_list[j] == target:
                    print([i,j])
                    


find_pairs([1,2,3,2,3,4,5,6], 6)