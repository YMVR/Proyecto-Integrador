import os
import readchar




def clear_terminal (numero):
    os.system ('cls' if os.name == 'nt' else clear )
    print (numero)
    
    
def main ():
    numero= 0
    while numero <= 50:
          clear_terminal (numero)
          key= input (f"Presiona la tecla 'n' para aumentar y cualquier otra para salir ")
          if key == 'n':
            numero += 1
          else:
            break

if __name__== "__main__":
    main()



             












