def check_type(fn):
     def comprobar(*args):
         for arg in args:
             if not isinstance(arg, int):
                 raise TypeError("%s no es  de tipo int " %(args))
         return fn(*args)
     return comprobar

@check_type
def sigma(*args):
	return sum([i for i in args])
