## Table of Content:

- [Python Documentation](#python-documentation)
  - [Naming Convenience](#naming-convenience)
  - [Classes](#classes)
  - [Data Structures](#data-structures)
      - [1. Stack ✓](#1-stack-)
      - [2. Queue ✓](#2-queue-)
      - [3. Linked List ✓](#3-linked-list-)
      - [4. Doubly Linked List ✓](#4-doubly-linked-list-)
      - [5. Circular Linked List ✓](#5-circular-linked-list-)
  - [Algorithm](#algorithm)
    - [Sorting](#sorting)
      - [1. Selection Sort ✓](#1-selection-sort-)
      - [2. Bubble Sort ✓](#2-bubble-sort-)
      - [3. Insertion Sort ✓](#3-insertion-sort-)
      - [4. Merge Sort](#4-merge-sort)
      - [5. Quick Sort](#5-quick-sort)
    - [Searching](#searching)
      - [1. Linear Search ✓](#1-linear-search-)
      - [2. Binary Search (for sorted) ✓](#2-binary-search-for-sorted-)

# Python Documentation

Keep it simple, like if 12 year old reads this document he/she will be able to understand.

## Naming Convenience
Recommended [naming convenience](https://peps.python.org/pep-0008/#naming-conventions) for defining a _function_, _modules (files)_, and _variables_ are use all **lower_cases** maybe use underscore for readability, for _class_ are **UpperCamelCase**, and for _packages_ are **lowercases** although the use of underscores is discouraged.

## Classes

Some Noted about classes:

Class is a logical grouping of data and methods. Instance of a class is called objects. Data and methods are called class attributes. Class functions are called methods.

```python    
name = 'Aravind'

name - object name
'Aravind' - object of string class
```

## Data Structures

#### 1. Stack ✓
   
Based on Last In, First Out (LIFO) arrangement, new elements are inserted at top of the stack one at the time and user can delete the top element of the stack one at time.

#### 2. Queue ✓

Based on First In, First Out (FIFO) arrangement, new element are insert at rear/ last and we can delete the first element in front of the list one at time.

#### 3. Linked List ✓

Each element in a linked list is call node, a node contain of data and next attributes \[Data:Next]. next hold another node and so on. we track the head element of the linked list and perform insertion and deletion operations. we traversing the list one by one by it's data a→b→c.

#### 4. Doubly Linked List ✓

Similar to linked list, each elements in this doubly linked list is node, unlike single linked list, this node contain previous, data and next attributes in it's node \[Previous:Data:Next]. We track the first element as head and perform add or delete operation based on head element. we traversing through the each element one by one with help of assigning the iterating current node.

#### 5. Circular Linked List ✓

This is more like Singly Linked List, Each node contain data:next pairs. Unlike Linked List, we keep track of last element of the list, this is more useful to insert or delete the last element, for example in linked list, we have to traversing element from first to last, but in CLL we know the reference of last value and insert directly at end of the list. and last.next hold the head of the element node we easy determine and perform insertion and deletion operation.

## Algorithm

### Sorting

#### 1. Selection Sort ✓
#### 2. Bubble Sort ✓
#### 3. Insertion Sort ✓
#### 4. Merge Sort
#### 5. Quick Sort

### Searching

#### 1. Linear Search ✓
#### 2. Binary Search (for sorted) ✓
