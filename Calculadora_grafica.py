import tkinter as tk
from tkinter import messagebox
from calculadora_basica import Calculadora

class CalculadoraGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculadora")
        self.root.geometry("300x400")

