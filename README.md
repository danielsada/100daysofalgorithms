# 100daysofalgorithms

Hello! I'm Daniel Sada. I'm trying to do an algorithm or two a day or at least try to solve a problem a day. I'll be alternating between new algorithms and working in problems with those algorithms.

Algorithms so far with complexities:

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


## Quick Find [(Go to Code.)](quickfind.py)

```
Complexity:
Initialize => O(n)
Union      => O(n)
Connected  => O(1)
```

## Quick Union [(Go to Code.)](quickunion.py)

```
Complexity:
Initialize => O(N)
Union      => O(N)
Connected  => O(N)
```

## Weighted Union Find [(Go to Code.)](weightedunionfind.py)

```
Complexity:
Initialize => O(n)
Union      => O(lg N)
Connected  => O(lg N)
```

## PathFlattened and Weighted Union Find [(Go to Code.)](pathflattenedunionfind.py)

```
Complexity:
Complexity:
Initialize => O(n)
Union      
    => O( N + M lg* N) (about linear in practice as lg* of N^65536 is 5)
Connected  
    => O( N + M lg* N) (about linear in practice as lg* of N^65536 is 5)
```
