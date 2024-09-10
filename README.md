# Dumb Telegram Bot

Dumb (formerly pobot) is a minimalistic, idiotic LLM-based chatbot for Telegram.
Given the history of a Telegram conversation, Dumb can mimic a user, their janky syntax and awful political position.

# Usage

Dumb can be called with the following command:

```/mimic <user> <theme>```

For instance:

![Example usage](/docs/img/dumb_bot.png)


## Main Features

- It is mostly french
- Can retrieve the syntaxical style of a user, by using querying a Telegram Chat history export
- 

## Requirements to build and run your own instance

### Get a Telegram Bot API Token

To use this bot, you need to create your own bot account and, most importantly, you must bring your own Telegram API bot token.
Get started by sending `/start` to [@BotFather](https://telegram.me/BotFather). You can find more information about telegram bots [*here*](https://core.telegram.org/bots).

### Get an Open API key

All you need is [here](https://help.openai.com/en/articles/7039783-how-can-i-access-the-chatgpt-api).


### Export a Telegram Chat history

**Caution:** Your Telegram Chat History will be passed to OpenAI APIs. In case you don't want to leak private information to a provider that will definitely use, analyse and train LLMs on your data, **don't use this bot**.

Dumb uses a local export of a Chat history to mimic a given user, based on their previous posts.



## Getting started

### Local python execution (Linux)

Clone the repo first:

 ```
 git clone https://github.com/RaphPfister/dumb-telegram-bot.git && cd dumb-telegram-bot/
 ```

Create a python 3.11 conda environment and install the requirements:

```bash
conda create -n dumb-bot311 python=3.11
conda activate dumb-bot311
# In case conda encounters an error, run
# `source activate`
# before activating your conda environment
```

Set your OpenAI key and Telegram token as environment variables with:

```bash
export OPENAI_API_KEY=...
export TELEGRAM_API_TOKEN=...
```

Run the bot
```
python dumb_telegram_bot/bot.py 
```


### Install and run via pip

*WIP*

### Remote Docker execution & deploy to production

*WIP*


# How it works

![architecture](/docs/img/architecture.png)


## Known limitations

Despite our efforts, Dumb can sometimes lose the mimicked user personnality and can thus fall back into a **lame, naive, blank ChatGPT behaviour**. Eww.

Increasing the size of the randomized context (with the `--n-samples` argument) can sometimes help improving the quality, for a more personnalized result.