# Seu main.py
from tkinter import *
from tkinter import ttk
from conection_withmysql import connection_mysql # Importa a função corrigida

# ... (Seu código Tkinter de setup) ...

def check_login():
    # 1. Obter a conexão
    conn = connection_mysql() 
    
    if conn is None:
        print("Falha na conexão com o banco de dados. Verifique as credenciais.")
        return
        
    # --- Simulação: Pegar os dados de entrada do usuário ---
    # *ATENÇÃO: Você deve usar variáveis Tkinter (StringVar) para pegar os dados reais da GUI.
    user_input = "admin" # Substituir por variável da GUI
    pass_input = "admin" # Substituir por variável da GUI

    try:
        cursor = conn.cursor()
        
        # 2. Consultar o banco de dados
        query = "SELECT nome_admin, pass_admin FROM tbl_admin WHERE nome_admin = %s AND pass_admin = %s"
        
        # ATENÇÃO: É seguro passar os valores na tupla para evitar SQL Injection.
        cursor.execute(query, (user_input, pass_input)) 
        
        # 3. Pegar o resultado da consulta
        result = cursor.fetchone() 
        
        if result:
            print(f"🎉 Login SUCESSO! Bem-vindo(a), {result[0]}!")
        else:
            print("🛑 Login FALHOU! Usuário ou senha incorretos.")
            
    except Exception as e:
        print(f"Erro ao executar consulta: {e}")
        
    finally:
        # 4. Fechar a conexão no main
        if conn and conn.is_connected():
            conn.close()
            print("🔗 Conexão MySQL fechada.")

# ... (Seu código Tkinter de execução) ...