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