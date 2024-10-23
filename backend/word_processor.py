# backend/word_processor.py
import jieba
import nltk
from backend.words_repository import insert_word_into_db, word_exists_in_db

# Baixar recursos do NLTK necessários (apenas uma vez)
nltk.download('punkt')

def process_user_input(user_input: str):
    """Processa a entrada do usuário para segmentar e inserir novas palavras no banco de dados."""
    
    # Dividir palavras latinas usando nltk
    latin_words = nltk.word_tokenize(user_input)

    # Dividir palavras chinesas usando jieba
    chinese_words = list(jieba.cut(user_input))

    # Combinar os dois conjuntos de palavras
    words = latin_words + chinese_words

    # Iterar sobre as palavras e verificar se já existem no banco de dados
    for word in words:
        word = word.strip()  # Remove espaços em branco desnecessários
        if word and not word_exists_in_db(word):
            insert_word_into_db(-3, word)  # Inserir com a lesson = -3
    return words