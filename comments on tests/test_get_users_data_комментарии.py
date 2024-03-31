#Импортируем из файла contracts необходимую нам схему
    from core.contracts import USER_DATA_SCHEMA

#Кладем в соответствующую переменную необходимый нам json для дальнейшего взаимодействия с ним
    users_data = response.json()['data']

#Для каждого элемента из списка users_data выполняются определенные действия ("Цикл")
    for item in users_data:
        validate(response.json()['data'], USER_DATA_SCHEMA)

#Подтверди, что
    assert
