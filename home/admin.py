from django.contrib import admin

from home.models import Person_name, Budget_Approval, Reimbursement_form, Purchase_order

admin.site.register(Person_name)
admin.site.register(Budget_Approval)
admin.site.register(Reimbursement_form)
admin.site.register(Purchase_order)

