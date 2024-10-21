# Função para verificar se todas as palavras na resposta estão na lista permitidas
def is_valid_response(response: str, allowed_words: set) -> bool:
    return all(word.lower() in allowed_words for word in response.split())