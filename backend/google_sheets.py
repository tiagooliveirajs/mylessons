# backend/google_sheets.py

import os
import gspread
from google.oauth2.service_account import Credentials
from backend.words_repository import insert_word_into_db
from dotenv import load_dotenv

# Carregar variáveis de ambiente do arquivo .env
load_dotenv()

# Definir os escopos que vamos usar para acessar o Google Sheets
SCOPES = ['https://www.googleapis.com/auth/spreadsheets.readonly']

# URL da planilha do Google, obtida do arquivo .env
SPREADSHEET_URL = os.getenv("GOOGLE_SHEET_URL")

def populate_db_from_sheets():
    """Função para popular o banco de dados a partir do Google Sheets"""
    
    # Verifica se o arquivo de credenciais existe
    if not os.path.exists('credentials.json'):
        print("Google Sheets credentials not found.")
        return
    
    if not SPREADSHEET_URL:
        print("Google Sheet URL not found in environment variables.")
        return
    
    try:
        # Autenticação com Google Sheets
        creds = Credentials.from_service_account_file('credentials.json', scopes=SCOPES)
        client = gspread.authorize(creds)
        
        # Abrir a planilha pelo URL
        sheet = client.open_by_url(SPREADSHEET_URL).sheet1
        rows = sheet.get_all_values()

        # Iterar sobre as linhas da planilha
        for row in rows:
            lesson = row[0]
            words = row[1].split()  # Assume que as palavras são separadas por espaços
            
            # Se a célula de "lesson" estiver vazia, atribuir -1
            lesson = -1 if not lesson else int(lesson)
            
            # Inserir cada palavra no banco de dados
            for word in words:
                if word:
                    insert_word_into_db(lesson, word)

        print("Database populated successfully from Google Sheets.")
    
    except Exception as e:
        print(f"An error occurred while accessing the Google Sheet: {e}")