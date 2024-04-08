import tkinter as tk
import re

# Lista interna para almacenar los objetos
lista_objetos = []

def filtrar_elementos(lista):
    '''Función que toma una lista de elementos y devuelve solo los útiles.'''
    regex = re.compile(r'^(?!.*(?:_on|_so|_fla|.swf|header|formas|sprites|textos|sonidos|fuentes|marcos|scenes|otros|scripts|<default package>|Asset)$).*$', re.IGNORECASE)
    return [elemento for elemento in lista if regex.match(elemento)]

def crear_lineas(lista_filtrada, prefijo):
    '''Recibe una lista filtrada y un prefijo y devuelve otra lista formateada para ser utilizada en un NPC con todos los elementos de la lista filtrada.'''
    lines = ["initial: DO\n    on activate A1\n\n"]
    for i, elemento in enumerate(lista_filtrada, start=1):
        lines.append(f"A{i}: DO\n    user.state get\n    inventory.add 1 {prefijo}.{elemento}\n    after 1 A{i+1}\n\n")
    return lines

def mostrar_salida(prefijo):
    '''Utiliza la funcion de filtro y la funcion de formateo y lo muestra en la caja de texto llamada salida_text'''
    lista_filtrada = filtrar_elementos(lista_objetos)
    output_lines = crear_lineas(lista_filtrada, prefijo)
    salida_text.delete("1.0", tk.END)
    salida_text.insert(tk.END, '\n'.join(output_lines))
    info_label.config(text="Encode preparado, copia y pega en BASE64")

def guardar_contenido():
    '''Toma lo que esta dentro de la primer caja de texto llamada TEXTO y lo guarda en lista_objetos'''
    lista_objetos.clear()
    lista_objetos.extend(texto.get("1.0", tk.END).splitlines())

def copiar_contenido():
    '''Permite copiar el contenido de la caja de texto llamada salida_text'''
    contenido = salida_text.get("1.0", tk.END)
    root.clipboard_clear()
    root.clipboard_append(contenido)

root = tk.Tk()
root.title("Obtener colecciones BY: TERMER")
root.configure(bg="orange3")

# Parte superior del GUI
info_label = tk.Label(root, text="Ingresa el contenido del SWF", bg="gold")
info_label.pack(pady=5)

texto = tk.Text(root, bg="lemon chiffon")
texto.pack(fill=tk.BOTH, expand=True)

boton_guardar = tk.Button(root, text="Guardar", command=guardar_contenido, bg="light goldenrod", fg="black")
boton_guardar.pack(side=tk.TOP, padx=5, pady=5)

# Parte central del GUI
prefijo_label = tk.Label(root, text="Ingresa el nombre del SWF y su ruta correspondiente:", bg="gold")
prefijo_label.pack(side=tk.LEFT, padx=5, pady=5)

prefijo_entry = tk.Entry(root)
prefijo_entry.pack(side=tk.LEFT, padx=5, pady=5)

boton_main = tk.Button(root, text="Crear encode", command=lambda: mostrar_salida(prefijo_entry.get()), bg="light goldenrod", fg="black")
boton_main.pack(side=tk.LEFT, padx=5, pady=5)

# Parte inferior del GUI
info_label = tk.Label(root, text="Esperando generar ENCODE", bg="gold")
info_label.pack(pady=5)

salida_text = tk.Text(root, bg="lemon chiffon")
salida_text.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)

boton_copiar = tk.Button(root, text="Copiar contenido", command=copiar_contenido, bg="light goldenrod", fg="black")
boton_copiar.pack(pady=5)

credits_label = tk.Label(root, text="APP Y TODOS LOS SCRIPTS CREADOS BY TERMER @termer en discord", bg="gold")
credits_label.pack(fill=tk.BOTH)

root.mainloop()
