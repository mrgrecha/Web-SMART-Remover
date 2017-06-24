from django.template import Library

register = Library()

@register.filter
def get_trash_name(value):
    return value[2:].replace('[', '').replace(']', '').replace("'", '')


@register.filter
def cut_redundant(value, symbols):
    for symbol in symbols:
        value = value.replace(symbol, '')
    return value

