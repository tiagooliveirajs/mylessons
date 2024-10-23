# backend/google_sheets_integration.py

from backend.words_repository import word_exists_in_db, insert_word_into_db, get_lesson_for_word

# Variável para controlar a inserção de dados da planilha
ALLOW_SHEET_INSERTION = True  # Defina como True se quiser permitir a inserção dos dados da planilha

def populate_db_from_sheets(sheet_rows):
    """Popula o banco de dados a partir dos dados da planilha Google Sheets."""
    if not ALLOW_SHEET_INSERTION:
        print("Insertion from Google Sheets is disabled.")
        return
    
    for row in sheet_rows:
        lesson = row[0]
        words = row[1].split() if len(row) > 1 and row[1] else None  # Palavra(s) na segunda coluna

        # Regra 2: Ignorar linhas sem palavras
        if not words:
            continue

        # Regra 1: Quando a primeira e a segunda coluna estão preenchidas
        if lesson and words:
            lesson = int(lesson)
            for word in words:
                if not word_exists_in_db(word):
                    insert_word_into_db(lesson, word)
                else:
                    # Regra 4: Atualizar 'lesson' se for diferente
                    current_lesson = get_lesson_for_word(word)
                    if current_lesson != lesson:
                        insert_word_into_db(lesson, word)

        # Regra 3: Quando há apenas palavras e a primeira coluna está vazia
        elif not lesson and words:
            for word in words:
                if not word_exists_in_db(word):
                    insert_word_into_db(-1, word)  # Definir lesson como -1
                else:
                    # Atualiza o lesson para -1 se for diferente
                    current_lesson = get_lesson_for_word(word)
                    if current_lesson != -1:
                        insert_word_into_db(-1, word)

    print("Database populated from Google Sheets.")