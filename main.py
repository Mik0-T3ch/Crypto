import os

# version temporal y de prueba de una función para main 

class opciones:
    def __init__(self):
        print('=' *  20)
        print('opciones')
        print('=' * 20 + '\n')
        print('1 - ')
        print('2 - ')
        print('3 - ')
        
        self.cifrador()
    
    def opcion_user(self):
        self.opcion = input('\nseleciona una opción -> ')
        return self.opcion
    
    def mensaje_a_cifrar(self):
        self.opcion_user()
        self.mensaje = input('\n-----escribe tu mensaje -> ')
        return self.mensaje
    
    def cifrador(self):
        self.mensaje_a_cifrar()
        print(f'\ntu mensaje cifrado :\n\n{self.mensaje}')
        print('gay el que lo lea, x2 si es Mik0')
        

opciones()
