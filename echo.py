from flask import Flask, request

app = Flask(import_name=__name__)

@app.route("/echo")
def echo():
 to_echo = request.args.get("echo", "")
 response = "{}".format(to_echo)
 return response

if __name__ == "__main__":
 app.run()

#http://localhost:5000/echo?echo=echo+this+back+to+me
