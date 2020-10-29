from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Hello World!"

@app.route('/add_two_nums', methods=["POST"])
def add_two_nums():
    dataDict = request.get_json()
    return jsonify(dataDict)
    # x = data_dict["x"]
    # y = data_dict["y"]
    # z= x+y
    #
    # retJson = {
    #     "z": z
    # }
    # return jsonify(retJson), 200

@app.route('/1')
def first_page():
    age = 2*12
    retJson={
        'Name' : 'additya',
        'Age' : age,
        'Phone' : [
            {
            "Mobile Phone" : "iPhone",
            "Number" : 0
            },
            {
            "Mobile Phone" : "Samsung ",
            "Number" : 85720405
            }
        ]

    }
    return jsonify(retJson)
@app.route('/2')
def second_page():
    a = str(sum(n for n in range(1,10) if n%3==0 or n%5==0))
    return a

if __name__=="__main__":
    app.run(debug=True)
