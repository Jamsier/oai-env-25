#!/bin/bash

docker compose up oai-cu -d
sleep 5s

docker compose up oai-du -d
sleep 10s

docker compose up oai-nr-ue -d
sleep 15s

docker exec -it rfsim5g-oai-nr-ue bash -c "ip route replace default via 10.0.0.1 dev oaitun_ue1"
# sleep 5s

docker compose up oai-nr-ue2 -d
sleep 15s

docker exec -it rfsim5g-oai-nr-ue2 bash -c "ip route replace default via 10.0.0.1 dev oaitun_ue1"
sleep 5s

docker compose up oai-nr-ue3 -d
sleep 15s

docker exec -it rfsim5g-oai-nr-ue3 bash -c "ip route replace default via 10.0.0.1 dev oaitun_ue1"
sleep 5s

# docker compose up oai-nr-ue4 -d
# sleep 15s

# docker exec -it rfsim5g-oai-nr-ue4 bash -c "ip route replace default via 10.0.0.1 dev oaitun_ue1"
# sleep 5s

docker stats