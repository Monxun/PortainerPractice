#!/bin/sh

# DOCKER
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh

# DOCKER-COMPOSE
sudo curl -L https://github.com/docker/compose/releases/download/1.21.2/docker-compose-`uname -s`-`uname -m` -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose
sudo docker volume create portainer_data

# KIND - K8
curl -Lo ./kind https://kind.sigs.k8s.io/dl/v0.11.1/kind-linux-amd64
chmod +x ./kind
mv ./kind /root/kind

# PORTAINER
sudo docker run -d -p 9000:9000 -p 8000:8000 --name PORTAINER --restart always -v /var/run/docker.sock:/var/run/docker.sock -v /srv/portainer:/data portainer/portainer

# HELM
snap install helm --classic

# CONFIGURE KUBECTL
alias k=kubectl
complete -F __start_kubectl k

# INSTALL KREW PLUGIN MANAGER
# https://www.freecodecamp.org/news/how-to-set-up-a-serious-kubernetes-terminal-dd07cab51cd4/
(
  set -x; cd "$(mktemp -d)" &&
  OS="$(uname | tr '[:upper:]' '[:lower:]')" &&
  ARCH="$(uname -m | sed -e 's/x86_64/amd64/' -e 's/\(arm\)\(64\)\?.*/\1\2/' -e 's/aarch64$/arm64/')" &&
  KREW="krew-${OS}_${ARCH}" &&
  curl -fsSLO "https://github.com/kubernetes-sigs/krew/releases/latest/download/${KREW}.tar.gz" &&
  tar zxvf "${KREW}.tar.gz" &&
  ./"${KREW}" install krew
)
export PATH="${KREW_ROOT:-$HOME/.krew}/bin:$PATH"
kubectl krew
kubectl krew update
# kubectl ctx
kubectl krew install ctx
# kubectl ns
kubectl krew install ns

# INSTALL CONTEXT TERMINAL


# CREATE CLUSTER
kind create cluster

# INSTALL METALLB LOAD BALANCER
k apply -f https://raw.githubusercontent.com/metallb/metallb/master/manifests/namespace.yaml
k apply -f https://raw.githubusercontent.com/metallb/metallb/master/manifests/metallb.yaml
k get pods -n metallb-system --watch
METALLB_IP_RANGE=$(docker network inspect -f '{{.IPAM.Config}}' kind 2>&1)

cat <<EOF | kubectl apply -f - 
apiVersion: v1
kind: ConfigMap
metadata:
  namespace: metallb-system
  name: config
data:
  config: |
    address-pools:
    - name: default
      protocol: layer2
      addresses:
      - {{ METALLB_IP_RANGE }}
EOF