import tkinter as tk
from GUI.login_screen import LoginScreen # Importa a tela de login

def main():
    root = tk.Tk()
    root.title("E-commerce Manager")
    
    # Cria a instância da primeira tela (Tela de Login)
    login_frame = LoginScreen(root)
    login_frame.pack(fill="both", expand=True)

    root.mainloop()

if __name__ == "__main__":
    main()