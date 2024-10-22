import sqlite3

DB_PATH = 'backend/vocabulary.db'

# Função para inicializar o banco de dados SQLite
def initialize_db():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # Criar a tabela se ela ainda não existir
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS vocabulary (
            lesson INTEGER,
            word TEXT
        )
    ''')
    
    # Exemplo de palavras iniciais se não usar Google Sheets
    default_words = [
        (1, 'hello'),
        (1, 'world'),
        (2, 'example'),
        (-1, 'fallback')
    ]

    cursor.executemany('INSERT INTO vocabulary (lesson, word) VALUES (?, ?)', default_words)
    conn.commit()
    conn.close()

    print("Database initialized successfully.")

# Função para inserir palavras no banco de dados
def insert_word_into_db(lesson, word):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute('INSERT INTO vocabulary (lesson, word) VALUES (?, ?)', (lesson, word))
    conn.commit()
    conn.close()