1. 下载 https://github.com/ymcui/Chinese-LLaMA-Alpaca-2
2. 创建一个conda环境给llama
```
conda create -n llama python=3.10
conda activate llama
```
3 安装其它依赖
```
pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121

```
4. 安装requirements.txt里的package，因为正在windows平台很多包和linux不一致，所以一个一个安装
```
pip install --proxy=http://127.0.0.1:10809 peft transformers sentencepiece bitsandbytes-windows
```
5. 安装api server
```
pip install --proxy=http://127.0.0.1:10809 fastapi uvicorn shortuuid sse_starlette
```
6. 启动
```
python scripts/openai_server_demo/openai_api_server.py --base_model ./mymodel/ --gpus 0,1
```