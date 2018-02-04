from server.webserver import App

class IndexApp(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def register_routes(self):
        self.add_route('', self.sendIndex)

    def sendIndex(self, request, response, pathmatch=None):
        text = 'Servername: '+ self.servername
        response.send(body=text)