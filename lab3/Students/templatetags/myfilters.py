from django import template

register = template.Library()

@register.filter
def multiply(value, arg):
    try:
        return value * int(arg)
    except (ValueError, TypeError):
        return ''


@register.filter(name='alternating_case')
def alternating_case(value):
    if not isinstance(value, str):
        return value

    result_chars = []
    for i, char in enumerate(value):
        if i % 2 == 0:
            result_chars.append(char.upper())
        else:
            result_chars.append(char.lower())
    return ''.join(result_chars)
