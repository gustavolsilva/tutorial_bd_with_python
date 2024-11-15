import os
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, Integer, String

# Configurando a Engine do BD
engine = create_engine('sqlite:///database.db')

# Configurado a Sessão
Session = sessionmaker(bind=engine)

# Criando a tabela
Base = declarative_base()

# Clsse que cria a tabela de usuário
class Usuario(Base):
    """
    Classe para criar a tabela de usuários
    Ela contém os campos id do tipo inteiro, nome e tipo do tipo string
    """
    __tablename__ = 'usuarios'
    id = Column(Integer, primary_key=True)
    nome = Column(String, nullable=False)
    tipo = Column(String, nullable=False)


def insert_usuario(nome_usuario: String, tipo_usuario: String):
    """
    Função para inserir um novo usuário no banco de dados
    """
    session = Session()
    try:
        if all([nome_usuario, tipo_usuario]):
            usuario = Usuario(nome=nome_usuario, tipo=tipo_usuario)
            session.add(usuario)
            session.commit()
            print(f"Usuario {nome_usuario} cadastrado com sucesso!")
        else:
            print("É obrigatório preencher o nome e o tipo de usuário!")
    except Exception as e:
        session.rollback()
        print(f"Ocorreu um erro ao tentar cadastrar usuário {nome_usuario}: {e}")
    finally:
        session.close()

def select_usuarios(nome_usuario: String = ""):
    """
    Função para consultar os usuários cadastrados no banco de dados
    """
    session = Session()
    try:
        if nome_usuario:
            dados = session.query(Usuario).filter(Usuario.nome == nome_usuario)
        else:
            dados = session.query(Usuario).all()
        usuarios = [f"Nome: {usuario.nome} - Tipo: {usuario.tipo}" for usuario in dados]
        for usuario in usuarios:
            print(usuario)
    except Exception as e:
        print(f"Ocorreu algum erro ao consultar o(s) usuário(s): {e}")
    finally:
        session.close()

def update_nome_usuario(id_usuario: Integer, nome_usuario: String):
    """
    Função para atualizar o nome do usuário no banco de dados
    """
    session = Session()
    try:
        if all([id_usuario, nome_usuario]):
            usuario = session.query(Usuario).filter(Usuario.id == id_usuario).first()
            usuario.nome = nome_usuario
            session.commit()
            print(f"Nome do usuário atualizado com sucesso!")
        else:
            print(f"É obrigatório informar o ID e o novo nome do usuário!")
    except Exception as e:
        session.rollback()
        print(f"Ocorreu um erro ao atualizar o usuário {id_usuario}: {e}")
    finally:
        session.close()

def delete_usuario(id_usuario: Integer):
    """
    Função para excluir um usuário do banco de dados
    """
    session = Session()
    try:
        if id_usuario:
            usuario = session.query(Usuario).filter(Usuario.id == id_usuario).first()
            session.delete(usuario)
            session.commit()
            print(f"Usuário de ID {id_usuario} deletado com sucesso!")
        else:
            print(f"É obrigatório informar o ID do usuário a ser deletado!")
    except Exception as e:
        session.rollback()
        print(f"Erro ao tentar deletar  o usuário de ID {id_usuario}: {e}")
    finally:
        session.close()

if __name__ == '__main__':
    os.system('clear')
    Base.metadata.create_all(engine)
    # insert_usuario("Lucas", "Convidado")
    # select_usuarios("Manuela")
    # update_nome_usuario(2, "Maria")
    delete_usuario(3)