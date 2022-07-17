# package2
The package2 provides module1.method1() and module2.method1().
```
[package2]
  module1.py
    method1()
  module2.py
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
$ pip show package2
Name: package2
Version: 0.1
Summary: The package2 provides module1 and module2.
Home-page: http://github.com/countchu
Author: CountChu
Author-email: visualge@gmail.com
License: MIT
Location: /home/zhugy2/work/PyTemplates/BuildPackage/package2
Requires: 
Required-by:
```

## Import the package
```
$ python 
>>> import package2.module1
The package2.module1 is imported.

>>> package2.module1.method1()
It is method1() of package2.module1()

$ python 
>>> import package2.module2
The package2.module2 is imported.

>>> package2.module2.method1()
It is method1() of package2.module2()
```

## Run the packages
```
$ python -m package2.module1 -a -b -c
main() in module1
argv =  ['/home/zhugy2/work/PyTemplates/BuildPackage/package2/package2/module1.py', '-a', '-b', '-c']

$ python -m package2.module2 -a -b -c
main() in module2
['/home/zhugy2/work/PyTemplates/BuildPackage/package2/package2/module2.py', '-a', '-b', '-c']
```
