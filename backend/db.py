# backend/db.py

import sqlite3

DB_PATH = 'backend/words.db'  # Certifique-se de que o caminho está correto

def get_db_connection():
    """Função que retorna uma conexão com o banco de dados."""
    conn = sqlite3.connect(DB_PATH)
    return conn

# Função para inicializar o banco de dados SQLite
def initialize_db():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # Criar a tabela 'words' se ela ainda não existir
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS words (
            lesson INTEGER,
            word TEXT UNIQUE
        )
    ''')

    # Exemplo de palavras iniciais se não usar Google Sheets
    default_words = [
        (1, '你好'),
        (1, '张伟'),
        (2, '叫'),
        (-1, '你'),
        (-1, '名字')
    ]

    cursor.executemany('INSERT INTO words (lesson, word) VALUES (?, ?)', default_words)
    conn.commit()
    conn.close()

    print("Database initialized successfully.")

# Função para inserir palavras no banco de dados
def insert_word_into_db(lesson, word):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute('INSERT INTO words (lesson, word) VALUES (?, ?)', (lesson, word))
    conn.commit()
    conn.close()

# Função para buscar todas as palavras da tabela words
def fetch_all_words():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    cursor.execute("SELECT word FROM words")
    rows = cursor.fetchall()
    
    conn.close()
    
    # Extrair apenas as palavras da consulta
    return [row[0] for row in rows]