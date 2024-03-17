###


- llama
```
tail -f /home/jay/github/llama2/Chinese-LLaMA-Alpaca-2/nohup.out

less /home/jay/github/llama2/Chinese-LLaMA-Alpaca-2/nohup.out
```


- homegpu
```
curl -O https://jiucai-fun.oss-cn-shanghai.aliyuncs.com/homegpu-1.0.jar

sh /deployhomegpu.sh stopUpdateStart /usr/local/homegpu/homegpu-1.0.jar

tail -f /usr/local/homegpu/spring.log

less /usr/local/homegpu/spring.log

sh /deployhomegpu.sh stop homegpu

less /usr/local/homegpu/spring.log | grep "java.lang.RuntimeException: java.io.InterruptedIOException: timeout" | wc -l
```


- homev2ray
```
sh /deployv2ray.sh stopUpdateStart /usr/local/homev2ray/homev2ray-1.0.jar

less /usr/local/homev2ray/spring.log

sh /deployhomegpu.sh stop homev2ray
```

### llama安装

- pip install -r requirements.txt --proxy=http://127.0.0.1:10809
- pip install fastapi uvicorn shortuuid sse_starlette --proxy=http://127.0.0.1:10809

- pydantic版本限制，会有报错：ERROR - Exception in ASGI application
```
pip uninstall pydantic
pip install pydantic==1.10.9 --proxy=http://127.0.0.1:10809
```
- conda activate llama
- cd /home/jay/github/llama2/Chinese-LLaMA-Alpaca-2/
- nohup python scripts/openai_server_demo/openai_api_server.py --base_model /home/jay/github/chinese-alpaca-2-7b-hf --gpus 0 &


```curl
curl http://localhost:19327/v1/completions \
  -H "Content-Type: application/json" \
  -d '{
    "prompt": "告诉我中国的首都在哪里"
  }'
```

```
conda activate llama
less /home/jay/github/llama2/Chinese-LLaMA-Alpaca-2/nohup.out
```

### llama量化安装

- 直接运行
```
conda activate llama
nohup /home/jay/github/llama.cpp/server -m /home/jay/github/mymodel/chinese-alpaca-2-13b-hf/ggml-model-q4_0.gguf -c 4096 -ngl 999 --host 0.0.0.0 > /myllama.log 2>&1 &
```