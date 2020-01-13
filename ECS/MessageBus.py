from collections import deque

class MessageBus:
    def __init__(self, game_environment):
        self.subscribers = {}
        self.queue = deque()
        self.game_environment = game_environment

    def subscribe(self, name, subscriber):
        if not name in self.subscribers:
            self.subscribers[name] = []
        self.subscribers[name].append(subscriber)


    def publish(self, name, message):
        self.queue.append((name,message))
        pass

    
    def dispatch_messages(self):
        while self.queue:
            (name, message) = self.queue.popleft()
            if name in self.subscribers:
                for subscriber in self.subscribers[name]:
                    subscriber(self.game_environment, message)
