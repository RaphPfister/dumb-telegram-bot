"""
cli and app runner
"""
import argparse

from dumb_telegram_bot import bot


def parse_args():

    arg_parser = argparse.ArgumentParser()

    arg_parser.add_argument(
        "--n-samples",
        type=int,
        default=300,
        required=False,
        help="Size of the randomized history context"
    )
    arg_parser.add_argument(
        "--telegram-json-history",
        type=str,
        default="data/result.json",
        required=False,
        help="Path to the json export of a telegram chat, likely named result.json"
    )
    args = arg_parser.parse_args()
    return args


if __name__=="__main__":

    args = parse_args()

    args.n_samples
    args.telegram_json_history

    bot_instance = bot.create_bot_routes(n_samples=args.n_samples, telegram_json_history=args.telegram_json_history)
    bot_instance.infinity_polling()
