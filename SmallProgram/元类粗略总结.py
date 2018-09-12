# ________元类____________


# 首先我们可以通过type去创造一个类
# def __init__(cls, what, bases=None, dict=None):  # known special case of type.__init__
#     """
#     type(object_or_name, bases, dict)
#     type(object) -> the object's type   这个是显示对象的类型，也是最常用的
#     type(name, bases, dict) -> a new type   我们用的是这一种
#     # (copied from class doc)
#     """
#     pass
# 这个就是type类的__init__方法
base_creator = type('Base_1', (object,), {'func1': lambda x: print(10)})
base_1 = base_creator()
base_1.func1()
print(type(base_1))  # <class '__main__.Base_1'>
print('----------------------------------------------------------------------------------------------------------')


# type就是所有类默认的元类，那base_creator这个对象，是什么呢？
# 其实就是我们平时说的类名，在Python里所有的所有都是对象（一切皆对象）
# 那接下来用平时常见的类创建方法

class A:
    pass


a = A()
print(a)  # <__main__.A object at 0x0000024DA567C9E8>  一个class A的对象
print(type(a))  # <class '__main__.A'>  打印对象a的类型
print(type(A))  # <class 'type'>  打印class A的类型

# 这里就要引入type这个元类（metaclass），就我现在的资料翻查，
# 我发现所有的元类都是以type或者继承了type的类（今年长城略疯狂，哎。。。）
# a metaclass is a class whose instances are classes 这是wiki上的解释也就是说元类的实例也是类，
# 往往资料上的都会有一切皆对象这句话，其实我感觉迷惑的地方就在这里。继续看wiki的解释
# Just as an ordinary class defines the behavior of certain objects
# 一个普通类定义对象的行为，这里可以把类理解成模板
# a metaclass defines the behavior of certain classes and their instances
# 一个元类定义的是某些类和这些类所产生的实例的行为，请心里默念三遍，然后我们仔细看一下这句话
# 之前说过普通类可以理解成模板，定义实例的行为（可以做什么，可以存什么），
# 那元类定义是类，定义类里有什么，也就是创建模板，base_creator = type('Base', (object,), {'func1': lambda x: print(10)})
# type作为元类就可以定义‘Base’这个类里面有些什么，继承什么，名字叫什么
# 这里就是重点，乍看上去没什么元类和普通类没啥区别啊，最后都是去控制实例行为，只不过他能控制类的行为，但是类又不是直接用
# 之前我们看到行为这个词，可能有点不太理解，这里就可以给出解释，
# 行为，实例的行为可能是调用方法什么的，但是类的行为只有一个，创建类，这样是不是就好理解了，我们继续看wiki的解释
# Not all object-oriented programming languages support metaclasses 不是所有面向对象的语言都支持元类，这个就是告诉我们，
# 这个是个特有的概念，别去混淆c++什么的
# 综上所述，个人感觉关键问题就在行为这个词那我们来分析一下类的行为和实例的行为怎么解释
print('----------------------------------------------------------------------------------------------------------')


# 这里要先说一下Python类的特殊方法
# 1、__init__我们常说这个是构造方法，其实是错的，他是一个对于实例的配置方法
# 2、__new__这个才是创建实例的方法
# 先说这两点，我们来证实一下
class Base:
    def __init__(self):
        print('Base __init__')
        self.name = 'aaa'
        print(self)

    def __call__(self, *args, **kwargs):
        print('Base __call__')

    def __new__(cls, *args, **kwargs):
        print('Base __new__')
        print(cls)
        print(type(cls))
        instance = object.__new__(cls)
        print(instance)
        print(type(instance))
        return instance

    def show(self):
        print(self.name)


base = Base()
print('instance is created')
print(base)
base.show()  # aaa

# Base __new__
# 1、执行__new__
# <class '__main__.Base'>
# 2、__new__的第一个参数cls里面存的是一个类，我们再来看一下cls是什么类型
# <class 'type'>
# 3、他是一个type类型********我们先MARK一下*********
# <__main__.Base object at 0x000001640822FA58>
# <class '__main__.Base'>
# 4、通过object的new方法来创建一个cls的实例，也就是一个Base的实例，然后返回这个实例
# ------接下来就是见证奇迹的时刻---------
# Base __init__
# 居然直接跳到了__init__这个是不是感觉有点不太对，他怎么跳过去的？难道是解释器自动的？带着疑问我们先看一下结果
# <__main__.Base object at 0x000001640822FA58>
# instance is created
# <__main__.Base object at 0x000001640822FA58>
# 没问题，创建的实例就是__new__创建的，证明OK，这里就已经根据类来定义了实例的行为，什么行为？
# base.show()方法就是行为，也就是这个实例可以做什么动作，用什么方法
# 那接下来就有另外一个问题了，他到底是怎么从__new__跳到__init__的呢？
# 大家看步骤3，我们mark的cls的类型，原因就在这里。接下来我们来试验一下元类的行为到底是什么？

print('-------------------------------------------------------------------------------------------------------')


