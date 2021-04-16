# Getting Pod by IP

## First solution, quick and dirty
You can use a simple CLI command with **kubectl**, but you have to be connected to the cluster:
```
host:/$ kubectl get --all-namespaces  --output json  pods | jq '.items[] | select(.status.podIP=="192.168.49.2")' | jq .metadata.name
"etcd-minikube"
"kube-apiserver-minikube"
"kube-controller-manager-minikube"
"kube-proxy-pzfr7"
"kube-scheduler-minikube"
"storage-provisioner"

```
It's good for a one time use, but it might not be as compelling for intensive use.

## Second solution, Python Kubernetes client

