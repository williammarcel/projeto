import psycopg2 

class AppBD:
    def __init__(self):
        print('Metodo construtor')

    def abrirconexao(self):
        try:
            self.connection = psycopg2.connect(
                user="postgres",
                password="2512",
                host="127.0.0.1",
                port="5432",
                database="postgres"
            )
        except (Exception,psycopg2.Error) as erro:
            if (self.connection):
                print("falha ao se conectar com o banco de dados", erro)

    #selecionar todos os alunos

    def selecionardados(self):
        try:
            self.abrirconexao()
            cursor = self.connection.cursor()

            print("selecionar todos os alunos")
            sql_select_query = """ SELECT * FROM "alunos" """

            cursor.execute(sql_select_query)
            registros = cursor.fetchall()
            print(registros)

        except (Exception, psycopg2.Error) as erro:
            print("error ao selecionar operação",erro)
        finally:
            if (self.connection):
                cursor.close()
                self.connection.close()
                print("A conexão com o postgres foi fechada.")
        return registros

    #inserir alunos

    def inserirdados(self,nome,idade):
        try:
            self.abrirconexao()
            cursor = self.connection.cursor()
            postgres_insert_query = """ INSERT INTO "alunos"("nome","idade") VALUES (%s,%s) """
            record_to_insert = (nome,idade)
            cursor.execute(postgres_insert_query,record_to_insert)
            self.connection.commit()
            count =cursor.rowcount
            print(count, "registro inseridos com sucesso na tabela alunos")
        except(Exception, psycopg2.Error) as erro:
            if(self.connection):
                print("falha ao inserir registro na tabela alunos",erro)

        finally:
            if (self.connection):
                cursor.close()
                self.connection.close()
                print("A conexão com o postegres foi fechada.")

    #atualizar dados
    def atualizardados(self,nome,idade):
        try:
            self.abrirconexao()
            cursor = self.connection.cursor()

            print('registro antes da atualização')
            sql_selct_query = """ SELECT * FROM "alunos" where "nome" = %s"""
            cursor.execute(sql_selct_query, (nome,))
            record = cursor.fetchall()
            print(record)
            #atualizar registro
            sql_selct_query = """UPDATE "alunos" set "nome = %s, "idade" = %S where "nome" = %s"""
            cursor.execute(sql_selct_query,(nome,idade))
            self.connection.commit()
            count = cursor.rowcount
            print(count, "registro atualizados com sucesso!")
            print("registro depois da atualização")
            sql_selct_query = """SELECT * FROM "alunos" where "nome"= %s"""
            cursor.execute(sql_selct_query,(nome,))
            record = cursor.fetchall()
            print(record)

        except(Exception, psycopg2.Error) as erro:
            if(self.connection):
                print("error ao atualizar",erro)

        finally:
            if (self.connection):
                cursor.close()
                self.connection.close()
                print("A conexão com o postegres foi fechada.")

    #excluir dados
    def excluirdados(self,nome):
        try:
            self.abrirconexao()
            cursor = self.connection.cursor()
            sql_delete_query = """DELETE FROM "alunos" where "nome" = %s """
            cursor.execute(sql_delete_query,(nome,))

            self.connection.commit()
            count = cursor.rowcount
            print(count,"registros excluidos com sucesso!")
        except(Exception,psycopg2.Error) as erro:
            print("erro na exclusão",erro)
        finally:
            if (self.connection):
                cursor.close()
                self.connection.close()
                print("A conexão foi fechada")