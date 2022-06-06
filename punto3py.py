class calculadora:
    def __init__(self):
        self.a=int(input('Ingrese un numero: '))
        self.b=int(input('Ingrese un numero: '))

    def  suma (self):
        sum=self.a+self.b
        print('Suma: ',sum)

    def resta (self):
        rest=self.a-self.b
        print('Resta: ',rest)

    def multiplicacion (self):
        mult=self.a*self.b
        print('Multiplicacion: ',mult)

    def division (self):
        div=self.a/self.b
        print('Division: ',div)

calc=calculadora()
calc.suma()
calc.resta()
calc.multiplicacion()
calc.division()
