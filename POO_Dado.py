import random

class Dice:
    faces = 6
    
    def roll(self):
        return random.randint(1, self.faces)

def validating_number(msg):
    while True:
        value = input(msg).strip()
        if value.isdigit() and 2 >= int(value) >= 1:
            return int(value)
        else:
            print('Error: Valor erroneo, intente de nuevo')

def main():

    dice = Dice()

    while True:
        code = validating_number('\n1.Tirar el dado\n2.Salir\n')

        if code == 1:
            print(dice.roll())
        elif code == 2:
            return

if __name__ == '__main__':
    main()