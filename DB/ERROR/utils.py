
# ATENÇÃO: É ALTAMENTE RECOMENDADO MOVER ESTA FUNÇÃO PARA UM MÓDULO 
# CENTRAL (ex: conection_sql.py ou utils.py) para ser reutilizada em 
# outras telas (estoque, produtos, etc.).
# ----------------------------------------------------------------------
class registrar_historico:    
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