# Add your clarifying questions here
# Given a list [1, 2, 3, 4, 5] and a number 3, rotate the items in the list 3 places over to the right. The output should be: [3, 4, 5, 1, 2].
#Hard mode: Rotate the list "in-place" without creating a new list.
#Write your clarifying questions and implementation in `rotate_list.py`. To execute your code, run `python3 rotate_list.py` in the terminal.

def rotate_list(list, shift_by):

#### Easy method
    
    # updated_list = list[:]    
    # for i in range(len(list)): 
    #     if (shift_by + i) < len(list):
    #         index = i + shift_by
            
    #     elif (shift_by + i) >= len(list): 
    #         index = (i + shift_by) % len(list)
    #     updated_list[index] = list[i]
    # print(list)
    # print (updated_list)

# hard method (no new list created)
    len_list = len(list)
    list = list + list
    for i in range(len_list): 
        if (shift_by + i) < len_list:
            index = i + shift_by + (len_list)
        elif (shift_by + i) >= len_list: 
            index = (i + shift_by) % len_list+ (len_list)
        list[index] = list[i]
    print(list)

    del list[:len_list]
    print(list)

rotate_list([1,2,3,4,5], 3)
rotate_list([1,2,3,4,5,6], 4)


