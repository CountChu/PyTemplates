# package1
The package1 provides method1().
```
[package1]
  __init_.py
    method1()
```

## Install the package editable
```
[PyTemplates/BuildPackage/package1]
$ pip install -e . 

```

## Install the package
```
[PyTemplates/BuildPackage/package1]
$ pip install .
```

## Check the package
```
$ pip show package1
Name: package1
Version: 0.1
Summary: The package1 displays messages when importing it.
Home-page: http://github.com/countchu
Author: Chu
Author-email: visualge@gmail.com
License: MIT
Location: /home/zhugy2/.local/lib/python3.8/site-packages
Requires: 
Required-by:
```

## Import the package
```
$ python 
>>> import package1
The package1 is loaded.

>>> package1.method1()
It is package1.method1().

>>> help(package1.method1)
Help on function method1 in module package1:

method1()
    It is package1.method1().
```

## Run the package
```
$ python -m package1 -a -b -c                                 
The package1 is loaded.
main() in package1
argv =  ['/home/zhugy2/work/PyTemplates/BuildPackage/package1/package1/__main__.py', '-a', '-b', '-c']
It is package1.method1().
```
