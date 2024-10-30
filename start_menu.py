from menu import show_menu
from class_dog import DogGame

def main(): #entrada de dados temporariamente
    dog_name = str(input("Qual o nome do animal? "))
    dog_race = str(input("Qual a raça do animal? "))
    dog = DogGame (dog_name, dog_race)

    while True:
        show_menu()
        option = input("Qual opção desejada?: ")

        if option == '1':
            dog.to_awake()

        elif option == '2':
            dog.to_play()

        elif option == '3':
            dog.to_feed()

        elif option == '4':
            dog.to_rest()
            
        elif option == '5':
            print("Saindo do jogo. Até a próxima!")
            break
        else:
            print("Opção inválida, tente novamente.")
