import tkinter as tk
from tkinter import ttk

def obtener_datos():
    # Función para obtener los datos ingresados
    empresa = entry_empresa.get()
    
    palabras_clave_text = text_palabras_clave.get("1.0", tk.END).strip()
    palabras_clave_list = palabras_clave_text.splitlines()  # Convertir el texto en una lista
    
    url_mapa_text = text_url_mapa.get("1.0", tk.END).strip()
    url_mapa_list = url_mapa_text.splitlines()  # Convertir el texto en una lista
    
    url_imagen = entry_url_imagen.get()

    # Aquí puedes procesar o almacenar los datos como desees
    print("Empresa:", empresa)
    print("Palabras clave:", palabras_clave_list)
    print("URLs del mapa:", url_mapa_list)
    print("URL de la imagen:", url_imagen)

# Crear la ventana principal
root = tk.Tk()
root.title("Interfaz de Entrada")

# Crear y colocar las etiquetas y campos de entrada
label_empresa = ttk.Label(root, text="Nombre de la empresa:")
label_empresa.grid(row=0, column=0, sticky="w", padx=10, pady=5)
entry_empresa = ttk.Entry(root)
entry_empresa.grid(row=0, column=1, padx=10, pady=5)

label_palabras_clave = ttk.Label(root, text="Palabras clave:")
label_palabras_clave.grid(row=1, column=0, sticky="w", padx=10, pady=5)
text_palabras_clave = tk.Text(root, height=5, width=30)
text_palabras_clave.grid(row=1, column=1, padx=10, pady=5)

label_url_mapa = ttk.Label(root, text="URLs del mapa:")
label_url_mapa.grid(row=2, column=0, sticky="w", padx=10, pady=5)
text_url_mapa = tk.Text(root, height=5, width=30)
text_url_mapa.grid(row=2, column=1, padx=10, pady=5)

label_url_imagen = ttk.Label(root, text="URL de la imagen:")
label_url_imagen.grid(row=3, column=0, sticky="w", padx=10, pady=5)
entry_url_imagen = ttk.Entry(root)
entry_url_imagen.grid(row=3, column=1, padx=10, pady=5)

# Botón para obtener los datos
btn_obtener = ttk.Button(root, text="Obtener Datos", command=obtener_datos)
btn_obtener.grid(row=4, column=0, columnspan=2, pady=10)

root.mainloop()
