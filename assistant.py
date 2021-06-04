'''Голосовой асистент созданный для упрощения рабочего 
экспирианса (Предпологаемы функции: считывание голоса,
обработка команд. Команды: выключение компьютера, 
открытие программ, поиск)'''

import pyttsx3

#озвучивание текста
engine = pyttsx3.init()
engine.say('СЛайв слайв слайв')
engine.runAndWait()


#комманды
opt = {
	'alias': ('слайв', 'раб', 'слеив' , 'факинг слэйв', 'слэйв', 
		'slave', 'fucking slave', 'слэив', 'факинг слэив',
		'факинг слеив'),
	'tbr': ('скажи', 'подскажи', 'произнеси', 'озвучь', 'сколько',
		'расскажи'),
	'cmds': {
		'music': ('включи музыку')
	}
}

#чтение комманды
def listen_command():
	x = input('Скажите вашу команду: ')
	return x

#выполнение комманды
def do_this_command(message):
	message = message.lower()

	if 'привет' in message:
		say_message("Привет dungeon master")
	elif 'пока' in message:
		say_message('Пока Boy next door')
		exit()
	else:
		say_message('я не понял твоей комманды slave')

#блок функций для выполнение комманд
def say_message(message):
	print(message)


#цикл для постоянного выпонлнения программы 
if __name__ == "__main__":
	while True:
		command = listen_command()
		do_this_command(command)