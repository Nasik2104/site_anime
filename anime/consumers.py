import json
from channels.generic.websocket import AsyncWebsocketConsumer


class WatchTogetherConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = f'watch_together_{self.room_name}'

        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        current_time = text_data_json.get('currentTime')

        print(f"Отримано: {message} на часі: {current_time}")

        if current_time == 0:
            current_time = 0.1

        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'send_message',
                'message': message,
                'currentTime': current_time
            }
        )

    async def send_message(self, event):
        message = event['message']
        current_time = event.get('currentTime')

        await self.send(text_data=json.dumps({
            'message': message,
            'currentTime': current_time
        }))


class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = f'chat_{self.room_name}'

        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        user = text_data_json['username']

        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message,
                'username': user
            }
        )

    async def chat_message(self, event):
        message = event['message']
        user = event['username']

        await self.send(text_data=json.dumps({
            'message': message,
            'username': user
        }))
