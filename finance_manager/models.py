from django.db import models


class Bank(models.Model):
    name = models.CharField(max_length=256)
    country = models.CharField(max_length=256)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Banks"


class Account(models.Model):
    TYPE_CHOICES = (
        ("current_account", "Current Account"),
        ("saving_account", "Saving Account"),
        ("life_assurance", "Life Assurance"),
    )

    name = models.CharField(max_length=256)
    bank = models.ForeignKey(Bank, on_delete=models.CASCADE)
    account_type = models.CharField(max_length=256, choices=TYPE_CHOICES)

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


class Transaction(models.Model):
    date = models.DateField()
    account = models.ForeignKey("Account", on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    comment = models.TextField()
    category_1 = models.ForeignKey(
        "Category", on_delete=models.CASCADE, related_name="category_1", null=True
    )
    category_2 = models.ForeignKey(
        "Category", on_delete=models.CASCADE, related_name="category_2", null=True
    )
    category_3 = models.ForeignKey(
        "Category", on_delete=models.CASCADE, related_name="category_3", null=True
    )

    def __str__(self):
        return self.account + " - " + str(self.amount)

    class Meta:
        verbose_name_plural = "Transactions"
