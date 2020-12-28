# Primitive and Non-primitive Data Structures
## Taken from https://www.thecrazyprogrammer.com/2018/10/types-of-data-structures.html

###
The main purpose of a data structure is they give us a way to work with data. The right selection of an appropriate data structure for solving a particular problem can prove very beneficial and helps reduce the complexity of a program.

### Primitive Data Structures
These are data structures which are supported at the machine level. These are integral to the system and have predefined behavior and specifications. 
Examples of these include integer, float, character and pointers. 
Note that pointers don't hold a data value, but instead hold memory addresses of the data values. These are called reference data types. 

### Non-primitive Data Structures
These are data structures which cannot be performed without the primitive data structures. 
Examples of these include Arrays, Files, Lists, Linear lists, and Non-linear lists.

#### Arrays
Arrays are homogeneous & continguous collection of same data types. They use static memory allocation, meaning that if memory space is allocated for one, it cannot be changed during runtime. These are used to implement vectors, matricies and also other data structures. Because elements are stored in consecutive memory allocations, insertions & deletions are complex in arrays.

#### Files
A collection of records. Primarily used for managing large amounts of data which is not in the primary storage of the system. Helps to process, manage, access & retrieve or basically work with the data. 

#### Lists 
Support dynamic memory allocation which can be changed at run time.
The two types of lists are:

a) Linear Lists
Those which have the elements stored in a sequential order. Insertions & deletions are easier in lists. Linear Lists are further divided into two types:
    - Stacks
        Stacks follow a "LIFO" technique for storing & retreiving elements. The stack has the primary fucntions of Push(), which inserts an item into the stack, and Pop(), which removes an element from the stack.
    - Queues
        Queues follow a "FIFO" mechanism for storing & retreieving elements. The "Enqueue" operation is used to insert an element into the queue whereas the "Dequeue" operation is for removing an element from the queue.

b) Non Linear Lists
Those which have the elements stored in a non-sequential order. Further divided into two types:
    - Graphs
        Used to represent a network. Comprises of vertices & edges to connect the vertices. Useful when it comes to study a network.
    -Trees
        Comprised of nodes connected in a particular arrangement and they make search operations on the data items easily. Consist of a root node which is further divided into various child nodes. The number of levels of the tree is also called the height of the tree. 


# Big O Notation 
## Notes on the following video: https://www.youtube.com/watch?v=v4cd1O4zkGw

### Understanding Big O Notation
Big O is used to calculate the limiting behavior of a function when the argument tends toward a particular value or infinity. Specifically in computer science, it is used to classify algorithms according to how their run time or space requirements grow as the input size grows. 
# IT IS JUST A WAY TO CALCULATE HOW MUCH MEMORY A PROGRAM WILL USE OR HOW LONG IT WILL TAKE TO PROCESS DATA. REMEMBER THAT DATA STRUCTURES ARE ALL ABOUT OPTIMZATION, OR PROCESSING DATA QUICKLY AND EFFICIENTLY
You can classify many types of data processing as processing in either constant time (where the time it takes to process remains constant no matter how much data is being processed) and linear time (where processing time grows exponentially according to the amount of data processed). In a comparison, constant time beats linear data if data is sufficiently big.
# BIG O CAN THUS BE SIMPLIFIED AS HOW TIME SCALES WITH RESPECT TO SOME INPUT VARIABLES

Examine the following code: 
boolean contains(array, x){
    for each element in array{
        if element == x{
            return true
        }
    }
}

This function would be linear, or O(n), where n is the size of the array

Now examine the following code:
void printPairs(array){
    for each x in array{
        for each y in array{
            print x, y
        }
    }
}
This would be described as O(n^2), where n is the size of the array

