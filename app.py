import os
from flask import Flask

from flask import request
import cgi

app = Flask(__name__)


def reqdata(req):
    r = []
    r.append("Formkeys: " + `req.form.items()`)
    r.append("Files:" + `req.files.items()`)
    r.append("Headers:" + `req.headers.items()`)
    r.append("Data:" + `req.data`)
    r.append("Len: " + `req.content_length`)
    r.append("Type: " + `req.content_type`)

    return '\n'.join(r)+ "\n\n"

@app.route("/log")
def log():
    return "<pre>" + cgi.escape(open("/tmp/pushlog.txt").read()) + "</pre>"

@app.route('/')
def hello():
    print request
    open("/tmp/pushlog.txt", "a").write(reqdata(request))
    return 'Hello World!'

if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.debug = True
    app.run(host='0.0.0.0', port=port)