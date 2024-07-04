from django.db import models




class OrderPayment(models.Model):
    type_status = (
        (1, "Yaratildi"),
        (2, "To'landi"),
        (3, "Bekor qilindi"),
    )
    amount = models.IntegerField(default=0)
    status = models.IntegerField(default=1, choices=type_status)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Order Payment"
        verbose_name_plural = "Order Payments"

    def __str__(self):
        return f"{self.amount}"

