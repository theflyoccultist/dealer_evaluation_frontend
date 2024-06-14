from flask import Flask, send_from_directory
from flask_cors import CORS

app = Flask("Product deal check")

cors = CORS(app, resources={r"/*": {"origins": "*"}})

@app.route("/")
def getHomePage():
  return send_from_directory('html', "index.html")

if __name__=="__main__":
    app.run(port=5001,debug=True) 
    # When no port is specified, starts at default port 5000
