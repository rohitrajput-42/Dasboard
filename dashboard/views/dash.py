from django.shortcuts import render
from django.views import View
from dashboard.models.data import Data
from dashboard.models.category import Category

class Dash(View):

    def get(self, request):

        datas = None
        categories = Category.get_all_categories()
        categoryID = request.GET.get('category')

        if categoryID:
            datas = Data.get_all_datas_by_categoryid(categoryID)
        else:   
            datas = Data.get_all_datas()

        data = {}
        data['datas'] = datas 
        data['categories'] = categories

        return render(request, 'index.html', data)