from Logger import logger

nested_list = [
    ['a', 'b', 'c'],
    ['d', 'e', 'f'],
    [1, 2, None],
]

my_logger = logger(path = "/Users/ruachaj/PycharmProjects/pythonProject1/venv/Logger/logger.txt")

@my_logger
def flat_generator(any_list):
    for x in range(len(any_list)):
        for y in range(len(any_list[x])):
            yield any_list[x][y]

for item in flat_generator(nested_list):
    print(item)
