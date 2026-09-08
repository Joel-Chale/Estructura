import tkinter as tk
from tkinter import simpledialog

def memoria_estatica():
    root = tk.Tk()
    root.withdraw()

    calificaciones = [None] * 5

    for i in range(5):
        respuesta = simpledialog.askstring("Entrada", "captura la calificacion: ")
        if respuesta is not None:
            calificaciones[i] = int(respuesta)

if __name__ == "__main__":
    memoria_estatica()