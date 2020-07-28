import numpy as np
def game_core_v5(number):
    count = 0
    
    predict = np.random.randint(1,101)
    lower_boundary = 1
    upper_boundary = 100
    while number!= predict:
        # Увеличиваем count
        count += 1 
        # Сдвигаем границы
        if predict < number:
            lower_boundary = predict  
        elif predict > number:
            upper_boundary = predict
        # Пересчитываем границы
        predict = np.random.randint(lower_boundary, upper_boundary + 1)
    return(count)

def score_game(game_core):
    count_ls = []
    np.random.seed(1)
    random_array = np.random.randint(1,101, size=(1000))
    for number in random_array:
        count_ls.append(game_core(number))
    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за {score} попыток")
    return(score)

score_game(game_core_v5)