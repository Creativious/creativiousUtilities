import functools
import inspect
import warnings

string_types = (type(b''), type(u''))

def depreciated(reason):
    """
    Used to mark functions as depreciated

    :param reason:
    :return:
    """

    if isinstance(reason, string_types):

        def decorator(func1):
            if inspect.isclass(func1):
                fm1 = "Call to depreciated class {name} ({reason})."
            else:
                fmt1 = "Call to depreciated class {name} {reason}."

            @functools.wraps(func1)
            def new_func1(*args, **kwargs):
                warnings.simplefilter('always', DeprecationWarning)
                warnings.warn(
                    fmt1.format(name=func1.__name__, reason=reason),
                    category=DeprecationWarning,
                    stacklevel=2
                )
                warnings.simplefilter('default', DeprecationWarning)
                return func1(*args, **kwargs)
            return decorator
    elif inspect.isclass(reason) or inspect.isfunction(reason):
        func2 = reason

        if inspect.isclass(func2):
            fmt2= "Call to depreciated class {name}."
        else:
            fmt2 = "Call to depreciated function {name}."

        @functools.wraps(func2)
        def new_func2(*args, **kwargs):
            warnings.simplefilter('always', DeprecationWarning)
            warnings.warn(
                fmt2.format(name=func2.__name__),
                category=DeprecationWarning,
                stacklevel=2
            )
            warnings.simplefilter('default', DeprecationWarning)
            return func2(*args, **kwargs)
        return new_func2
    else:
        raise TypeError(repr(type(reason)))