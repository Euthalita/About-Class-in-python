class Point:
    def __init__(self, initX, initY):
        self.x = initX
        self.y = initY


    def getX(self):
        return self.x


    def getY(self):
        return self.y

#Mesmo exemplo de forma diferente. Observe que o nome do parametros não é o mesmo, porém não diferencia em nada
class OtherPoint:
    def __init__(self, initX, initY):
        self.initX = initX
        self.initY = initY

    def getX(self):
        return self.initX

    def getY(self):
        return self.initY


valor = OtherPoint(9, 3)
print(valor.getX())
print(valor.getY())



