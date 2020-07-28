import numpy as np

LOWER_PREDICTED_NUMBER = 1
UPPER_PREDICTED_NUMBER = 100

def do_predict(lower_boundary, upper_boundary):
    return (np.random.randint(lower_boundary, upper_boundary + 1))

def game_core_v5(number, lower_boundary, upper_boundary):
    count = 0
    
    predict = do_predict(lower_boundary, upper_boundary)
    while number!= predict:
        # Увеличиваем count
        count += 1 
        # Сдвигаем границы
        if predict < number:
            lower_boundary = predict  
        elif predict > number:
            upper_boundary = predict
        # Пересчитываем границы
        predict = do_predict(lower_boundary, upper_boundary)
    return(count)

def score_game(game_core, lower_predicted_number, upper_predicted_number):
    count_ls = []
    np.random.seed(1)
    random_array = np.random.randint(lower_predicted_number, upper_predicted_number + 1, size=(1000))
    for number in random_array:
        count_ls.append(game_core(number, lower_predicted_number, upper_predicted_number))
    score = int(np.mean(count_ls))
    print("Ваш алгоритм угадывает число в среднем за", score, "попыток")
    return(score)

score_game(game_core_v5, LOWER_PREDICTED_NUMBER, UPPER_PREDICTED_NUMBER)