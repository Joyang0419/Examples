# """
# wrong example
# The sub-class whale can still invoke the method “walk” but it shouldn’t, and we must avoid it.
# """
#
#
# class Mammals:
#     @staticmethod
#     def swim():
#         print("Can Swim")
#
#     @staticmethod
#     def walk():
#         print("Can Walk")
#
#
# class Human(Mammals):
#     pass
#
#
# class Whale(Mammals):
#     pass
#
#
# if __name__ == "__main__":
#     Human.swim()  # Humans can swim
#     Human.walk()  # Humans can walk
#
#     Whale.swim()  # Whales can swim
#     Whale.walk()  # Can Walk

"""
good example
"""


class Walker:
    @staticmethod
    def walk():
        return print("Can Walk")


class Swimmer:
    @staticmethod
    def swim():
        return print("Can Swim")


class Human(Walker, Swimmer):
    pass

class Whale(Swimmer):
    pass


if __name__ == "__main__":
    Human.walk()
    Human.swim()
    Whale.swim()

# Humans can walk
# Humans can swim
# Whales can swim
