# 100daysofalgorithms

Hello! I'm Daniel Sada. I've covered most of this algorithms in classes before, but I didn't implement them myself, and see what roadblocks I've got. I'm trying to do an algorithm or two a day or at least try to solve a problem a day. I'll be alternating between new algorithms and working in problems with those algorithms. I'm also fairly new with python, and I want to get aquaintanced with Python3.

# Running unit tests.

Clone the project, then run :

```
python -m unittest discover algorithms/test -v
```

# Topics to cover:
 - [x] union-find
 - [x] binary search
 - [x] stacks
 - [x] queues   
 - [x] insertion sort
 - [x] selection sort
 - [x] shellsort
 - [x] quicksort
 - [x] 3-way quicksort
 - [x] mergesort
 - [x] heapsort
 - [x] Graham scan
 - [x] binary heaps
 - [x] binary search trees
 - [x] kd-trees
 - [x] red−black trees
 - [x] depth-first search
 - [x] breadth-first search
 - [x] topological sort
 - [x] Kosaraju−Sharir
 - [x] Kruskal
 - [x] Prim
 - [x] Dijkistra
 - [X] Bellman−Ford
 - [X] Ford−Fulkerson
 - [X] LSD radix sort
 - [X] MSD radix sort
 - [X] 3-way radix quicksort
 - [X] multiway tries
 - [X] ternary search tries
 - [X] Knuth−Morris−Pratt
 - [X] Boyer-Moore
 - [X] Rabin−Karp
 - [X] regular expression matching
 - [X] run-length coding
 - [X] Huffman coding
 - [X] LZW compression 
 - [x] Ford fulkerson flow graphs.
 
 Machine Learning
 - [X] Linear Regression
 - [X] Training and Loss
 - [X] Gradient Descent
 - [X] Learning Rates and Batch vs Stochastic learning.
 - [X] Tensorflow implemented linear regression.

Syntax Matching
- [X] Syntax matching for atomlike editors. 

# Day to Day log.

Day 1:
- [x] Quick Find
- [x] Quick Union

Day 2:
- [x] Union Find
- [x] Weighted Union Find
- [x] Flattened Path Union Find

Day 3:
- [x] (partial) (undirected) Graph API

Day 4:
- [x] (finished) (undirected) Graph API
- [x] Graph API tests.
- [x] Depth-First search initialization

Day 5: 
- [x] Path between two nodes with backtracking.
- [x] Breath-first search (not finished)

Day 6:
- [x] Breath-first search
- [x] Breath-first tests

Day 7:
- [x] Connected components

Day 8:
- [x] Bipartite Graph Problem
  
Day 9:
- [x] Heap
- [x] MinHeap

Day 10:
- [x] Min Heap

Day 11:
- [x] Min Heap
- [x] Max Heap
- [x] Heap Unit tests.

Day 12: 
- [x] Bipartite grahps
- [x] Bipartite graph tests.

Day 13:
- [x] Refactoring some components to use .V instead of .num_V(), more pythonic.
- [x] Directed Graph API
- [x] Started Topological Sort

Day 14:
- [x] Finished topological sort. (tests pending)
- [x] Finished undirected graph cycle detection.
- [x] Added tests to connected components.
- [x] Started directed cycle detection.  

Day 15:
- [x] Finished directed cycle detection
- [x] Kosajaru-Sharir algoritms for strongly connected components
- [x] Added tests for topological sort
- [x] Added reversal of directed graphs
- [x] A sample stack problem, as we are in python.

Day 16:
- [x] Binary search problem for completion.

Day 17: 
- [x] Created Snippets for faster coding.
- [x] Selection Sort

Day 18: 
 - [x] insertion sort
 - [x] shellsort

Day 19:
 - [x] Weighted Graph and Edge API and 
 - [x] Minimum Spanning Trees API. 

Day 20:
- [x] Kruskal's implementation for finding the Minimum Spanning Tree of a Weighted Graph. 

Day 21:
- [x] Mergesort implemented specifically for python.

Day 22:
- [x] Sorting tests for shell sort, insertion sort, selection sort, etc. Standardize all sorts to have the same property .sorted

Day 23:
- [x] Quicksort

Day 24: 
- [x] Dijkstra's Three way quicksort 

Day 25:
- [x] Added priority queue.er (Which is only a Max Heap that implements total ording) 
- [x] Implemented tupled ordering in max heap to make max heap usable for a priority queue. 
- [x] Added tests for max heaps with tuples and priority queues.

Day 26:
- [x] Started working on Binary Search Trees and Symbol tables. 

Day 27:
- [x] Finished Binary Search Tree get and put implementations, 
- [x] Added some unit tests for bst

Day 28:
- [x] Added ceiling, floor min and max to bst.

Day 29:
- [x] Added python iterators
- [x] Started rank

Day 30:
- [x] Started working on hibbard's deletion for binary search trees
- [x] adding some unit tests, debugging some bugs.

Day 31:
- [x] Bugfixing, bst methods should take keys, not items.
- [x] Added more unit tests.

Day 32 : 
- [x] Started to learn (and code) red black trees. 

Day 33:
- [X] Implemented rotate left, rotate right, move left move right and put for Red Black Trees

Day 34:
- [x] Finished Red Black Tree Deletion, 
- [x] RBT Minimum, 
- [x] Balancing the tree.

Day 35:
- [x] Linted the entire project, fixed all of the warnings in the files. 

Day 36:
- [x] Learned about kd trees. 
- [x] Added some more tests to BSTs
- [x] level order traversal for BST.

Day 37:
- [x] Added unit tests to my Red Black tree implementation.
- [x] Bugfixing RBTs
- [x] Discovered delete min was not implemented correctly

