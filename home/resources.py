from import_export import resources

from home.models import Budget_Approval


class PersonResource(resources.ModelResource):
    class Meta:
        model = Budget_Approval