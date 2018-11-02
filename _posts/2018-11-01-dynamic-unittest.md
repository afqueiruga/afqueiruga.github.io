---
layout: post
title: "Generating TestCases in Python behind a library"
date: 2018-08-21
categories: python
---

## Unittest

The quirky part about the unittest framework is that the programmer leaves behind class definitions which are detected and then initialized by the framework. That works fine for the most part, but then how do you loop to populate the framework? What if I'm trying to write a library that **makes** a unittest framework? Well, this is what I'm trying to do --- test generation software.

I found two methods online:

- `setattr`: It's simple and works, but, for making a testing library, the user's view of it is kludgy:  
```python
generated_tests = [
    mytestlib.maketestfunc(),
    mytestlib.maketestfunc(),
]
class UsersTestCase(unittest.TestCase):
    pass
mytestlib.fill_using_setattr(UsersTestCase, generated_tests)
```
- `__metaclass__`: It looks more elegant, but I couldn't get the method to work in Python 3, only in Python 2.
I don't think it could be hidden from the user either.

I played around with a few things after reading everyone's own solutions on the internet, and I think I've come up with an elegant solution.

## Generating TestCases by calling `type()`.

The method is to directly call `type` with three arguments.
The following code blocks in this section make one working example.

The class generator is quite simple:

```python
import unittest as ut
def make_testcase(suite):
    return type('MyTestCase',                   # The class name
                (ut.TestCase,),                 # Inherit only TestCase
                {fn.name : fn for fn in suite}) # Generate a dictionary
```

Simple! Pythonic! The library now has to define a method for generating the
class methods, lest the user finds this all worthless.
The simple toy example here lets the users provide two numbers to test if they multiply to 100:

```python
def MyTestFunctionGenerator(a,b):
    """Generates class methods for a unittest object"""
    def fn(self):
        """Performs one test"""
        self.assertTrue( a*b == 100 )
    fn.name = "test_{0}_{1}".format(a,b)
    return fn
```

The above two methods can be hidden inside of a library, with a `from awesometestinglibrary import *`.
Now the user can just instantiate a list of class methods for everything that
needs to be tested:

```python
test_list = [
    MyTestFunctionGenerator(50,2),
    MyTestFunctionGenerator(5,20),
    MyTestFunctionGenerator(-50,-2),
    #MyTestFunctionGenerator(10,11), # Fails intentionally
]
```

Now the user calls the first library functions gets a unittest type:

```python
MyTestCase = make_testcase(test_list)
```
Note that the return type _must_ be assigned a value, or else the unittest framework won't discover it.
But I think that's the only caveat to the end user!

## My Use Case

How this looks to the end-user in the testing library I'm developing is:
```python
import HydrogeologyTest as hgtest
# import scripts for myUniaxial, myShear, myTerzaghi
suite = [
    hgtest.ExactTestRunner(hgtest.oracles.Uniaxial, myUniaxial),
    hgtest.ExactTestRunner(hgtest.oracles.Shear,    myShear),
    hgtest.ConvergenceTestRunner(hgtest.oracles.Terzaghi, myTerzaghi, 1),
]
TestSuite = hgtest.make_suite(suite)
```
and that's it! The user just has to define Python functions that runs their code the specified test problem and returns results, and `hgtest` takes care of the rest.

Each of those items in the `suite` list are complicated classes that are asynchronously scheduling a batch run of expensive simulations.
Each class compares the user's code against a library of known oracles from analytical solutions, or reference.
There are further hidden options for tuning how thorough the testing needs to be done for a given run. (It can get expensive!)

The function generator from the working example makes class methods with a `self` argument directly. In the implementation which I'm working on now, I start with a list of functions that return `True`/`False` instead of directly call `self.assertTrue`.  There I have another routine that looks like:
```python
def make_testcase_classmethod(simplefunc):
    def fn(self):
         return self.assertTrue(simplefunc())
    return fn
```
which just wraps up a non-TestCase function. That keeps it simple so that unittest-specific code is only in one file, and leaves it extendable to be wrapped by other test frameworks.

## References:

- https://docs.python.org/3/library/functions.html#type
- https://eli.thegreenplace.net/2014/04/02/dynamically-generating-python-test-cases
- https://stackoverflow.com/questions/32899/how-do-you-generate-dynamic-parametrized-unit-tests-in-python
- https://chris-lamb.co.uk/posts/generating-dynamic-python-tests-using-metaclasses
