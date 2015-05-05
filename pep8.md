###Python PEP8编码规范


*  缩进：4个空格，不使用Tap，更不能混合使用Tap和空格。
*  每行最大长度79，（大于79，建议使用反斜杠"\"换行；最好在括号中的逗号","后换行）
*  类和top-level函数定义之间空两行；类中的方法定义之间空一行；函数内逻辑无关段落之间空一行；其他地方尽量不要再空行。

*  模块内容的顺序：模块说明和docstring—import—globals&constants—其他定义。其中import部分，又按标准、三方和自己编写顺序依次排放，之间空一行。
*  不要在一句import中多个库，比如import os, sys不推荐（更不推荐 import *）。
*  如果采用from XX import XX引用库，可以省略‘module.’，都是可能出现命名冲突，这时就要采用import XX。

*  各种右括号前不要加空格。
*  逗号、冒号、分号前不要加空格。
*  函数的左括号前不要加空格。如Func(1)。
*  序列的左括号前不要加空格。如list[2]。
*  操作符左右各加一个空格，不要为了对齐增加空格。
*  函数默认参数使用的赋值符左右省略空格。
*  不要将多句语句写在同一行，尽管使用‘；’允许。
*  if/for/while语句中，即使执行语句只有一句，也必须另起一行。

*  块注释，在一段代码前增加的注释。在‘#’后加一空格。段落之间以只有‘#’的行间隔。比如：
```
# Description : Module config.
# 
# Input : None
#
# Output : None
```
*  行注释，在一句代码后加注释。比如：x = x + 1  # Increment x 但是这种方式尽量少使用(如果要用，请在"#"前加2个空格，后面加一个空格)。

*  为所有的共有模块、函数、类、方法写docstrings；非共有的没有必要，但是可以写注释（在def的下一行）。
*  如果docstring要换行，参考如下例子,详见PEP 257
```
"""Return a foobang
Optional plotz says to frobnicate the bizbaz first.
"""
```

*  尽量单独使用小写字母‘l’，大写字母‘O’等容易混淆的字母。
*  模块命名尽量短小，使用全部小写的方式，可以使用下划线。
*  包命名尽量短小，使用全部小写的方式，不可以使用下划线。
*  类的命名使用CapWords的方式，模块内部使用的类采用_CapWords的方式。
*  异常命名使用CapWords+Error后缀的方式。
*  全局变量尽量只在模块内有效，类似C语言中的static。实现方法有两种，一是__all__机制;二是前缀一个下划线。
*  函数命名使用全部小写的方式，可以使用下划线。
*  常量命名使用全部大写的方式，可以使用下划线。
*  类的属性（方法和变量）命名使用全部小写的方式，可以使用下划线。
*  类的属性有3种作用域public、non-public和subclass API，可以理解成C++中的public、private、protected，non-public属性前，前缀一条下划线。
*  类的属性若与关键字名字冲突，后缀一下划线，尽量不要使用缩略等其他方式。
*  为避免与子类属性命名冲突，在类的一些属性前，前缀两条下划线。比如：类Foo中声明__a,访问时，只能通过Foo._Foo__a，避免歧义。如果子类也叫Foo，那就无能为力了。
*  类的方法第一个参数必须是self，而静态方法第一个参数必须是cls。

*  编码中考虑到其他python实现的效率等问题，比如运算符‘+’在CPython（Python）中效率很高，都是Jython中却非常低，所以应该采用.join()的方式。
*  尽可能使用‘is’‘is not’取代‘==’，比如if x is not None 要优于if x。
*  使用基于类的异常，每个模块或包都有自己的异常类，此异常类继承自Exception。
*  异常中不要使用裸露的except，except后跟具体的exceptions。
*  异常中try的代码尽可能少。比如：
```
try:
value = collection[key]
except KeyError:
return key_not_found(key)
else:
return handle_value(value)
```
要优于
```
try:
# Too broad!
return handle_value(collection[key])
except KeyError:
# Will also catch KeyError raised by handle_value()
return key_not_found(key)
```
*  使用startswith() and endswith()代替切片进行序列前缀或后缀的检查。比如：
```
Yes:  if foo.startswith('bar'):优于
No:  if foo[:3] == 'bar':
```
*  使用isinstance()比较对象的类型。比如
```
Yes:  if isinstance(obj, int): 优于
No:  if type(obj) is type(1):
```
*  判断序列空或不空，有如下规则
```
Yes:  if not seq:
if seq:
```
优于
```
No:  if len(seq)
if not len(seq)
```
*  字符串不要以空格收尾。
*  二进制数据判断使用 if boolvalue的方式。
*  尽可能的使用列表解析代或map替for循环