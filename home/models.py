from django.db import models

class Person_name(models.Model):
    name=models.CharField(max_length=30)
    Team = models.CharField(max_length=50)
    Team_Head = models.CharField(max_length=50)
    CEO = models.CharField(max_length=50)


    def __str__(self):
        return self.name


class Budget_Approval(models.Model):
    name=models.ForeignKey(Person_name, on_delete=models.CASCADE)
    purpose=models.CharField(max_length=50)
    request_date=models.CharField(max_length=50)
    request_approval_date=models.CharField(max_length=50)
    delivery_due_date = models.CharField(max_length=50)
    no = models.CharField(max_length=50)
    ventor = models.CharField(max_length=50)
    product = models.CharField(max_length=50)
    spec = models.CharField(max_length=50)
    quantity = models.CharField(max_length=50)
    unit_price = models.CharField(max_length=50)
    total_price = models.CharField(max_length=50)
    remark = models.CharField(max_length=50)
    total= models.CharField(max_length=50)


    def __str__(self):
        return self.name

class Reimbursement_form(models.Model):
    name=models.ForeignKey(Person_name, on_delete=models.CASCADE)
    date=models.CharField(max_length=50)
    item=models.CharField(max_length=50)
    paid_to= models.CharField(max_length=50)
    payment = models.CharField(max_length=50)
    detail = models.CharField(max_length=50)
    amount = models.CharField(max_length=50)
    remark= models.CharField(max_length=50)
    sub_total = models.CharField(max_length=50)
    total = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Purchase_order(models.Model):
    name = models.ForeignKey(Person_name, on_delete=models.CASCADE)
    purchase_no=models.CharField(max_length=50)
    date_of_purchase=models.CharField(max_length=50)
    attension = models.CharField(max_length=50)
    contact_person = models.CharField(max_length=50)
    tel = models.CharField(max_length=50)
    ventor= models.CharField(max_length=50)
    delivery_date= models.CharField(max_length=50)
    delivery_purchase = models.CharField(max_length=50)
    no = models.CharField(max_length=50)
    product= models.CharField(max_length=50)
    spec= models.CharField(max_length=50)
    unit= models.CharField(max_length=50)
    quantity = models.CharField(max_length=50)
    unit_price = models.CharField(max_length=50)
    sum = models.CharField(max_length=50)
    remark = models.CharField(max_length=50)
    total = models.CharField(max_length=50)

    def __str__(self):
        return self.name





