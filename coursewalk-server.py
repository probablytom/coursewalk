from flask import Flask
from flask_cors import CORS
from TreeBuilder import Tree
app = Flask(__name__)
CORS(app)

@app.route('/')
def rootData():
    return Tree('example').root.json_representation()

if __name__ == "__main__":
    app.run(host='localhost',
            port=9255)
