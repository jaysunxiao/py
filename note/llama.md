- pip install -r requirements.txt --proxy=http://127.0.0.1:10809
- pip install fastapi uvicorn shortuuid sse_starlette --proxy=http://127.0.0.1:10809

- pydantic版本限制，会有报错：ERROR - Exception in ASGI application
```
pip uninstall pydantic
pip install pydantic==1.10.9 --proxy=http://127.0.0.1:10809
```

- nohup python scripts/openai_server_demo/openai_api_server.py --base_model /home/jay/github/chinese-alpaca-2-7b-hf --gpus 0 &


```curl
curl http://localhost:19327/v1/completions \
  -H "Content-Type: application/json" \
  -d '{
    "prompt": "告诉我中国的首都在哪里"
  }'
```