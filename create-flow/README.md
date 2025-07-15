1. `strip-gtp.py`
    - 讀取 `.pcap` 檔案，並將帶有 GTP header 的封包拆除，其餘保持不變
2. 使用 cicflowmeter 將拆掉 GTP Header 的封包轉乘 flow
    - https://github.com/hamelin/cicflowmeter-docker
    - Dockerfile
       ```Dockerfile
        FROM ubuntu:18.04

        RUN apt-get update -y && apt-get upgrade -y
        RUN apt-get install -y gradle maven git libpcap-dev
        
        RUN git clone https://github.com/ahlashkari/CICFlowMeter /code
        RUN cd /code/jnetpcap/linux/jnetpcap-1.4.r1425 && \
            mvn install:install-file \
            -Dfile=jnetpcap.jar -DgroupId=org.jnetpcap -DartifactId=jnetpcap \
            -Dversion=1.4.1 -Dpackaging=jar
        WORKDIR /code
        RUN gradle --no-daemon build
        
        COPY gradle-task /gradle-task
        RUN cat /gradle-task >>build.gradle && rm /gradle-task
        
        COPY go /go
        RUN chmod 500 /go
        ENTRYPOINT ["/go"]
       ```
