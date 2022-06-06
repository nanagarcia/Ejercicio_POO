class alumno:
    def __init__(self):
        self.nombre= input('Ingrese su nombre: ')
        self.nota=float(input('Ingrese su nota: '))
    def mostrar(self):
        print('Nombre: ',self.nombre)
        print('Nota: ',self.nota)
        
class nota(alumno):
    def notas(self):
        if (self.nota >= 3.0):
            print('Estado: Aprobó')
        else:
            print('Estado: Reprobó')

p1=alumno()
p1.mostrar()
nota=nota()
nota.notas()
