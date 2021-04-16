from flask import Flask, request
import json

app = Flask(__name__)

@app.route('/', methods=['GET'])
def get_query_string():
    param = request.query_string
    print(type(param))
    ans = [{"task_name":param.decode(),"task_info":"aaaaa"},{"task_name":"task2","task_info":"bbbbb"}]
    data = json.dumps(ans, indent=2)
    return data
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
