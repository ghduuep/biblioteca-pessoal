import google.generativeai as genai
import os
from dotenv import load_dotenv
from api.consulta_api import lista_livros

load_dotenv()

genai.configure(api_key=os.getenv("API_KEY"))

def recomenda():
	model = genai.GenerativeModel(model_name="gemini-1.5-flash", system_instruction="Você é uma IA integrada em um sistema de livros. Você recebera uma lista de livros com suas avaliacoes e recomendara outros titulos semelhantes")
	livros = lista_livros()
	response = model.generate_content(f'Recomende titulos semelhantes aos de maior nota dessa lista: {livros}')
	print(response.text)