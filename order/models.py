from warehouse.models import *
class Order(models.Model):

    costumer = models.ForeignKey(Customer,on_delete=models.CASCADE)
    code     = models.PositiveIntegerField()

class OrderItem(models.Model):

    code = models.ForeignKey (Order, on_delete=models.CASCADE)
    product = models.ForeignKey (Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField ( )
    price = models.PositiveIntegerField ( )

    def total_price(self):
        total_price = self.quantity * self.price
        return total_price

    total_price = property (total_price)
