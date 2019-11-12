from flask import Flask, url_for, render_template
app=Flask(__name__)

class PrefixMiddleware(object):
    def __init__(self, app, prefix=''):
        self.app=app
        self.prefix=prefix

    def __call__(self, environ,start_response):
        print(environ['PATH_INFO'])
        if environ['PATH_INFO'].lower().replace('/flaskredirect', '').startswith(self.prefix):
            environ['PATH_INFO'] = environ['PATH_INFO'].lower().replace('/flaskredirect', '')[len(self.prefix)]
            environ['SCRIPT_NAME'] = self.prefix
            return self.app(environ, start_response)
        else:
            start_response('404', [('Content-Type', 'text/plain')])
            return [environ['PATH_INFO'].encode()]
        

app.wsgi_app = PrefixMiddleware(app.wsgi_app, prefix='/pff')


@app.route('/test')
def test():
    return "test"

@app.route('/')
def index():
    return "hello world"


if __name__ == '__main__':
    app.run(port=9010)