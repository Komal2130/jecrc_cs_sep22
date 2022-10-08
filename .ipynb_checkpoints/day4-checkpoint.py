Python 3.10.6 (tags/v3.10.6:9c7b4bd, Aug  1 2022, 21:53:49) [MSC v.1932 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
d1={'name':['Akash','Akshat','Sunny'],'Age':[25,20,22],}
type(d1)
<class 'dict'>
len(d1)
2
d1[1]
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    d1[1]
KeyError: 1
d1['name']
['Akash', 'Akshat', 'Sunny']
d1['age']
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    d1['age']
KeyError: 'age'
d1['Age']
[25, 20, 22]
d1
{'name': ['Akash', 'Akshat', 'Sunny'], 'Age': [25, 20, 22]}
d1,keys
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    d1,keys
NameError: name 'keys' is not defined
d1.keys
<built-in method keys of dict object at 0x00000211565B6C40>
d1.keys()
dict_keys(['name', 'Age'])






d1.values()
dict_values([['Akash', 'Akshat', 'Sunny'], [25, 20, 22]])
d1.items()
dict_items([('name', ['Akash', 'Akshat', 'Sunny']), ('Age', [25, 20, 22])])
print d1
SyntaxError: Missing parentheses in call to 'print'. Did you mean print(...)?
print (d1)
{'name': ['Akash', 'Akshat', 'Sunny'], 'Age': [25, 20, 22]}
d1['contact_no.']=[555666777,777888999,555666777]
print (d1)
{'name': ['Akash', 'Akshat', 'Sunny'], 'Age': [25, 20, 22], 'contact_no.': [555666777, 777888999, 555666777]}
d1['name']
['Akash', 'Akshat', 'Sunny']
d1['name'][0]
'Akash'
d1['name'][0][::-1]
'hsakA'
d1[name][0]='meenal'
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    d1[name][0]='meenal'
NameError: name 'name' is not defined
d1['name'][0]='meenal'
d1
{'name': ['meenal', 'Akshat', 'Sunny'], 'Age': [25, 20, 22], 'contact_no.': [555666777, 777888999, 555666777]}
del d1['contact_no.']
d1
{'name': ['meenal', 'Akshat', 'Sunny'], 'Age': [25, 20, 22]}
d1.get(age)
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    d1.get(age)
NameError: name 'age' is not defined
d1.get('Age')
[25, 20, 22]
d1.get('email')
d1
{'name': ['meenal', 'Akshat', 'Sunny'], 'Age': [25, 20, 22]}
a=20
b='ML'
print(a,b)
20 ML
print (a,b,sep='   '0)
SyntaxError: invalid syntax. Perhaps you forgot a comma?
print (a,b,sep='   ')
20   ML
print (a,b,sep='          ')
20          ML
print(a,b,sep='&')
20&ML
print(a)
20
print(b)
ML
print(a,end='\n')
20
print(a,end='######')
20######
