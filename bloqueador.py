import tkinter as tk

class Bloqueador():
    hostsFile = "C:/Windows/System32/drivers/etc/hosts"
    
    
    def __init__(self):
        self.window = tk.Tk()
        self.window.geometry("400x150")
        self.window.title("Bloqueador de Páginas")
        self.window.resizable(width=False, height=False)
        self.createLabel()
        self.createEntry()
        self.boton_crear()
        self.boton_eliminar()
        self.boton_listar()
        self.window.mainloop()
        
    def createLabel(self):
        self.label = tk.Label(self.window, text="Ingresa URL:")
        self.label.pack(pady=5)
    
    def createEntry(self):
        self.entry = tk.Entry(self.window, width=30)
        self.entry.pack()

    def boton_crear(self):     
        self.addButton = tk.Button(self.window, text="Añadir", command=self.agregar_url)
        self.addButton.pack(pady=5)

    def boton_eliminar(self):     
        self.removeButton = tk.Button(self.window, text="Eliminar", command=self.eliminar_url)
        self.removeButton.pack(pady=5)
        
    def boton_listar(self):
        self.addButton = tk.Button(self.window, text="Listar", command=self.listar_url)
        self.addButton.pack(pady=5)
