from kubernetes import client, config


def main():
    req_ip = "10.0.0.1" # to be replaced by the users IP from the API requests
    config.load_incluster_config()

    v1 = client.CoreV1Api()
    print("Listing pods with their IPs:")
    ret = v1.list_pod_for_all_namespaces(watch=False)
    for i in ret.items:
        print("%s\t%s\t%s" %
              (i.status.pod_ip, i.metadata.namespace, i.metadata.name))
        if i.status.pod_ip == req_ip:
            print("pod name: {}".format(i.metadata.name))


if __name__ == '__main__':
    main()
