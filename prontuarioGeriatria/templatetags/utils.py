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


@register.filter(name='cpf_mask')
def cpf_mask(cpf):
    first = cpf[0:3]
    second = cpf[3:6]
    third = cpf[6:9]
    fourth = cpf[9:11]
    return first + '.' + second + '.' + third + '-' + fourth

@register.filter(name='add_classes')
def add_classes(value, arg):
    css_classes = value.field.widget.attrs.get('class', '')
    if css_classes:
        css_classes = css_classes.split(' ')
    else:
        css_classes = []
    args = arg.split(' ')
    for a in args:
        if a not in css_classes:
            css_classes.append(a)
    return value.as_widget(attrs={'class': ' '.join(css_classes)})

@register.filter(name='add_disabled')
def add_disabled(value):
    return value.as_widget(attrs={'disabled': '', })

@register.filter(name='add_checked_and_class')
def add_disabled_and_class(value, arg):
    css_classes = value.field.widget.attrs.get('class', '')
    if css_classes:
        css_classes = css_classes.split(' ')
    else:
        css_classes = []
    args = arg.split(' ')
    for a in args:
        if a not in css_classes:
            css_classes.append(a)
    return value.as_widget(attrs={'class': ' '.join(css_classes), 'disabled': '', 'checked': ''})

@register.filter(name='add_indeterminate_and_class')
def add_indeterminate_and_class(value, arg):
    css_classes = value.field.widget.attrs.get('class', '')
    if css_classes:
        css_classes = css_classes.split(' ')
    else:
        css_classes = []
    args = arg.split(' ')
    for a in args:
        if a not in css_classes:
            css_classes.append(a)
    return value.as_widget(attrs={'class': ' '.join(css_classes), 'disabled': '', 'readonly': ''})