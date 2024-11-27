from api.consulta_api import lista_livros, adiciona_livro, remove_livro, atualiza_livro
from ia.recomendacao import recomenda
import time

def menu():
	print(r'''
 | |__   ___   ___ | | _____ 
 | '_ \ / _ \ / _ \| |/ / __|
 | |_) | (_) | (_) |   <\__ \
 |_.__/ \___/ \___/|_|\_\___/ ''')
	print('''\nMenu:
1 - Listar livros da minha biblioteca
2 - Adicionar um livro a minha biblioteca
3 - Atualizar dado de um livro
4 - Remover um livro
5 - Consultar recomendações baseadas no meu gosto

0 - Sair''')
	escolha = int(input('Escolha uma opção: '))
	match escolha:
		case 1:
			livros = lista_livros()
			for livro in livros:
				id = livro['id']
				titulo = livro['titulo']
				autor = livro['autor']
				genero = livro['genero']
				lido = livro['lido']
				avaliacao = livro['avaliacao']
				print(f'''
ID: {id}
Título: {titulo}
Autor: {autor}
Gênero: {genero}
Lido: {'☑' if lido == True else '☐'}
Nota: {avaliacao}''')
			time.sleep(2)
			menu()
		case 2:
			titulo, autor, genero, lido, nota = pega_dados_livro()
			adiciona_livro(titulo, autor, genero, lido, nota)
			time.sleep(2)
			menu()
		case 3:
			id = int(input('Qual o ID do livro que você deseja atualizar? '))
			titulo, autor, genero, lido, nota = pega_dados_livro()
			print(atualiza_livro(id, titulo, autor, genero, lido, nota))
		case 4:
			id = int(input('Qual o ID do livro que você deseja excluir? '))
			print(remove_livro(id))
			time.sleep(2)
			menu()
		case 5:
			recomenda()
			time.sleep(2)
			menu()
		case 0:
			print('Saindo...')
		case _:
			print('Opção inválida...')
			time.sleep(2)
			menu()

def pega_dados_livro():
	titulo = str(input('Titulo: '))
	autor = str(input('Autor: '))
	genero = str(input('Gênero (F/NF): '))
	lido = str(input('Lido? (S/N): ')).lower()
	if lido == 's':
		lido = True
	else:
		lido = False
	nota = str(input('Avaliação (0-5 ou em branco): ')).strip()
	if nota == '':
		nota = None
	else:
		nota = int(nota)

	return titulo, autor, genero, lido, nota

if __name__ == '__main__':
	menu()