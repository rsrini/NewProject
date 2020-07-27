from flask import Flask, request

app = Flask(import_name=__name__)

@app.route("/echo", methods=["POST"])
def echo():
 name = request.values.get("name", "")
 to_echo = request.values.get("echo", "")
 response = "Hey there {}! You said {}".format(name, to_echo)
 return response

app.run()