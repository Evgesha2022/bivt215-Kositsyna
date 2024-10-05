#!/usr/bin/env python3
import sys
import os

# Добавляем корневую директорию проекта в пути поиска модулей
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.cli import welcome_user  # noqa: E402
from src.engine import play_game  # noqa: E402
from games.nok import get_question as nok_question  # noqa: E402
from games.geom_progr import get_question as progression_question  # noqa: E402

# Меню с играми
games = {
    "1": {
        "name": "Least Common Multiple (LCM)",
        "get_question": nok_question,
    },
    "2": {
        "name": "Geometric Progression",
        "get_question": progression_question,
    },
}


def main():
    player_name = welcome_user()

    # Выводим меню с играми
    print("\nPlease choose a game:")
    for key, game in games.items():
        print(f"{key}: {game['name']}")

    # Получаем выбор пользователя
    choice = input("\nEnter the number of the game you want to play: ")

    # Проверяем выбор и запускаем выбранную игру
    if choice in games:
        print(f"\nYou chose: {games[choice]['name']}\n")
        play_game(games[choice], player_name)
    else:
        print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
