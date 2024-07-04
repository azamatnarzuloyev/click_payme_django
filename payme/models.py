from django.db import models

# Create your models here.

class Order(models.Model):
    """Order model"""

    order_no = models.CharField(max_length=150)
    # order_id = models.CharField(max_length=200, blank=True)
    summa = models.IntegerField(blank=True)
    is_finished = models.BooleanField(default=False)

    def __str__(self):
        return f"id: {self.id}"
    
    class Meta:
        verbose_name = "Order"
        verbose_name_plural = "Orders"