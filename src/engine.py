MAX_ROUNDS = 3  # Количество раундов


def play_game(game, player_name):

    print("Welcome to the Brain Games!")

    for round_num in range(MAX_ROUNDS):
        # Получаем вопрос и правильный ответ
        question, correct_answer = game['get_question']()

        # Показываем вопрос игроку
        print(f"Question: {question}")

        # Получаем ответ от игрока
        player_answer = input("Your answer: ")

        # Проверяем ответ
        if player_answer == str(correct_answer):
            print("Correct!")
        else:
            print(
                f"'{player_answer}' is wrong answer ;(. "
                f"Correct answer was '{correct_answer}'."
            )
            print(f"Let's try again, {player_name}!")
            return

    # Если игрок правильно ответил на все вопросы
    print(f"Congratulations, {player_name}!")
