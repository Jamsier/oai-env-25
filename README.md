# oai-env-25

1. clone the repo
  ```bash
  git clone https://github.com/Jamsier/oai-env-25.git
  ```
2. Pull the images
  ```bash
  cd ~/oai-env-25
  docker compose pull

  cd ~/oai-env-25/rfsim-cu-du-split
  docker compose pull
  ```
3. Run the OAI-CN
  ```bash
  cd ~/oai-env-25

  ./run-cn.sh
  # or
  docker compose up -d
  ```
4. RUN the OAI-CU, OAI-DU, OAI-nr-UE
  ```bash
  cd ~/oai-env-25/rfsim-cu-du-split

  ./run-ran.sh
  # or
  docker compose up oai-cu -d
  docker compose up oai-du -d
  docker compose up oai-nr-ue -d
  ```
