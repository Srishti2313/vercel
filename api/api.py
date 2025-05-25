from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Your student marks data (load from file or hardcode here)
data = [{"name":"z35IY7h","marks":83},{"name":"6","marks":38},{"name":"p7a5V","marks":31},{"name":"Ister0uXem","marks":44},{"name":"gC","marks":86},{"name":"cxtb0mFK","marks":36},{"name":"QmuZJ","marks":27},{"name":"By8snmr","marks":23},{"name":"T8DPF428a","marks":20},{"name":"zItX","marks":14},{"name":"iSb01NNXs","marks":23},{"name":"NS9t5SJz","marks":30},{"name":"Z","marks":10},{"name":"7lRETnAD","marks":97},{"name":"KMqejzH","marks":61},{"name":"IJ","marks":79},{"name":"u8","marks":20},{"name":"s6o2oFcvW9","marks":78},{"name":"zA4N7m6ek","marks":50},{"name":"ffeU7B1aPg","marks":10},{"name":"8w9pP","marks":32},{"name":"cy1ZJy","marks":35},{"name":"T","marks":37},{"name":"GBWaSz9R","marks":53},{"name":"weXVSU","marks":14},{"name":"iImoGg","marks":45},{"name":"mCrXCbWpK","marks":69},{"name":"03bnbT4T","marks":11},{"name":"tfC59gr9","marks":8},{"name":"21h6Cu7Iqd","marks":41},{"name":"mxD49LmAZ8","marks":55},{"name":"gHyy","marks":13},{"name":"tW3v8i9FP1","marks":52},{"name":"Qm6Etcr","marks":56},{"name":"t0","marks":81},{"name":"a8sjwGI","marks":52},{"name":"EFKFoJE","marks":68},{"name":"l","marks":23},{"name":"Yj","marks":80},{"name":"ko1dVt","marks":0},{"name":"zoBAxnJs","marks":16},{"name":"QUGwx6B","marks":12},{"name":"w155MhF","marks":43},{"name":"B","marks":29},{"name":"eGNrExP5","marks":99},{"name":"ACoO8d6","marks":63},{"name":"hDDHJB","marks":58},{"name":"9","marks":50},{"name":"LYbbG2eSci","marks":14},{"name":"ccJqRv","marks":49},{"name":"W","marks":97},{"name":"urNVu5Hfb","marks":83},{"name":"HIZ","marks":58},{"name":"Elq83eHmuI","marks":59},{"name":"8EuW4doe","marks":71},{"name":"g3zk","marks":63},{"name":"Fj9","marks":66},{"name":"1L","marks":56},{"name":"AIQz7xYz","marks":25},{"name":"hW4l","marks":99},{"name":"AoWrAc31","marks":43},{"name":"TPc1e6M","marks":89},{"name":"QXRtik","marks":93},{"name":"H5TzED","marks":25},{"name":"uM","marks":8},{"name":"TBFB","marks":15},{"name":"b6luLQ9Bo","marks":14},{"name":"dRBNzefa2D","marks":44},{"name":"OOf","marks":24},{"name":"TwDk5QgIr","marks":14},{"name":"Fp","marks":7},{"name":"irewe1uIa5","marks":9},{"name":"RMT2JmgPVP","marks":91},{"name":"b2W","marks":46},{"name":"XNF","marks":99},{"name":"BwRwtaGRVt","marks":17},{"name":"xpp","marks":19},{"name":"Xd5n6Nqfjj","marks":42},{"name":"y6lP","marks":6},{"name":"IbiUx7sVWf","marks":79},{"name":"XarTq3zXB","marks":11},{"name":"H","marks":51},{"name":"rK5hXJJ","marks":55},{"name":"42Jvoh","marks":76},{"name":"2oW8H9oCq","marks":98},{"name":"229gGd1F","marks":43},{"name":"Rn","marks":75},{"name":"aW4","marks":95},{"name":"zhGu2fLDLq","marks":81},{"name":"9zp5SlaPt","marks":53},{"name":"L","marks":44},{"name":"MDOSrH","marks":66},{"name":"GVOxSIK83","marks":99},{"name":"ukKYcgrnkt","marks":51},{"name":"VRr5PKa","marks":87},{"name":"sb","marks":5},{"name":"7Nna67","marks":81},{"name":"aW9Y","marks":31},{"name":"lmg4WgH","marks":59},{"name":"lPOp","marks":16}]

@app.route("/api")
def get_marks():
    names = request.args.getlist('name')
    marks = []
    for n in names:
        mark = next((item['marks'] for item in data if item['name'] == n), None)
        marks.append(mark if mark is not None else None)
    return jsonify({"marks": marks})

if __name__ == "__main__":
    app.run()
