from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView, ListView

from home.models import Budget_Approval, TemporaryBudgetApproval


class Demo(TemplateView):
    template_name = 'base.html'
    model=TemporaryBudgetApproval


    def post(self, request, *args, **kwargs):
        c = self.request.POST.get('index')
        name=self.request.POST.get('name')
        TemporaryBudgetApproval.objects.all().delete()
        if c==None or c== '':
            c=1
        else:
            c = int(self.request.POST.get('index'))
        for i in range(1, c + 1):
            purpose = self.request.POST.get('txtpurpose'+ str(i))
            request_date = self.request.POST.get('txtreqdate'+ str(i))
            # request_approval_date = self.request.POST.get('txtreqappdate'+ str(i))
            delivery_due_date = self.request.POST.get('txtdelivplace'+ str(i))
            number = self.request.POST.get('txtnol'+ str(i))
            ventor = self.request.POST.get('txtvendor'+ str(i))
            product = self.request.POST.get('txtproductt'+ str(i))
            spec = self.request.POST.get('txtspecc'+ str(i))
            quantity = self.request.POST.get('txtquant'+ str(i))
            unit_price = self.request.POST.get('txtunitpricee'+ str(i))
            total_price = self.request.POST.get('txttotalprice'+ str(i))
            remark = self.request.POST.get('txtremarkk'+ str(i))
            total = self.request.POST.get('txttotalmoney'+ str(i))
            form=Budget_Approval(name=name, purpose=purpose, request_date=request_date, delivery_due_date=delivery_due_date, number=number, ventor=ventor, product=product, spec=spec, quantity=quantity,unit_price=unit_price, total_price=total_price, remark=remark, total=total)
            form1=TemporaryBudgetApproval(name=name, purpose=purpose, request_date=request_date, delivery_due_date=delivery_due_date, number=number, ventor=ventor, product=product, spec=spec, quantity=quantity,unit_price=unit_price, total_price=total_price, remark=remark, total=total)
            form.save()
            form1.save()
            print(TemporaryBudgetApproval)
        return HttpResponse('Done')


class Temporary(ListView):
    template_name = 'temporary.html'
    model=TemporaryBudgetApproval

    def get(self, request, *args, **kwargs):
        budget = TemporaryBudgetApproval.objects.all()
        print(budget)
        return render(request, 'temporary.html', {'f': budget})


class Temp_excel(ListView):
    template_name = 'temp_excel.html'

    def get(self, request, *args, **kwargs):
        budget = TemporaryBudgetApproval.objects.all()
        print(budget)
        return render(request, 'temp_excel.html', {'f': budget})
