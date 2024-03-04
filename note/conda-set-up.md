### Linux下安装miniconda

- https://blog.csdn.net/Baby_of_breath/article/details/124041687

- source ~/.bashrc

### Windows安装miniconda安装

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