from tkinter import ttk, W, E, constants as c

class HistoryScreen(ttk.Frame):
    
    def __init__(self, container):
        super().__init__(container, padding="20")
        self.pack(fill="both", expand=True)

        self.columnconfigure(0, weight=1)
        self.rowconfigure(1, weight=1) # A linha da tabela deve expandir
        
        self._create_widgets()

    def _create_widgets(self):
        ttk.Label(self, text="Histórico de Movimentação", font=('Arial', 16, 'bold')).grid(
            column=0, row=0, pady=(0, 15), sticky=c.N
        )
        
        # --- Tabela de Histórico (Treeview) ---
        tree = ttk.Treeview(self, columns=("data", "usuario", "acao", "detalhes"), show="headings")
        
        tree.heading("data", text="Data/Hora")
        tree.heading("usuario", text="Usuário")
        tree.heading("acao", text="Ação")
        tree.heading("detalhes", text="Detalhes")
        
        tree.column("data", width=150)
        tree.column("usuario", width=100)
        tree.column("acao", width=100)
        tree.column("detalhes", width=300)
        
        # Posiciona a tabela para preencher a tela
        tree.grid(column=0, row=1, sticky="NSEW", padx=10, pady=10)

        # Botão Voltar
        ttk.Button(self, text="<< Voltar ao Painel", command=self._go_back_to_main).grid(
            column=0, row=2, pady=(15, 0), sticky=c.W
        )

    # --- Métodos de Lógica ---
    
    def _go_back_to_main(self):
        # Transição de tela
        self.destroy()
        from .main_screen import MainScreen 
        MainScreen(self.master)