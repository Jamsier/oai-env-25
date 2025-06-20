#!/bin/bash

docker compose up oai-cu -d
sleep 5s

docker compose up oai-du -d
sleep 10s

docker compose up oai-nr-ue -d
sleep 20s

docker exec -it rfsim5g-oai-nr-ue bash -c "ip a && ip route replace default via 10.0.0.1 dev oaitun_ue1"
sleep 5s

docker stats