from telegram import Update
from telegram.ext import CallbackContext
from backend.lm_studio_llm import LMStudioLLM
from backend.prompt import prompt_template
from backend.validator import is_valid_response
from langchain import LLMChain

# Load words from words.json for validation
import json
with open('backend/words.json', 'r') as f:
    data = json.load(f)
allowed_words = set(data['words'])

# Função chamada quando o comando /start é recebido
async def start(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text("Welcome to the bot!")

# Função que lida com as mensagens do usuário
async def handle_message(update: Update, context: CallbackContext) -> None:
    user_input = update.message.text

    # Criar uma instância da LLM personalizada para o LangChain
    llm = LMStudioLLM()

    try:
        # Gerar uma resposta usando LangChain
        chain = LLMChain(llm=llm, prompt=prompt_template)
        agent_response = chain.run({
            "allowed_words": ', '.join(allowed_words),
            "input": user_input
        })

        # Verificar se a resposta é válida
        if is_valid_response(agent_response, allowed_words):
            await update.message.reply_text(agent_response)
        else:
            # Se a resposta não for válida, pedir à LLM para reformular a resposta
            agent_response = chain.run({
                "allowed_words": ', '.join(allowed_words),
                "input": user_input
            })
            await update.message.reply_text(agent_response)

    except Exception as e:
        await update.message.reply_text(f"An error occurred: {e}")