from django.shortcuts import render
from django.views.generic import TemplateView, ListView

from home.models import Budget_Approval


class Demo(TemplateView):
    template_name = 'base.html'


    def post(self, request, *args, **kwargs):

        name = self.request.POST.get('name')
        purpose = self.request.POST.get('txtPurpose')
        request_date = self.request.POST.get('txtreqdate')
        request_approval_date = self.request.POST.get('txtreqappdate')
        delivery_due_date = self.request.POST.get('txtdelivplace')
        no = self.request.POST.get('txtno')
        ventor = self.request.POST.get('txtvendor')
        product = self.request.POST.get('txtproduct')
        spec = self.request.POST.get('txtspec')
        quantity = self.request.POST.get('txtquant')
        unit_price = self.request.POST.get('txtunitprice')
        n = self.request.POST.get('txttotalprice')
        total_price = self.request.POST.get('txtremarks')
        remark = self.request.POST.get('txttotal')
        total = self.request.POST.get('txttotal')
        form=Budget_Approval(name=name, purpose=purpose, request_date=request_date, request_approval_date=request_approval_date, delivery_due_date=delivery_due_date, no=no, ventor=ventor, product=product, spec=spec, quantity=quantity, unit_price=unit_price, n=n, total_price=total_price,remark=remark, total=total)
        form.save()
        print('lol')
        return render(request, 'base.html')
