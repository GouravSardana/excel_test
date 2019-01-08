from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from home.models import Person_name, Budget_Approval, Reimbursement_form, Purchase_order, TemporaryBudgetApproval, \
    Temporary_Reimbursement_form

admin.site.register(Person_name)
admin.site.register(Reimbursement_form)
admin.site.register(Purchase_order)
admin.site.register(TemporaryBudgetApproval)
admin.site.register(Temporary_Reimbursement_form)


@admin.register(Budget_Approval)
class PersonAdmin(ImportExportModelAdmin):
    pass

