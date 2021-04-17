#!/bin/bash
# add "" to the ip
ip='"'$1'"'
# execute the query
minikube.exe kubectl -- get --all-namespaces  --output json pods | jq ".items[] | select(.status.podIP==${ip})" | jq '{name: .metadata.name, namespace: .metadata.namespace}'
