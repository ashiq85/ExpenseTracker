from django.db import models
from django.utils import timezone
from django.core.validators import MinValueValidator
from django.core.exceptions import ValidationError
from decimal import Decimal

def validate_not_in_future(value):
    if value > timezone.now().date():
        raise ValidationError('Expense date cannot be in the future.')

class Expense(models.Model):
    CATEGORY_CHOICES = [
        ('food', 'Food'),
        ('transport', 'Transport'),
        ('shopping', 'Shopping'),
        ('bills', 'Bills'),
        ('entertainment', 'Entertainment'),
        ('other', 'Other'),
    ]

    title = models.CharField(max_length=200)
    amount = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(Decimal('0.01'))])
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='other')
    date = models.DateField(default=timezone.now, validators=[validate_not_in_future])
    note = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.title} - {self.amount}"
