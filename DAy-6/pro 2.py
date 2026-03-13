Python 3.14.3 (tags/v3.14.3:323c59a, Feb  3 2026, 16:04:56) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.

==================================== RESTART: Shell ====================================
data={}
data['sai']=False
data
{'sai': False}
data['sharan']=False
data
{'sai': False, 'sharan': False}

======== RESTART: C:/Users/SHARAN/OneDrive/Desktop/PFS-course work/DAy-6/pro.py ========
enter no of students:5
enter the name:sai
enter the name:nandu
enter the name:rahul
enter the name:shiva
enter the name:ramu
{'sai': False, 'nandu': False, 'rahul': False, 'shiva': False, 'ramu': False}

======== RESTART: C:/Users/SHARAN/OneDrive/Desktop/PFS-course work/DAy-6/pro.py ========
enter no of students:5
enter the name:sai
enter the name:ramu
enter the name:rahul
enter the name:bunny
enter the name:sharan
sai
Enter the sai status (0-absent,1-present):1
ramu
Enter the ramu status (0-absent,1-present):2
rahul
Enter the rahul status (0-absent,1-present):3
bunny
Enter the bunny status (0-absent,1-present):4
sharan
Enter the sharan status (0-absent,1-present):5
Traceback (most recent call last):
  File "C:/Users/SHARAN/OneDrive/Desktop/PFS-course work/DAy-6/pro.py", line 51, in <module>
    priint(data)
NameError: name 'priint' is not defined. Did you mean: 'print'?

======== RESTART: C:/Users/SHARAN/OneDrive/Desktop/PFS-course work/DAy-6/pro.py ========
enter no of students:4
enter the name:sai
enter the name:sharan
enter the name:rahul
enter the name:bunny
sai
Enter the sai status (0-absent,1-present):0
sharan
Enter the sharan status (0-absent,1-present):1
rahul
Enter the rahul status (0-absent,1-present):2
bunny
Enter the bunny status (0-absent,1-present):0
Traceback (most recent call last):
  File "C:/Users/SHARAN/OneDrive/Desktop/PFS-course work/DAy-6/pro.py", line 51, in <module>
    priint(data)
NameError: name 'priint' is not defined. Did you mean: 'print'?

======== RESTART: C:/Users/SHARAN/OneDrive/Desktop/PFS-course work/DAy-6/pro.py ========
enter no of students:4
enter the name:sai
enter the name:sharan
enter the name:ramua
enter the name:rahul
sai
Enter the sai status (0-absent,1-present):1
sharan
Enter the sharan status (0-absent,1-present):
======== RESTART: C:/Users/SHARAN/OneDrive/Desktop/PFS-course work/DAy-6/pro.py ========
enter no of students:4
enter the name:sai
enter the name:ramu
enter the name:venu
enter the name:teja
sai
Enter the sai status (0-absent,1-present):1
ramu
Enter the ramu status (0-absent,1-present):0
venu
Enter the venu status (0-absent,1-present):1
teja
Enter the teja status (0-absent,1-present):0
{'sai': False, 'ramu': False, 'venu': False, 'teja': False}

======== RESTART: C:/Users/SHARAN/OneDrive/Desktop/PFS-course work/DAy-6/pro.py ========
enter no of students:5
enter the name:venu
enter the name:teja
enter the name:charam
enter the name:saran
enter the name:ramesh
venu
Enter the venu status (0-absent,1-present):1
teja
Enter the teja status (0-absent,1-present):1
charam
Enter the charam status (0-absent,1-present):0
saran
Enter the saran status (0-absent,1-present):0
ramesh
Enter the ramesh status (0-absent,1-present):1
{'venu': True, 'teja': True, 'charam': False, 'saran': False, 'ramesh': True}

======== RESTART: C:/Users/SHARAN/OneDrive/Desktop/PFS-course work/DAy-6/pro.py ========
enter no of students:5
enter the name:ere
enter the name:dfds
enter the name:fgs
enter the name:egefes
enter the name:fef
ere
Enter the ere status (0-absent,1-present):00
dfds
Enter the dfds status (0-absent,1-present):1
fgs
Enter the fgs status (0-absent,1-present):0
egefes
Enter the egefes status (0-absent,1-present):0
fef
Enter the fef status (0-absent,1-present):1
{'ere': False, 'dfds': True, 'fgs': False, 'egefes': False, 'fef': True}

s = 'python'
s
'python'
s = "python"
s
'python'
s = '''python'''
s
'python'
s+' lang'
'python lang'
s*10
'pythonpythonpythonpythonpythonpythonpythonpythonpythonpython'
'-'*20
'--------------------'
'46848'*20
'4684846848468484684846848468484684846848468484684846848468484684846848468484684846848468484684846848'
s[4]
'o'
s[0]
'p'
s[-3]
'h'
s[-1]
'n'
s[-2]
'o'
name = 'sai sharan venu shiva teja rahul rao'
names
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    names
NameError: name 'names' is not defined. Did you mean: 'name'?
name
'sai sharan venu shiva teja rahul rao'
names[0]
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    names[0]
NameError: name 'names' is not defined. Did you mean: 'name'?
name[0]
's'
name[-5]
'l'
name[:8]
'sai shar'
name[10:]
' venu shiva teja rahul rao'
name[10:16]
' venu '
name[9:16]
'n venu '
name[12:19]
'enu shi'
name
'sai sharan venu shiva teja rahul rao'
name[::-1]
'oar luhar ajet avihs unev narahs ias'
nmae[-5::]
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    nmae[-5::]
NameError: name 'nmae' is not defined
name[-5::]
'l rao'
name[-12:-16]
''
name[-12:-6]
'ja rah'
name[-1:-3]
''
name[-3:-8]
''
name[-5:-8:-11]
'l'
name
'sai sharan venu shiva teja rahul rao'
name[]
SyntaxError: invalid syntax
name[::2]
'sisaa eusiatj au a'
name
'sai sharan venu shiva teja rahul rao'
'sai'in name
True
'ramu'not in name
True
name
'sai sharan venu shiva teja rahul rao'
len(name)
36
>>> max(name)
'v'
>>> min(name)
' '
>>> chr(89)
'Y'
>>> chr(65)
'A'
>>> chr(90)
'Z'
>>> chr(91)
'['
>>> ord('a')
97
>>> ord('z')
122
>>> name
'sai sharan venu shiva teja rahul rao'
>>> sorted(name)
[' ', ' ', ' ', ' ', ' ', ' ', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'e', 'e', 'h', 'h', 'h', 'i', 'i', 'j', 'l', 'n', 'n', 'o', 'r', 'r', 'r', 's', 's', 's', 't', 'u', 'u', 'v', 'v']
>>> name
'sai sharan venu shiva teja rahul rao'
>>> name.replace('sai','ramu')
'ramu sharan venu shiva teja rahul rao'
>>> name
'sai sharan venu shiva teja rahul rao'
>>> name.split()
['sai', 'sharan', 'venu', 'shiva', 'teja', 'rahul', 'rao']
>>> s='python programming'
>>> s.center(30,'-')
'------python programming------'
>>> s.center(50,'-')
'----------------python programming----------------'
>>> s.ljust(30,'-')
'python programming------------'
>>> s.rjusr(30.'-')
SyntaxError: invalid syntax. Perhaps you forgot a comma?
>>> s.rjust(30,'-')
'------------python programming'
>>> s='       python      '
>>> s
'       python      '
>>> s.strip()
'python'