Day 38:
- [x] Learned about 1D and 2D interval search with BSTs
- [x] Implemented in some cases python __len__ __repr__ __build_subclass__ etc, also __add__.

Day 39:
- [x]  More changes in imports.
- [x] started prim's algorithm for MSTs 
- [x] Seeing whether a contains method is useful in a MST.

Day 40:
- [x] Kept working on prim's algorithm for minimum spanning trees. 
- [x] I added some unit tests for prim.
- [x] Dunder methods for Heap, PQ, Edge, etc.

Day 41:
- [x] Finally finished Prim's algorithm. 
- [x] Added Heap unit tests, priority queue unit tests, fixed weighted graph. 
- [x] Added tests for weighted graphs.

Day 42: 
- [x] Read about Delaunay's Triangulation and Voronoi diagrams. 
- [x] Learned about how Prim & Kruskal's algorithms can be used for k-clustering and that it can be close to linear. 
- [x] Implemented Directed Weighted Graphs API.

Day 43:
- [x] Started working on Dijkstra 
- [x] MinimumIndexedPriority queues.

Day 44: 
- [x] Continued implementing Dijkstra implemented with MinimumIndixedPriority queues

Day 45: 
- [x] Did Dijkstra unit test, still debugging. 

Day 46:
- [x] Finished Dijkstra implementation with Indexed Minimum Priority Queues

Day 47:
- [x] Implemented Bellman-Ford for negative directed graphs without negative cycles.

Day 48:
- [x] Added unit tests for Bellman-Ford.(& fixed a bug! :D)  
- [x] Started learning about the min-cut/max-flow problems. I was ecstatic that they are equivalent! It is amazing to see it.

Day 49:
- [x] Finished learning about the Ford-Fulkerson. 
- [x]  Started Least Significant Digit radix sort.

Day 50:
- [x] Unit tests for String sorts
- [x] Finished LSD radix sort.

Day 51:
- [x] Coded and unit tested MSD radix sort
- [x] Coded and unit tested three way radix sort.

Day 52:
- [x] Learned R-Way Tries 
- [x] Ternary Search Tries.
- [x] Started coding them.

Day 53:
- [X] R-Way tries
- [X] Ternary search trees.
- [X] Unit tests for symbol tables

Day 54:
- [x] Learned about Knuth-Morris-Pratt
- [x] Learned about Boyer-Moore
- [x] Created DFA on paper to understand it.

Day 55:
- [X] Coded Knuth-Morris-Pratt
- [X] Started Boyer-Moore

Day 56: 
- [x] Finished Boyer-Moore
- [x] Updated logbook.

Day 57:
- [x] Boyer-Moore Tests
- [x] KMP and Boyer-Moore benchmarking start

 Day 58:
- [x] Boyer moore UT finished.
- [x] Benchmarks: (I expected find to win as it is implemented in CPython)
BoyerMoore took 0.655519962310791 secs. Find took 0.006417036056518555 secs. KnuthMP took 0.8751339912414551 secs

Day 59:
- [x] Learned about Rabin-Karp hashtag substring search, and run time length encoding. 

Day 60:
- [x] Started BinaryStreams API and Unit tests. This gives way to Data Compression algorithms.

Day 61:
- [x] Learned about Huffman Compression with Shannon-Fano codes (which has a 4.7 bits/char rating),
- [x] Learned about Lempel-Ziv-Welch compression. (which has a 3.32 bits/char rating)

Day 62:
- [x] BREAK

Day 63:
- [x] Worked on learning Linear Programming, with Brewers problem for solving maximization of variables with constraints.

Day 64:
- [x] Started implementing Simplex algorithm. Simplex let's you maximize profits, given a set of constraints.

Day 65:
- [x] Finished simplex.

Day 66:
- [x] Tensorflow start. Learning from Google's crash course of machine learning.
- [x] Learned about linear regressions 
- [x] Stochastic gradient descent

Day 67:
- [x] First Tensorflow program (linear)

Day 68:
- [x] Mock interviews with Interviewing.io (stack problam and preorder traversal)

Day 69:
- [x] Dynamic programming lessons. Reviewing past problems.

Day 70:
- [x] Learned about Generalization, Validation, Training and Test sets for machine learning.

Day 71:
- [x] Coding exercise on Jupyter notebook on Model Validation. 

Day 72:
- [x] Started to learn how to do syntax highlighting for @code working on porting @todotxt 

Day 73:
- [x] BREAK. Finals week.

Day 74:
- [x] Finished Syntax highliting, got into a roadblock but learned what I wanted to learn.

Day 75:
- [x] Worked on FordFulkerson algorithm for Max-Flow and Capacity (Max Flow, Min Cut)

Day 76:
- [x]  Worked on a flow network implementation for implementing the FordFulkerson algorithm.

Day 77:
- [x] Experimented a bit with CORS headers, kept working on the Ford-Fulkerson Algorithm

Day 78:     
- [x] Micro service deployment architectures, 
- [x] I'm trying to enable CORS between all of them. Hell raised. I know CORS is for security, but whoa..

Day 79:
- [x] Worked on a phong shader & a yaw and pitch camera based on Euler angles using quaternions. (private repo)

Day 80:
- [x] Cleaned up project, pausing for internship.

Day 81:
- [x] Renamed tests to be auto-discoverable, adding more tests to the suite, removing print statements from all the sides so we get a clean test pass.
- [ ] Starting astar algorithm,
- [ ] Changing email to correct one 



Things to implement when finished researching regular algorithms (due to the time they take)
 - [ ] Ford Fulkerson
 - [ ] Graham scan
 - [ ] Kd-trees

TODO after all algorithms:
- [ ] Determine complexities
- [ ] Add docstrings to tests
- [ ] Burrows−Wheeler transform.

# Links
## I will fill this as soon as I finish
 