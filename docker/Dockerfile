FROM pytorch/pytorch:1.5-cuda10.1-cudnn7-devel
ENV LD_LIBRARY_PATH=/usr/local/lib:$LD_LIBRARY_PATH

WORKDIR /workspace/

# install basics
RUN apt-get update -y
RUN apt-get install -y git curl ca-certificates bzip2 cmake tree htop bmon iotop sox libsox-dev libsox-fmt-all vim



##
## Installing CUDA  dev environment
##

# Pre-installation actions
# RUN apt-get install -y linux-headers-$(uname -r)
# RUN apt-get install wget

## Getting the cuda 10.2

# from  https://developer.nvidia.com/cuda-downloads?target_os=Linux&target_arch=x86_64&target_distro=Ubuntu&target_version=1804&target_type=deblocal

# RUN wget https://developer.download.nvidia.com/compute/cuda/repos/ubuntu1804/x86_64/cuda-ubuntu1804.pin
# RUN mv cuda-ubuntu1804.pin /etc/apt/preferences.d/cuda-repository-pin-600
# RUN wget http://developer.download.nvidia.com/compute/cuda/10.2/Prod/local_installers/cuda-repo-ubuntu1804-10-2-local-10.2.89-440.33.01_1.0-1_amd64.deb

# RUN dpkg -i cuda-repo-ubuntu1804-10-2-local-10.2.89-440.33.01_1.0-1_amd64.deb
# RUN apt-key add /var/cuda-repo-10-2-local-10.2.89-440.33.01/7fa2af80.pub
# RUN apt-get update
# RUN (echo 71 ; echo 6) | apt-get -y install cuda


## Getting the cuda 10.1
# RUN wget https://developer.download.nvidia.com/compute/cuda/repos/ubuntu1804/x86_64/cuda-ubuntu1804.pin
# RUN mv cuda-ubuntu1804.pin /etc/apt/preferences.d/cuda-repository-pin-600
# RUN wget http://developer.download.nvidia.com/compute/cuda/10.1/Prod/local_installers/cuda-repo-ubuntu1804-10-1-local-10.1.243-418.87.00_1.0-1_amd64.deb
# RUN dpkg -i cuda-repo-ubuntu1804-10-1-local-10.1.243-418.87.00_1.0-1_amd64.deb
# RUN apt-key add /var/cuda-repo-10-1-local-10.1.243-418.87.00/7fa2af80.pub
# RUN apt-get update
# RUN (echo 71 ; echo; echo 6; echo) | apt-get -y install cuda
       


# # Just for monkeying around inside the container,
# # remove for production use
RUN apt-get install -y emacs less


# # Install Anaconda
WORKDIR /tmp
RUN curl -O https://repo.anaconda.com/archive/Anaconda3-2020.02-Linux-x86_64.sh
RUN  (echo ; echo "yes"; echo; echo "yes"; echo ; echo )  | bash Anaconda3-2020.02-Linux-x86_64.sh
RUN conda update -n base -c defaults conda

# # # Set up conda environment
COPY danspeech.yml .
RUN conda env create -n danspeech -f danspeech.yml
RUN conda config --append envs_dirs /opt/conda/envs


# Installing pytorch

# WORKDIR /
# RUN git clone https://github.com/danspeech/danspeech
# RUN git clone https://github.com/danspeech/danspeech_training
# RUN git clone https://github.com/SeanNaren/deepspeech.pytorch
# # RUN conda activate danspeech (using trick from here https://pythonspeed.com/articles/activate-conda-dockerfile/)
SHELL ["conda", "run", "-n", "danspeech", "/bin/bash", "-c"]

RUN conda install pytorch torchvision -c pytorch

# # install python deps
# # RUN pip install danspeech

# # Alternatively: Install from fresh source
RUN git clone https://github.com/danspeech/danspeech
RUN cd danspeech &&   pip install .

# Install warpctc
WORKDIR /
RUN git clone https://github.com/baidu-research/warp-ctc.git
WORKDIR warp-ctc/build
RUN Torch_DIR=/opt/conda/envs/danspeech/lib/python3.8/site-packages/torch/share/cmake/Torch/ cmake ../

# XXX Commented out, since the next line will crash the build.
# RUN make

# # Install CTC decode
# RUN git clone --recursive https://github.com/parlance/ctcdecode.git
# RUN cd ctcdecode && pip install wget && export CUDA_VISIBLE_DEVICES=0  &&  pip install .


# # WORKDIR /workspace/deepspeech.pytorch
# # launch jupyter
# # RUN mkdir data; mkdir notebooks;
# # CMD jupyter-notebook --ip="*" --no-browser --allow-root
