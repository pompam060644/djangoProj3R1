from django.db import models
class product():
    def __init__(self,pid, pname, colors, size, price, amount, promotion):
        self.__pid = pid
        self.__pname = pname
        self.__colors = colors
        self.__size = size
        self.__price = price
        self.__amount = amount
        self.__promotion = promotion
        self.__setDiscount()
        self.__setSum()
        self.__setNet()

    def __setDiscount(self):
        if self.__promotion == "มี":
            self.__discount = self.__price * 0.3
        else:
            self.__discount = 0
    def __setSum(self):
        self.__sum = self.__price - self.__discount
    def __setNet(self):
        self.__net = self.__sum * self.__amount
    def getPid(self):
        return self.__pid
    def getPname(self):
        return self.__pname
    def getColor(self):
        return self.__colors
    def getSize(self):
        return self.__size
    def getPrice(self):
        return self.__price
    def getAmount(self):
        return self.__amount
    def getPromotion(self):
        return self.__promotion

    def getDiscount(self):
        return self.__discount
    def getNet(self):
        return self.__net
#lab12
class GoodsCategory(models.Model):
    cid = models.CharField(max_length=6, primary_key=True, default="")
    gc_name = models.CharField(max_length=50, default="")
    desc = models.CharField(max_length=200, default="")
    def __str__(self):
        return str(self.cid)+ ":" + self.gc_name + ":" + self.desc

class Goods(models.Model):
    g_category = models.ForeignKey(GoodsCategory, on_delete=models.CASCADE, default=None)
    gid = models.CharField(max_length=6, primary_key=True, default="")
    g_name = models.CharField(max_length=50, default="")
    brand = models.CharField(max_length=50, default="")
    g_models = models.CharField(max_length=50, default="")
    price = models.FloatField(default=0.00)
    Net = models.IntegerField(default=0)
    product = models.CharField(max_length=200, default="")
    def __str__(self):
        return str(self.gid) + ":" + self.g_name + ":" + str(self.price)

class Customer(models.Model):
    cid = models.CharField(max_length=6, primary_key=True, default="")
    name = models.CharField(max_length=50, default="")
    surname = models.CharField(max_length=50, default="")
    address = models.CharField(max_length=200, default="")
    tel = models.CharField(max_length=10, default="")
    gender = models.CharField(max_length=1, default="")
    carreer = models.CharField(max_length=50, default="")
    password = models.CharField(max_length=50, default="")
    def __str__(self):
        return str(self.cid) + ":" + self.name + ":" + self.surname + ":" + self.tel

class Order(models.Model):
    oid = models.CharField(max_length=6, primary_key=True, default="")
    date = models.DateField(auto_now_add=True, blank=True)
    cid = models.ForeignKey(Customer, on_delete=models.CASCADE, default=None)
    status = models.CharField(max_length=50, default="")
    def __str__(self):
        return str(self.oid) + ":" + str(self.date) + ":" + str(self.cid)
class  OderDetails(models.Model):
    did = models.CharField(max_length=6, primary_key=True, default="")
    oid = models.ForeignKey(Order, on_delete=models.CASCADE, default=None)
    gid = models.ForeignKey(Goods, on_delete=models.CASCADE, default=None)
    price = models.FloatField(default= 0.00)
    quantity = models.IntegerField(default=0)
    def __str__(self):
        return str(self.did) + ":" + str(self.oid) + ":" + str(self.gid) + ":" + str(self.price)