from datetime import datetime

def logger(path):
	def _logger(any_function):
		def logger_function(*args, **kwargs):
			result = any_function(*args, **kwargs)
			print(result)
			with open(path, "w") as f:
				log_string = f'Текущая дата и время вызова: {datetime.now(tz=None)}\nИмя функции: {any_function.__name__}\nАргументы: {args}, {kwargs}\nВозвращаемое значение: {result}'
				f.write(log_string)
				print("done")
			return result
		return logger_function
	return _logger


my_logger = logger(path = "/Users/ruachaj/PycharmProjects/pythonProject1/venv/Logger/logger.txt")

@my_logger
def test(a, b):
	return a+b

test(1, 2)