### 4 Important Rules to Know about Big O
##### 1
Different steps get added.
For example if you had a function that took O(a) and O(b), you would say it is O(a+b).
##### 2
Constants are dropped. This is because, as explained in the notes, any number times or added to infinity is still infinity. 
Remember that Big O isn't concerned with anything but explaining the optimization, explaining the run time. It is not a mathematical formula in that a result is expected.
##### 3
If you have different inputs, you must use different variables to represent them. Always remember that Big O is a explanation of the run time, how the function or program scales. 
Because of this, if you have a function that calculates the intersection size of two arrays, the function is not O(n^2) because, what does N mean here? N must stand for something. In this case you would say O(a*b) with a being the length of array A and b being the length of array b. You cannot simply call it N and thats it when there's two different arrays.
##### 4
Drop non-dominate terms. This can be rather confusing and you may have to look this up to determine when exactly you should be dropping one and whether it is one that can be dropped, but basically a non-dominate term is one that can be swallowed in by another, meaning another one takes precedence over it in terms of deciding the run time.


# More notes on Big-O Notation
## Notes on the following video: https://www.youtube.com/watch?v=itn09C2ZB9Y
### Big O Notation: Time
The fastest way to determine a functions Big O notation is to first examine what part of the function repeats over and over again based on the input. 
For example take the following code:

    char data[] = {'A', 'B', 'C'};
    for(int i=0; i < sizeof(data); i++){
        cout << data[i] << "\n";
    }

In this case our print statement is what really determines the program speed because it is the part of the function that repeats over and over again, depending on the input that is provided.
In this case we could say the function has a Big-O notation of O(n) because the run time grows in a linear line with the input size, thus it is a linear function. 
##### Think of linear as meaning that it grows one for one with the input size. For each input, the function must run one more time. Thus it grows linearly with the input. 
Now for example let's add another for loop and array

    char data[7] = {'A', 'B', 'C', 'D', 'E', 'F', 'G'};
    int data2[5] = {1, 2, 3, 4, 5};
    for(int i=0; i < sizeof(data); i++){
        cout << data[i] << "\n";
    }
    for(int j=0; j < sizeof(data2); j++){
        cout << data2[j] << "\n";
    }
Now that we have two functions that really determine the program speed, we can now say that this program is O(n+a), n being the first one and a being the second one. 
Now what if we combine our for functions into a nested for loop?
    char data[7] = {'A', 'B', 'C', 'D', 'E', 'F', 'G'};
    int data2[5] = {1, 2, 3, 4, 5};
    for(int j=0; j < sizeof(data2); j++){
        for(int i=0; i < sizeof(data); i++){
            cout << data2[j] + data1[i]<< "\n";
        }
    }

In this case, our Big O notation would be O(n * a) because n is being essentially multipled by a. 
This is why if you want to aim for optmization, you really want to avoid too many nested for loops no matter what language you are running. In all languages this process is very slow.
Now lets say you modify the code again to get rid of data 2.
    char data[7] = {'A', 'B', 'C', 'D', 'E', 'F', 'G'};
    for(int j=0; j < sizeof(data); j++){
        for(int i=0; i < sizeof(data); i++){
            cout << data[i] + data[j] << "\n";
        }
    }

In this function, instead of iterating thru 2 arrays, we are not iterating thru the same array twice each for loop. This thus results in a big O notation of O(n^2). 
Lets say that we have an input array of 3; this would result in the above for loop processing 9 times total. Thus it is growing exponentially. Here we have it running with an array of 7 items; this would result in the for loop processing 49 times. You can see how quickly this would get out of control.

### Big O Notation: Space
Big O noation is also used when you are trying to calculate the amount of space a program might take up in memory. This is another key factor in optimization. 
Take the following below code for example: 
    const data = {'a', 'b', 'c'};
    const out = {};
    for(int i = 0; i < sizeof(data); i++){
        out[i] = data[i]
    }

