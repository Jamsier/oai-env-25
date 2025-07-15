1. `strip-gtp.py`
    - 讀取 `.pcap` 檔案，並將帶有 GTP header 的封包拆除，其餘保持不變
2. 使用 cicflowmeter 將拆掉 GTP Header 的封包轉乘 flow
    - https://github.com/hamelin/cicflowmeter-docker