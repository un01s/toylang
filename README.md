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

## step3: parse multiple lines

Restructure the code with ```class```, and add the function to handle multiple lines of code.

```
$ cat code.txt
1 2 +
3 4 +
$ python3 interp.py code.txt
3
7
```

## step4: handle variables

```
$ cat code.txt 
x = 1 2 +
y = x 3 +
$ python3 interp.py code.txt
{'x': 3, 'y': 6}
```

## setp5: add while loop

```
$ cat code2.txt 
n = 5
r = 1
while n 1 >=
  r = r n *
  n = n 1 - 
end
$ python3 interp.py code2.txt
{'n': 0, 'r': 120}
```

The code is to calculate the factorial of a number, like ```5!``` in the example. 

To handle while loop, the arithmetic operations like ```*```, and ```-``` are added. Also the comparison like ```>=``` is added too. To deal with the loop, for ```while```, we have to look forward for its ```end```. And for ```end```, look backward for its ```while```. So the program counter ```pc``` in the code.
 
## notes

The code written by Dr Laurence Tratt is pythonic. The steps are incremental and easy to follow. 