# 1、type就是python class默认的元类，我们可以通过继承type来实现自定义的元类，之后的步骤有点复杂。。。大家跟紧了
# 2、我们之前已经证明了，一个类创建对象的过程，类的对象是一个实例，而元类的对象还是一个类，但是创建方法是差不多的
# 3、遗漏问题：__new__是怎么跳到__init__的
# 接下来我就写一个自定义的type然后根据之前的步骤完善它的__new__,__init__,另外再加一个__call__方法
# 我先说一个__call__方法，我直接下一个简单的例子：
class B:
    def __call__(self, *args, **kwargs):
        print('B __call__')


b = B()
b()  # B __call__
# 这个时候call就会被调用，也就是说类B创建了一个实例对象b，当b使用()运算符的时候，类B的__call__方法被调用
# 那我们之前写的base = Base()是不是就是调用了创建类Base的元类的__call__方法呢？也就是type的__call__方法？
# 看我下面的例子我们来一起验证一下
print('-------------------------------------------------------------------------------------------------------')


class BaseTypeTest(type):
    def __call__(cls, *args, **kwargs):
        print('BaseTypeTest __call__')


class NewBaseTest(metaclass=BaseTypeTest):  # 设置NewBaseTest的元类为BaseTypeTest，python3.6是这么设置的，2.x可不是
    pass


new_base_test = NewBaseTest()  # BaseTypeTest __call__

# 没问题，BaseTypeTest的__call__方法的确被调用了，这里我就是一个简单的证明，接下去我完善一下，大家再看
print('-------------------------------------------------------------------------------------------------------')


class BaseType(type):
    def __init__(cls, o: object, *args, **kwargs):
        super().__init__(o, args[0], args[1])
        print('BaseType __init__')
        print(cls)
        print(type(cls))
        print(id(cls))
        print(o)
        print(type(o))
        print(args)
        print(kwargs)

    def __call__(cls, *args, **kwargs):
        print('BaseType __call__')
        print(cls)
        print(type(cls))
        print(args)
        print(kwargs)
        instance = cls.__new__(cls, args, kwargs)
        print('instance created')
        cls.__init__(instance)
        print('instance inited')
        print(instance)
        print(type(instance))
        return instance

    def __new__(mcs, *args, **kwargs):
        print('BaseType __new__')
        print(mcs)
        print(type(mcs))
        print(args)
        print(kwargs)
        instance = type.__new__(mcs, args[0], args[1], args[2])
        print(instance)
        print(type(instance))
        print(id(instance))
        return instance


class NewBase(metaclass=BaseType):
    def __init__(self):
        print('NewBase __init__')
        self.name = 'aaa'
        print(self)

    def __call__(self, *args, **kwargs):
        print('NewBase __call__')

    def __new__(cls, *args, **kwargs):
        print('NewBase __new__')
        print(cls)
        print(type(cls))
        instance = object.__new__(cls)
        print(instance)
        print(type(instance))
        return instance

    def show(self):
        print(self.name)


