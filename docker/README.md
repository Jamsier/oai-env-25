# Build OAI docker images



1. clone openairinterface
```
git clone https://gitlab.eurecom.fr/oai/openairinterface5g.git
cd openairinterface5g
git checkout f3eb713084e4134ca265f1153b68a102714a319a
```

2. Replace the dockerfile in the docker/

3. Build images
```
docker build -t ran-base -f docker/Dockerfile.base.ubuntu22 .
docker build -t ran-build -f docker/Dockerfile.build.ubuntu22 .
docker build -t oai-gnb -f docker/Dockerfile.gNB.ubuntu22 .
docker build -t oai-nr-ue -f docker/Dockerfile.nrUE.ubuntu22 .
```