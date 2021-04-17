# Getting Pod by IP

## First solution, quick and dirty
You can use a simple CLI command with **kubectl**, but you have to be connected to the cluster:
```
$ kubectl get --all-namespaces  --output json  pods | jq '.items[] | select(.status.podIP=="192.168.49.2")' | jq '{name: .meta
data.name, namespace: .metadata.namespace}'
{
  "name": "etcd-minikube",
  "namespace": "kube-system"
}
{
  "name": "kube-apiserver-minikube",
  "namespace": "kube-system"
}
{
  "name": "kube-controller-manager-minikube",
  "namespace": "kube-system"
}
{
  "name": "kube-proxy-pzfr7",
  "namespace": "kube-system"
}
{
  "name": "kube-scheduler-minikube",
  "namespace": "kube-system"
}
{
  "name": "storage-provisioner",
  "namespace": "kube-system"
}

```
I found a number of one line commands that solves the challenge, non of which are very readable or maintainable.
It's good for a one time use, but it might not be as compelling for intensive use.

## Second solution, Python Kubernetes client
**main.py** contains a flask web app with a single GET endpoint.
When provoked, the server queries all pods from the kubernetes cluster and returns the name and namespace of the pods with an IP equal to the IP added to the GET request.
### How to use
I used minikube, so first I had to tunnel the service so it can be accessed from my browser:

```
minikube.exe service kube-client-service
```
This also automatically opens a browser window with the proxy address and port.

I prefer curl, And I just add a */?IP-ADDRESS* to the URL:
```
$ curl http://127.0.0.1:65487/?192.168.49.2
[
  {
    "name": "etcd-minikube",
    "namespace": "kube-system"
  },
  {
    "name": "kube-apiserver-minikube",
    "namespace": "kube-system"
  },
  {
    "name": "kube-controller-manager-minikube",
    "namespace": "kube-system"
  },
  {
    "name": "kube-proxy-pzfr7",
    "namespace": "kube-system"
  },
  {
    "name": "kube-scheduler-minikube",
    "namespace": "kube-system"
  },
  {
    "name": "storage-provisioner",
    "namespace": "kube-system"
  }
]
```
### How to deploy
1. Have a kubernetes cluster running - I used minikube.
2. connect to the cluster with kubectl - minikube has it included, you can alias it:
```
alias kubectl="minikube.exe kubectl --"
```
3. apply the cluster role, cluster role binding and the deployment:
```
kubectl apply -f cluster-role.yaml
kubectl apply -f cluster-role-binding.yaml
kubectl apply -f deployment.yaml
```
The deployment also includes the service manifest
