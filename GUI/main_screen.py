from tkinter import ttk, W, E, CENTER

class MainScreen(ttk.Frame):
    
    def __init__(self, container):
        # 1. Configura o Frame principal
        super().__init__(container, padding="100 100 200 200")
        self.pack(fill="both", expand=True)
        
        # 2. Configura a grade para expansão (centralização)
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
        
        # 3. Cria os Widgets de navegação
        self._create_widgets()

    def _create_widgets(self):
        # Título da tela
        ttk.Label(self, text="Painel de Controle - EletricShop", font=('Arial', 16, 'bold')).grid(
            column=0, row=0, columnspan=2, pady=(0, 20), sticky= 'ew'
        )

        # --- Linha 1: Cadastro e Estoque ---
        
        # Botão: Cadastrar Novo Usuário (Admin)
        self._create_button("Cadastrar Usuário", self._open_cadastrar_usuario, 1, 0)
        
        # Botão: Pesquisar Materiais (Estoque)
        self._create_button("Pesquisar Estoque", self._open_pesquisar_estoque, 1, 1)

        # --- Linha 2: Cadastros de Suporte ---
        
        # Botão: Cadastrar Material / Fornecedor
        self._create_button("Cadastrar Produtos/Fornecedores", self._open_cadastrar_produtos, 2, 0)
        
        # Botão: Cadastrar Marcas / Categorias
        self._create_button("Cadastrar Marcas/Categorias", self._open_cadastrar_marcas, 2, 1)
        
        # Botão: Sair do Sistema
        ttk.Button(self, text="Sair", command=self.quit).grid(
            column=0, row=3, columnspan=2, pady=(30, 0), sticky= 'ew'
        )
        
        # Adiciona um pequeno padding em todos os filhos
        for child in self.winfo_children(): 
            child.grid_configure(padx=10, pady=10)

    def _create_button(self, text, command, row, column):
        """Função auxiliar para criar botões padronizados."""
        # Frame para dar padding e estilo ao botão
        btn_frame = ttk.Frame(self, width=200, height=100, relief='raised')
        btn_frame.grid(row=row, column=column, padx=15, pady=15, sticky="NSEW")
        
        # Botão real
        button = ttk.Button(btn_frame, text=text, command=command)
        button.pack(expand=True, fill='both', ipadx=20, ipady=20)
        
        # Configura o frame para não encolher para o tamanho de seus filhos
        self.grid_columnconfigure(column, weight=1)
        self.grid_rowconfigure(row, weight=1)
        
        return button
        
    # --- Métodos de Navegação (Placeholder) ---
    # Estes métodos serão implementados com as próximas telas

    def _open_cadastrar_usuario(self):
        print("Abrindo tela: Cadastrar Usuário")
        # futura_tela = UserRegistrationScreen(self.master)
        # futura_tela.tkraise()

    def _open_pesquisar_estoque(self):
        print("Abrindo tela: Pesquisar Estoque")

    def _open_cadastrar_produtos(self):
        print("Abrindo tela: Cadastrar Produtos/Fornecedores")

    def _open_cadastrar_marcas(self):
        print("Abrindo tela: Cadastrar Marcas/Categorias")

# --- Teste Rápido (Opcional, pode ser removido depois) ---
# if __name__ == '__main__':
#     import tkinter as tk
#     root = tk.Tk()
#     root.title("Main Screen Test")
#     MainScreen(root)
#     root.mainloop()