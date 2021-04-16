from kubernetes import client, config
from flask import Flask, request
import json

app = Flask(__name__)

@app.route('/', methods=['GET'])
def get_query_string():
    return check_pods(request.query_string.decode())

def check_pods(req_ip):
    ans_json = []
    config.load_incluster_config()
    v1 = client.CoreV1Api()
    print("Listing pods with their IPs:")
    ret = v1.list_pod_for_all_namespaces(watch=False)
    for i in ret.items:
        print("%s\t%s\t%s" %
              (i.status.pod_ip, i.metadata.namespace, i.metadata.name))
        if i.status.pod_ip == req_ip:
            ans_json.append({"name": i.metadata.name, "namespace": i.metadata.namespace})
    data = json.dumps(ans_json, indent=2)
    return data

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
