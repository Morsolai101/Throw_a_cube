import time
from random import randint
from pyfiglet import figlet_format
from plyer import notification


def roll_dice():
    """Генерує випадкове число від 1 до 4 (симуляція кидка кубика)."""
    return randint(1, 6)


def animate_dice_roll(result):
    """Здійснює анімацію кидка кубика відповідно до результату."""
    print("Кидок кубика...")

    dice_frames = {
        1: [
            "   _______   ",
            "  |       |  ",
            "  |   *   |  ",
            "  |       |  ",
            "   -------   "
        ],
        2: [
            "   _______   ",
            "  |     * |  ",
            "  |       |  ",
            "  | *     |  ",
            "   -------   "
        ],
        3: [
            "   _______   ",
            "  | *     |  ",
            "  |   *   |  ",
            "  |     * |  ",
            "   -------   "
        ],
        4: [
            "   _______   ",
            "  | *   * |  ",
            "  |       |  ",
            "  | *   * |  ",
            "   -------   "
        ],
        5: [
            "   _______   ",
            "  | *   * |  ",
            "  |   *   |  ",
            "  | *   * |  ",
            "   -------   "
        ],
        6: [
            "   _______   ",
            "  |  *  * |  ",
            "  |  *  * |  ",
            "  |  *  * |  ",
            "   -------   "
        ]
    }

    for frame in dice_frames[result]:
        print(frame)
        time.sleep(0.4)


def achivky_permoga(permoga):
    Balu = f"{permoga} Балів"
    Vugralu = f"Ви виграли {permoga} разів. Фартуна на вашій стороні."
    if permoga > 10:
        if permoga > 20:
            if permoga > 40:
                if permoga > 80:
                    if permoga > 100:
                        notification.notify(
                            title=Balu,
                            message=Vugralu,
                            app_icon=None
                        )
                elif permoga == 80:
                    notification.notify(
                        title=Balu,
                        message=Vugralu,
                        app_icon=None
                    )
            elif permoga == 40:
                notification.notify(
                    title=Balu,
                    message=Vugralu,
                    app_icon=None
                )
        elif permoga == 20:
            notification.notify(
                title=Balu,
                message=Vugralu,
                app_icon=None
            )
    elif permoga == 10:
        notification.notify(
            title=Balu,
            message=Vugralu,
            app_icon=None
        )


def achivky_lose(lose):
    Progra = f"{lose} Пройграшів"
    Progralu = f"Ви програли {lose} разів. Фартуна на вашій стороні."
    if lose > 10:
        if lose > 20:
            if lose > 40:
                if lose > 80:
                    if lose > 100:
                        notification.notify(
                            title=Progra,
                            message=Progralu,
                            app_icon=None
                        )
                elif lose == 80:
                    notification.notify(
                        title=Progra,
                        message=Progralu,
                        app_icon=None
                    )
            elif lose == 40:
                notification.notify(
                    title=Progra,
                    message=Progralu,
                    app_icon=None
                )
        elif lose == 20:
            notification.notify(
                title=Progra,
                message=Progralu,
                app_icon=None
            )
    elif lose == 10:
        notification.notify(
            title=Progra,
            message=Progralu,
            app_icon=None
        )


def main():
    win_count = 0
    lose_count = 0

    while True:
        print(
            f"Вгадайте число від 1 до 6 або введіть 'exit' для виходу (Виграші: {win_count}, Програші: {lose_count}):")
        guess = input()

        if guess == 'exit':
            break

        if guess.isnumeric():
            guess = int(guess)
            if 1 <= guess <= 6:
                dice_roll = roll_dice()
                animate_dice_roll(dice_roll)
                print(f"Випало число {dice_roll}")

                if guess == dice_roll:
                    print("Ви вгадали!")
                    win_count += 1
                    achivky_permoga(win_count)

                else:
                    print("Ви не вгадали. Спробуйте ще раз.")
                    achivky_lose(lose_count)
                    lose_count += 1
            else:
                # Повідомлення про невірний ввід
                print("Будь ласка, введіть число від 1 до 6.")
        else:
            # Повідомлення про невірний ввід
            print("Будь ласка, введіть числове значення або 'exsit' для виходу.")

    # Вивід результату гри
    print(
        f"Гра закінчена. Ви програли {win_count} разів і програли {lose_count} разів.")


if __name__ == "__main__":
    print(figlet_format("Throw a cube!"))
    main()