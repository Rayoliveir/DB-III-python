from services.usuario_service import UsuarioService
from repositories.usuario_repository import UsuarioRepository
from config.database import Session
import os


def main():
    session = Session()
    repository = UsuarioRepository(session)
    service = UsuarioService(repository)

    print("Adicionar usuario")
    nome = input("Nome: ")
    email = input("E-mail: ")
    senha = input("Senha: ")

    service.criar_usuario(nome=nome, email=email, senha=senha)

    print("\n- Lista de todos os usuarios cadastrados -")
    lista_usuarios = service.listar_todos_usuarios()
    for usuario in lista_usuarios:
        print(
            f"\nNome: {usuario.nome} \nE-mail: {usuario.email} \nSenha: {usuario.senha}"
        )


if __name__ == "__main__":
    os.system("cls || clear")
    main()
