from datetime import date, timedelta
from decimal import Decimal
from random import choice, randint

from django.core.management.base import BaseCommand

from core.models import Budget, Category, CategoryType, Goal, Transaction


class Command(BaseCommand):
    help = "Seed demo data for local development"

    def handle(self, *args, **options):
        income_categories = ["Salary", "Freelance"]
        expense_categories = ["Food", "Transport", "Rent", "Entertainment"]

        for name in income_categories:
            Category.objects.get_or_create(name=name, type=CategoryType.INCOME)

        for name in expense_categories:
            Category.objects.get_or_create(name=name, type=CategoryType.EXPENSE)

        # Remove previously seeded rows to keep reruns clean.
        Transaction.objects.filter(description__startswith="[seed]").delete()
        Budget.objects.filter(category__name__in=expense_categories).delete()
        Goal.objects.filter(name__startswith="[seed]").delete()

        expense_cats = list(Category.objects.filter(type=CategoryType.EXPENSE))
        income_cats = list(Category.objects.filter(type=CategoryType.INCOME))

        today = date.today()

        for _ in range(20):
            cat = choice(expense_cats + income_cats)
            amount = Decimal(randint(10, 3000))
            tx_date = today - timedelta(days=randint(0, 60))
            Transaction.objects.create(
                amount=amount,
                date=tx_date,
                category=cat,
                description="[seed] demo transaction",
            )

        month_start = today.replace(day=1)
        for cat in expense_cats:
            Budget.objects.create(
                category=cat,
                amount=Decimal(randint(200, 1200)),
                month=month_start,
            )

        Goal.objects.create(
            name="[seed] Emergency Fund",
            target_amount=Decimal("5000.00"),
            current_amount=Decimal("1200.00"),
            deadline=today + timedelta(days=180),
        )

        self.stdout.write(self.style.SUCCESS("Seed data created."))
