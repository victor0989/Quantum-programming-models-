# testing functions in the shell with print()

>>> def func(x):
...     return x + 1
... def test_answer():
  File "<stdin>", line 3
    def test_answer():
    ^
SyntaxError: invalid syntax
>>> def func(x):
...     return x + 1
... 
>>> def test_answer():
...     assert func(3) == 5
... 
>>> print(func(x))
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'x' is not defined
>>> print(func)
<function func at 0x7f4946552ee0>
>>> print(test_answer)
<function test_answer at 0x7f4946552f70>
