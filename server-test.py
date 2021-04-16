from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['GET'])
def get_query_string():
    param = request.query_string
    print(type(param))
    ans = param.decode() + " decoding works"
    return ans.encode()
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
