from tkinter import ttk, StringVar, W, E
from DB.CONECTION.conection_sql import get_connection # Importa a função do novo módulo

from GUI.main_screen import MainScreen


class LoginScreen(ttk.Frame):
    
    # O 'container' é a janela root do Tkinter
    def __init__(self, container):
        super().__init__(container, padding="100 100 200 200")
        
        # Configuração inicial do frame na janela
        self.grid(column=0, row=0, sticky=(W, E))
        
        # 1. Variáveis de Controle
        self.username_var = StringVar()
        self.password_var = StringVar()
        self.status_var = StringVar() # Para exibir mensagens de status
        
        # 2. Configurar a Interface
        self._create_widgets()
            
        # 3. Ajustes de UI
        # Adiciona padding em todos os widgets dentro do frame
        for child in self.winfo_children(): 
            child.grid_configure(padx=5, pady=5)
            
        # Foca no campo de usuário ao iniciar
        self.user_entry.focus()

    def _create_widgets(self):
        # Título
        ttk.Label(self, text="Login sistema", font=('Arial', 14, 'bold')).grid(column=0, row=0, columnspan=2, pady=10)

        # Campo Usuário
        ttk.Label(self, text="Usuário:").grid(column=0, row=1, sticky=W)
        self.user_entry = ttk.Entry(self, width=25, textvariable=self.username_var)
        self.user_entry.grid(column=1, row=1, sticky=(W, E))

        # Campo Senha
        ttk.Label(self, text="Senha:").grid(column=0, row=2, sticky=W)
        self.pass_entry = ttk.Entry(self, width=25, textvariable=self.password_var, show="*")
        self.pass_entry.grid(column=1, row=2, sticky=(W, E))
        
        # Rótulo de Status
        ttk.Label(self, textvariable=self.status_var, foreground='red').grid(column=0, row=4, columnspan=2, pady=10)

        # Botão Login chama o método _check_login
        ttk.Button(self, text="Login", command=self._check_login).grid(column=1, row=3, sticky=E)
        
        # Botão Sair
        ttk.Button(self, text="Sair", command=self.quit).grid(column=0, row=3, sticky=W)

    def _check_login(self):
        """Método que pega os inputs do usuário e consulta o banco de dados."""
        user_input = self.username_var.get()
        pass_input = self.password_var.get()
        
        conn = get_connection() # Chama a função de conexão do módulo DB
        
        if conn is None:
            self.status_var.set("❌ Falha na conexão com o DB.")
            return

        try:
            cursor = conn.cursor()
            
            # Query com placeholders seguros
            query = "SELECT nome_admin FROM tbl_admin WHERE nome_admin = %s AND pass_admin = %s"
            
            cursor.execute(query, (user_input, pass_input)) 
            result = cursor.fetchone() 
            
            if result:
                self.status_var.set(f"🎉 SUCESSO! Bem-vindo(a), {result[0]}!")
                self.after(500, self.switch_to_main_screen)
            else:
                self.status_var.set("🛑 Usuário ou senha incorretos.")
                
        except Exception as e:
            self.status_var.set("Erro interno na consulta.")
            print(f"Erro ao executar consulta: {e}")
            
        finally:
            # Fechamento da conexão sempre no final do uso
            if conn and conn.is_connected():
                conn.close()

def switch_to_main_screen(self):
    self.destroy()
    MainScreen(self.master)
