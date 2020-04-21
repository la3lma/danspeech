FROM pytorch/pytorch:1.4-cuda10.1-cudnn7-devel
ENV LD_LIBRARY_PATH=/usr/local/lib:$LD_LIBRARY_PATH

WORKDIR /workspace/

# install basics
RUN apt-get update -y
RUN apt-get install -y git curl ca-certificates bzip2 cmake tree htop bmon iotop sox libsox-dev libsox-fmt-all vim



# Just for monkeying around inside the container,
# remove for production use
RUN apt-get install -y emacs less


# Install Anaconda
WORKDIR /tmp
#RUN curl -O https://repo.anaconda.com/archive/Anaconda3-2019.03-Linux-x86_64.sh
RUN curl -O https://repo.anaconda.com/archive/Anaconda3-2020.02-Linux-x86_64.sh
# RUN [ $(sha256sum Anaconda3-2019.03-Linux-x86_64.sh) = "45c851b7497cc14d5ca060064394569f724b67d9b5f98a926ed49b834a6bb73a" ] || exit 1
RUN  (echo ; echo "yes"; echo; echo "yes"; echo ; echo )  | bash Anaconda3-2020.02-Linux-x86_64.sh
RUN conda update -n base -c defaults conda

# # Set up conda environment
COPY danspeech.yml .
RUN conda env create -f danspeech.yml
RUN conda activate danspeech

# SHELL ["conda", "run", "-n", "myenv", "/bin/bash", "-c"]

# install python deps
# RUN pip install danspeech

# Alternatively: Install from fresh sourcne
#  RUN git clone https://github.com/danspeech/danspeech
#  RUN cd danspeech &&   pip install .


# Install CTC decode
# RUN git clone --recursive https://github.com/parlance/ctcdecode.git
# RUN cd ctcdecode && pip install .


# WORKDIR /workspace/deepspeech.pytorch
# launch jupyter
# RUN mkdir data; mkdir notebooks;
# CMD jupyter-notebook --ip="*" --no-browser --allow-root
