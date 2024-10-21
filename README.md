# MyLessons Bot

MyLessons is a Telegram bot that interacts with the LM Studio API, responding to users based on a predefined list of allowed words. It uses Langchain to manage communication with the large language model (LLM).

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/mylessons.git
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Create a `.env` file in the project root and add your Telegram bot token and LM Studio API URL:
   ```
   TELEGRAMBOT_TOKEN=your-telegram-bot-token
   LMSTUDIOAPI_URL=your-lm-studio-url
   ```

4. Run the bot:
   ```
   python run.py
   ```

## Usage

The bot is designed to respond to user inputs using only a predefined list of words. If a response contains words outside of this list, it will ask the LLM to reformulate the response.

## Development

Feel free to modify the `words.json` file to change the list of allowed words or expand the functionality by editing the `backend` and `frontend` modules.

## License

This project is licensed under the GNU GENERAL PUBLIC LICENSE.