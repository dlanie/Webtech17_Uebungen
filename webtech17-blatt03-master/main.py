from server import webserver
from server.apps.static import StaticApp
from server.apps.index import IndexApp

if __name__ == '__main__':
    server = webserver.Webserver(port=8080)
    server.add_app(StaticApp(prefix = 'static', name = "StaticApp", path='static', einstiegsroute='/static/'))
    #server.add_app(StaticApp(prefix='Dynamic', name="DynamicApp", path='Dynamic', einstiegsroute='/Dynamic/'))
    #server.add_app(StaticApp(prefix='Test', name="TestApp", path='Test', einstiegsroute='/Test/'))
    #server.add_app(StaticApp(prefix='World', name="WorldApp", path='World', einstiegsroute='/World/'))
    server.add_app(IndexApp(servername = "Toller Server", name="IndexApp", einstiegsroute=''))
    server.serve()