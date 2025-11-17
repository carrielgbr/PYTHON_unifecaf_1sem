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
        """Método que tenta logar como Admin ou User e salva as credenciais na sessão."""
        user_input = self.username_var.get()
        pass_input = self.password_var.get()
        
        conn = get_connection()
        if conn is None:
            self.status_var.set("❌ Falha na conexão com o DB.")
            return

        cursor = None
        user_data = None
        user_type = None

        try:
            cursor = conn.cursor()
            
            # --- TENTATIVA 1: LOGIN COMO ADMINISTRADOR ---
            # CORRIGIDO: Agora usa a variável admin_query. Adicionado ID na seleção.
            admin_query = "SELECT id_admin, nome_admin FROM tbl_admin WHERE nome_admin = %s AND pass_admin = %s" 
            
            cursor.execute(admin_query, (user_input, pass_input)) 
            result = cursor.fetchone() 

            if result:
                # CORRIGIDO: Atribuição correta do dicionário: user_data = {...}
                user_data = { 
                    'id': result[0],    # id_admin
                    'name': result[1],  # nome_admin
                }
                user_type = 'A'
            
            # --- TENTATIVA 2: LOGIN COMO USUÁRIO COMUM (Se falhou como Admin) ---
            if user_data is None:
                # Assumindo que a coluna é id_users (verifique no seu DB)
                user_query = "SELECT id_users, nome_user FROM tbl_users WHERE nome_user = %s AND pass_user = %s" 

                cursor.execute(user_query, (user_input, pass_input))
                result = cursor.fetchone()

                if result:
                    user_data = {
                        'id': result[0],    # id_users
                        'name': result[1],  # nome_user
                    }
                    user_type = 'U'

            # --- PROCESSAMENTO DO RESULTADO E SESSÃO ---
            if user_data:
                
                # Salva os dados na Sessão
                self.master.session.user_id = user_data['id']
                self.master.session.user_type = user_type
                # CORRIGIDO: Nome do atributo na sessão deve ser o mesmo que você usa no main.py (user_name)
                self.master.session.username = user_data['name'] 

                tipo_msg = "Administrador" if user_type == 'A' else "Usuário"
                # CORRIGIDO: Fechamento da string e da tupla da mensagem de status
                self.status_var.set(f"✅ Bem-vindo, {user_data['name']} ({tipo_msg})!")
                self.after(500, self._switch_to_main_screen)
                
            else:
                self.status_var.set("❌ Usuário ou senha inválidos.")
                
        except AttributeError:
            # Captura se self.master.session não existir
            self.status_var.set("❌ Erro de sessão: master não possui atributo session.")
            print("❌ Erro de sessão: Configure a AppSession no main.py.")
            
        except Exception as e:
            self.status_var.set(f"❌ Erro ao executar login: {e}")
            print(f"❌ Erro ao executar login: {e}")

        finally:
            if conn and conn.is_connected():
                conn.close()

# O método _switch_to_main_screen está correto, apenas movi para fora do _check_login
def _switch_to_main_screen(self):
    self.destroy()
    # Importação local para evitar circular import
    from .main_screen import MainScreen
    main_frame = MainScreen(self.master)
    main_frame.pack(fill="both", expand=True)