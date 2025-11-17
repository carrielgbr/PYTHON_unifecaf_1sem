from tkinter import ttk, StringVar, W, E, constants as c
# Importa a função de conexão com o banco
from DB.CONECTION.conection_sql import get_connection
from DB.ERROR.utils import registrar_historico
# Importa a MainScreen para o retorno

# ----------------------------------------------------------------------
# ATENÇÃO: É ALTAMENTE RECOMENDADO MOVER ESTA FUNÇÃO PARA UM MÓDULO 
# CENTRAL (ex: conection_sql.py ou utils.py) para ser reutilizada em 
# outras telas (estoque, produtos, etc.).
# ----------------------------------------------------------------------
def registrar_historico(conn, executor_id, executor_tipo, acao, tabela, objeto_id, tela):
    query = """
        INSERT INTO tbl_historico (id_executor, tipo_executor, acao, tabela_afetada, id_objeto_afetado, tela_origem)
        VALUES (%s, %s, %s, %s, %s, %s)
    """
    try:
        cursor = conn.cursor()
        # Garante que o objeto_id seja INT (se for None, registra 0 ou NULL, dependendo do design da sua tabela)
        obj_id = objeto_id if objeto_id is not None else 0 
        cursor.execute(query, (executor_id, executor_tipo, acao, tabela, obj_id, tela))
        conn.commit()
    except Exception as e:
        print(f"⚠️ Erro ao registrar histórico: {e}")
# ----------------------------------------------------------------------

