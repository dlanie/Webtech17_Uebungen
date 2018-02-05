from server.webserver import Middleware, Cookie
import json

class AuthMiddleware(Middleware):

    def __init__(self, template):
        self.request = None
        self.response = None
        self.template = template
        super().__init__()


    def process_request(self, request, response):
        self.request=request
        self.response = response
        request.auth = self


    def process_response(self, response):
        pass


    def check(self):
        try:
            return(self.request.session.get_data('username'))
        except KeyError:
            return(False)

    def do(self):
        if self.check is False:
            self.response.send_template('login.mustache',
                                        {'pagename': pagename,
                                        'pagetitle': 'Show Wiki Page',
                                        'pages': self.pages()})
            return(False)
        else:
            #Json file einlesen
            file = open('credentials.json', "r")
            data = json.load(file)

            #Prüfen ob username und password vorhanden sind
            match = False
            try:
                for i in range(len(data['users'])):
                        if data['users'][i]['username'] == self.request.params['username'] and data['users'][i]['password'] == self.request.params['password']:
                            match = True
            except KeyError:
                print("Username or Password are missing!")

            #username in die session schreiben
            if match:
                self.request.session.set_data('username', self.request.params['username'])
                print(self.request.session.get_data('username'))
                return(True)
            else:
                return(False)
