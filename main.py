"""Module for create your game-character."""
from random import randint


from graphic_arts.start_game_banner import run_screensaver


DEFAULT_ATTACK = 5
DEFAULT_DEFENCE = 10
DEFAULT_STAMINA = 80


class Character:
    BRIEF_DESC_CHAR_CLASS = 'отважный любитель приключений'
    RANGE_VALUE_ATTACK = (1, 3)
    RANGE_VALUE_DEFENCE = (5, 10)
    SPECIAL_BUFF = 15
    SPECUAL_SKILL = 'Luck'
    
    def __init__(self, name):
        self.name = name
    
    def attack(self):
        value_attack = DEFAULT_ATTACK + randint(*self.RANGE_VALUE_ATTACK)
        return (f'{self.name} нанёс противнику {value_attack} урона')
    
    def deffence(self):
        value_defence = randint(*self.RANGE_VALUE_DEFENCE)
        return (f'{self.name} блокировал {DEFAULT_DEFENCE + value_defence}'
                'ед. урона')
    
    def special(self):
        return (f'{self.name} применил специальное умение'
                f'"{self.SPECUAL_SKILL} {self.SPECIAL_BUFF}"')
    
    def __str__(self):
        return f'{self.__class__.__name__} - {self.BRIEF_DESC_CHAR_CLASS}.'
        

class Warrior(Character):
    BRIEF_DESC_CHAR_CLASS = (' дерзкий воин ближнего боя. '
                             'Сильный, выносливый и отважный')
    RANGE_VALUE_ATTACK = (3, 5)
    RANGE_VALUE_DEFENCE = (5, 10)
    SPECIAL_BUFF = DEFAULT_STAMINA + 25
    SPECIAL_SKILL = 'Выносливость'


class Mage(Character):
    BRIEF_DESC_CHAR_CLASS = (' находчивый воин дальнего боя. '
                             'Обладает высоким интеллектом')
    RANGE_VALUE_ATTACK = (5, 10)
    RANGE_VALUE_DEFENCE = (-2, 2)
    SPECIAL_BUFF = DEFAULT_ATTACK + 40
    SPECIAL_SKILL = 'Атака'


class Healer(Character):
    BRIEF_DESC_CHAR_CLASS = (' могущественный заклинатель. '
                             'Черпает силы из природы, веры и духов')
    RANGE_VALUE_ATTACK = (-3, -1)
    RANGE_VALUE_DEFENCE = (2, 5)
    SPECIAL_BUFF = DEFAULT_DEFENCE + 30
    SPECIAL_SKILL = 'Защита'


def start_training(char_name: str, char_class: Character) -> str:
    print(f'{char_class.BRIEF_DESC_CHAR_CLASS}')
    print('Потренируйся управлять своими навыками.')
    print('Введи одну из команд: attack — чтобы атаковать противника, '
          'defence — чтобы блокировать атаку противника или '
          'special — чтобы использовать свою суперсилу.')
    print('Если не хочешь тренироваться, введи команду skip.')
    cmd: str = None
    while cmd != 'skip':
        cmd = input('Введи команду: ')
        if cmd == 'attack':
            print(f'{char_class.attack()}')
        if cmd == 'defence':
            print(f'{char_class.deffence()}')
        if cmd == 'special':
            print(f'{char_class.special()}')
    return 'Тренировка окончена.'


def choice_char_class(char_name):
    """Function for selecting character class."""
    game_classes = {'warrior': Warrior, 'mage': Mage, 'healer': Healer}
    approve_choice = None
    
    while approve_choice != 'y':
        selected_class = input('Введи название персонажа,за которого хочешь '
                               'играть: Воитель — warrior, Маг — mage, Лекарь '
                               '— healer: ')
        char_class: Character = game_classes[selected_class](char_name)
        print(char_class)
        approve_choice = input('Нажми (Y), чтобы подтвердить выбор, '
                               'или любую другую кнопку, '
                               'чтобы выбрать другого персонажа ').lower()
    return char_class


if __name__ == '__main__':
    run_screensaver()
    print('Приветствую тебя, искатель приключений!')
    print('Прежде чем начать игру...')
    char_name: str = input('...назови себя: ')
    print(f'Здравствуй, {char_name}! '
          'Сейчас твоя выносливость — 80, атака — 5 и защита — 10.')
    print('Ты можешь выбрать один из трёх путей силы:')
    print('Воитель, Маг, Лекарь')
    char_class: str = choice_char_class(char_name)
    print(start_training(char_name, char_class))
