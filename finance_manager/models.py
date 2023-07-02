from django.db import models


class Account(models.Model):
    TYPE_CHOICES = (
        ('current_account', 'Current Account'),
        ('saving_account', 'Saving Account'),
        ('life_assurance', 'Life Assurance'),
    )

    name = models.CharField(max_length=50)
    account_type = models.CharField(max_length=50, choices=TYPE_CHOICES)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "Accounts"


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "Categories"


class Subcategory(models.Model):
    name = models.CharField(max_length=50)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "Subcategories"


class Transaction(models.Model):
    date = models.DateField()
    description = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    subcategory = models.ForeignKey(Subcategory, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.description
    
    class Meta:
        verbose_name_plural = "Transactions"