def upper_attr(future_class_name, future_class_parents, future_class_attr):

    uppercase_attrs = {}
    for name, value in future_class_attr.items():
        if not name.startswith("__"):
            uppercase_attrs[name.upper()] = value
        else:
            uppercase_attrs[name] = value

    return type(future_class_name, future_class_parents, uppercase_attrs)


class UpperAttrMeta(type):

    def __new__(cls, clsname, bases, dct):

        uppercase_attrs = {}
        for name, val in dct.items():
            if not name.startswith("__"):
                uppercase_attrs[name.upper()] = val
            else:
                uppercase_attrs[name] = val

        return super(UpperAttrMeta, cls).__new__(cls, clsname, bases, uppercase_attrs)


class Foo(metaclass=UpperAttrMeta):
    bar = "bip"


print(hasattr(Foo(), "bar"))
print(hasattr(Foo(), "BAR"))

f = Foo()
print(f.BAR)
print(Foo.__mro__)
