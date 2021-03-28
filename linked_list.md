# LINKED LIST
![linked_list](linked_list.png)
## Introduction
A linked list is a linear data structure. Elements in a linked list are not stored at a contiguous memory location. All the elements in a linked list are "linked" together by pointers (pnext and pprev). The data, pprev, and pnext together are referred to as a node. Each node has a pointer that is pointing to the previous node and another pointing to the next node. The first node in a linked list is referred to as being the "head" and the last node being referred to as "tail".
## Uses of Linked List

## Linked List vs. Array

## Performance
| Linked List Operations | Description                                               | Performance |
| ---------------------- | --------------------------------------------------------- | ----------- |
| insert_head(value)     | Adds "value" before the head.                             | O(1)        |
| insert_tail(value)     | Adds "value" after the tail.                              | O(1)        |
| insert(i, value)       | Adds "value" after node "i".                              | O(n)        |
| remove_head()          | Removes the first item.                                   | O(1)        |
| remove_tail(index)     | Removes the last item.                                    | O(1)        |
| remove()               | Removes node "i".                                         | O(n)        |
| size()                 | Returns the size of the linked list.                      | O(1)        |
| empty()                | Returns true if the length of the linked list is zero.    | O(1)        |
## Example

## Problem to Solve

You can check your code with the solution here: [Solution](linked_list_solution.py)



[Back to Welcome Page](welcome.md)