class UserManagementScreen(ttk.Frame):
    
    def __init__(self, container):
        super().__init__(container, padding="20")
        self.pack(fill="both", expand=True) 

        self.columnconfigure(0, weight=1)
        self.rowconfigure(1, weight=1) # Faz o notebook (abas) expandir

        # Variáveis de controle
        self.search_var = StringVar()
        self.status_var = StringVar()
        # NOVAS VARS para Cadastro
        self.new_user_name_var = StringVar()
        self.new_user_pass_var = StringVar()
        
        self._create_widgets()

    def _create_widgets(self):
        ttk.Label(self, text="Administração de Usuários", font=('Arial', 16, 'bold')).grid(
            column=0, row=0, pady=(0, 15), sticky=c.N
        )

        # --- 1. Sistema de Abas (Notebook) para separar funções ---
        notebook = ttk.Notebook(self)
        notebook.grid(column=0, row=1, sticky="NSEW", padx=10, pady=10)
        
        # Cria as abas (Frames)
        self.tab_search = ttk.Frame(notebook, padding="10")
        self.tab_register = ttk.Frame(notebook, padding="10")
        
        notebook.add(self.tab_search, text='Pesquisar / Gerenciar')
        notebook.add(self.tab_register, text='Cadastrar Novo')

        # --- 2. Conteúdo da Aba 'Pesquisar / Gerenciar' ---
        self._setup_search_tab()

        # --- 3. Conteúdo da Aba 'Cadastrar Novo' ---
        self._setup_register_tab()
        
        # Botão Voltar para o Painel Principal
        ttk.Button(self, text="<< Voltar ao Painel", command=self._go_back_to_main).grid(
            column=0, row=2, pady=(15, 0), sticky=c.W
        )

    # ... (método _setup_search_tab permanece inalterado) ...
    def _setup_search_tab(self):
        # Campo de Pesquisa
        ttk.Label(self.tab_search, text="Nome ou ID do Usuário:").grid(column=0, row=0, sticky=c.W, pady=5)
        ttk.Entry(self.tab_search, width=40, textvariable=self.search_var).grid(column=1, row=0, sticky=(c.W, c.E))
        ttk.Button(self.tab_search, text="Pesquisar", command=self._search_user).grid(column=2, row=0, padx=10)
        
        # Tabela de Resultados (Treeview)
        #tree = ttk.Treeview(self.tab_search, columns=("id", "nome", "status"), show="headings")
        self.tree = ttk.Treeview(self.tab_search, columns=("id", "nome", "status"), show="headings")
        self.tree.heading("id", text="ID")
        self.tree.heading("nome", text="Nome do Usuário")
        self.tree.heading("status", text="Status")
        self.tree.column("id", width=50)
        self.tree.column("nome", width=200)
        self.tree.column("status", width=100)
        self.tree.grid(column=0, row=1, columnspan=3, pady=10, sticky="NSEW")
        
        # Botões de Ação na Tabela (Ativar/Desativar/Excluir)
        ttk.Button(self.tab_search, text="Ativar/Desativar").grid(column=0, row=2, sticky=c.W)
        ttk.Button(self.tab_search, text="Excluir Usuário").grid(column=1, row=2, sticky=c.E)
        
        # Configurações de expansão para a aba de pesquisa
        self.tab_search.columnconfigure(1, weight=1)
        self.tab_search.rowconfigure(1, weight=1) # Faz a Treeview expandir

        self.tree.grid(column=0, row=1, columnspan=3, pady=10, sticky="NSEW")
    
    def _setup_register_tab(self):
        # Campos de Cadastro (placeholders)
        ttk.Label(self.tab_register, text="Nome:").grid(column=0, row=0, sticky=c.W, pady=5)
        # Associa a variável de controle new_user_name_var
        ttk.Entry(self.tab_register, width=30, textvariable=self.new_user_name_var).grid(column=1, row=0, sticky=c.E)
        
        ttk.Label(self.tab_register, text="Senha:").grid(column=0, row=1, sticky=c.W, pady=5)
        # Associa a variável de controle new_user_pass_var
        ttk.Entry(self.tab_register, width=30, show="*", textvariable=self.new_user_pass_var).grid(column=1, row=1, sticky=c.E)

        ttk.Button(self.tab_register, text="Salvar Novo Usuário", command=self._register_user).grid(
            column=1, row=2, pady=10, sticky=c.E
        )

    # --- Métodos de Lógica (Atualizados) ---
    
    def _search_user(self):
                # Lógica de consulta ao banco de dados para a Treeview
              #  print(f"Pesquisando usuário: {self.search_var.get()}")

            conn = get_connection()
            if conn is None:
                print("Erro: Não foi possível estabelecer conexão com o MySQL.")
                return

                search_term = self.search_var.get()

            # 1. Limpar resultados anteriores da Treeview
            for item in self.tree.get_children():
                self.tree.delete(item)

            try:
                cursor = conn.cursor()

                # O termo de busca é usado como wildcard (procura por qualquer parte do nome)
                search_pattern = f"%{search_term}%"

                # Consulta SQL para buscar usuários
                # Status (Tipo) é determinado pelo campo id_admin estar preenchido ou não, 
                # mas aqui vamos usar uma consulta simples por nome e ID
                query = """
                SELECT 
                    u.id_users, 
                    u.nome_user,
                    CASE 
                        WHEN u.id_admin IS NOT NULL THEN 'Cadastrado por Admin'
                        ELSE 'Usuário Padrão'
                    END AS status_user
                FROM 
                    tbl_users u
                WHERE 
                    u.nome_user LIKE %s OR CAST(u.id_users AS CHAR) LIKE %s
                ORDER BY 
                    u.nome_user;
                """

                cursor.execute(query, (search_pattern, search_pattern))
                results = cursor.fetchall()

                if not results:
                    self.tree.insert('', 'end', values=('', 'Nenhum usuário encontrado.', ''))

                else:
                    # 2. Inserir os novos resultados na Treeview
                    for id_user, nome, status in results:
                        self.tree.insert('', 'end', values=(id_user, nome, status))

            except Exception as e:
                print(f"❌ Erro ao executar pesquisa: {e}")
                self.tree.insert('', 'end', values=('', f'Erro de consulta: {e}', ''))

            finally:
                if conn and conn.is_connected():
                    conn.close()




    def _register_user(self):
        """Lógica de inserção no banco de dados e registro de histórico."""
        
        conn = get_connection()
        if conn is None: return

        # Pega os inputs
        nome_novo = self.new_user_name_var.get()
        pass_novo = self.new_user_pass_var.get()
        
        if not nome_novo or not pass_novo:
            print("🚨 Nome e Senha são obrigatórios.")
            return

        try:
            # Garante que a sessão existe e que o usuário está logado
            if not hasattr(self.master, 'session') or self.master.session.user_id is None:
                 raise Exception("Erro de Sessão: Administrador não identificado.")
            
            executor_id = self.master.session.user_id 
            executor_tipo = self.master.session.user_type
            
            # --- 1. Cadastrar na tbl_users ---
            cursor = conn.cursor()
            
            # id_admin é o ID do executor logado que está cadastrando o novo user
            query_user = "INSERT INTO tbl_users (nome_user, pass_user, id_admin) VALUES (%s, %s, %s)"
            cursor.execute(query_user, (nome_novo, pass_novo, executor_id))
            
            novo_user_id = cursor.lastrowid # Pega o ID do usuário recém-criado
            
            # --- 2. Registrar no Histórico ---
            registrar_historico(
                conn,
                executor_id,
                executor_tipo,
                f'CADASTRO NOVO USER: {nome_novo}', # Ação detalhada
                'tbl_users',
                novo_user_id,
                'UserManagementScreen'
            )
            
            print(f"✅ Usuário '{nome_novo}' cadastrado com sucesso por {self.master.session.username}.")
            
            # Limpa os campos após o sucesso
            self.new_user_name_var.set("")
            self.new_user_pass_var.set("")
            
        except Exception as e:
            print(f"❌ Erro ao cadastrar/registrar histórico: {e}")
            conn.rollback() 
        finally:
            if conn and conn.is_connected():
                conn.close()

    def _go_back_to_main(self):
        # Transição de tela
        self.destroy()
        from .main_screen import MainScreen
        MainScreen(self.master)