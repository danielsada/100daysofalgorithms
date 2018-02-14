# 100daysofalgorithms

Hello! I'm Daniel Sada. I'm trying to do an algorithm or two a day or at least try to solve a problem a day. I'll be alternating between new algorithms and working in problems with those algorithms.

Algorithms so far with complexities:

Day 1:
- [x] Quick Find
- [x] Quick Union

Day 2:
- [x] Union Find
- [x] Weighted Union Find
- [x] Flattened Path Union Find

Day 3:
- [x] (partial) (undirected) Graph API

In progress :

- [ ] Depth-first search
- [ ] Breath-first search
- [ ] Connected components
- [ ] Cycle in graphs problem
- [ ] Bipartite Graph Problem
- [ ] 7 Bridges of Konnisburg
- [ ] Hamiltonian Cycle
- [ ] Directed Graphs API
- [ ] Directed Graphs DFS
- [ ] Mark-sweep algorithm
- [ ] Directed Graphs BFS

# Union Find

## Comparison: 
```
Worst Case Scenario
quick-find =>  M N
quick-union => M N
weighted QU => N + M log N
QU + path compression => N + M log N
weighted QU + path compression => N + M lg* N

For M union-find operations in a set of N objects.
```


## Quick Find [(Go to Code.)](algorithms/quickfind.py)

```
Complexity:
Initialize => O(n)
Union      => O(n)
Connected  => O(1)
```

## Quick Union [(Go to Code.)](algorithms/quickunion.py)

```
Complexity:
Initialize => O(N)
Union      => O(N)
Connected  => O(N)
```

## Weighted Union Find [(Go to Code.)](algorithms/weightedunionfind.py)

```
Complexity:
Initialize => O(n)
Union      => O(lg N)
Connected  => O(lg N)
```

## PathFlattened and Weighted Union Find [(Go to Code.)](algorithms/pathflattenedunionfind.py)

```
Complexity:
Complexity:
Initialize => O(n)
Union      
    => O( N + M lg* N) (about linear in practice as lg* of N^65536 is 5)
Connected  
    => O( N + M lg* N) (about linear in practice as lg* of N^65536 is 5)
```
