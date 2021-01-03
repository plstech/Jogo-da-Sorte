#!/usr/bin/python3

from random import randint 
import os
chute = 0;
random = randint(0,10)
chances = 5;

os.system("clear")
while chute != random:
    chute = input("\033[1;37m "+"[Chute um numero de 0 a 10]: ")

    if chute.isnumeric():
        chute = int(chute)
        chances = chances - 1

        if chute == random:
            os.system("clear")
            print(f"\033[1;32m"+"Parabéns você acertou, e ganhou o game!")
            break;
        else:
           if chute > random:
               print("\033[1;31m"+"\n [ERROU] ~ Dica: É um número menor")
           else:
               print("\n [ERROU] ~ Dica: É um número maior")
   
           print("\033[1;35m"+" [Você ainda possui {} tentativas!]\n".format(chances))
         
        if chances == 0:
            os.system("clear")
            print("Suas chances acabaram, você perdeu!")
            break;