# 这里我还没有创建NewBase的实例，但是已经打印了一些内容我们先看一下
# BaseType __new__
# 1、他先进入了BaseType的__new__  我把代码复制下来方便观看
# def __new__(mcs, *args, **kwargs):
#     print('BaseType __new__')
#     print(mcs)                    <class '__main__.BaseType'>  mcs里面存着一个类（BaseType）
#     print(type(mcs))              <class 'type'> mcs的类型居然是type
#     print(args)                   args比较长我放在了下面，我们可以发现，里面存的其实就是类的一个描述，我们再开始的时候就用过
#     print(kwargs)
#     instance = type.__new__(mcs, args[0], args[1], args[2])
#     print(instance)               <class '__main__.NewBase'>
#     print(type(instance))         <class '__main__.BaseType'>
#     print(id(instance))           2364511257512
#     return instance
# 对比一下base_creator = type('Base_1', (object,), {'func1': lambda x: print(10)})
# args----------------------------------------------------------
# ('NewBase',
# (),
# {'__module__': '__main__', '__qualname__': 'NewBase',
#  '__init__': <function NewBase.__init__ at 0x0000023217B07950>,
#  '__call__': <function NewBase.__call__ at 0x0000023217B14BF8>,
#  '__new__': <function NewBase.__new__ at 0x0000023217B14EA0>,
#  'show': <function NewBase.show at 0x0000023217B14F28>})
# args-----------------------------------------------------------
# base_creator = BaseType('NewBase', (), {'__module__': __main__，......})这不就是创建了一个类么
# 再看生成的instance，类型是一个BaseType的类，里面存着另外一个类NewBase
# 这里我先总结一下，他符合我们之前测试的规律，__new__方法才是创造类的实例方法
# 然后生成了一个BaseType的对象，里面存着NewBase类。
# 那我换一种思路，从结果去猜测触发条件
# 1、BaseType的__new__被调用创建了一个实例存着NewBase
# 2、下方虽然我还没有讲到__init__大家也可以看到，解释器执行了BaseType __init__
# 3、我没有用平时的方法实例化类，但是我却得到了一个执行了obj = BaseType（NewBase）所得到的效果（伪代码）
# 4、既然生成了实例，这个实例在哪里呢？
# 我再次说明一个很重要的概念，元类的实例是一个类
# 其实实例就在这里 class NewBase(metaclass=BaseType) 我们先继续去看BaseType的__init__
# def __init__(cls, o: object, *args, **kwargs):
#     super().__init__(o, args[0], args[1])
#     print('BaseType __init__')
#     print(cls)                           <class '__main__.NewBase'>
#     print(type(cls))                     <class '__main__.BaseType'>
#     print(id(cls))                       2364511257512
#     print(o)                             NewBase
#     print(type(o))                       <class 'str'>
#     print(args)
#     print(kwargs)
# BaseType __init__
# 1、进入了BaseType的__init__
# < class '__main__.NewBase'>
# 2、这里打印了BaseType的__init__方法的第一个参数cls，往往我们的__init__方法一般第一个参数都是self，这里却是cls
# cls里存着<class '__main__.NewBase'>
# 我们再看下这个cls的类型
# < class '__main__.BaseType'>
# 3、这个cls是BaseType类型，再看他的id 2364511257512，和之前__new__创建的id相同
# args-------------------------------------------------------------
# ((), {'__module__': '__main__', '__qualname__': 'NewBase',
# '__init__': < function NewBase.__init__ at 0x000001763C1F7840 >,
# '__call__': < function NewBase.__call__ at 0x000001763C1F77B8 >,
# '__new__': < function NewBase.__new__ at 0x000001763C1F7950 >,
# 'show': < functionNewBase.show at 0x000001763C204BF8 >})
# args-------------------------------------------------------------
# 看到这里明显能发现这就是一个class A:....   a = A()的过程，充分说明我们之前的猜测
# 程序的确执行了obj = BaseType（NewBase）类似的操作，唯一符合的也只有这一句了
# class NewBase(metaclass=BaseType):
# 事实的确如此，这个思路必须要转变，往往其他oop语言都是通过预编译去解释类的定义的，
# 但是python是先通过类的元类去生成一个类然后再去做其他的工作，
# 元类生成类---->类生成对象
# 猜测证实了，但是我们还有另外一个问题没有解决，就是__new__和__init__是怎么连起来的
# 下面我就要开始讲了，
# 如果这里没有看明白请回头重新看一遍，不然下面这些更看不明白了
# 接下来我来生成NewBase的实例

print('----------------------------------------------------------------------')
new_base = NewBase()
print('obj is created')
print(new_base)  # <__main__.NewBase object at 0x000001F179F3EAC8>
new_base.show()  # aaa


# 他打印了一些新内容
# BaseType __call__
# 我把上面代码复制下来
# def __call__(cls, *args, **kwargs):
#     print('BaseType __call__')
#     print(cls)                <class '__main__.NewBase'>
#     print(type(cls))          <class '__main__.BaseType'>
#     print(args)
#     print(kwargs)
#     instance = cls.__new__(cls, args, kwargs)   调用的是NewBase的__new__
#     print('instance created')
#     cls.__init__(instance)                      调用的是NewBase的__init__
#     print('instance inited')
#     print(instance)                <__main__.NewBase object at 0x000002A82C3CEAC8>
#     print(type(instance))          <class '__main__.NewBase'>
#     return instance                返回一个NewBase对象

# 看完打印的内容，我来写个伪代码
# NewBase = BaseType()  ----------->class NewBase(metaclass=BaseType):........
# base = NewBase()   --------------> BaseType的__call__
# 按照我们之前说的NewBase()执行的时候会调用BaseType的__call__方法
# 在BaseType的__call__方法里可以发现他调用了NewBase的__new__方法，然后再调用了BaseNew的__init__方法
# 然后返回了一个NewBase的实例，这样__new__和__init__就联系起来了
# 总结一句，普通类生成实例的时候调用的是这个普通类所规定的元类（默认是type）的__call__方法
# 之前我们说过，元类是用来定义类和类实例的行为，这里我们就可以通过__call__方法去定义


class CType(type):
    def __new__(mcs, *args, **kwargs):
        if args[0] == 'C1':
            return type.__new__(mcs, args[0], args[1], {'new_show': lambda x: print('new C1')})
        else:
            return type.__new__(mcs, args[0], args[1], args[2])


class C1(metaclass=CType):
    def show(self):
        print('C1')


class C2(metaclass=CType):
    def show(self):
        print('C2')


c1 = C1()
c1.new_show()  # new C1
# c1.show() 报错：AttributeError: 'C1' object has no attribute 'show'
c2 = C2()
c2.show()  # C2
# c2.new_show()   报错AttributeError: 'C2' object has no attribute 'new_show'
# 说白了，我就是能够通过元类，动态的给某些类添加属性，方法等等
# 元类号称Python黑魔法，自然能做很多很多事情，我这里只不过是举了一个最简单的例子，之后如果我用到了，还会再记录一下
