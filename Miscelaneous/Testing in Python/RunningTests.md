# How to run unit tests

## No packages declared

```
new_project
├── antigravity.py
└── test_antigravity.py
```

> Tests can be run like this: 

```
$ cd new_project
$ python -m unittest test_antigravity
```

> Or simply:
``` 
$ cd new_project
$ python -m unittest
```

## Using src and test
```
new_project
├── src
│   ├── __init__.py         # make it a package
│   └── antigravity.py
└── test
    ├── __init__.py         # also make test a package
    └── test_antigravity.py
```

> Import the classes/functions like this: 
``` 
# import the package
import src

# import the src module
from src import antigravity

# or an object inside the src module
from src.antigravity import my_object
```

#### Running a single test module
> To run a single test module, in this case ```test_antigravity.py```:
```
$ cd new_project
$ python -m unittest test.test_antigravity
```
#### Running a single test case or test method:
Also you can run a single ```TestCase``` or a single test method:
``` 
$ python -m unittest test.test_antigravity.GravityTestCase
$ python -m unittest test.test_antigravity.GravityTestCase.test_method
```
#### Running all tests:
> You can also use ```test discovery``` which will discover and run all the tests for you, they must be modules or packages named ```test*.py``` (can be changed with the -p, --pattern flag):
``` 
$ cd new_project
$ python -m unittest discover
```
> This will run all the test*.py modules inside the test package.