import mysql.connector

# Detalhes da conexão
DB_CONFIG = {
    "host": "localhost",
    "user": "root",
    "password": "root", # Corrigir se a senha do usuário 'root' for outra
    "database": "eletric_shop" 
}

def connection_mysql():
    try:
        conexao = mysql.connector.connect(**DB_CONFIG)

        if conexao.is_connected():
            print("✅ Conexão com o MySQL realizada com sucesso!")
            
        # O PONTO CRÍTICO: RETORNAR O OBJETO DE CONEXÃO
        return conexao 

    except mysql.connector.Error as err:
        print(f"❌ Erro ao conectar ao MySQL: {err}")
        return None  # Retorna None em caso de falha

    # O BLOCO 'finally' FOI REMOVIDO DAQUI, pois a conexão será fechada no main.py