from django.template import Library
register = Library()


@register.filter(name='add_attr')
def add_attr(field, css):
    attrs = {}
    definition = css.split(',')

    for d in definition:
        if ':' not in d:
            attrs[d] = True
            # attrs['class'] = d
        else:
            key, val = d.split(':')
            attrs[key] = val

    return field.as_widget(attrs=attrs)


@register.filter(name='phone_number')
def phone_number(number):
    size = len(number)
    if size == 8:
        first = number[0:4]
        second = number[4:8]
        return first + '-' + second
    if size == 9:
        first = number[0:5]
        second = number[5:9]
        return first + '-' + second
    if size == 10:
        first = number[0:2]
        second = number[2:6]
        third = number[6:10]
        return '(' + first + ')' + ' ' + second + '-' + third
    if size == 11:
        first = number[0:2]
        second = number[2:7]
        third = number[7:11]
        return '(' + first + ')' + ' ' + second + '-' + third
