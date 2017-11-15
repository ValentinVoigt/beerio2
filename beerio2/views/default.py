from pyramid.response import Response
from pyramid.view import view_config

from wtforms_alchemy import ModelForm

from beerio2.models import Product

class ProductForm(ModelForm):
    class Meta:
        model = Product
        only = [
            'name',
            'company',
            'volume_ml',
        ]

@view_config(route_name='home', renderer='beerio2:templates/mytemplate.mako')
def my_view(request):
    form = ProductForm(request.POST)
    result = {'form': form}

    if request.method == 'POST' and form.validate():
        result['data'] = form.data

    return result
