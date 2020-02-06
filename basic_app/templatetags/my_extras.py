from django import template

register = template.Library()


@register.filter(name='cut')
def cut(value, arg):
    """
    This cuts out all values of "arg" from the string!
    :param value: string
    :param arg: new arg
    :return: new string
    """
    return value.replace(arg, '')

# register.filter("cut", cut)
