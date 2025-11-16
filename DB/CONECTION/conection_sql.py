import mysql.connector

# Detalhes da conexão (Use os dados que funcionaram)
DB_CONFIG = {
    "host": "localhost",
    "user": "root",
    "password": "root", 
    "database": "eletric_shop" 
}

def get_connection():
    """Tenta estabelecer e retornar o objeto de conexão com o MySQL."""
    try:
        # A conexão só é feita quando esta função é chamada
        conexao = mysql.connector.connect(**DB_CONFIG)
        if conexao.is_connected():
            print("✅ Conexão com o MySQL realizada com sucesso!")
        
        # Retorna o objeto de conexão aberto
        return conexao 
        
    except mysql.connector.Error as err:
        print(f"❌ Erro ao conectar ao MySQL: {err}")
        # Retorna None em caso de falha para ser tratado pelo chamador
        return None