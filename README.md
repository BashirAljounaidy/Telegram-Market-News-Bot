# Telegram Echo Bot

This is a simple Telegram echo bot that replies with the same message that it receives.

## Requirements

- Python 3.6 or later
- Telethon library
- python-dotenv

## Installation

1.  Clone or download the repository
2.  Create a `.env` file in the root of the project and set your telegram api id, api hash and bot token in it.

Copy code

`TELEGRAM_API_ID=your_api_id
TELEGRAM_API_HASH=your_api_hash
TELEGRAM_BOT_TOKEN=your_bot_token`

3.  Install the dependencies:

Copy code

`pip install -r requirements.txt`

4.  Run the script:

Copy code

`python bot.py`

## Usage

1.  Start the bot by running the script
2.  Send a message to the bot starting with "/news"
3.  The bot will reply with "market news"
4.  You can also pass an argument after the command like "/news aapl"
5.  The bot will reply with "market news aapl"

Please keep in mind that, you need to have a valid bot token which is generated by botfather in telegram, and the bot should be added to the group or channel, in order to use it.

## Note

This bot only checks for one argument after the command, if there is any space after the argument it will not work as expected.

## License

This project is licensed under the MIT License.

## Acknowledgments

- Telethon library
- python-dotenv

This should give users a good idea of how to set up and use the Telegram echo bot script.

Please keep in mind that, you need to create a `requirements.txt` file with the dependencies in order to run the script. It should have the following lines:

Copy code

`telethon
python-dotenv`
