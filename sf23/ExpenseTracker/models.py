
from django.db import models

# Choices for giving dropdown options in form


CATEGORY_CHOICES = (
    ("food", "Food"),
    ("transportation", "Transportation"),
    ("clothing", "Clothing"),
    ("health", "Health"),
    ("electronics", "Electronics"),
    ("recreational", "Recreational"),
    ("utility", "Utility"),
    ("miscellaneous", "Miscellaneous"),
)
EXPENSE_TYPE_CHOICES = (
    ("personal use", "Personal Use"),
    ("bill sharing", "Bill Sharing"),
    ("family expense", "Family Expense"),
    ("lend", "Lend"),
    ("miscellaneous", "Miscellaneous"),
)

PAYMENT_CHOICES = (
    ("cash", "Cash"),
    ("credit card", "Credit Card"),
    ("online payment", "Online Payment"),
)



class ExpenseRecords(models.Model):
    """
    Expense model
    return: Expense object
    arguments:
    date: date of expense
    category: category of expense
    amount: amount of expense
    expense_type: type of expense
    payment_method: payment method of expense
    """

    amount = models.FloatField()
    date = models.DateField()
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    expense_type = models.CharField(max_length=20, choices=EXPENSE_TYPE_CHOICES)
    mode_of_payment = models.CharField(max_length=20, choices=PAYMENT_CHOICES)
    remarks = models.CharField(null=True, blank=True, max_length=255)

    def __str__(self):
        return f"{self.remarks}, Rs. {self.amount}"