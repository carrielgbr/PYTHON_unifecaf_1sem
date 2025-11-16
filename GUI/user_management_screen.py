from tkinter import ttk, StringVar, W, E, constants as c

class UserManagementScreen(ttk.Frame):
    
    def __init__(self, container):
        super().__init__(container, padding="20")
        self.pack(fill="both", expand=True) # Exibe o frame

        # Configura o layout para expansão
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

        # Variáveis de controle para campos de entrada e status
        self.search_var = StringVar()
        self.status_var = StringVar()
        
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

    def _setup_search_tab(self):
        # Campo de Pesquisa
        ttk.Label(self.tab_search, text="Nome ou ID do Usuário:").grid(column=0, row=0, sticky=c.W, pady=5)
        ttk.Entry(self.tab_search, width=40, textvariable=self.search_var).grid(column=1, row=0, sticky=(c.W, c.E))
        ttk.Button(self.tab_search, text="Pesquisar", command=self._search_user).grid(column=2, row=0, padx=10)
        
        # Tabela de Resultados (Treeview)
        # Treeview simula a listagem de usuários
        tree = ttk.Treeview(self.tab_search, columns=("id", "nome", "status"), show="headings")
        tree.heading("id", text="ID")
        tree.heading("nome", text="Nome do Usuário")
        tree.heading("status", text="Status")
        tree.column("id", width=50)
        tree.column("nome", width=200)
        tree.column("status", width=100)
        tree.grid(column=0, row=1, columnspan=3, pady=10, sticky="NSEW")
        
        # Botões de Ação na Tabela (Ativar/Desativar/Excluir)
        ttk.Button(self.tab_search, text="Ativar/Desativar").grid(column=0, row=2, sticky=c.W)
        ttk.Button(self.tab_search, text="Excluir Usuário").grid(column=1, row=2, sticky=c.E)
        
        # Configurações de expansão para a aba de pesquisa
        self.tab_search.columnconfigure(1, weight=1)
        self.tab_search.rowconfigure(1, weight=1) # Faz a Treeview expandir

    def _setup_register_tab(self):
        # Campos de Cadastro (placeholders)
        ttk.Label(self.tab_register, text="Nome:").grid(column=0, row=0, sticky=c.W, pady=5)
        ttk.Entry(self.tab_register, width=30).grid(column=1, row=0, sticky=c.E)
        
        ttk.Label(self.tab_register, text="Senha:").grid(column=0, row=1, sticky=c.W, pady=5)
        ttk.Entry(self.tab_register, width=30, show="*").grid(column=1, row=1, sticky=c.E)

        ttk.Button(self.tab_register, text="Salvar Novo Usuário", command=self._register_user).grid(
            column=1, row=2, pady=10, sticky=c.E
        )

    # --- Métodos de Lógica ---
    
    def _search_user(self):
        # Lógica de consulta ao banco de dados para a Treeview
        print(f"Pesquisando usuário: {self.search_var.get()}")

    def _register_user(self):
        # Lógica de inserção no banco de dados
        print("Cadastrando novo usuário...")

    def _go_back_to_main(self):
        # Transição de tela
        self.destroy()
        # Importa a MainScreen localmente para evitar problemas de dependência circular
        from .main_screen import MainScreen 
        MainScreen(self.master)