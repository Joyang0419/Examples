# # unfit OCP example
# class Animal:
#     def __init__(self, name: str):
#         self.name = name
#
#     def get_name(self) -> str:
#         pass
#
#
# def animal_sound(animals: list):
#     for animal in animals:
#         if animal.name == 'lion':
#             print('roar')
#         elif animal.name == 'mouse':
#             print('squeak')
#         elif animal.name == 'snake':
#             print('hiss')
#         elif animal.name == 'people':
#             print('hello world')
#
#
# if __name__ == "__main__":
#     animals = [
#         Animal('lion'),
#         Animal('mouse'),
#         Animal('snake')
#     ]
#     animal_sound(animals)


# fit OCP principle

from typing import List


class Animal:
    def __init__(self, name: str):
        self.name = name

    def make_sound(self):
        pass


class Lion(Animal):
    def make_sound(self):
        return 'roar'


class Mouse(Animal):
    def make_sound(self):
        return 'squeak'


class Snake(Animal):
    def make_sound(self):
        return 'hiss'


class People(Animal):
    def make_sound(self):
        return "hello_world"


def animal_sound(animals: List[Animal]):
    for animal in animals:
        print(animal.make_sound())


if __name__ == "__main__":
    animals = [
        Lion(name="LionKing"),
        Snake(name="SnakeKing"),
        People(name="Joy")
    ]

    animal_sound(animals)