This function basically creates a copy of all the items in the first array, thus this function will take space in memory. 
In the above case we can see that the returned list will grow incrementally with the array passed in. Thus this function has a Big O notation of O(n). 
The amount of space this list will take will be the exact same amount of space as the data passed in. 
Now let's take another example: 

    const data = {'a', 'b', 'c'};
    const out = {};
    for(int i = 0; i < sizeof(data); i++){
        out[i] = {}
        for(int j = 0; j < sizeof(data); j++){
        out[i][j] = data[i]
    }
This function will then create three different arrays inside of one array, and each array will be an item in data repeated three times. This thus means the program will grow exponentially and thus has a big O notation of O(n^2). 
# Data Structures: an Introduction 
## Notes on the following video: https://www.youtube.com/watch?v=RBSGKlAvoiM

### Abstract Data Type
An Abstract Data Type (ADT) is an abstraction of a data structure which provides only the interface to which a data structure must adhere to. This is different from an actual Implementation, or DS.

Examples of Abstraction: 
    List 
    Queue
    Map
    Vehicle

Examples of Implementation (DS)
    Dynamic Array - List 
    Linked List - List
    Linked List based Queue - Queue
    Array based Queue - Queue
    Stack based Queue - Queue
    Tree Map - Map
    Hash Map / Hash Table - Map
    Golf Cart - Vehicle
    Bicycle - Vehicle
    Smart Car - Vehicle

### Computational Complexity Analysis
Computational Complexity Analysis deals with two different questions:
a) How much time does this algorithm need to finish?
b) How much space does this algorithm need for its computation?

To answer these questions we use Big-O notation. 
Big-O Notation gives an upper bound of the complexity in the worst case, helping to quantify performance as the input size becomes arbitrarily large.

Some examples of Big-O Notation:
n - the size of the input
Complexities ordered in from smallest to largest

Constant Time: 0(1)
Logarithmic Time: 0(log(n))
Linear Time: 0(n)
Linearithmic Time: 0(nlog(n))
Quadric Time: 0(n^2)
Cubic Time: 0(n^3)
Exponential Time: 0(b^n), b > 1
Factorial Time: 0(n!)

Big-O Properties
Big-O only really cares about numbers where the input goes extremely high, to infinity, and is thus not used when working with small numbers. 
Because we only care when a number is big, we thus get our first two Big-O Properties:
Note that 'c' stands for 'constant'
0 (n + c) = 0(n)
0(cn) = 0(n), c > 0
Because you can think of n as representing infinity, we can simplify adding c away because adding c to infinity is just infinity, and multiplying c by infinity is just infinity again, so we can simply ignore constants. 

Constant Time is where a function does not depend on n, and instead run on set variables.
For example:
a := 1 
b := 2
c := a + 5*b
This function depends solely on constant, set variables and thus runs in constant time.

i := 0
While i < 11 Do
    i = i + 1

This function also depends solely on constants and thus runs in constant time.

The opposite of constant time is Linear Time, where a function relies on n: 0(n)
For example:
i := 0              f(n) = n
While i < n Do      0(f(n)) = 0(n)
    i = i + 1
This function does depend on a n, which can be anything and as we established will be used to represent infinite, and thus they work on a linear time, meaning they do not have a set value and can thus run infinitely.

### Dynamic and Static Arrays

What is an static array?
    A fixed length container containing n elements indexable from the range [0, n-1], with slots/indexes that can be referenced with a number. 
When and where is a Array used?
Static Arrays are by far the most widely used form of array anywhere. In fact, it is often hard to write a program that does not use them. 
    - Storing and accessing sequential data
        The most common use of them. Used to temporarily store objects. 
    - Temporarily storing objects
    - Used by IO routines as buffers
        Suppose you are trying to read thru information that is much too large for your memory to contain. You can use a static array as a buffer, adding items into it one by one so that you can read thru everything sequentially.
    - Lookup tables and inverse loopup tables
        Static Arrays can also be used to create a lookup table thanks to their indexing properties, which make it very easy retrieve information as all you have to do is provide the items index location. 
    - Can be used to return multiple values from a function
        Static Arrays can be used as a workaround for programming languages that only allow one return value. You can return a pointer that points to a array with the values that we want to return. This is a neat little "hack" for those situations. 
    - Used in dynamic programming to cache answers to subproblems.
        As the name implies, static arrays are often used to cache answers to subproblems in order to help speed up a program, for example the coin change problem.
