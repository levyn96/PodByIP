from kubernetes import client, config
from flask import Flask, request

app = Flask(__name__)

@app.route('/data', methods=['GET'])
def get_query_string():
    return check_pods(request.query_string)

def check_pods(req_ip):
    config.load_incluster_config()
    v1 = client.CoreV1Api()
    print("Listing pods with their IPs:")
    ret = v1.list_pod_for_all_namespaces(watch=False)
    for i in ret.items:
        print("%s\t%s\t%s" %
              (i.status.pod_ip, i.metadata.namespace, i.metadata.name))
        if i.status.pod_ip == req_ip:
            print("pod name: {}".format(i.metadata.name))
            return i.metadata.name


if __name__ == '__main__':
    app.run(debug=True)
