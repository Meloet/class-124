from flask import Flask, jsonify, request
app = Flask(__name__)
phonenumbers=[
    {
        'id':1,
        'name':'anyname',
        'contact':'8566340'
    },
    {
        'id':2,
        'name':'anyName0',
        'contact':'85663240'
    }
]
@app.route('/show')
def shownumbers():
    return jsonify({
        'data': phonenumbers
    })

if(__name__=="__main__"):
    app.run(debug=True)