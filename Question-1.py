# -*- coding: utf-8 -*-
"""
Created on Fri Dec 15 20:11:35 2023

@author: RanjitPandey1605
"""

def my_stack_implementation(given_list,operator,new_element=None):
    if operator == 'add' and new_element != None:
        given_list.insert(0,  new_element)
    elif operator == 'remove' :
        given_list.pop(0)
    return given_list
def my_queue_implementation(given_list,operator,new_element=None):
    if operator == 'add' and new_element != None:
        given_list.append(new_element)
    elif operator == 'remove':
        given_list.pop(0)
    return given_list
        

if __name__ == '__main__':        

    new_list = [1,2,3,4]

    print("Adding new element to the stack")
    new_list = my_stack_implementation(new_list, 'add',0)
    print(new_list)

    print("Adding remove an element from stack")
    new_list = my_stack_implementation(new_list, 'remove')
    print(new_list)

    print("Adding new element to the queue")
    new_list = my_queue_implementation(new_list, 'add', 5)
    print(new_list)

    print("Adding remove and element from the queue")
    new_list = my_queue_implementation(new_list, 'remove')
    print(new_list)