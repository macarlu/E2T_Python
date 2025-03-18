import tkinter as tk
'''class UI(tk.Frame):
    """Docstring."""
    
    def __init__(self, parent):
        tk.Frame.__init__(self,parent)
        self.parent = parent
        self.init_ui()
        
    def init_ui(self):
        """Aqui colocariamos los widgets."""
        self.parent.title("Un titulo para la ventana")

        etiqueta = tk.Label(root, text="Probando Label")
        etiqueta.pack()

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("800x600")
    app = UI(parent = root)
    app.mainloop()
    root.destroy()

def funcion():
    print("Excelente")

root = tk.Tk()
boton = tk.Button(root, text="Que te parece?", command=funcion)
boton.pack()
boton.invoke()
root.mainloop()'''

root = tk.Tk()
campo_de_texto = tk.Entry(root)
campo_de_texto.pack()
'Hola Mundo!!!'
campo_de_texto.get()
root.mainloop()