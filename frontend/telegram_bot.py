import os
from dotenv import load_dotenv
from telegram.ext import Application, CommandHandler, MessageHandler, filters
from frontend.bot_handlers import start, handle_message

# Carregar as variáveis de ambiente
load_dotenv()
TOKEN = os.getenv("TELEGRAMBOT_TOKEN")

# Função principal para configurar o bot
def start_bot():  # Alterado de 'main' para 'start_bot'
    # Criar a aplicação do Telegram bot
    application = Application.builder().token(TOKEN).build()

    # Adicionar o comando /start e o handler para mensagens
    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    # Iniciar o bot
    application.run_polling()

if __name__ == "__main__":
    start_bot()  # Alterado de 'main' para 'start_bot'