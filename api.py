import os
from flask import Flask, request, send_file, jsonify
from flask_cors import CORS, cross_origin
from csv_parser import getColumns, dataPrep, dataVisualizerCommunicator

UPLOAD_FOLDER = './files/'

app = Flask(__name__)
cors = CORS(app)

@app.route("/visualize", methods=['GET', 'POST'])
@cross_origin()
def uploadCSV():
    if request.method == "POST":
        filename = request.args.get('name')
        current_csv = UPLOAD_FOLDER + filename
        print(filename)
        with open(current_csv, 'wb') as file:
            file.write(request.data)
            file.close()
        print(getColumns(current_csv))
        return jsonify(getColumns(current_csv))


@app.route("/visualize", methods=['GET', 'POST'])
@cross_origin()
def displayCSV():
    finished = False
    if request.method == "POST":
        data = request.get_json()
        inputFields = dataPrep(data, UPLOAD_FOLDER)
        return dataVisualizerCommunicator(inputFields)
    if request.method == 'GET':
        file = request.args.get('file')
        return send_file(file, mimetype="image/gif")


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=4000, debug=True)
