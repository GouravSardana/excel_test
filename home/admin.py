from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from home.models import Person_name, Budget_Approval, Reimbursement_form, Purchase_order

admin.site.register(Person_name)
admin.site.register(Reimbursement_form)
admin.site.register(Purchase_order)

@admin.register(Budget_Approval)
class PersonAdmin(ImportExportModelAdmin):
    pass

