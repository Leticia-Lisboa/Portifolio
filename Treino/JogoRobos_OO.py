# Orientação a objetos Python
# Jogo dos robôs
# O robô pode andar ao longo de uma matriz 10x10 e encontrar recompensas
import random

#Classe que determina posição


class Point(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

#Classe Robo determina a posição( herda da classe Point) e os movimentos do robo


class Robot(Point):

    def move_up(self):
        if self.y < 10:
            self.y = self.y + 1
        else:
            print('Movimento proibido')

    def move_down(self):
        if self.y > 0:
            self.y = self.y - 1
        else:
            print('Movimento proibido')

    def move_left(self):
        if self.x > 0:
            self.x = self.x - 1
        else:
            print('Movimento proibido')

    def move_right(self):
        if self.x < 10:
            self.x = self.x + 1
        else:
            print('Movimento proibido')
    def __str__(self):
        return '<%s, %s>' % (self.x, self.y)

#Classe recompensa  herda a posição da Classe Point e acrescenta o nome da recompensa


class Reward(Point):
    def __init__(self, x, y, name):
        super(Reward, self).__init__(x,y)
        self.name = name

    def __str__(self):
        return '<%s, %s> : %s' % (self.x, self.y, self. name)

    def __repr__(self):
        return '<Reward> %s' % str(self)

reward1 = Reward(1, 1, 'moeda de ouro')


#Verifica se o robô encontrou recompensa


def check_reward(robot, rewards):
    ok = False
    for reward in rewards:
        if reward.x == robot.x and reward.y == robot.y:
            print("o robô achou a recompensa: %s", reward.name)
            ok = True
    return ok

#Criando Recompensas em locais aleatorios


r1 = Reward(random.randint(0, 10), random.randint(0, 10), 'moeda')
r2 = Reward(random.randint(0, 10), random.randint(0, 10), 'gasolina')
r3 = Reward(random.randint(0, 10), random.randint(0, 10), 'arma')

rewards = [r1, r2, r3]    # Lista de recompensas


robot = Robot(random.randint(0, 10), random.randint(0, 10))   #Robo

for i in range(10):
    moviment = input("Digite up, down, left ou rignt para o movimento: ")

    if moviment == 'up':
        robot.move_up()
    elif moviment == 'down':
        robot.move_down()
    elif moviment == 'left':
        robot.move_left()
    elif moviment == 'right':
        robot.move_right()
    else:
        print('Movimento inválido')
        continue
    print(robot)
    check_reward(robot, rewards)







