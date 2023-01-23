from flask import Flask,jsonify, request

app = Flask(__name__)

contacts = [
    {
        'Contact': "123456789",
        'Name': 'Bob',
        'done': False, 
        'id': 1
    },
    {
        'Contact': "987654321",
        'Name': 'Ash',
        'done': False, 
        'id': 2
    }
]

@app.route("/add-data", methods=["POST"])
def add_task():
    if not request.json:
        return jsonify({
            "status":"error",
            "message": "Please provide all required information"
        },400)

    task = {
        'id': tasks[-1]['id'] + 1,
        'Name': request.json['Name'],
        'Contact': request.json.get('Contact', ""),
        'done': False
    }
    contacts.append(task)
    return jsonify({
        "status":"success",
        "message": "Contact added succesfully!"
    })
    

@app.route("/get-data")
def get_task():
    return jsonify({
        "data" : contacts
    }) 

if (__name__ == "__main__"):
    app.run(debug=True)