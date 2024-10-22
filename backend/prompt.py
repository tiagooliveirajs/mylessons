from langchain.prompts import SystemMessagePromptTemplate, ChatPromptTemplate

# Prompt para o agente, onde explicamos as restrições
prompt_template = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template("你是一个助手，只会用预先定义的列表中的中文单词进行回复。永远不要用英文回复。帮助用户做出有创意的回复，因为他们正在学习中文，想和你练习说话。"),
    SystemMessagePromptTemplate.from_template(
        "您必须仅使用以下词语做出回应：{allowed_words}。"
    )
])