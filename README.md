# CRW25

1. clone the repo
  ```bash
  git clone https://github.com/Jamsier/CRW25.git
  ```
2. Pull the images
  ```bash
  cd ~/CRW25
  docker compose pull

  cd rfsim-cu-du-split
  docker compose pull
  ```
3. Run the OAI-CN
  ```bash
  cd ~/CRW25

  ./run-cn.sh
  # or
  docker compose up -d
  ```
4. RUN the OAI-CU, OAI-DU, OAI-nr-UE
  ```bash
  cd rfsim-cu-du-split

  ./run-ran.sh
  # or
  docker compose up oai-cu -d
  docker compose up oai-du -d
  docker compose up oai-nr-ue -d
  ```
