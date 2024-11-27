import requests

URL = 'http://127.0.0.1:8000/livros/'

def requisicao(metodo, endpoint='', dados=None, params=None):
	url_completa = URL + endpoint
	try:
		match metodo:
			case 'GET':
				response = requests.get(url_completa)
			case 'POST':
				response = requests.post(url_completa, dados)
			case 'PUT':
				response = requests.put(url_completa, params)
			case 'DELETE':
				response = requests.delete(url_completa)
		return response
	except requests.exceptions.ConnectionError as e:
		return f'Erro de conexão: {e}'

def lista_livros():
	response = requisicao('GET')
	livros = response.json()
	return livros

def adiciona_livro(titulo, autor, genero, lido, nota):
	livro = {'titulo': titulo, 'autor': autor, 'genero': genero, 'lido': lido, 'avaliacao': nota}
	return requisicao('POST', dados=livro)

def atualiza_livro(id, titulo, autor, genero, lido, nota):
	livro = {'id': id, 'titulo': titulo, 'autor': autor, 'genero': genero, 'lido': lido, 'avaliacao': nota}
	return requisicao('PUT', endpoint=str(id), params=livro)

def remove_livro(id):
	confirma = str(input('Tem certeza que deseja excluir esse titulo? (S/N): ')).lower()
	if confirma == 's':
		return requisicao('DELETE', endpoint=str(id))
	return 'Deleção cancelada, o título será mantido na biblioteca :)'