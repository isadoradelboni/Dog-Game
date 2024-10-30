#CRIANDO UMA CLASSE:
class DogGame: 
#CONSTRUINDO UMA CLASSE:
    def __init__(self, name, race) :
        self.name = name #nome
        self.race = race #raça
        self.tiredness = 0 #nível de cansaço
        self.hunger = 0 #nível de fome
        self.active = False #acordado / dormindo
        self.alive = True #vivo / morto

#CRIANDO MÉTODOS DA CLASSE:
    def to_awake (self): #função para acordar o cachorro
        if self.active == False:
            self.active = True
            print(f"O(A) {self.name} acordou!. O nível de cansaço é {self.tiredness} e de fome é {self.hunger}. ")
        else:
            print(f"O(A) {self.name} ainda está dormindo.")

    def to_play(self): #função para brincar com o cachorro
        if self.alive == True:
            if self.active:
                self.tiredness += 1
                self.hunger += 1
                print(f"Você brincou com {self.name}! O nível de cansaço agora é {self.tiredness} e de fome é {self.hunger}.")
                if self.hunger == 6:
                    print(f"O(A) {self.name} morreu de fome! Você deveria ter cuidado melhor do seu bichinho! :( ")
                    self.alive = False
                    return
                elif self.tiredness == 5:
                    print(f"{self.name} está tão cansado(a) que decidiu dormir sozinho(a).")
                    self.tiredness = 0
                    self.active = False
            else: 
                print(f"O(A) {self.name} está dormindo.")
        else:
            print(f"O(A) {self.name} ainda está morto.")
            
        

    
    def to_feed(self):  #função para alimentar o cachorro
        if self.hunger == 0:
            print(f"O(A) {self.name} não está com fome. O nível de fome é {self.hunger}. ")
        elif self.hunger >= 6:
            print(f"O(A) {self.name} morreu de fome! Você deveria ter cuidado melhor do seu bichinho! :( ")
            self.alive = False
            return
        else :
            self.hunger = 0
            print(f"O(A) {self.name} foi alimentado(a). O nível de fome agora é {self.hunger}.")
            
    def to_rest(self): #função para descansar o cachorro
        if self.tiredness == 5:
            print(f"{self.name} está tão cansado(a) que decidiu dormir sozinho(a).")
            self.tiredness = 0
            self.active = False 
        elif self.tiredness == 0:
            print(f"O(A) {self.name} não está cansado.")
        else:
            self.tiredness = 0
            print(f"O(A) {self.name} descansou! Nível de cansaço agora é {self.tiredness}.")