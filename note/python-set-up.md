### pip使用

- pip常用源
```
https://pypi.tuna.tsinghua.edu.cn/simple
https://mirrors.aliyun.com/pypi/simple
https://pypi.douban.com/simple/
https://pypi.mirrors.ustc.edu.cn/simple/
```

- pip install xxx --proxy=http://127.0.0.1:10809

- pip install xxx -i http://mirrors.aliyun.com/pypi/simple/ --trusted-host mirrors.aliyun.com
```
解决ssl不信任错误
WARNING: Retrying (Retry(total=4, connect=None, read=None, redirect=None, status=None)) after connection broken by 'SSLError(SSLEOFError(8, 'EOF occurred in violation of protocol (_ssl.c:997)'))': /simple/vllm/
```

### stable diffusion

- 安装CUDA，使用 nvidia-smi 查看cuda的版本，安装完成后使用 nvcc --version 查看cuda版本
- git clone https://github.com/AUTOMATIC1111/stable-diffusion-webui
- conda env create -n sd -f environment-wsl2.yaml 创建虚拟环境
- 下载训练模型xxx.ckpt放入models\Stable-diffusion文件夹里面。
- 启动webui.bat

- 注意查看pytorch的版本

```
import torch
torch.__version__
torch.cuda.is_available()
```

- 卸载cpu版本的torch，并安装gpu版本

```
pip uninstall torch
pip uninstall torchvision
pip uninstall torchaudio
pip uninstall numpy

# 卸载numpy的原因是防止torch和numpy版本不匹配
# 到官网安装找到安装语句，注意匹配当前机器安装的cuda版本，https://pytorch.org/
pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121
```

### so-vits-svc

- conda create -n svc python=3.8.10
- conda search python
- set http_proxy=http://127.0.0.1:10809
- set https_proxy=http://127.0.0.1:10809
- pip install -r requirements_win.txt

- 导入训练集，确保激活了conda环境
    - python resample.py
    - python preprocess_flist_config.py
    - python preprocess_hubert_f0.py

- 导入训练集后，可以开始训练
    - python train.py -c configs/config.json -m 44k