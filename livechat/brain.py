from django.core.cache import cache
"""
the brain class contains all the logic of the game 
for the data stored in the cache each of them is updated by  setting the cache to their current
values
"""

class Brain:
    def __init__(self):
        self.cache = cache
        self.indicator = None
        self.canvas = None
        self.turns = None
        self.players_list = None
        self.rounds = None
    # the setmove increments the number of moves of players
    def setMove(self,game_id,game_ended=False):
        if game_ended:
            self.indicator = 0
        else:
            self.indicator+=1

        print(self.indicator)
        previous_indicator = self.indicator
        memory = self.cache.get(game_id)
        memory["indicator"] = previous_indicator
        self.cache.set(game_id,memory,None)
    # updates the game board
    def updateCanvas(self,row,col,uuid,game_id):
        print(row,col)
        if self.canvas[row][col] == 0:
            user_id = self.handleTurn(uuid)
            x_is_next = self.indicator % 2 == 0 
            if (self.rounds % 2 == 1):
                x_is_next = not x_is_next
            print(self.indicator,"indicator 11")
            if x_is_next: 
                self.canvas[row][col] = 2
                # player = "X"
                game_ended =  self.calculateWinningCombination()
                previous_canvas = self.canvas
                memory = self.cache.get(game_id)
                memory["canvas"] = previous_canvas
                self.cache.set(game_id,memory,None)
                self.setMove(game_id)
                print(self.cache.get(game_id))
                print(self.indicator,"indicator 12")
                if game_ended:
                    self.setMove(game_id,game_ended=True)
                    self.update_no_of_rounds(game_id)
                    return {"canvas":self.canvas,"game_ended":True,"message":game_ended,"type":"game_play"}
                # return {"row":row,"col":col,"player":player,"id":user_id}
                return {"canvas":self.canvas,"game_ended":False,"player":user_id,"type":"game_play"}
            else: 
                self.canvas[row][col] = 1
                # player = "O"
                game_ended =  self.calculateWinningCombination()
                previous_canvas = self.canvas
                memory = self.cache.get(game_id)
                memory["canvas"] = previous_canvas
                self.cache.set(game_id,memory,None)
                self.setMove(game_id)
                print(self.cache.get(game_id))
                print(self.indicator,"indicator 12")
                if game_ended:
                    self.setMove(game_id,game_ended=True)
                    self.update_no_of_rounds(game_id)
                    return {"canvas":self.canvas,"message":game_ended,"game_ended":True,"type":"game_play"}
                return {"canvas":self.canvas,"game_ended":False,"player":user_id,"type":"game_play"}
        else:
            return {"canvas":self.canvas,"game_ended":False,"type":"game_play"}
            # return {"row":row,"col":col,"player":player,"id":user_id}
            # select the canvas in memmory and update the cache with the updated 
            # version of the canvas
            # print(self.cache.get(game_id))
            # print(self.indicator,"indicator 12")
            # return {"canvas":self.canvas,"game_ended":False}
    def handleTurn(self,id):
        # if not id in self.turns:
        #     self.turns[id] = id
        if len(self.turns) == 0:
            self.turns.append(id)
        else:
            last_played = self.turns[len(self.turns)-1]
            if not last_played == id:
                self.turns.append(id)
        print(self.turns)
        return self.turns[len(self.turns)-1]
    def decide_first_player(self,uuid,game_id):
        print(self.players_list,"1")
        if len(self.players_list) < 3:
            self.players_list.append(uuid)
            print(self.players_list,"2")
            previous_players_list = self.players_list
            memory = self.cache.get(game_id)
            print(memory)
            memory["player_list"] = previous_players_list
            print(memory)
            self.cache.set(game_id,memory,None)
            print(self.cache.get(game_id))

            
            # print()
            return self.players_list,self.canvas
        # pass
    def calculateWinningCombination(self):
        for i in range(len(self.canvas)):
            row = self.canvas[i]
            if len(set(row)) == 1:
                return self.checkWinner(row)
                        
            column = [row[i] for row in self.canvas]
            if len(set(column)) == 1:
                return self.checkWinner(column)
        diag_one = []  
        for i in range(len(self.canvas)):
            diag_one.append(self.canvas[i][i])
        if len(set(diag_one)) == 1:
            return self.checkWinner(diag_one)
        diag_two = []
        for i in range(len(self.canvas)):
            diag_two.append(self.canvas[i][len(self.canvas)-1-i])
        if len(set(diag_two)) == 1:
            return self.checkWinner(diag_two)
        print(self.indicator)
        if self.indicator >= 8:
            return "It Is A Draw"
    def checkWinner(self,array):
        
        if 1 in set(array):
            msg = "Coco O Wins"
            return msg
        elif 2 in set(array):
            msg = "Surfer X Wins"
            return msg
    def return_canvas(self):
        return self.canvas
    
    def set_cache(self,key):
        self.cache.set(key,{"canvas":[[0,0,0],[0,0,0],[0,0,0]],"indicator":0,"turns":[],"player_list":[],"rounds":0},None)
        self.indicator = self.cache.get(key)["indicator"]
        self.canvas = self.cache.get(key)["canvas"]
        self.players_list =self.cache.get(key)["player_list"]
        self.turns = self.cache.get(key)["turns"]
        self.rounds = self.cache.get(key)["rounds"]
    def rematch(self,game_id):
        # previous_canvas = []
        for i in range(len(self.canvas)):
            row = self.canvas[i]
            for j in range(len(row)):
                 row[j] = 0

        self.turns.clear()
        previous_canvas = self.canvas
        previous_turns = self.turns
        memory = self.cache.get(game_id)
        memory["canvas"] = previous_canvas
        memory["turns"] =  previous_turns
        self.cache.set(game_id,memory,None)
        player = self.players_list[0]
        print(memory,self.rounds)
        if  (self.rounds % 2 == 1):
            player = self.players_list[1]
        return {"canvas":self.canvas,"game_ended":True,"type":"rematch_game","player":player}
        
    
    def update_no_of_rounds(self,game_id):
        self.rounds+=1
        print(self.rounds)
        previous_rounds = self.rounds
        memory = self.cache.get(game_id)
        memory["rounds"] = previous_rounds
        self.cache.set(game_id,memory,None)
        
            
