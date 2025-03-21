"""Игра угадай число не более чем за 20 попыток.
Компьютер сам загадывает и угадывает число
"""

import numpy as np

def game_core_v3(number: int = 1) -> int:
    """Сначала задаем начальное random число (predict), затем зная диапазон в котором загадано число, определяем его границы start и finish. 
    Создаем цикл, условием выхода из цикла будет равенство переданного в функцию числа (number) с подобранным числом (predict).
    В качестве условий сравниваем числа predict и number, и в зависимости от знака равенства < или > сдвигаем границы, 
    презаписывая значения переменных start или finish.
    Затем производим расчет нового значения для (predict) и снова сравниваем, до тех пор пока не угадаем (number), 
    т.е. когда выполнится условие number == predict

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    count = 0
    predict = np.random.randint(1, 101)
    start = 0
    finish = 101

    while number != predict:
        count += 1
        if predict < number:
            start = predict
        elif predict > number:
            finish = predict
        predict = (start + finish) // 2 

    return count
#game_core_v3()

def score_game(game_core_v3) -> int:
    """За какое количество попыток в среднем за 1000 подходов угадывает наш алгоритм

    Args:
        game_core_v3 ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    #np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000))  # загадали список чисел

    for number in random_array:
        count_ls.append(game_core_v3(number))

    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за: {score} попытки")

if __name__ == '__main__':
    
    score_game(game_core_v3)