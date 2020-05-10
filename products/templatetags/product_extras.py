from django import template

register = template.Library()

#filtro que no tiene Django
@register.filter()
def price_format(value):
    return '${0:.2f}'.format(value)

@register.filter()
def quantity_product_format(quantity=1):
    if quantity>1:
        return '{} {}'.format(quantity, 'productos')
    else:
        return '{} {}'.format(quantity, 'producto')


@register.filter()
def quantity_add_format(quantity=1):
    return  '{} {}'.format(
        quantity_product_format(quantity), 
        'agregados' if quantity > 1 else 'agregado'
    )


