import os
from backend.db import initialize_db  # Função que inicializa e popula o banco de dados
from backend.google_sheets import populate_db_from_sheets

# Verifica se o arquivo credentials.json existe
if os.path.exists('credentials.json'):
    print("Google Sheets credentials found. Populating database from Google Sheets...")
    populate_db_from_sheets()  # Função que popula o banco de dados a partir da planilha Google Sheets
else:
    print("Google Sheets credentials not found. Skipping Google Sheets integration.")
    initialize_db()  # Inicializa o banco de dados sem Google Sheets

# Aqui você iniciaria o bot, ou qualquer outra funcionalidade principal
from frontend.telegram_bot import start_bot

if __name__ == "__main__":
    start_bot()