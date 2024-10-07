# chat/consumers.py
import json
from channels.generic.websocket import AsyncWebsocketConsumer

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        # Obtém o nome da sala a partir da URL
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = f'chat_{self.room_name}'

        # Adiciona o cliente ao grupo da sala de chat
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        # Aceita a conexão WebSocket
        await self.accept()

    async def disconnect(self, close_code):
        # Remove o cliente do grupo da sala de chat
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    # Recebe a mensagem do WebSocket
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        # Envia a mensagem para o grupo da sala de chat
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message
            }
        )

    # Recebe a mensagem do grupo da sala de chat
    async def chat_message(self, event):
        message = event['message']

        # Envia a mensagem de volta ao WebSocket para todos os clientes conectados
        await self.send(text_data=json.dumps({
            'message': message
        }))
