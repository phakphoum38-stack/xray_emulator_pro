from flask import Flask, jsonify

app = Flask(__name__)

state = {
    "kv":80,
    "ma":200,
    "time":100
}

@app.route("/status")
def status():

    return jsonify(state)

@app.route("/set/<kv>/<ma>/<time>")
def configure(kv,ma,time):

    state["kv"] = int(kv)
    state["ma"] = int(ma)
    state["time"] = int(time)

    return jsonify(state)

def run():

    app.run(port=5000)
