# main.py
import tkinter as tk
from GUI.login_screen import LoginScreen 

class AppSession:
    """Armazena o estado do usuário logado."""
    def __init__(self):
        self.user_id = None
        self.user_type = None  # 'A' para Admin, 'U' para User
        self.username = None

def main():
    root = tk.Tk()
    root.title("E-commerce Manager")
    
    # *** ESTE PASSO É CRUCIAL ***
    # Anexa a instância da sessão à janela root
    root.session = AppSession() 

    login_frame = LoginScreen(root)
    # Certifique-se de que a LoginScreen é empacotada ou gradeada
    # No seu código da LoginScreen, você já usa .grid(column=0, row=0, sticky=(W, E))
    
    root.mainloop()

if __name__ == "__main__":
    main()