from services.usuario_service import UsuarioService
from repositories.usuario_repository import UsuarioRepository
from config.database import Session

def main():
    session = Session()
    repository = UsuarioRepository(session)
    service = UsuarioService(repository)

    print("Adicionar usuario")
    nome = input("\nNome: ")
    email = input("\nE-mail: ")
    senha = input("\nSenha: ")

    service.criar_usuario(nome=nome, email=email, senha=senha)

    print("\nLista de todos os usuarios cadastrados")
    lista_usuarios = service.listar_todos_usuarios()
    for usuario in lista_usuarios:
        print(f"\nNome: {usuario.nome} \nE-mail: {usuario.email} \nSenha: {usuario.senha}")

if __name__ == "__main__":
    main()