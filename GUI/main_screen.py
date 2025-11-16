from tkinter import ttk, W, E, CENTER
# Não precisamos do get_connection aqui, pois ele só é usado para DB.
# from DB.CONECTION.conection_sql import get_connection 

# Importa as classes das telas que serão navegadas (user_management_screen e history_screen)
from GUI.user_management_screen import UserManagementScreen
from GUI.history_screen import HistoryScreen 

class MainScreen(ttk.Frame):
    
    def __init__(self, container):
        # 1. Configura o Frame principal
        super().__init__(container, padding="20 20 20 20")
        
        # ESSENCIAL: Empacota o frame para que ele seja visível
        self.pack(fill="both", expand=True) 

        # 2. Configura a grade para expansão (centralização)
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        
        # Faz o grid se expandir para centralizar o conteúdo
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1) 
        
        # 3. Cria os Widgets de navegação
        self._create_widgets()

    def _create_widgets(self):
        # Título da tela
        # Usamos sticky='ew' para que o título preencha a largura centralizada
        ttk.Label(self, text="Painel de Controle - EletricShop", font=('Arial', 16, 'bold')).grid(
            column=0, row=0, columnspan=2, pady=(0, 20), sticky='ew' 
        )

        # --- Linha 1: Cadastro e Estoque ---
        
        # Botão: Gerenciar Usuários (Link para UserManagementScreen)
        self._create_button("Gerenciar Usuários", self._open_user_management, 1, 0)
        
        # Botão: Pesquisar Materiais (Estoque)
        self._create_button("Pesquisar Estoque", self._open_pesquisar_estoque, 1, 1)

        # --- Linha 2: Cadastros de Suporte ---
        
        # Botão: Cadastrar Material / Fornecedor
        self._create_button("Cadastrar Produtos/Fornecedores", self._open_cadastrar_produtos, 2, 0)
        
        # Botão: Cadastrar Marcas / Categorias
        self._create_button("Cadastrar Marcas/Categorias", self._open_cadastrar_marcas, 2, 1)
        
        # Botão: Histórico de Movimentação (Link para HistoryScreen)
        self._create_button("Histórico de Movimentação", self._open_history, 3, 0)
        
        # Botão: Sair do Sistema
        # Usamos columnspan=2 e sticky='ew' para centralizar no rodapé ou deixar W para alinhamento.
        ttk.Button(self, text="Sair", command=self.quit).grid(
            column=1, row=3, pady=(30, 0), sticky=CENTER 
        )
        
        # Adiciona um pequeno padding em todos os filhos
        for child in self.winfo_children(): 
            child.grid_configure(padx=10, pady=10)

    def _create_button(self, text, command, row, column):
        """Função auxiliar para criar botões padronizados."""
        btn_frame = ttk.Frame(self, width=250, height=100, relief='raised')
        btn_frame.grid(row=row, column=column, padx=15, pady=15, sticky="NSEW")
        
        # Faz o Frame e o Botão interno expandirem juntos
        btn_frame.grid_columnconfigure(0, weight=1)
        btn_frame.grid_rowconfigure(0, weight=1)
        
        button = ttk.Button(btn_frame, text=text, command=command)
        button.grid(row=0, column=0, sticky="NSEW", ipadx=20, ipady=20)
        
        return button
        
    # --- Métodos de Navegação (Troca de Tela) ---

    def _open_user_management(self):
        """Abre a tela de Gerenciamento de Usuários."""
        self.destroy()
        UserManagementScreen(self.master)

    def _open_history(self):
        """Abre a tela de Histórico de Movimentação."""
        self.destroy()
        HistoryScreen(self.master)

    def _open_pesquisar_estoque(self):
        print("Abrindo tela: Pesquisar Estoque (A ser implementada)")
        # Futura implementação: self.destroy(); EstoqueScreen(self.master)

    def _open_cadastrar_produtos(self):
        print("Abrindo tela: Cadastrar Produtos/Fornecedores (A ser implementada)")
        # Futura implementação: self.destroy(); CadastroProdutoScreen(self.master)

    def _open_cadastrar_marcas(self):
        print("Abrindo tela: Cadastrar Marcas/Categorias (A ser implementada)")
        # Futura implementação: self.destroy(); CadastroMarcaScreen(self.master)