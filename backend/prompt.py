from langchain.prompts import SystemMessagePromptTemplate, ChatPromptTemplate

# Prompt para o agente, onde explicamos as restrições
prompt_template = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template("You are an assistant that only responds with words from a predefined list. Identify the predominant language from the list. Help the user with creative responses, as they are learning that language and want to chat with you to practice it."),
    SystemMessagePromptTemplate.from_template(
        "You must provide a response using only the following words: {allowed_words}. "
        "If you cannot respond fully, apologize and say you can't complete the request fully."
    )
])