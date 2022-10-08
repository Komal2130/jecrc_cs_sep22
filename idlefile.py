Python 3.9.7 (tags/v3.9.7:1016ef3, Aug 30 2021, 20:19:38) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 5+3
8
>>> 8*9
72
>>> 10/3
3.3333333333333335
>>> 10//3
3
>>> 'heelo'*3
'heeloheeloheelo'
>>> hello*3
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    hello*3
NameError: name 'hello' is not defined
>>> 'hello'+ 'world'
'helloworld'
>>> 'hello'+ 'world'
'helloworld'
>>> 'hello '+'world'
'hello world'
>>> 'hello' + ' world'
'hello world'
>>> 'hello'+ ' ' + 'world'
'hello world'
>>> print('hello Python')
hello Python
>>> a='Python'
>>> b=10
>>> id(a)
1816028230576
>>> id(b)
1816025918032
>>> a = 'Machine Learning'
>>> print(a)
Machine Learning
>>> print(b)
10
>>> print(a,b)
Machine Learning 10
>>> import
SyntaxError: invalid syntax
>>> 
>>> 
>>> 
>>> 
>>> 
>>> import keyword
>>> keyword.kwlist()
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    keyword.kwlist()
TypeError: 'list' object is not callable
>>> keyword.kwlist
['False', 'None', 'True', '__peg_parser__', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
>>> len(keyword.kwlist)
36
>>> 1='python'
SyntaxError: cannot assign to literal
>>> a 1 = 200
SyntaxError: invalid syntax
>>> a$ = 'hii'
SyntaxError: invalid syntax
>>> with =200
SyntaxError: invalid syntax
>>> a_1=2000
>>> _='hello'
>>> #a=200
>>> '''asdfghjkasdfghj'''
'asdfghjkasdfghj'
>>> """wertyuiopsdfghjklcvb"""
'wertyuiopsdfghjklcvb'
>>> a=20
>>> b=55
>>> a,b,c = 20, 55, 60
>>> print(a)
20
>>> print(b)
55
>>> print(c)
60
>>> x=y=z=100
>>> print(y)
100
>>> print(x)
100
>>> print(z)
100
>>> a=20
>>> print(a)
20
>>> a+=50
>>> print(a)
70
>>> a = a+ 50
>>> 
>>> 2 *3
6
>>> 2 ** 3
8
>>> 2<5 and 10 < 100
True
>>> 2>5 and 10 < 100
False
>>> 2<5 or 10 < 100
True
>>> 2>5 or 10 < 100
True
>>> a =5
>>> type(a)
<class 'int'>
>>> b = 5.5
>>> type(b)
<class 'float'>
>>> c = 3+2j
>>> type(c)
<class 'complex'>
>>> print(type(c))
<class 'complex'>
>>> a_1= 'silent plz'
>>> 
>>> type(a_1)
<class 'str'>
>>> my_list = [12,'abc', 2.3]
>>> type(my_list)
<class 'list'>
>>> 
>>> 
>>> 
>>> 
>>> a = (12,'gg',5.5)
>>> type(a)
<class 'tuple'>
>>> t = 12, 'gg',5.5
>>> type(t)
<class 'tuple'>
>>> print(t)
(12, 'gg', 5.5)
>>> s = {56,23,12}
>>> type(s)
<class 'set'>
>>> d = {'name' : 'Akshat', 'Age': 22}
>>> type(d)
<class 'dict'>
>>> c = 3+2j
>>> c.real
3.0
>>> c.imag
2.0
>>> bool(45)
True
>>> bool(-10)
True
>>> bool(None)
False
>>> bool(False)
False
>>> bool([])
False
>>> bool(())
False
>>> bool({})
False
>>> bool([56,100,'ab'])
True
>>> 