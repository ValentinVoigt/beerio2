from pyramid.response import Response
from pyramid.view import view_config

from wtforms_alchemy import ModelForm

from beverages.models import Product

class ProductForm(ModelForm):
    class Meta:
        model = Product
        only = [
            'name',
            'company',
            'volume_ml',
        ]

@view_config(route_name='home', renderer='beverages:templates/mytemplate.mako')
def my_view(request):
    form = ProductForm(request.POST)
    result = {'form': form}

    if request.method == 'POST' and form.validate():
        result['data'] = form.data

    return result