Complexity

Access
    Static Array - Constant
    Dynamic Array - Constant
    Static & Dynamic are both constant because of their indexing properties. In order to find any element within any array you only need its index. This operation time does not increase no matter how many items are in the array. 
Search
    Static Array - Linear
    Dynamic Array - Linear
    Both arrays have a linear speed when searching however, namely because in a search you would have to potentially traverse the entire array for the item, especially in the worst case scenario in which the element does not exist.
Insertion
    Static Array - Not Possible
    Dynamic Array - Linear
    Not possible in a Static Array because Static Arrays cannot grow or shrink in size.
    Assuming a scenario in which you are creating a new dynamic array out of a static array, insertion operates on linear time, because you would need to shift all the elements to the right, and add them one by one to the new array.
Appending
    Static Array - Not Possible
    Dynamic Array - Constant
    Not possible in a Static Array because Static Arrays cannot grow or shrink in size.
    Appending operates in constant time because when you insert, you are adding another slot to the array and adding an item to the newly created slot; there is no shifting of items happening in this scenario.
Deletion
    Static Array - Not Possible
    Dynamic Array - Linear
    Not possible in a Static Array because Static Arrays cannot grow or shrink in size.
    Deletion operates on Linear time for the same reason it does in Insertion. Potentially, you would have to shift all the elements in the array to the left, and then copy each element into a static array. It's like Insertion but in reverse. 

Dynamic Array implementation details 
    One way to implement a dynamic array is to use a static array.
    1) Create a static array with an initial capacity. 
    2) Add elements to the underlying static array, keeping track of the number of elements.
    3) If adding another element will exceed the capacity, then create a new static array with twice the capacity and copy the original elements into it.
Code Implementation 
    A fun experiment if you ever learn how to read that fucking gobbledygook that is Java is maybe taking the example dynamic array code from the video and implementing it in C++. 


Singly and Doubly Linked Lists

What is a linked list?
    A sequential list of nodes that hold data which point to other nodes also containing data.
Where are linked lists used?
    Used in many List, Queue & Stack implementations, primarily thanks to indexing. 
    Great for creating circular lists, by making the pointer of the last node link back to the first node. Circular lists are commonly to represent looping patterns like polygons.
    Can easily mode real world objects such as trains. 
    Used in seperate chainging, which is present in certain Hashtable implementations to deal with hashing collisions, as well as implmentation of adjacency lists for graphs. 
Terminology
    Head: The first node in a linked list. 
    Tail: The last node in a linked list.
    Pointer: Reference to another node. 
    Node: An object containing data and pointers.
Singly Linked vs Doubly Linked
    Singly linked lists only hold a reference to the next node. In the implmentation you always maintain a reference to the head to the linked list and a reference to the tail node quick additions/ removals.
    Nodes on a doubly linked lists on the other hand hold a reference to the next and previous node. In the implementation you always maintain a reference to the head and the tail of the doubly linked list to do quick additions/removals from both ends of your list. 
Pros & Cons of Singly & Doubly Linked Lists
    Singly Linked
    Pros
        uses less memory
            This is because of pointers. Pointers can actually take up quite a bit of memory: on a 64bit machine they are 8 bits and on a 32bit machine they are 4bits.
        simpler implementation
    Cons
        Cannot easily access previous elements
    
    Doubly Linked
    Pros 
        Can be traversed backwards
    Cons    
        Takes 2x memory
            Due to all the pointers that doubly linked lists make use of, they are often twice as memory heavy as a single linked list.

Complexity Analysis
    Singly linked list complexity:
    Search : 0(n)
    Insert at head: O(1)
    Insert at tail: O(1)
    Remove at head: O(1)
    Remove at tail: 0(n)
    Remove at middle: 0(n)
    Doubly linked list complexity: 
    Search : 0(n)
    Insert at head: O(1)
    Insert at tail: O(1)
    Remove at head: O(1)
    Remove at tail: 0(1)
    Remove at middle: 0(n)

