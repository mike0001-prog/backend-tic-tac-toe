import json
from channels.generic.websocket import WebsocketConsumer,AsyncWebsocketConsumer
from channels.db import database_sync_to_async
from .models import Message
class Chat(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = f'chat_{self.room_name}'
        print(self.room_group_name)
        
        # Join room group
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )
        # print("connected")
        print("CONNECTED", self.channel_name)

        await self.accept()

    async def disconnect(self, close_code):
        await self.close()   
    # @database_sync_to_async
    async def receive(self, text_data):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = f'chat_{self.room_name}'

        print(self.room_group_name)
        text_data_json = json.loads(text_data)
        # print(text_data)
        expression = text_data_json['message']
        # Message.objects.create(text=expression)
        # self.save_message(text_data_json)
        result = f"yes {expression}"
        await self.channel_layer.group_send(
             self.room_group_name,
            {
                "type": "chat.message",
                "message": result,
            }
        )
        print("broadcasted")
        # await self.send(text_data=json.dumps({
        #     'result': result
        # }))
    async def chat_message(self, event):
        print("EVENT:", event)
        print("chatting")
        await self.send(text_data=json.dumps({
            "message": event["message"],
        }))
    async def dispatch(self, message):
        print("DISPATCH RECEIVED:", message)
        await super().dispatch(message)

    # def create_list(self,event):
    #     self.send(
    #           text_data=json.dumps({
    #         'message': event['message'],
        
    #           }))
    # @database_sync_to_async
    # def save_message(self, data):
    #     Message.objects.create(
    #         text=data["expression"]
    #     )
    # async def chat_message(self, event):
    #     await self.send(
    #         text_data=json.dumps({
    #         'message': event['message'],
            
    #     }))
from  .brain import Brain
# pip install django-cors-headers


class Game(AsyncWebsocketConsumer):
    brain = Brain() 
    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = f'chat_{self.room_name}'
        print(self.room_group_name)
        # self.brain.cache.get(self.room_name)
        if not self.brain.cache.get(self.room_name):
            self.brain.set_cache(self.room_name)
        # print(len(self.brain.players_list))
        # Join room group
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )
        
        print("CONNECTED", self.channel_name)

        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_send(
            self.room_group_name,
            {
               "type" : "player.disconnect",
               "message":{"message":"opponent disconnected","type":"player_disconnect"} 
            }
        )
        await self.close()   
    
    async def receive(self, text_data):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = f'chat_{self.room_name}'
        # b.setMove() 
        # print(indicator)
        
        print(self.room_group_name)
        text_data_json = json.loads(text_data)
        print(text_data_json)
        # player = b.updateCanvas(text_data_json["row"],text_data_json["column"],text_data_json["id"])
        
        # turn = b.handleTurn(text_data_json["id"])      
        if text_data_json["type"] == "game_play":
            data = self.brain.updateCanvas(text_data_json["row"],text_data_json["column"],text_data_json["uuid"],text_data_json["game_id"])
            # turn = b.handleTurn(text_data_json["id"]) 
            await self.channel_layer.group_send(
             self.room_group_name,
            {
                "type": "game.play",
                "message": data,
            }
        )
        if text_data_json["type"] == "rematch_game":
            data = self.brain.rematch(text_data_json["game_id"])
            # turn = b.handleTurn(text_data_json["id"]) 
            await self.channel_layer.group_send(
             self.room_group_name,
            {
                "type": "rematch.game",
                "message": data,
            }
        )
        
        if text_data_json["type"] == "make_connection":
            players,canvas = self.brain.decide_first_player(text_data_json["uuid"],text_data_json["game_id"])
            print(len(players))
            if len(players) == 2:
                message = {"type":"make_connection","player":players[0] ,"canvas":canvas} #the first player that connected 
                await self.channel_layer.group_send(
                self.room_group_name,
                {
                    "type": "make.connection",
                    "message": message,
                }
    )
        print("broadcasted")
    
    async def game_play(self, event):
        print("EVENT:", event)
        print("chatting")
        await self.send(text_data=json.dumps({
            "message": event["message"],
        }))
    async def rematch_game(self,event):
        await self.send(text_data=json.dumps({
            "message": event["message"],
        }))

    async def make_connection(self,event):
        await self.send(text_data=json.dumps({
            "message": event["message"],
        }))
    async def player_disconnect(self,event):
        await self.send(text_data=json.dumps({
            "message": event["message"],
        }))
    async def dispatch(self, message):
        print("DISPATCH RECEIVED:", message)
        await super().dispatch(message)