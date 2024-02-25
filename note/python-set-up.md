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

### conda安装

- miniconda直接从清华大学的镜像下载
- https://mirrors.tuna.tsinghua.edu.cn/anaconda/miniconda/

- 下面是安装教程
- https://mirrors.tuna.tsinghua.edu.cn/help/anaconda/

```
Windows 用户无法直接创建名为 .condarc 的文件，可先执行 conda config --set show_channel_urls yes 生成该文件之后再修改。
一般 .condarc 文件存放在：C:\Users\jay\


Linux各系统都可以通过修改用户目录下的 .condarc 文件来使用 TUNA 镜像源
```

```
channels:
  - defaults
show_channel_urls: true
default_channels:
  - https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
  - https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/r
  - https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/msys2
custom_channels:
  conda-forge: https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud
  msys2: https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud
  bioconda: https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud
  menpo: https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud
  pytorch: https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud
  pytorch-lts: https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud
  simpleitk: https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud
proxy_servers:
    http: http://127.0.0.1:10809
    https: http://127.0.0.1:10809
```

- 运行 conda clean -i 清除索引缓存，保证用的是镜像站提供的索引。 conda clean -all 清除全部的缓存
- 运行 conda create -n test1 python=3.10 测试一下吧。
- 使用 conda activate test1 激活这个环境
- conda env list 列出所有已经安装的环境
- conda remove -n test2 --all 移除test2这个环境
- conda list 当前环境安装了哪些软件包
- conda install requests 安装request软件包

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