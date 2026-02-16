from django.db import models


class CategoryType(models.TextChoices):
    INCOME = "income", "Income"
    EXPENSE = "expense", "Expense"


class FrequencyType(models.TextChoices):
    DAILY = "daily", "Daily"
    WEEKLY = "weekly", "Weekly"
    BIWEEKLY = "biweekly", "Biweekly"
    MONTHLY = "monthly", "Monthly"
    YEARLY = "yearly", "Yearly"


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(
        max_length=10, choices=CategoryType.choices, default=CategoryType.EXPENSE
    )  # 'income' or 'expense'

    def __str__(self):
        return f"{self.name} ({self.get_type_display()})"


class Transaction(models.Model):
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.TextField(blank=True)

    def __str__(self):
        return f"{self.date} - {self.category.name} - ${self.amount}"


class Budget(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    month = models.DateField()  # Use the first day of the month to represent the month

    def __str__(self):
        return f"{self.category.name} budget for {self.month:%Y-%m}: ${self.amount}"


class RecurringTransaction(models.Model):
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.TextField(blank=True)
    frequency = models.CharField(max_length=10, choices=FrequencyType.choices)

    def __str__(self):
        return f"{self.category.name} - ${self.amount} ({self.get_frequency_display()})"


class Goal(models.Model):
    name = models.CharField(max_length=100)
    target_amount = models.DecimalField(max_digits=10, decimal_places=2)
    current_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    deadline = models.DateField()

    def __str__(self):
        return f"{self.name}: ${self.current_amount}/${self.target_amount} by {self.deadline}"
