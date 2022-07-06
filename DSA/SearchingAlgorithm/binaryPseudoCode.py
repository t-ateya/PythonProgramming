"""
    Create function with two parameters which are sorted array and a value 
    -Create two pointers: a left pointer at the start of the array and a right pointer at the end of the array
    -Based on left and right pointers, calculate the middle pointer
    -While middle is not equal to the value and start <= end loop:
        -if the middle is greater than the value move the right pointer down
        -if the middle is less than the value move the left pointer up
    - If value is never found return -1
    
"""