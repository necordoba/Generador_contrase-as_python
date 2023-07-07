# Importa la biblioteca Tkinter para trabajar con la interfaz gráfica de usuario (GUI)
import tkinter as tk  
# Importa el módulo messagebox de Tkinter para mostrar mensajes en la GUI
from tkinter import messagebox  
# Importa el módulo random para generar contraseñas aleatorias
import random  
# Importa el módulo string para trabajar con caracteres
import string  

def generate_password(length, include_special_chars=True):
    # Define los caracteres válidos para la contraseña: letras y dígitos
    chars = string.ascii_letters + string.digits  
    # Si se incluyen caracteres especiales, añádelos a los caracteres válidos
    if include_special_chars:
        chars += string.punctuation  
    # Genera una contraseña aleatoria usando los caracteres válidos y la longitud especificada
    password = ''.join(random.choice(chars) for _ in range(length))  
    # Devuelve la contraseña generada
    return password  

def generate_passwords(length_entry, special_chars_var, num_passwords_entry):
    # Obtiene la longitud ingresada por el usuario como un entero
    length = int(length_entry.get())  
    # Obtiene el valor de la casilla de verificación de caracteres especiales
    include_special_chars = special_chars_var.get()  
    # Obtiene la cantidad de contraseñas a generar ingresada por el usuario

    # Inicializa una lista para almacenar las contraseñas generadas
    num_passwords = int(num_passwords_entry.get())  
    passwords = [] 
    for _ in range(num_passwords):
        # Genera una contraseña llamando a la función generate_password()
        password = generate_password(length, include_special_chars)  
        # Agrega la contraseña generada a la lista de contraseñas
        passwords.append(password)  
         # Muestra un cuadro de mensaje con las contraseñas generadas
    messagebox.showinfo("Contraseñas generadas", "\n".join(passwords)) 

def main():
    # Crea una ventana principal de la GUI
    window = tk.Tk()  
    # Establece el título de la ventana
    window.title("Generador de Contraseñas")  
    # Establece las dimensiones de la ventana
    window.geometry("300x200")  

     # Crea una etiqueta para mostrar el texto "Longitud"
    length_label = tk.Label(window, text="Longitud:") 
    # Muestra la etiqueta en la ventana
    length_label.pack()  

    # Crea un campo de entrada para que el usuario ingrese la longitud de la contraseña
    length_entry = tk.Entry(window)  
    # Muestra el campo de entrada en la ventana
    length_entry.pack()  

    # Crea una variable booleana para almacenar el estado de la casilla de verificación de caracteres especiales
    special_chars_var = tk.BooleanVar()  
     # Establece el valor inicial de la variable en True (casilla de verificación marcada por defecto)
    special_chars_var.set(True) 

    # Crea una casilla de verificación para permitir al usuario seleccionar si incluir o no caracteres especiales
    special_chars_checkbox = tk.Checkbutton(window, text="Incluir caracteres especiales", variable=special_chars_var)  
    
     # Muestra la casilla de verificación en la ventana
    special_chars_checkbox.pack() 
    # Crea una etiqueta para mostrar el texto "Cantidad de contraseñas"
    num_passwords_label = tk.Label(window, text="Cantidad de contraseñas:")  
    # Muestra la etiqueta en la ventana
    num_passwords_label.pack()  
    # Crea un campo de entrada para que el usuario ingrese la cantidad de contraseñas a generar
    num_passwords_entry = tk.Entry(window)  
     # Muestra el campo de entrada en la ventana
    num_passwords_entry.pack() 

     # Crea un botón con texto "Generar Contraseñas" y establece su comando para llamar a la función generate_passwords() con los elementos de la interfaz necesarios como argumentos
    generate_button = tk.Button(window, text="Generar Contraseñas", command=lambda: generate_passwords(length_entry, special_chars_var, num_passwords_entry)) 
    # Muestra el botón en la ventana
    generate_button.pack()  

    # Inicia el bucle principal para que la ventana responda a las interacciones del usuario
    window.mainloop()  

if __name__ == '__main__':
    main()