The Stack

    What is a stack?
        A stack is a one-ended linear data structure which models a real world stack by having two primary operations, namely push and pop. 
        Stacks work off the top, pushing an elements onto the top and popping elements off of it. This behavior is commonly known as LIFO, or Last In First Out. You can think of this as the exact same behavior as the stack from MTG: The last effect to have been done is resolved first. 
        It is criticial to understand that in a stack you only have power over the TOP ELEMENT IN THE STACK. You cannot change anything off of the most bottom parts of it unless you pop elements off until you reach it. You can only work off the top most element. 
    When and where is a stack used?
        Stacks are extremely common and you will find them in many different programs.
        - Used by undo mechanisms in text editors
        - Used in compiler syntax checking for matching brackets and braces
        - Can be used to model a pile of books or plates
        - Used behind the scenes to support recursion by keeping track of previous function calls
        - Can be used to do a Depth First Search (DFS) on a graph. 
    Complexity Analysis
        Pushing     O(1)
        Popping     O(1)
        Peeking     O(1)
        Searching   O(n)
        Size        O(1)

        All of the operations in the stack operate on constant time except for searching. This is because the item we are searching for may not necessarily be at the top of the stack which would mean we would have to search thru every single element in the stack to find it. Everything else on the other hand operates on linear time because you are simply manipulating things one at a time.
    Implementation details
        The following is pseudo-code explaining some example stack usage for determining whether or not a bracket sequence is valid or invalid. It is valid only when every bracket is closed. 
        [{}] => valid
        (()()) => valid
        {] => invalid
        [()]))() => invalid
        []{}({}) => valid 

        Let S be a stack
        For bracket in bracket_string:
            rev = getReversedBracket(bracket)
            if isLeftBracket(bracket):
                S.push(bracket)
            else if S.isEmpty() or S.pop() != rev:
                return false //Invalid
        return S.isEmpty() //valid if s is empty
    pushing elements on stack
    popping elements from stack

The Queues

    What is a queue?
        A queue is a linear data structure which models real world queues by having two primary operations, namely enqueue and dequeue. 
        All queues have a front and a back, and items are added from the back and removed from the front. They simulate real life queues and an easy way to think about them is to think of a line for a movie.
    Terminology
        There isn't any consistency in regards to the terminology for queues across languages. Enqueue can also be called adding or offering, and dequeing can also be called removing or polling. 
    When and where is a queue used?
        - Any waiting line models a queue, for example a lineup for a movie.
        - Can be used to efficiently keep track of the x most recently added elements.
        - Web server request management where you want first come first serve.
        - breadth first search (BFS) graph traversal.
    Complexity Analysis
        Enqueue     O(1)
        Dequeue     O(1)
        Peeking     O(1)
        Contains    O(n)
        Removal     O(n)
        Is Empty    O(1)
        Note that peeking is an operation for seeing the elements in the queue. 
        Contains is to check if the item is in the queue.
        While everything operates on constant time for obvious reasons, Contains and removal operate on linear time because you would potentially need to look thru the entire queue to find your item.
    Coding a Breadth First Search. 
        Breadth First Search acts as a way to traverse a graph in which one node visits its adjacent nodes until all the nodes have been visited. 
    Implementing queues
        Queues are popularly implemented using arrays, linked lists and doubly linked lists. Do note that if you are going to be using a static array to make sure you are allocating enough slots for it. 
        Our first node will have the head and tail pointer at the same node, the only node available, however it changes as we enqueue and dequeue items. As we enqueue, our tail pointer moves forward. Conversely, when we dequeque, our head pointer now moves forward. The previous position which now has no value will then need to have its memory freed in C++ & C# so make note of that. 

Priority Queues (PQ's) with an interlude on heaps
    