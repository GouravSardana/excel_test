from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView, ListView

from home.models import Budget_Approval, TemporaryBudgetApproval, Temporary_Reimbursement_form, \
    Temporary_Purchase_order, Reimbursement_form


class Demo(TemplateView):
    template_name = 'base.html'
    model=TemporaryBudgetApproval


    def post(self, request, *args, **kwargs):
        c = self.request.POST.get('index')
        name=self.request.POST.get('name')
        form_name = self.request.POST.get('form-name')
        TemporaryBudgetApproval.objects.all().delete()
        Temporary_Reimbursement_form.objects.all().delete()
        Temporary_Purchase_order.objects.all().delete()
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
            # elif form_name=='Reimbursement Form':
            #     date = self.request.POST.get('txtdate1' + str(i))
            #     item = self.request.POST.get('txtitems1' + str(i))
            #     paid = self.request.POST.get('txtpaidto1'+ str(i))
            #     payment = self.request.POST.get('txtpaymethod1' + str(i))
            #     detail = self.request.POST.get('txtdetails1' + str(i))
            #     amount = self.request.POST.get('txtamount1' + str(i))
            #     remark = self.request.POST.get('txtremarks1' + str(i))
            #     subtotal = self.request.POST.get('txtsubtotal1' + str(i))
            #     total = self.request.POST.get('txttotal1' + str(i))
            #     form=Reimbursement_form(date=date, item=item, paid=paid, payment=payment, detail=detail, amount=amount, remark=remark, subtotal=subtotal, total=total)
            #     form1=Temporary_Reimbursement_form(date=date, item=item, paid=paid, payment=payment, detail=detail, amount=amount, remark=remark, subtotal=subtotal, total=total)
            #     print(form)
            #     form.save()
            #     form1.save()
            # else:
            #     return HttpResponse('lol')

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






class Template_re_form(ListView):
    template_name = 'template_re_form'

    def get(self, request, *args, **kwargs):
        budget = Temporary_Reimbursement_form.objects.all()
        print(budget)
        return render(request, 'template_re_form.html', {'f': budget})
