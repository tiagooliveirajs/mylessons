from backend.db import fetch_all_words

# Função para verificar se todas as palavras na resposta estão na lista de palavras permitidas no banco de dados
def is_valid_response(response: str) -> bool:
    # Buscar todas as palavras permitidas no banco de dados
    allowed_words = fetch_all_words()
    
    # Converter para um set para facilitar a busca
    allowed_words_set = set(word.lower() for word in allowed_words)
    
    # Verificar se todas as palavras da resposta estão no conjunto de palavras permitidas
    return all(word.lower() in allowed_words_set for word in response.split())