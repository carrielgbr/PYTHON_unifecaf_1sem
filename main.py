import tkinter as tk
from GUI.login_screen import LoginScreen # Importa a tela de login

def main():
    root = tk.Tk()
    root.title("E-commerce Manager")
    
    # Cria a instância da primeira tela (Tela de Login)
    login_frame = LoginScreen(root)
    login_frame.pack(fill="both", expand=True)

    root.mainloop()

class AppSession:
    """Classe para armazenar o estado do usuário logado."""
    def __init__(self):
        self.user_id = None
        self.user_type = None  # 'A' para Admin, 'U' para User
        self.username = None

if __name__ == "__main__":
    main()