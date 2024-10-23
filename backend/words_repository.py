# backend/words_repository.py

from backend.db import get_db_connection

def word_exists_in_db(word: str) -> bool:
    """Verifica se a palavra já existe no banco de dados."""
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM words WHERE word = ?", (word,))
    result = cursor.fetchone()[0]
    conn.close()
    return result > 0

def get_lesson_for_word(word: str) -> int:
    """Busca o valor de lesson para uma palavra existente no banco de dados."""
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT lesson FROM words WHERE word = ?", (word,))
    result = cursor.fetchone()
    conn.close()
    return result[0] if result else None

def insert_word_into_db(lesson: int, word: str) -> None:
    """Insere uma nova palavra no banco de dados, ou atualiza o valor de lesson se a palavra já existir."""
    conn = get_db_connection()
    cursor = conn.cursor()

    if word_exists_in_db(word):
        # Verifica a lição atual e atualiza caso seja diferente
        current_lesson = get_lesson_for_word(word)
        if current_lesson != lesson:
            cursor.execute("UPDATE words SET lesson = ? WHERE word = ?", (lesson, word))
    else:
        # Insere nova palavra com lição associada
        cursor.execute("INSERT INTO words (lesson, word) VALUES (?, ?)", (lesson, word))

    conn.commit()
    conn.close()

def fetch_all_words():
    """Busca todas as palavras da tabela words."""
    conn = get_db_connection()
    cursor = conn.cursor()
    
    cursor.execute("SELECT word FROM words")
    rows = cursor.fetchall()
    
    conn.close()
    
    # Extrair apenas as palavras da consulta
    return [row[0] for row in rows]