FROM liyaodev/base-gpu-u20-py310:v1.0.0
LABEL maintainer=liyaodev

RUN pip install --no-cache-dir --upgrade pip \
    -i https://pypi.tuna.tsinghua.edu.cn/simple

# ENV Install
## Install PyTorch
RUN pip install --no-cache-dir \
    torch==2.3.1 torchvision==0.18.1 torchaudio==2.3.1 \
    -i https://pypi.tuna.tsinghua.edu.cn/simple

## Install PyG
RUN pip install --no-cache-dir \
    torch_geometric \
    -i https://pypi.tuna.tsinghua.edu.cn/simple

## Install rapids-singlecell
RUN pip install --no-cache-dir \
    'rapids-singlecell[rapids12]' \
    --extra-index-url=https://pypi.nvidia.com

## Install Jupyter-lab
RUN pip install  --no-cache-dir \
    jupyterlab \
    -i https://pypi.tuna.tsinghua.edu.cn/simple

## Install OmicVerse
COPY ./omicverse /tmp/omicverse
RUN pip install --no-cache-dir \
    /tmp/omicverse \
    -i https://pypi.tuna.tsinghua.edu.cn/simple
    # -i https://pypi.tuna.tsinghua.edu.cn/simple \
    # && rm -rf /tmp/omicverse

RUN pip install --no-cache-dir \
    numba==0.59 \
    pandas==1.5.3 \
    scvelo==0.3.2 \
    palantir==1.3.3 \
    wget==3.2 \
    -i https://pypi.tuna.tsinghua.edu.cn/simple

WORKDIR /app

COPY ./ov_test.py /app

# ENV Config
ENV PYTHONUNBUFFERED 1

# Define default command.
# CMD ["/bin/sh", "-c", "cd /app && tail -f /dev/null"]
# CMD ["/app/start.sh"]
CMD ["/bin/bash"]
# CMD ["jupyter-lab"]
