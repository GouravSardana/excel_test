from django.shortcuts import render
from django.views.generic import TemplateView, ListView



class Demo(TemplateView):
    template_name = 'base.html'
    # def post(self, request, *args, **kwargs):
    #     count=2
    #     for i in range(1, count+1):
    #         n = self.request.POST.get('n_'+ str(i))
    #         p = self.request.POST.get('p_' + str(i))
    #         form = Person(n=n, p=p)  # = wala model ka naam
    #         print(form)
    #         form.save()
    #
    #     return render(request, 'index.html')