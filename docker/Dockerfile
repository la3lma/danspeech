FROM pytorch/pytorch:1.5-cuda10.1-cudnn7-devel
ENV LD_LIBRARY_PATH=/usr/local/lib:$LD_LIBRARY_PATH

WORKDIR /workspace/

# install basics
RUN apt-get update -y
RUN apt-get install -y git curl ca-certificates bzip2 cmake tree htop bmon iotop sox libsox-dev libsox-fmt-all vim

##
## Install Gnu Emacs (just for playing around whild developing this container,
## remove for production).
##

RUN apt-get install -y emacs less

##
## Install Anaconda
##

# Get the distro and install it
WORKDIR /tmp
RUN curl -O https://repo.anaconda.com/archive/Anaconda3-2020.02-Linux-x86_64.sh
RUN  (echo ; echo "yes"; echo; echo "yes"; echo ; echo )  | bash Anaconda3-2020.02-Linux-x86_64.sh
RUN conda update -n base -c defaults conda

# ... then set up conda environment for danspeech
COPY danspeech.yml .
RUN conda env create -n danspeech -f danspeech.yml
RUN conda config --append envs_dirs /opt/conda/envs

#  Make it available easily from the command line
# (using trick from here https://pythonspeed.com/articles/activate-conda-dockerfile/)
SHELL ["conda", "run", "-n", "danspeech", "/bin/bash", "-c"]

##
##  Install torch
##
RUN conda install pytorch torchvision -c pytorch


##
## Install danspeech
##

WORKDIR /

# Not from pip (which we could)
# RUN pip install danspeech

# ... but from freh source
RUN git clone https://github.com/danspeech/danspeech
RUN cd danspeech &&   pip install .

##
##  Install warpctc
##
WORKDIR /
RUN git clone https://github.com/baidu-research/warp-ctc.git
WORKDIR warp-ctc/build


######
######   Things below this line is in general not working,
######   debugging under way
###### 

RUN Torch_DIR=/opt/conda/envs/danspeech/lib/python3.8/site-packages/torch/share/cmake/Torch/ cmake ../

# XXX Commented out, since the next line will crash the build.
RUN make

# # Install CTC decode
# RUN git clone --recursive https://github.com/parlance/ctcdecode.git
# RUN cd ctcdecode && pip install wget && export CUDA_VISIBLE_DEVICES=0  &&  pip install .

##
## Start a jupyter notebook (not sure if we want to do this,
## but keeping code here for now)
##
# # WORKDIR /workspace/deepspeech.pytorch
# # launch jupyter
# # RUN mkdir data; mkdir notebooks;
# # CMD jupyter-notebook --ip="*" --no-browser --allow-root


##
## Eventually we'll buiild at least the first one of these
##
# RUN git clone https://github.com/danspeech/danspeech_training
# RUN git clone https://github.com/SeanNaren/deepspeech.pytorch
