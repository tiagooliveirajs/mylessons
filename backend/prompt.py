from langchain.prompts import SystemMessagePromptTemplate, ChatPromptTemplate

# Prompt para o agente, onde explicamos as restrições
prompt_template = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template("You are an assistant that only responds with words from a predefined list."),
    SystemMessagePromptTemplate.from_template(
        "You must provide a response using only the following words: {allowed_words}. "
        "If you cannot respond fully, apologize and say you can't complete the request fully."
    )
])