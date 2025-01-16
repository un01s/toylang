# toy programming language in Python

this is the notes after watching [creating your own programming language](https://www.youtube.com/watch?v=Q2UDHY5as90) by Dr Laurence Tratt. Here is [his blog](https://tratt.net/laurie/blog/).

## step1: setup

Just show something.

```
$ cat code.txt
1 2 +
$ python3 interp.py code.txt 
1 2 +
```

The code uses [reverse polish notation](https://en.wikipedia.org/wiki/Reverse_Polish_notation) instead of usual mathematic notation. Then it will be easier for later [stack machine](https://en.wikipedia.org/wiki/Stack_machine).

## step2: parsing with split

As said before, the code adopts the reverse polish notation. Here parse the line with ```split()``` function. If it is digits, push it to the stack. If it is the plus sign, pop the stack twice and push the result back.

```
$ cat code.txt
1 2 +
$ python3 interp.py code.txt
3
```

