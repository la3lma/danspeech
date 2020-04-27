# README / TODO for the docker image for danspeech

Right now the build is blocked by an issue I don't understand.  It is
related to building warp-ctc.  Since that is blocking everything, at
this time it's the only thing on my TODO list to fix.  If you have any
insigths at all on how to fix this, please don't be shy: Reach out to
me on rmz@telenordigital.com or call me on +47 47900184.

How to reproduce:


1. Run ./build-container.sh. My build will obviously start from cached results, but the error consistently happens
   on the "cmake ../" step when building warp-ctc:


       rmz@loke:~/git/danspeech/docker$ ./build-container.sh 
       Sending build context to Docker daemon  35.33kB
       Step 1/24 : FROM pytorch/pytorch:1.5-cuda10.1-cudnn7-devel
        ---> 059dca74c93c
       Step 2/24 : ENV LD_LIBRARY_PATH=/usr/local/lib:$LD_LIBRARY_PATH
        ---> Using cache
        ---> 0f475e808411
       Step 3/24 : WORKDIR /workspace/
        ---> Using cache
        ---> bd9036d92d76
       Step 4/24 : RUN apt-get update -y
        ---> Using cache
        ---> c1ca9389f5fe
       Step 5/24 : RUN apt-get install -y git curl ca-certificates bzip2 cmake tree htop bmon iotop sox libsox-dev libsox-fmt-all vim
        ---> Using cache
        ---> f89022d9370d
       Step 6/24 : RUN apt-get install -y emacs less
        ---> Using cache
        ---> e33806b504c6
       Step 7/24 : WORKDIR /tmp
        ---> Using cache
        ---> 93cb81304d7c
       Step 8/24 : RUN curl -O https://repo.anaconda.com/archive/Anaconda3-2020.02-Linux-x86_64.sh
        ---> Using cache
        ---> 6dc851dc2c34
       Step 9/24 : RUN  (echo ; echo "yes"; echo; echo "yes"; echo ; echo )  | bash Anaconda3-2020.02-Linux-x86_64.sh
        ---> Using cache
        ---> 3d8e07b6e522
       Step 10/24 : RUN conda update -n base -c defaults conda
        ---> Using cache
        ---> 00c564d8083f
       Step 11/24 : COPY danspeech.yml .
        ---> Using cache
        ---> 3f7fee8aa401
       Step 12/24 : RUN conda env create -n danspeech -f danspeech.yml
        ---> Using cache
        ---> 3b9384f9ed26
       Step 13/24 : RUN conda config --append envs_dirs /opt/conda/envs
        ---> Using cache
        ---> 81ff13a59238
       Step 14/24 : SHELL ["conda", "run", "-n", "danspeech", "/bin/bash", "-c"]
        ---> Using cache
        ---> ae01a8ae2727
       Step 15/24 : RUN conda install pytorch torchvision -c pytorch
        ---> Using cache
        ---> 04138121cda8
       Step 16/24 : WORKDIR /
        ---> Using cache
        ---> 2723bf6109a5
       Step 17/24 : RUN git clone https://github.com/danspeech/danspeech
        ---> Using cache
        ---> 36de4a5eea6f
       Step 18/24 : RUN cd danspeech &&   pip install .
        ---> Using cache
        ---> 7ccada11fc0d
       Step 19/24 : WORKDIR /
        ---> Using cache
        ---> d5f0239a3d35
       Step 20/24 : RUN git clone https://github.com/baidu-research/warp-ctc.git
        ---> Using cache
        ---> b06dffcbe27e
       Step 21/24 : WORKDIR warp-ctc/build
        ---> Using cache
        ---> fbc90a3b8c92
       Step 22/24 : RUN Torch_DIR=/opt/conda/envs/danspeech/lib/python3.8/site-packages/torch/share/cmake/Torch/  cmake ../
        ---> Running in 0a6a5b05429a
       ERROR conda.cli.main_run:execute(32): Subprocess for 'conda run ['/bin/bash', '-c', 'Torch_DIR=/opt/conda/envs/danspeech/lib/python3.8/site-packages/torch/share/cmake/Torch/  cmake ../']' command failed.  (See above for error)
       CMake Error at CMakeLists.txt:177 (ADD_TORCH_PACKAGE):
         Unknown CMake command "ADD_TORCH_PACKAGE".



       -- The C compiler identification is GNU 7.4.0
       -- The CXX compiler identification is GNU 7.4.0
       -- Check for working C compiler: /usr/bin/cc
       -- Check for working C compiler: /usr/bin/cc -- works
       -- Detecting C compiler ABI info
       -- Detecting C compiler ABI info - done
       -- Detecting C compile features
       -- Detecting C compile features - done
       -- Check for working CXX compiler: /usr/bin/c++
       -- Check for working CXX compiler: /usr/bin/c++ -- works
       -- Detecting CXX compiler ABI info
       -- Detecting CXX compiler ABI info - done
       -- Detecting CXX compile features
       -- Detecting CXX compile features - done
       -- Looking for pthread.h
       -- Looking for pthread.h - found
       -- Looking for pthread_create
       -- Looking for pthread_create - not found
       -- Looking for pthread_create in pthreads
       -- Looking for pthread_create in pthreads - not found
       -- Looking for pthread_create in pthread
       -- Looking for pthread_create in pthread - found
       -- Found Threads: TRUE  
       -- Found CUDA: /usr/local/cuda (found suitable version "10.1", minimum required is "6.5") 
       -- Found CUDA: /usr/local/cuda (found version "10.1") 
       -- Caffe2: CUDA detected: 10.1
       -- Caffe2: CUDA nvcc is: /usr/local/cuda/bin/nvcc
       -- Caffe2: CUDA toolkit directory: /usr/local/cuda
       -- Caffe2: Header version is: 10.1
       -- Found CUDNN: /usr/lib/x86_64-linux-gnu/libcudnn.so  
       -- Found cuDNN: v7.6.5  (include: /usr/include, library: /usr/lib/x86_64-linux-gnu/libcudnn.so)
       -- Automatic GPU detection failed. Building for common architectures.
       -- Autodetected CUDA architecture(s): 3.5;5.0;5.2;6.0;6.1;7.0;7.0+PTX;7.5;7.5+PTX
       -- Added CUDA NVCC flags for: -gencode;arch=compute_35,code=sm_35;-gencode;arch=compute_50,code=sm_50;-gencode;arch=compute_52,code=sm_52;-gencode;arch=compute_60,code=sm_60;-gencode;arch=compute_61,code=sm_61;-gencode;arch=compute_70,code=sm_70;-gencode;arch=compute_75,code=sm_75;-gencode;arch=compute_70,code=compute_70;-gencode;arch=compute_75,code=compute_75
       -- Found torch: /opt/conda/envs/danspeech/lib/python3.8/site-packages/torch/lib/libtorch.so  
       -- cuda found TRUE
       -- Torch found /opt/conda/envs/danspeech/lib/python3.8/site-packages/torch/share/cmake/Torch
       -- Building shared library with GPU support
       -- NVCC_ARCH_FLAGS-DONNX_NAMESPACE=onnx_c2-gencodearch=compute_35,code=sm_35-gencodearch=compute_50,code=sm_50-gencodearch=compute_52,code=sm_52-gencodearch=compute_60,code=sm_60-gencodearch=compute_61,code=sm_61-gencodearch=compute_70,code=sm_70-gencodearch=compute_75,code=sm_75-gencodearch=compute_70,code=compute_70-gencodearch=compute_75,code=compute_75-Xcudafe--diag_suppress=cc_clobber_ignored-Xcudafe--diag_suppress=integer_sign_change-Xcudafe--diag_suppress=useless_using_declaration-Xcudafe--diag_suppress=set_but_not_used-std=c++14-Xcompiler-fPIC--expt-relaxed-constexpr--expt-extended-lambda -O2 -gencode arch=compute_30,code=sm_30 -gencode arch=compute_35,code=sm_35 -gencode arch=compute_50,code=sm_50 -gencode arch=compute_52,code=sm_52 -gencode arch=compute_60,code=sm_60 -gencode arch=compute_61,code=sm_61 -gencode arch=compute_62,code=sm_62 -gencode arch=compute_70,code=sm_70 --std=c++11 -Xcompiler -fopenmp
       -- Building Torch Bindings with GPU support
       -- Configuring incomplete, errors occurred!
       See also "/warp-ctc/build/CMakeFiles/CMakeOutput.log".
       See also "/warp-ctc/build/CMakeFiles/CMakeError.log".

       Removing intermediate container 0a6a5b05429a
        ---> 4642dbd1b911
       Step 23/24 : RUN pwd
        ---> Running in df0707b6d9d8
       /warp-ctc/build

       Removing intermediate container df0707b6d9d8
        ---> 0852000279ca
       Step 24/24 : RUN make
        ---> Running in faadbde69c14
       ERROR conda.cli.main_run:execute(32): Subprocess for 'conda run ['/bin/bash', '-c', 'make']' command failed.  (See above for error)
       make: *** No targets specified and no makefile found.  Stop.

       Removing intermediate container faadbde69c14
        ---> 627d11f2f559
       Successfully built 627d11f2f559
       Successfully tagged rmz/danspeech-cuda10.1:latest
       rmz@loke:~/git/danspeech/docker$ 



1.  I couldn't find any of the log files above, so I instead tried to start a version of the image and run the cmake command from the comand line. I then got this result:



       (base) root@d4c66736b301:/warp-ctc/build# cmake ../
       -- Found CUDA: /usr/local/cuda (found suitable version "10.1", minimum required is "6.5") 
       -- Found CUDA: /usr/local/cuda (found version "10.1") 
       -- Caffe2: CUDA detected: 10.1
       -- Caffe2: CUDA nvcc is: /usr/local/cuda/bin/nvcc
       -- Caffe2: CUDA toolkit directory: /usr/local/cuda
       -- Caffe2: Header version is: 10.1
       -- Found cuDNN: v7.6.5  (include: /usr/include, library: /usr/lib/x86_64-linux-gnu/libcudnn.so)
       -- Automatic GPU detection failed. Building for common architectures.
       -- Autodetected CUDA architecture(s): 3.5;5.0;5.2;6.0;6.1;7.0;7.0+PTX;7.5;7.5+PTX
       -- Added CUDA NVCC flags for: -gencode;arch=compute_35,code=sm_35;-gencode;arch=compute_50,code=sm_50;-gencode;arch=compute_52,code=sm_52;-gencode;arch=compute_60,code=sm_60;-gencode;arch=compute_61,code=sm_61;-gencode;arch=compute_70,code=sm_70;-gencode;arch=compute_75,code=sm_75;-gencode;arch=compute_70,code=compute_70;-gencode;arch=compute_75,code=compute_75
       -- cuda found TRUE
       -- Torch found /opt/conda/envs/danspeech/lib/python3.8/site-packages/torch/share/cmake/Torch
       -- Building shared library with GPU support
       -- NVCC_ARCH_FLAGS-DONNX_NAMESPACE=onnx_c2-gencodearch=compute_35,code=sm_35-gencodearch=compute_50,code=sm_50-gencodearch=compute_52,code=sm_52-gencodearch=compute_60,code=sm_60-gencodearch=compute_61,code=sm_61-gencodearch=compute_70,code=sm_70-gencodearch=compute_75,code=sm_75-gencodearch=compute_70,code=compute_70-gencodearch=compute_75,code=compute_75-Xcudafe--diag_suppress=cc_clobber_ignored-Xcudafe--diag_suppress=integer_sign_change-Xcudafe--diag_suppress=useless_using_declaration-Xcudafe--diag_suppress=set_but_not_used-std=c++14-Xcompiler-fPIC--expt-relaxed-constexpr--expt-extended-lambda -O2 -gencode arch=compute_30,code=sm_30 -gencode arch=compute_35,code=sm_35 -gencode arch=compute_50,code=sm_50 -gencode arch=compute_52,code=sm_52 -gencode arch=compute_60,code=sm_60 -gencode arch=compute_61,code=sm_61 -gencode arch=compute_62,code=sm_62 -gencode arch=compute_70,code=sm_70 --std=c++11 -Xcompiler -fopenmp
       -- Building Torch Bindings with GPU support
       CMake Error at CMakeLists.txt:169 (INSTALL):
         INSTALL TARGETS given no LIBRARY DESTINATION for shared library target
         "warpctc".


       CMake Error at CMakeLists.txt:177 (ADD_TORCH_PACKAGE):
         Unknown CMake command "ADD_TORCH_PACKAGE".


       -- Configuring incomplete, errors occurred!
       See also "/warp-ctc/build/CMakeFiles/CMakeOutput.log".
       See also "/warp-ctc/build/CMakeFiles/CMakeError.log".


1. The content of CMakeError.log

... and /warp-ctc/build/CMakeFiles/CMakeError.log:

     Determining if the pthread_create exist failed with the following output:
     Change Dir: /warp-ctc/build/CMakeFiles/CMakeTmp

     Run Build Command(s):/usr/bin/make cmTC_79844/fast 
     /usr/bin/make -f CMakeFiles/cmTC_79844.dir/build.make CMakeFiles/cmTC_79844.dir/build
     make[1]: Entering directory '/warp-ctc/build/CMakeFiles/CMakeTmp'
     Building C object CMakeFiles/cmTC_79844.dir/CheckSymbolExists.c.o
     /usr/bin/cc   -fPIC    -o CMakeFiles/cmTC_79844.dir/CheckSymbolExists.c.o   -c /warp-ctc/build/CMakeFiles/CMakeTmp/CheckSymbolExists.c
     Linking C executable cmTC_79844
     /opt/conda/envs/danspeech/bin/cmake -E cmake_link_script CMakeFiles/cmTC_79844.dir/link.txt --verbose=1
     /usr/bin/cc -fPIC     -rdynamic CMakeFiles/cmTC_79844.dir/CheckSymbolExists.c.o  -o cmTC_79844 
     CMakeFiles/cmTC_79844.dir/CheckSymbolExists.c.o: In function `main':
     CheckSymbolExists.c:(.text+0x1b): undefined reference to `pthread_create'
     collect2: error: ld returned 1 exit status
     CMakeFiles/cmTC_79844.dir/build.make:86: recipe for target 'cmTC_79844' failed
     make[1]: *** [cmTC_79844] Error 1
     make[1]: Leaving directory '/warp-ctc/build/CMakeFiles/CMakeTmp'
     Makefile:121: recipe for target 'cmTC_79844/fast' failed
     make: *** [cmTC_79844/fast] Error 2

     File /warp-ctc/build/CMakeFiles/CMakeTmp/CheckSymbolExists.c:
     /* */
     #include <pthread.h>

     int main(int argc, char** argv)
     {
       (void)argv;
     #ifndef pthread_create
       return ((int*)(&pthread_create))[argc];
     #else
       (void)argc;
       return 0;
     #endif
     }

     Determining if the function pthread_create exists in the pthreads failed with the following output:
     Change Dir: /warp-ctc/build/CMakeFiles/CMakeTmp

     Run Build Command(s):/usr/bin/make cmTC_2560f/fast 
     /usr/bin/make -f CMakeFiles/cmTC_2560f.dir/build.make CMakeFiles/cmTC_2560f.dir/build
     make[1]: Entering directory '/warp-ctc/build/CMakeFiles/CMakeTmp'
     Building C object CMakeFiles/cmTC_2560f.dir/CheckFunctionExists.c.o
     /usr/bin/cc   -fPIC -DCHECK_FUNCTION_EXISTS=pthread_create   -o CMakeFiles/cmTC_2560f.dir/CheckFunctionExists.c.o   -c /opt/conda/envs/danspeech/share/cmake-3.14/Modules/CheckFunctionExists.c
     Linking C executable cmTC_2560f
     /opt/conda/envs/danspeech/bin/cmake -E cmake_link_script CMakeFiles/cmTC_2560f.dir/link.txt --verbose=1
     /usr/bin/cc -fPIC -DCHECK_FUNCTION_EXISTS=pthread_create    -rdynamic CMakeFiles/cmTC_2560f.dir/CheckFunctionExists.c.o  -o cmTC_2560f -lpthreads 
     /usr/bin/ld: cannot find -lpthreads
     collect2: error: ld returned 1 exit status
     CMakeFiles/cmTC_2560f.dir/build.make:86: recipe for target 'cmTC_2560f' failed
     make[1]: *** [cmTC_2560f] Error 1
     make[1]: Leaving directory '/warp-ctc/build/CMakeFiles/CMakeTmp'
     Makefile:121: recipe for target 'cmTC_2560f/fast' failed
     make: *** [cmTC_2560f/fast] Error 2



1. The content of the  CMakeOutput.log:


       The system is: Linux - 4.15.0-96-generic - x86_64
       Compiling the C compiler identification source file "CMakeCCompilerId.c" succeeded.
       Compiler: /usr/bin/cc 
       Build flags: 
       Id flags:  

       The output was:
       0


       Compilation of the C compiler identification source "CMakeCCompilerId.c" produced "a.out"

       The C compiler identification is GNU, found in "/warp-ctc/build/CMakeFiles/3.14.0/CompilerIdC/a.out"

       Compiling the CXX compiler identification source file "CMakeCXXCompilerId.cpp" succeeded.
       Compiler: /usr/bin/c++ 
       Build flags: 
       Id flags:  

       The output was:
       0


       Compilation of the CXX compiler identification source "CMakeCXXCompilerId.cpp" produced "a.out"

       The CXX compiler identification is GNU, found in "/warp-ctc/build/CMakeFiles/3.14.0/CompilerIdCXX/a.out"

       Determining if the C compiler works passed with the following output:
       Change Dir: /warp-ctc/build/CMakeFiles/CMakeTmp

       Run Build Command(s):/usr/bin/make cmTC_6519d/fast 
       /usr/bin/make -f CMakeFiles/cmTC_6519d.dir/build.make CMakeFiles/cmTC_6519d.dir/build
       make[1]: Entering directory '/warp-ctc/build/CMakeFiles/CMakeTmp'
       Building C object CMakeFiles/cmTC_6519d.dir/testCCompiler.c.o
       /usr/bin/cc    -o CMakeFiles/cmTC_6519d.dir/testCCompiler.c.o   -c /warp-ctc/build/CMakeFiles/CMakeTmp/testCCompiler.c
       Linking C executable cmTC_6519d
       /opt/conda/envs/danspeech/bin/cmake -E cmake_link_script CMakeFiles/cmTC_6519d.dir/link.txt --verbose=1
       /usr/bin/cc      -rdynamic CMakeFiles/cmTC_6519d.dir/testCCompiler.c.o  -o cmTC_6519d 
       make[1]: Leaving directory '/warp-ctc/build/CMakeFiles/CMakeTmp'


       Detecting C compiler ABI info compiled with the following output:
       Change Dir: /warp-ctc/build/CMakeFiles/CMakeTmp

       Run Build Command(s):/usr/bin/make cmTC_50ac5/fast 
       /usr/bin/make -f CMakeFiles/cmTC_50ac5.dir/build.make CMakeFiles/cmTC_50ac5.dir/build
       make[1]: Entering directory '/warp-ctc/build/CMakeFiles/CMakeTmp'
       Building C object CMakeFiles/cmTC_50ac5.dir/CMakeCCompilerABI.c.o
       /usr/bin/cc   -v -o CMakeFiles/cmTC_50ac5.dir/CMakeCCompilerABI.c.o   -c /opt/conda/envs/danspeech/share/cmake-3.14/Modules/CMakeCCompilerABI.c
       Using built-in specs.
       COLLECT_GCC=/usr/bin/cc
       OFFLOAD_TARGET_NAMES=nvptx-none
       OFFLOAD_TARGET_DEFAULT=1
       Target: x86_64-linux-gnu
       Configured with: ../src/configure -v --with-pkgversion='Ubuntu 7.4.0-1ubuntu1~18.04.1' --with-bugurl=file:///usr/share/doc/gcc-7/README.Bugs --enable-languages=c,ada,c++,go,brig,d,fortran,objc,obj-c++ --prefix=/usr --with-gcc-major-version-only --program-suffix=-7 --program-prefix=x86_64-linux-gnu- --enable-shared --enable-linker-build-id --libexecdir=/usr/lib --without-included-gettext --enable-threads=posix --libdir=/usr/lib --enable-nls --with-sysroot=/ --enable-clocale=gnu --enable-libstdcxx-debug --enable-libstdcxx-time=yes --with-default-libstdcxx-abi=new --enable-gnu-unique-object --disable-vtable-verify --enable-libmpx --enable-plugin --enable-default-pie --with-system-zlib --with-target-system-zlib --enable-objc-gc=auto --enable-multiarch --disable-werror --with-arch-32=i686 --with-abi=m64 --with-multilib-list=m32,m64,mx32 --enable-multilib --with-tune=generic --enable-offload-targets=nvptx-none --without-cuda-driver --enable-checking=release --build=x86_64-linux-gnu --host=x86_64-linux-gnu --target=x86_64-linux-gnu
       Thread model: posix
       gcc version 7.4.0 (Ubuntu 7.4.0-1ubuntu1~18.04.1) 
       COLLECT_GCC_OPTIONS='-v' '-o' 'CMakeFiles/cmTC_50ac5.dir/CMakeCCompilerABI.c.o' '-c' '-mtune=generic' '-march=x86-64'
        /usr/lib/gcc/x86_64-linux-gnu/7/cc1 -quiet -v -imultiarch x86_64-linux-gnu /opt/conda/envs/danspeech/share/cmake-3.14/Modules/CMakeCCompilerABI.c -quiet -dumpbase CMakeCCompilerABI.c -mtune=generic -march=x86-64 -auxbase-strip CMakeFiles/cmTC_50ac5.dir/CMakeCCompilerABI.c.o -version -fstack-protector-strong -Wformat -Wformat-security -o /tmp/cclVlrU2.s
       GNU C11 (Ubuntu 7.4.0-1ubuntu1~18.04.1) version 7.4.0 (x86_64-linux-gnu)
               compiled by GNU C version 7.4.0, GMP version 6.1.2, MPFR version 4.0.1, MPC version 1.1.0, isl version isl-0.19-GMP

       GGC heuristics: --param ggc-min-expand=100 --param ggc-min-heapsize=131072
       ignoring nonexistent directory "/usr/local/include/x86_64-linux-gnu"
       ignoring nonexistent directory "/usr/lib/gcc/x86_64-linux-gnu/7/../../../../x86_64-linux-gnu/include"
       #include "..." search starts here:
       #include <...> search starts here:
        /usr/lib/gcc/x86_64-linux-gnu/7/include
        /usr/local/include
        /usr/lib/gcc/x86_64-linux-gnu/7/include-fixed
        /usr/include/x86_64-linux-gnu
        /usr/include
       End of search list.
       GNU C11 (Ubuntu 7.4.0-1ubuntu1~18.04.1) version 7.4.0 (x86_64-linux-gnu)
               compiled by GNU C version 7.4.0, GMP version 6.1.2, MPFR version 4.0.1, MPC version 1.1.0, isl version isl-0.19-GMP

       GGC heuristics: --param ggc-min-expand=100 --param ggc-min-heapsize=131072
       Compiler executable checksum: fa57db1fe2d756b22d454aa8428fd3bd
       COLLECT_GCC_OPTIONS='-v' '-o' 'CMakeFiles/cmTC_50ac5.dir/CMakeCCompilerABI.c.o' '-c' '-mtune=generic' '-march=x86-64'
        as -v --64 -o CMakeFiles/cmTC_50ac5.dir/CMakeCCompilerABI.c.o /tmp/cclVlrU2.s
       GNU assembler version 2.30 (x86_64-linux-gnu) using BFD version (GNU Binutils for Ubuntu) 2.30
       COMPILER_PATH=/usr/lib/gcc/x86_64-linux-gnu/7/:/usr/lib/gcc/x86_64-linux-gnu/7/:/usr/lib/gcc/x86_64-linux-gnu/:/usr/lib/gcc/x86_64-linux-gnu/7/:/usr/lib/gcc/x86_64-linux-gnu/
       LIBRARY_PATH=/usr/lib/gcc/x86_64-linux-gnu/7/:/usr/lib/gcc/x86_64-linux-gnu/7/../../../x86_64-linux-gnu/:/usr/lib/gcc/x86_64-linux-gnu/7/../../../../lib/:/lib/x86_64-linux-gnu/:/lib/../lib/:/usr/lib/x86_64-linux-gnu/:/usr/lib/../lib/:/usr/local/cuda/lib64/stubs/:/usr/lib/gcc/x86_64-linux-gnu/7/../../../:/lib/:/usr/lib/
       COLLECT_GCC_OPTIONS='-v' '-o' 'CMakeFiles/cmTC_50ac5.dir/CMakeCCompilerABI.c.o' '-c' '-mtune=generic' '-march=x86-64'
       Linking C executable cmTC_50ac5
       /opt/conda/envs/danspeech/bin/cmake -E cmake_link_script CMakeFiles/cmTC_50ac5.dir/link.txt --verbose=1
       /usr/bin/cc     -v -rdynamic CMakeFiles/cmTC_50ac5.dir/CMakeCCompilerABI.c.o  -o cmTC_50ac5 
       Using built-in specs.
       COLLECT_GCC=/usr/bin/cc
       COLLECT_LTO_WRAPPER=/usr/lib/gcc/x86_64-linux-gnu/7/lto-wrapper
       OFFLOAD_TARGET_NAMES=nvptx-none
       OFFLOAD_TARGET_DEFAULT=1
       Target: x86_64-linux-gnu
       Configured with: ../src/configure -v --with-pkgversion='Ubuntu 7.4.0-1ubuntu1~18.04.1' --with-bugurl=file:///usr/share/doc/gcc-7/README.Bugs --enable-languages=c,ada,c++,go,brig,d,fortran,objc,obj-c++ --prefix=/usr --with-gcc-major-version-only --program-suffix=-7 --program-prefix=x86_64-linux-gnu- --enable-shared --enable-linker-build-id --libexecdir=/usr/lib --without-included-gettext --enable-threads=posix --libdir=/usr/lib --enable-nls --with-sysroot=/ --enable-clocale=gnu --enable-libstdcxx-debug --enable-libstdcxx-time=yes --with-default-libstdcxx-abi=new --enable-gnu-unique-object --disable-vtable-verify --enable-libmpx --enable-plugin --enable-default-pie --with-system-zlib --with-target-system-zlib --enable-objc-gc=auto --enable-multiarch --disable-werror --with-arch-32=i686 --with-abi=m64 --with-multilib-list=m32,m64,mx32 --enable-multilib --with-tune=generic --enable-offload-targets=nvptx-none --without-cuda-driver --enable-checking=release --build=x86_64-linux-gnu --host=x86_64-linux-gnu --target=x86_64-linux-gnu
       Thread model: posix
       gcc version 7.4.0 (Ubuntu 7.4.0-1ubuntu1~18.04.1) 
       COMPILER_PATH=/usr/lib/gcc/x86_64-linux-gnu/7/:/usr/lib/gcc/x86_64-linux-gnu/7/:/usr/lib/gcc/x86_64-linux-gnu/:/usr/lib/gcc/x86_64-linux-gnu/7/:/usr/lib/gcc/x86_64-linux-gnu/
       LIBRARY_PATH=/usr/lib/gcc/x86_64-linux-gnu/7/:/usr/lib/gcc/x86_64-linux-gnu/7/../../../x86_64-linux-gnu/:/usr/lib/gcc/x86_64-linux-gnu/7/../../../../lib/:/lib/x86_64-linux-gnu/:/lib/../lib/:/usr/lib/x86_64-linux-gnu/:/usr/lib/../lib/:/usr/local/cuda/lib64/stubs/:/usr/lib/gcc/x86_64-linux-gnu/7/../../../:/lib/:/usr/lib/
       COLLECT_GCC_OPTIONS='-v' '-rdynamic' '-o' 'cmTC_50ac5' '-mtune=generic' '-march=x86-64'
        /usr/lib/gcc/x86_64-linux-gnu/7/collect2 -plugin /usr/lib/gcc/x86_64-linux-gnu/7/liblto_plugin.so -plugin-opt=/usr/lib/gcc/x86_64-linux-gnu/7/lto-wrapper -plugin-opt=-fresolution=/tmp/cc7gUhM8.res -plugin-opt=-pass-through=-lgcc -plugin-opt=-pass-through=-lgcc_s -plugin-opt=-pass-through=-lc -plugin-opt=-pass-through=-lgcc -plugin-opt=-pass-through=-lgcc_s --sysroot=/ --build-id --eh-frame-hdr -m elf_x86_64 --hash-style=gnu --as-needed -export-dynamic -dynamic-linker /lib64/ld-linux-x86-64.so.2 -pie -z now -z relro -o cmTC_50ac5 /usr/lib/gcc/x86_64-linux-gnu/7/../../../x86_64-linux-gnu/Scrt1.o /usr/lib/gcc/x86_64-linux-gnu/7/../../../x86_64-linux-gnu/crti.o /usr/lib/gcc/x86_64-linux-gnu/7/crtbeginS.o -L/usr/lib/gcc/x86_64-linux-gnu/7 -L/usr/lib/gcc/x86_64-linux-gnu/7/../../../x86_64-linux-gnu -L/usr/lib/gcc/x86_64-linux-gnu/7/../../../../lib -L/lib/x86_64-linux-gnu -L/lib/../lib -L/usr/lib/x86_64-linux-gnu -L/usr/lib/../lib -L/usr/local/cuda/lib64/stubs -L/usr/lib/gcc/x86_64-linux-gnu/7/../../.. CMakeFiles/cmTC_50ac5.dir/CMakeCCompilerABI.c.o -lgcc --push-state --as-needed -lgcc_s --pop-state -lc -lgcc --push-state --as-needed -lgcc_s --pop-state /usr/lib/gcc/x86_64-linux-gnu/7/crtendS.o /usr/lib/gcc/x86_64-linux-gnu/7/../../../x86_64-linux-gnu/crtn.o
       COLLECT_GCC_OPTIONS='-v' '-rdynamic' '-o' 'cmTC_50ac5' '-mtune=generic' '-march=x86-64'
       make[1]: Leaving directory '/warp-ctc/build/CMakeFiles/CMakeTmp'


       Parsed C implicit include dir info from above output: rv=done
         found start of include info
         found start of implicit include info
           add: [/usr/lib/gcc/x86_64-linux-gnu/7/include]
           add: [/usr/local/include]
           add: [/usr/lib/gcc/x86_64-linux-gnu/7/include-fixed]
           add: [/usr/include/x86_64-linux-gnu]
           add: [/usr/include]
         end of search list found
         implicit include dirs: [/usr/lib/gcc/x86_64-linux-gnu/7/include;/usr/local/include;/usr/lib/gcc/x86_64-linux-gnu/7/include-fixed;/usr/include/x86_64-linux-gnu;/usr/include]


       Parsed C implicit link information from above output:
         link line regex: [^( *|.*[/\])(ld|CMAKE_LINK_STARTFILE-NOTFOUND|([^/\]+-)?ld|collect2)[^/\]*( |$)]
         ignore line: [Change Dir: /warp-ctc/build/CMakeFiles/CMakeTmp]
         ignore line: []
         ignore line: [Run Build Command(s):/usr/bin/make cmTC_50ac5/fast ]
         ignore line: [/usr/bin/make -f CMakeFiles/cmTC_50ac5.dir/build.make CMakeFiles/cmTC_50ac5.dir/build]
         ignore line: [make[1]: Entering directory '/warp-ctc/build/CMakeFiles/CMakeTmp']
         ignore line: [Building C object CMakeFiles/cmTC_50ac5.dir/CMakeCCompilerABI.c.o]
         ignore line: [/usr/bin/cc   -v -o CMakeFiles/cmTC_50ac5.dir/CMakeCCompilerABI.c.o   -c /opt/conda/envs/danspeech/share/cmake-3.14/Modules/CMakeCCompilerABI.c]
         ignore line: [Using built-in specs.]
         ignore line: [COLLECT_GCC=/usr/bin/cc]
         ignore line: [OFFLOAD_TARGET_NAMES=nvptx-none]
         ignore line: [OFFLOAD_TARGET_DEFAULT=1]
         ignore line: [Target: x86_64-linux-gnu]
         ignore line: [Configured with: ../src/configure -v --with-pkgversion='Ubuntu 7.4.0-1ubuntu1~18.04.1' --with-bugurl=file:///usr/share/doc/gcc-7/README.Bugs --enable-languages=c,ada,c++,go,brig,d,fortran,objc,obj-c++ --prefix=/usr --with-gcc-major-version-only --program-suffix=-7 --program-prefix=x86_64-linux-gnu- --enable-shared --enable-linker-build-id --libexecdir=/usr/lib --without-included-gettext --enable-threads=posix --libdir=/usr/lib --enable-nls --with-sysroot=/ --enable-clocale=gnu --enable-libstdcxx-debug --enable-libstdcxx-time=yes --with-default-libstdcxx-abi=new --enable-gnu-unique-object --disable-vtable-verify --enable-libmpx --enable-plugin --enable-default-pie --with-system-zlib --with-target-system-zlib --enable-objc-gc=auto --enable-multiarch --disable-werror --with-arch-32=i686 --with-abi=m64 --with-multilib-list=m32,m64,mx32 --enable-multilib --with-tune=generic --enable-offload-targets=nvptx-none --without-cuda-driver --enable-checking=release --build=x86_64-linux-gnu --host=x86_64-linux-gnu --target=x86_64-linux-gnu]
         ignore line: [Thread model: posix]
         ignore line: [gcc version 7.4.0 (Ubuntu 7.4.0-1ubuntu1~18.04.1) ]
         ignore line: [COLLECT_GCC_OPTIONS='-v' '-o' 'CMakeFiles/cmTC_50ac5.dir/CMakeCCompilerABI.c.o' '-c' '-mtune=generic' '-march=x86-64']
         ignore line: [ /usr/lib/gcc/x86_64-linux-gnu/7/cc1 -quiet -v -imultiarch x86_64-linux-gnu /opt/conda/envs/danspeech/share/cmake-3.14/Modules/CMakeCCompilerABI.c -quiet -dumpbase CMakeCCompilerABI.c -mtune=generic -march=x86-64 -auxbase-strip CMakeFiles/cmTC_50ac5.dir/CMakeCCompilerABI.c.o -version -fstack-protector-strong -Wformat -Wformat-security -o /tmp/cclVlrU2.s]
         ignore line: [GNU C11 (Ubuntu 7.4.0-1ubuntu1~18.04.1) version 7.4.0 (x86_64-linux-gnu)]
         ignore line: [ compiled by GNU C version 7.4.0, GMP version 6.1.2, MPFR version 4.0.1, MPC version 1.1.0, isl version isl-0.19-GMP]
         ignore line: []
         ignore line: [GGC heuristics: --param ggc-min-expand=100 --param ggc-min-heapsize=131072]
         ignore line: [ignoring nonexistent directory "/usr/local/include/x86_64-linux-gnu"]
         ignore line: [ignoring nonexistent directory "/usr/lib/gcc/x86_64-linux-gnu/7/../../../../x86_64-linux-gnu/include"]
         ignore line: [#include "..." search starts here:]
         ignore line: [#include <...> search starts here:]
         ignore line: [ /usr/lib/gcc/x86_64-linux-gnu/7/include]
         ignore line: [ /usr/local/include]
         ignore line: [ /usr/lib/gcc/x86_64-linux-gnu/7/include-fixed]
         ignore line: [ /usr/include/x86_64-linux-gnu]
         ignore line: [ /usr/include]
         ignore line: [End of search list.]
         ignore line: [GNU C11 (Ubuntu 7.4.0-1ubuntu1~18.04.1) version 7.4.0 (x86_64-linux-gnu)]
         ignore line: [ compiled by GNU C version 7.4.0, GMP version 6.1.2, MPFR version 4.0.1, MPC version 1.1.0, isl version isl-0.19-GMP]
         ignore line: []
         ignore line: [GGC heuristics: --param ggc-min-expand=100 --param ggc-min-heapsize=131072]
         ignore line: [Compiler executable checksum: fa57db1fe2d756b22d454aa8428fd3bd]
         ignore line: [COLLECT_GCC_OPTIONS='-v' '-o' 'CMakeFiles/cmTC_50ac5.dir/CMakeCCompilerABI.c.o' '-c' '-mtune=generic' '-march=x86-64']
         ignore line: [ as -v --64 -o CMakeFiles/cmTC_50ac5.dir/CMakeCCompilerABI.c.o /tmp/cclVlrU2.s]
         ignore line: [GNU assembler version 2.30 (x86_64-linux-gnu) using BFD version (GNU Binutils for Ubuntu) 2.30]
         ignore line: [COMPILER_PATH=/usr/lib/gcc/x86_64-linux-gnu/7/:/usr/lib/gcc/x86_64-linux-gnu/7/:/usr/lib/gcc/x86_64-linux-gnu/:/usr/lib/gcc/x86_64-linux-gnu/7/:/usr/lib/gcc/x86_64-linux-gnu/]
         ignore line: [LIBRARY_PATH=/usr/lib/gcc/x86_64-linux-gnu/7/:/usr/lib/gcc/x86_64-linux-gnu/7/../../../x86_64-linux-gnu/:/usr/lib/gcc/x86_64-linux-gnu/7/../../../../lib/:/lib/x86_64-linux-gnu/:/lib/../lib/:/usr/lib/x86_64-linux-gnu/:/usr/lib/../lib/:/usr/local/cuda/lib64/stubs/:/usr/lib/gcc/x86_64-linux-gnu/7/../../../:/lib/:/usr/lib/]
         ignore line: [COLLECT_GCC_OPTIONS='-v' '-o' 'CMakeFiles/cmTC_50ac5.dir/CMakeCCompilerABI.c.o' '-c' '-mtune=generic' '-march=x86-64']
         ignore line: [Linking C executable cmTC_50ac5]
         ignore line: [/opt/conda/envs/danspeech/bin/cmake -E cmake_link_script CMakeFiles/cmTC_50ac5.dir/link.txt --verbose=1]
         ignore line: [/usr/bin/cc     -v -rdynamic CMakeFiles/cmTC_50ac5.dir/CMakeCCompilerABI.c.o  -o cmTC_50ac5 ]
         ignore line: [Using built-in specs.]
         ignore line: [COLLECT_GCC=/usr/bin/cc]
         ignore line: [COLLECT_LTO_WRAPPER=/usr/lib/gcc/x86_64-linux-gnu/7/lto-wrapper]
         ignore line: [OFFLOAD_TARGET_NAMES=nvptx-none]
         ignore line: [OFFLOAD_TARGET_DEFAULT=1]
         ignore line: [Target: x86_64-linux-gnu]
         ignore line: [Configured with: ../src/configure -v --with-pkgversion='Ubuntu 7.4.0-1ubuntu1~18.04.1' --with-bugurl=file:///usr/share/doc/gcc-7/README.Bugs --enable-languages=c,ada,c++,go,brig,d,fortran,objc,obj-c++ --prefix=/usr --with-gcc-major-version-only --program-suffix=-7 --program-prefix=x86_64-linux-gnu- --enable-shared --enable-linker-build-id --libexecdir=/usr/lib --without-included-gettext --enable-threads=posix --libdir=/usr/lib --enable-nls --with-sysroot=/ --enable-clocale=gnu --enable-libstdcxx-debug --enable-libstdcxx-time=yes --with-default-libstdcxx-abi=new --enable-gnu-unique-object --disable-vtable-verify --enable-libmpx --enable-plugin --enable-default-pie --with-system-zlib --with-target-system-zlib --enable-objc-gc=auto --enable-multiarch --disable-werror --with-arch-32=i686 --with-abi=m64 --with-multilib-list=m32,m64,mx32 --enable-multilib --with-tune=generic --enable-offload-targets=nvptx-none --without-cuda-driver --enable-checking=release --build=x86_64-linux-gnu --host=x86_64-linux-gnu --target=x86_64-linux-gnu]
         ignore line: [Thread model: posix]
         ignore line: [gcc version 7.4.0 (Ubuntu 7.4.0-1ubuntu1~18.04.1) ]
         ignore line: [COMPILER_PATH=/usr/lib/gcc/x86_64-linux-gnu/7/:/usr/lib/gcc/x86_64-linux-gnu/7/:/usr/lib/gcc/x86_64-linux-gnu/:/usr/lib/gcc/x86_64-linux-gnu/7/:/usr/lib/gcc/x86_64-linux-gnu/]
         ignore line: [LIBRARY_PATH=/usr/lib/gcc/x86_64-linux-gnu/7/:/usr/lib/gcc/x86_64-linux-gnu/7/../../../x86_64-linux-gnu/:/usr/lib/gcc/x86_64-linux-gnu/7/../../../../lib/:/lib/x86_64-linux-gnu/:/lib/../lib/:/usr/lib/x86_64-linux-gnu/:/usr/lib/../lib/:/usr/local/cuda/lib64/stubs/:/usr/lib/gcc/x86_64-linux-gnu/7/../../../:/lib/:/usr/lib/]
         ignore line: [COLLECT_GCC_OPTIONS='-v' '-rdynamic' '-o' 'cmTC_50ac5' '-mtune=generic' '-march=x86-64']
         link line: [ /usr/lib/gcc/x86_64-linux-gnu/7/collect2 -plugin /usr/lib/gcc/x86_64-linux-gnu/7/liblto_plugin.so -plugin-opt=/usr/lib/gcc/x86_64-linux-gnu/7/lto-wrapper -plugin-opt=-fresolution=/tmp/cc7gUhM8.res -plugin-opt=-pass-through=-lgcc -plugin-opt=-pass-through=-lgcc_s -plugin-opt=-pass-through=-lc -plugin-opt=-pass-through=-lgcc -plugin-opt=-pass-through=-lgcc_s --sysroot=/ --build-id --eh-frame-hdr -m elf_x86_64 --hash-style=gnu --as-needed -export-dynamic -dynamic-linker /lib64/ld-linux-x86-64.so.2 -pie -z now -z relro -o cmTC_50ac5 /usr/lib/gcc/x86_64-linux-gnu/7/../../../x86_64-linux-gnu/Scrt1.o /usr/lib/gcc/x86_64-linux-gnu/7/../../../x86_64-linux-gnu/crti.o /usr/lib/gcc/x86_64-linux-gnu/7/crtbeginS.o -L/usr/lib/gcc/x86_64-linux-gnu/7 -L/usr/lib/gcc/x86_64-linux-gnu/7/../../../x86_64-linux-gnu -L/usr/lib/gcc/x86_64-linux-gnu/7/../../../../lib -L/lib/x86_64-linux-gnu -L/lib/../lib -L/usr/lib/x86_64-linux-gnu -L/usr/lib/../lib -L/usr/local/cuda/lib64/stubs -L/usr/lib/gcc/x86_64-linux-gnu/7/../../.. CMakeFiles/cmTC_50ac5.dir/CMakeCCompilerABI.c.o -lgcc --push-state --as-needed -lgcc_s --pop-state -lc -lgcc --push-state --as-needed -lgcc_s --pop-state /usr/lib/gcc/x86_64-linux-gnu/7/crtendS.o /usr/lib/gcc/x86_64-linux-gnu/7/../../../x86_64-linux-gnu/crtn.o]
           arg [/usr/lib/gcc/x86_64-linux-gnu/7/collect2] ==> ignore
           arg [-plugin] ==> ignore
           arg [/usr/lib/gcc/x86_64-linux-gnu/7/liblto_plugin.so] ==> ignore
           arg [-plugin-opt=/usr/lib/gcc/x86_64-linux-gnu/7/lto-wrapper] ==> ignore
           arg [-plugin-opt=-fresolution=/tmp/cc7gUhM8.res] ==> ignore
           arg [-plugin-opt=-pass-through=-lgcc] ==> ignore
           arg [-plugin-opt=-pass-through=-lgcc_s] ==> ignore
           arg [-plugin-opt=-pass-through=-lc] ==> ignore
           arg [-plugin-opt=-pass-through=-lgcc] ==> ignore
           arg [-plugin-opt=-pass-through=-lgcc_s] ==> ignore
           arg [--sysroot=/] ==> ignore
           arg [--build-id] ==> ignore
           arg [--eh-frame-hdr] ==> ignore
           arg [-m] ==> ignore
           arg [elf_x86_64] ==> ignore
           arg [--hash-style=gnu] ==> ignore
           arg [--as-needed] ==> ignore
           arg [-export-dynamic] ==> ignore
           arg [-dynamic-linker] ==> ignore
           arg [/lib64/ld-linux-x86-64.so.2] ==> ignore
           arg [-pie] ==> ignore
           arg [-znow] ==> ignore
           arg [-zrelro] ==> ignore
           arg [-o] ==> ignore
           arg [cmTC_50ac5] ==> ignore
           arg [/usr/lib/gcc/x86_64-linux-gnu/7/../../../x86_64-linux-gnu/Scrt1.o] ==> ignore
           arg [/usr/lib/gcc/x86_64-linux-gnu/7/../../../x86_64-linux-gnu/crti.o] ==> ignore
           arg [/usr/lib/gcc/x86_64-linux-gnu/7/crtbeginS.o] ==> ignore
           arg [-L/usr/lib/gcc/x86_64-linux-gnu/7] ==> dir [/usr/lib/gcc/x86_64-linux-gnu/7]
           arg [-L/usr/lib/gcc/x86_64-linux-gnu/7/../../../x86_64-linux-gnu] ==> dir [/usr/lib/gcc/x86_64-linux-gnu/7/../../../x86_64-linux-gnu]
           arg [-L/usr/lib/gcc/x86_64-linux-gnu/7/../../../../lib] ==> dir [/usr/lib/gcc/x86_64-linux-gnu/7/../../../../lib]
           arg [-L/lib/x86_64-linux-gnu] ==> dir [/lib/x86_64-linux-gnu]
           arg [-L/lib/../lib] ==> dir [/lib/../lib]
           arg [-L/usr/lib/x86_64-linux-gnu] ==> dir [/usr/lib/x86_64-linux-gnu]
           arg [-L/usr/lib/../lib] ==> dir [/usr/lib/../lib]
           arg [-L/usr/local/cuda/lib64/stubs] ==> dir [/usr/local/cuda/lib64/stubs]
           arg [-L/usr/lib/gcc/x86_64-linux-gnu/7/../../..] ==> dir [/usr/lib/gcc/x86_64-linux-gnu/7/../../..]
           arg [CMakeFiles/cmTC_50ac5.dir/CMakeCCompilerABI.c.o] ==> ignore
           arg [-lgcc] ==> lib [gcc]
           arg [--push-state] ==> ignore
           arg [--as-needed] ==> ignore
           arg [-lgcc_s] ==> lib [gcc_s]
           arg [--pop-state] ==> ignore
           arg [-lc] ==> lib [c]
           arg [-lgcc] ==> lib [gcc]
           arg [--push-state] ==> ignore
           arg [--as-needed] ==> ignore
           arg [-lgcc_s] ==> lib [gcc_s]
           arg [--pop-state] ==> ignore
           arg [/usr/lib/gcc/x86_64-linux-gnu/7/crtendS.o] ==> ignore
           arg [/usr/lib/gcc/x86_64-linux-gnu/7/../../../x86_64-linux-gnu/crtn.o] ==> ignore
         collapse library dir [/usr/lib/gcc/x86_64-linux-gnu/7] ==> [/usr/lib/gcc/x86_64-linux-gnu/7]
         collapse library dir [/usr/lib/gcc/x86_64-linux-gnu/7/../../../x86_64-linux-gnu] ==> [/usr/lib/x86_64-linux-gnu]
         collapse library dir [/usr/lib/gcc/x86_64-linux-gnu/7/../../../../lib] ==> [/usr/lib]
         collapse library dir [/lib/x86_64-linux-gnu] ==> [/lib/x86_64-linux-gnu]
         collapse library dir [/lib/../lib] ==> [/lib]
         collapse library dir [/usr/lib/x86_64-linux-gnu] ==> [/usr/lib/x86_64-linux-gnu]
         collapse library dir [/usr/lib/../lib] ==> [/usr/lib]
         collapse library dir [/usr/local/cuda/lib64/stubs] ==> [/usr/local/cuda/lib64/stubs]
         collapse library dir [/usr/lib/gcc/x86_64-linux-gnu/7/../../..] ==> [/usr/lib]
         implicit libs: [gcc;gcc_s;c;gcc;gcc_s]
         implicit dirs: [/usr/lib/gcc/x86_64-linux-gnu/7;/usr/lib/x86_64-linux-gnu;/usr/lib;/lib/x86_64-linux-gnu;/lib;/usr/local/cuda/lib64/stubs]
         implicit fwks: []




       Detecting C [-std=c11] compiler features compiled with the following output:
       Change Dir: /warp-ctc/build/CMakeFiles/CMakeTmp

       Run Build Command(s):/usr/bin/make cmTC_755bd/fast 
       /usr/bin/make -f CMakeFiles/cmTC_755bd.dir/build.make CMakeFiles/cmTC_755bd.dir/build
       make[1]: Entering directory '/warp-ctc/build/CMakeFiles/CMakeTmp'
       Building C object CMakeFiles/cmTC_755bd.dir/feature_tests.c.o
       /usr/bin/cc   -std=c11 -o CMakeFiles/cmTC_755bd.dir/feature_tests.c.o   -c /warp-ctc/build/CMakeFiles/feature_tests.c
       Linking C executable cmTC_755bd
       /opt/conda/envs/danspeech/bin/cmake -E cmake_link_script CMakeFiles/cmTC_755bd.dir/link.txt --verbose=1
       /usr/bin/cc      -rdynamic CMakeFiles/cmTC_755bd.dir/feature_tests.c.o  -o cmTC_755bd 
       make[1]: Leaving directory '/warp-ctc/build/CMakeFiles/CMakeTmp'


           Feature record: C_FEATURE:1c_function_prototypes
           Feature record: C_FEATURE:1c_restrict
           Feature record: C_FEATURE:1c_static_assert
           Feature record: C_FEATURE:1c_variadic_macros


       Detecting C [-std=c99] compiler features compiled with the following output:
       Change Dir: /warp-ctc/build/CMakeFiles/CMakeTmp

       Run Build Command(s):/usr/bin/make cmTC_f1fdb/fast 
       /usr/bin/make -f CMakeFiles/cmTC_f1fdb.dir/build.make CMakeFiles/cmTC_f1fdb.dir/build
       make[1]: Entering directory '/warp-ctc/build/CMakeFiles/CMakeTmp'
       Building C object CMakeFiles/cmTC_f1fdb.dir/feature_tests.c.o
       /usr/bin/cc   -std=c99 -o CMakeFiles/cmTC_f1fdb.dir/feature_tests.c.o   -c /warp-ctc/build/CMakeFiles/feature_tests.c
       Linking C executable cmTC_f1fdb
       /opt/conda/envs/danspeech/bin/cmake -E cmake_link_script CMakeFiles/cmTC_f1fdb.dir/link.txt --verbose=1
       /usr/bin/cc      -rdynamic CMakeFiles/cmTC_f1fdb.dir/feature_tests.c.o  -o cmTC_f1fdb 
       make[1]: Leaving directory '/warp-ctc/build/CMakeFiles/CMakeTmp'


           Feature record: C_FEATURE:1c_function_prototypes
           Feature record: C_FEATURE:1c_restrict
           Feature record: C_FEATURE:0c_static_assert
           Feature record: C_FEATURE:1c_variadic_macros


       Detecting C [-std=c90] compiler features compiled with the following output:
       Change Dir: /warp-ctc/build/CMakeFiles/CMakeTmp

       Run Build Command(s):/usr/bin/make cmTC_fc75e/fast 
       /usr/bin/make -f CMakeFiles/cmTC_fc75e.dir/build.make CMakeFiles/cmTC_fc75e.dir/build
       make[1]: Entering directory '/warp-ctc/build/CMakeFiles/CMakeTmp'
       Building C object CMakeFiles/cmTC_fc75e.dir/feature_tests.c.o
       /usr/bin/cc   -std=c90 -o CMakeFiles/cmTC_fc75e.dir/feature_tests.c.o   -c /warp-ctc/build/CMakeFiles/feature_tests.c
       Linking C executable cmTC_fc75e
       /opt/conda/envs/danspeech/bin/cmake -E cmake_link_script CMakeFiles/cmTC_fc75e.dir/link.txt --verbose=1
       /usr/bin/cc      -rdynamic CMakeFiles/cmTC_fc75e.dir/feature_tests.c.o  -o cmTC_fc75e 
       make[1]: Leaving directory '/warp-ctc/build/CMakeFiles/CMakeTmp'


           Feature record: C_FEATURE:1c_function_prototypes
           Feature record: C_FEATURE:0c_restrict
           Feature record: C_FEATURE:0c_static_assert
           Feature record: C_FEATURE:0c_variadic_macros
       Determining if the CXX compiler works passed with the following output:
       Change Dir: /warp-ctc/build/CMakeFiles/CMakeTmp

       Run Build Command(s):/usr/bin/make cmTC_98b69/fast 
       /usr/bin/make -f CMakeFiles/cmTC_98b69.dir/build.make CMakeFiles/cmTC_98b69.dir/build
       make[1]: Entering directory '/warp-ctc/build/CMakeFiles/CMakeTmp'
       Building CXX object CMakeFiles/cmTC_98b69.dir/testCXXCompiler.cxx.o
       /usr/bin/c++     -o CMakeFiles/cmTC_98b69.dir/testCXXCompiler.cxx.o -c /warp-ctc/build/CMakeFiles/CMakeTmp/testCXXCompiler.cxx
       Linking CXX executable cmTC_98b69
       /opt/conda/envs/danspeech/bin/cmake -E cmake_link_script CMakeFiles/cmTC_98b69.dir/link.txt --verbose=1
       /usr/bin/c++       -rdynamic CMakeFiles/cmTC_98b69.dir/testCXXCompiler.cxx.o  -o cmTC_98b69 
       make[1]: Leaving directory '/warp-ctc/build/CMakeFiles/CMakeTmp'


       Detecting CXX compiler ABI info compiled with the following output:
       Change Dir: /warp-ctc/build/CMakeFiles/CMakeTmp

       Run Build Command(s):/usr/bin/make cmTC_9fd31/fast 
       /usr/bin/make -f CMakeFiles/cmTC_9fd31.dir/build.make CMakeFiles/cmTC_9fd31.dir/build
       make[1]: Entering directory '/warp-ctc/build/CMakeFiles/CMakeTmp'
       Building CXX object CMakeFiles/cmTC_9fd31.dir/CMakeCXXCompilerABI.cpp.o
       /usr/bin/c++    -v -o CMakeFiles/cmTC_9fd31.dir/CMakeCXXCompilerABI.cpp.o -c /opt/conda/envs/danspeech/share/cmake-3.14/Modules/CMakeCXXCompilerABI.cpp
       Using built-in specs.
       COLLECT_GCC=/usr/bin/c++
       OFFLOAD_TARGET_NAMES=nvptx-none
       OFFLOAD_TARGET_DEFAULT=1
       Target: x86_64-linux-gnu
       Configured with: ../src/configure -v --with-pkgversion='Ubuntu 7.4.0-1ubuntu1~18.04.1' --with-bugurl=file:///usr/share/doc/gcc-7/README.Bugs --enable-languages=c,ada,c++,go,brig,d,fortran,objc,obj-c++ --prefix=/usr --with-gcc-major-version-only --program-suffix=-7 --program-prefix=x86_64-linux-gnu- --enable-shared --enable-linker-build-id --libexecdir=/usr/lib --without-included-gettext --enable-threads=posix --libdir=/usr/lib --enable-nls --with-sysroot=/ --enable-clocale=gnu --enable-libstdcxx-debug --enable-libstdcxx-time=yes --with-default-libstdcxx-abi=new --enable-gnu-unique-object --disable-vtable-verify --enable-libmpx --enable-plugin --enable-default-pie --with-system-zlib --with-target-system-zlib --enable-objc-gc=auto --enable-multiarch --disable-werror --with-arch-32=i686 --with-abi=m64 --with-multilib-list=m32,m64,mx32 --enable-multilib --with-tune=generic --enable-offload-targets=nvptx-none --without-cuda-driver --enable-checking=release --build=x86_64-linux-gnu --host=x86_64-linux-gnu --target=x86_64-linux-gnu
       Thread model: posix
       gcc version 7.4.0 (Ubuntu 7.4.0-1ubuntu1~18.04.1) 
       COLLECT_GCC_OPTIONS='-v' '-o' 'CMakeFiles/cmTC_9fd31.dir/CMakeCXXCompilerABI.cpp.o' '-c' '-shared-libgcc' '-mtune=generic' '-march=x86-64'
        /usr/lib/gcc/x86_64-linux-gnu/7/cc1plus -quiet -v -imultiarch x86_64-linux-gnu -D_GNU_SOURCE /opt/conda/envs/danspeech/share/cmake-3.14/Modules/CMakeCXXCompilerABI.cpp -quiet -dumpbase CMakeCXXCompilerABI.cpp -mtune=generic -march=x86-64 -auxbase-strip CMakeFiles/cmTC_9fd31.dir/CMakeCXXCompilerABI.cpp.o -version -fstack-protector-strong -Wformat -Wformat-security -o /tmp/ccZGYNZB.s
       GNU C++14 (Ubuntu 7.4.0-1ubuntu1~18.04.1) version 7.4.0 (x86_64-linux-gnu)
               compiled by GNU C version 7.4.0, GMP version 6.1.2, MPFR version 4.0.1, MPC version 1.1.0, isl version isl-0.19-GMP

       GGC heuristics: --param ggc-min-expand=100 --param ggc-min-heapsize=131072
       ignoring duplicate directory "/usr/include/x86_64-linux-gnu/c++/7"
       ignoring nonexistent directory "/usr/local/include/x86_64-linux-gnu"
       ignoring nonexistent directory "/usr/lib/gcc/x86_64-linux-gnu/7/../../../../x86_64-linux-gnu/include"
       #include "..." search starts here:
       #include <...> search starts here:
        /usr/include/c++/7
        /usr/include/x86_64-linux-gnu/c++/7
        /usr/include/c++/7/backward
        /usr/lib/gcc/x86_64-linux-gnu/7/include
        /usr/local/include
        /usr/lib/gcc/x86_64-linux-gnu/7/include-fixed
        /usr/include/x86_64-linux-gnu
        /usr/include
       End of search list.
       GNU C++14 (Ubuntu 7.4.0-1ubuntu1~18.04.1) version 7.4.0 (x86_64-linux-gnu)
               compiled by GNU C version 7.4.0, GMP version 6.1.2, MPFR version 4.0.1, MPC version 1.1.0, isl version isl-0.19-GMP

       GGC heuristics: --param ggc-min-expand=100 --param ggc-min-heapsize=131072
       Compiler executable checksum: 38816e3807cdcb3c59571e251bd6c090
       COLLECT_GCC_OPTIONS='-v' '-o' 'CMakeFiles/cmTC_9fd31.dir/CMakeCXXCompilerABI.cpp.o' '-c' '-shared-libgcc' '-mtune=generic' '-march=x86-64'
        as -v --64 -o CMakeFiles/cmTC_9fd31.dir/CMakeCXXCompilerABI.cpp.o /tmp/ccZGYNZB.s
       GNU assembler version 2.30 (x86_64-linux-gnu) using BFD version (GNU Binutils for Ubuntu) 2.30
       COMPILER_PATH=/usr/lib/gcc/x86_64-linux-gnu/7/:/usr/lib/gcc/x86_64-linux-gnu/7/:/usr/lib/gcc/x86_64-linux-gnu/:/usr/lib/gcc/x86_64-linux-gnu/7/:/usr/lib/gcc/x86_64-linux-gnu/
       LIBRARY_PATH=/usr/lib/gcc/x86_64-linux-gnu/7/:/usr/lib/gcc/x86_64-linux-gnu/7/../../../x86_64-linux-gnu/:/usr/lib/gcc/x86_64-linux-gnu/7/../../../../lib/:/lib/x86_64-linux-gnu/:/lib/../lib/:/usr/lib/x86_64-linux-gnu/:/usr/lib/../lib/:/usr/local/cuda/lib64/stubs/:/usr/lib/gcc/x86_64-linux-gnu/7/../../../:/lib/:/usr/lib/
       COLLECT_GCC_OPTIONS='-v' '-o' 'CMakeFiles/cmTC_9fd31.dir/CMakeCXXCompilerABI.cpp.o' '-c' '-shared-libgcc' '-mtune=generic' '-march=x86-64'
       Linking CXX executable cmTC_9fd31
       /opt/conda/envs/danspeech/bin/cmake -E cmake_link_script CMakeFiles/cmTC_9fd31.dir/link.txt --verbose=1
       /usr/bin/c++      -v -rdynamic CMakeFiles/cmTC_9fd31.dir/CMakeCXXCompilerABI.cpp.o  -o cmTC_9fd31 
       Using built-in specs.
       COLLECT_GCC=/usr/bin/c++
       COLLECT_LTO_WRAPPER=/usr/lib/gcc/x86_64-linux-gnu/7/lto-wrapper
       OFFLOAD_TARGET_NAMES=nvptx-none
       OFFLOAD_TARGET_DEFAULT=1
       Target: x86_64-linux-gnu
       Configured with: ../src/configure -v --with-pkgversion='Ubuntu 7.4.0-1ubuntu1~18.04.1' --with-bugurl=file:///usr/share/doc/gcc-7/README.Bugs --enable-languages=c,ada,c++,go,brig,d,fortran,objc,obj-c++ --prefix=/usr --with-gcc-major-version-only --program-suffix=-7 --program-prefix=x86_64-linux-gnu- --enable-shared --enable-linker-build-id --libexecdir=/usr/lib --without-included-gettext --enable-threads=posix --libdir=/usr/lib --enable-nls --with-sysroot=/ --enable-clocale=gnu --enable-libstdcxx-debug --enable-libstdcxx-time=yes --with-default-libstdcxx-abi=new --enable-gnu-unique-object --disable-vtable-verify --enable-libmpx --enable-plugin --enable-default-pie --with-system-zlib --with-target-system-zlib --enable-objc-gc=auto --enable-multiarch --disable-werror --with-arch-32=i686 --with-abi=m64 --with-multilib-list=m32,m64,mx32 --enable-multilib --with-tune=generic --enable-offload-targets=nvptx-none --without-cuda-driver --enable-checking=release --build=x86_64-linux-gnu --host=x86_64-linux-gnu --target=x86_64-linux-gnu
       Thread model: posix
       gcc version 7.4.0 (Ubuntu 7.4.0-1ubuntu1~18.04.1) 
       COMPILER_PATH=/usr/lib/gcc/x86_64-linux-gnu/7/:/usr/lib/gcc/x86_64-linux-gnu/7/:/usr/lib/gcc/x86_64-linux-gnu/:/usr/lib/gcc/x86_64-linux-gnu/7/:/usr/lib/gcc/x86_64-linux-gnu/
       LIBRARY_PATH=/usr/lib/gcc/x86_64-linux-gnu/7/:/usr/lib/gcc/x86_64-linux-gnu/7/../../../x86_64-linux-gnu/:/usr/lib/gcc/x86_64-linux-gnu/7/../../../../lib/:/lib/x86_64-linux-gnu/:/lib/../lib/:/usr/lib/x86_64-linux-gnu/:/usr/lib/../lib/:/usr/local/cuda/lib64/stubs/:/usr/lib/gcc/x86_64-linux-gnu/7/../../../:/lib/:/usr/lib/
       COLLECT_GCC_OPTIONS='-v' '-rdynamic' '-o' 'cmTC_9fd31' '-shared-libgcc' '-mtune=generic' '-march=x86-64'
        /usr/lib/gcc/x86_64-linux-gnu/7/collect2 -plugin /usr/lib/gcc/x86_64-linux-gnu/7/liblto_plugin.so -plugin-opt=/usr/lib/gcc/x86_64-linux-gnu/7/lto-wrapper -plugin-opt=-fresolution=/tmp/ccdLBfXI.res -plugin-opt=-pass-through=-lgcc_s -plugin-opt=-pass-through=-lgcc -plugin-opt=-pass-through=-lc -plugin-opt=-pass-through=-lgcc_s -plugin-opt=-pass-through=-lgcc --sysroot=/ --build-id --eh-frame-hdr -m elf_x86_64 --hash-style=gnu --as-needed -export-dynamic -dynamic-linker /lib64/ld-linux-x86-64.so.2 -pie -z now -z relro -o cmTC_9fd31 /usr/lib/gcc/x86_64-linux-gnu/7/../../../x86_64-linux-gnu/Scrt1.o /usr/lib/gcc/x86_64-linux-gnu/7/../../../x86_64-linux-gnu/crti.o /usr/lib/gcc/x86_64-linux-gnu/7/crtbeginS.o -L/usr/lib/gcc/x86_64-linux-gnu/7 -L/usr/lib/gcc/x86_64-linux-gnu/7/../../../x86_64-linux-gnu -L/usr/lib/gcc/x86_64-linux-gnu/7/../../../../lib -L/lib/x86_64-linux-gnu -L/lib/../lib -L/usr/lib/x86_64-linux-gnu -L/usr/lib/../lib -L/usr/local/cuda/lib64/stubs -L/usr/lib/gcc/x86_64-linux-gnu/7/../../.. CMakeFiles/cmTC_9fd31.dir/CMakeCXXCompilerABI.cpp.o -lstdc++ -lm -lgcc_s -lgcc -lc -lgcc_s -lgcc /usr/lib/gcc/x86_64-linux-gnu/7/crtendS.o /usr/lib/gcc/x86_64-linux-gnu/7/../../../x86_64-linux-gnu/crtn.o
       COLLECT_GCC_OPTIONS='-v' '-rdynamic' '-o' 'cmTC_9fd31' '-shared-libgcc' '-mtune=generic' '-march=x86-64'
       make[1]: Leaving directory '/warp-ctc/build/CMakeFiles/CMakeTmp'


       Parsed CXX implicit include dir info from above output: rv=done
         found start of include info
         found start of implicit include info
           add: [/usr/include/c++/7]
           add: [/usr/include/x86_64-linux-gnu/c++/7]
           add: [/usr/include/c++/7/backward]
           add: [/usr/lib/gcc/x86_64-linux-gnu/7/include]
           add: [/usr/local/include]
           add: [/usr/lib/gcc/x86_64-linux-gnu/7/include-fixed]
           add: [/usr/include/x86_64-linux-gnu]
           add: [/usr/include]
         end of search list found
         implicit include dirs: [/usr/include/c++/7;/usr/include/x86_64-linux-gnu/c++/7;/usr/include/c++/7/backward;/usr/lib/gcc/x86_64-linux-gnu/7/include;/usr/local/include;/usr/lib/gcc/x86_64-linux-gnu/7/include-fixed;/usr/include/x86_64-linux-gnu;/usr/include]


       Parsed CXX implicit link information from above output:
         link line regex: [^( *|.*[/\])(ld|CMAKE_LINK_STARTFILE-NOTFOUND|([^/\]+-)?ld|collect2)[^/\]*( |$)]
         ignore line: [Change Dir: /warp-ctc/build/CMakeFiles/CMakeTmp]
         ignore line: []
         ignore line: [Run Build Command(s):/usr/bin/make cmTC_9fd31/fast ]
         ignore line: [/usr/bin/make -f CMakeFiles/cmTC_9fd31.dir/build.make CMakeFiles/cmTC_9fd31.dir/build]
         ignore line: [make[1]: Entering directory '/warp-ctc/build/CMakeFiles/CMakeTmp']
         ignore line: [Building CXX object CMakeFiles/cmTC_9fd31.dir/CMakeCXXCompilerABI.cpp.o]
         ignore line: [/usr/bin/c++    -v -o CMakeFiles/cmTC_9fd31.dir/CMakeCXXCompilerABI.cpp.o -c /opt/conda/envs/danspeech/share/cmake-3.14/Modules/CMakeCXXCompilerABI.cpp]
         ignore line: [Using built-in specs.]
         ignore line: [COLLECT_GCC=/usr/bin/c++]
         ignore line: [OFFLOAD_TARGET_NAMES=nvptx-none]
         ignore line: [OFFLOAD_TARGET_DEFAULT=1]
         ignore line: [Target: x86_64-linux-gnu]
         ignore line: [Configured with: ../src/configure -v --with-pkgversion='Ubuntu 7.4.0-1ubuntu1~18.04.1' --with-bugurl=file:///usr/share/doc/gcc-7/README.Bugs --enable-languages=c,ada,c++,go,brig,d,fortran,objc,obj-c++ --prefix=/usr --with-gcc-major-version-only --program-suffix=-7 --program-prefix=x86_64-linux-gnu- --enable-shared --enable-linker-build-id --libexecdir=/usr/lib --without-included-gettext --enable-threads=posix --libdir=/usr/lib --enable-nls --with-sysroot=/ --enable-clocale=gnu --enable-libstdcxx-debug --enable-libstdcxx-time=yes --with-default-libstdcxx-abi=new --enable-gnu-unique-object --disable-vtable-verify --enable-libmpx --enable-plugin --enable-default-pie --with-system-zlib --with-target-system-zlib --enable-objc-gc=auto --enable-multiarch --disable-werror --with-arch-32=i686 --with-abi=m64 --with-multilib-list=m32,m64,mx32 --enable-multilib --with-tune=generic --enable-offload-targets=nvptx-none --without-cuda-driver --enable-checking=release --build=x86_64-linux-gnu --host=x86_64-linux-gnu --target=x86_64-linux-gnu]
         ignore line: [Thread model: posix]
         ignore line: [gcc version 7.4.0 (Ubuntu 7.4.0-1ubuntu1~18.04.1) ]
         ignore line: [COLLECT_GCC_OPTIONS='-v' '-o' 'CMakeFiles/cmTC_9fd31.dir/CMakeCXXCompilerABI.cpp.o' '-c' '-shared-libgcc' '-mtune=generic' '-march=x86-64']
         ignore line: [ /usr/lib/gcc/x86_64-linux-gnu/7/cc1plus -quiet -v -imultiarch x86_64-linux-gnu -D_GNU_SOURCE /opt/conda/envs/danspeech/share/cmake-3.14/Modules/CMakeCXXCompilerABI.cpp -quiet -dumpbase CMakeCXXCompilerABI.cpp -mtune=generic -march=x86-64 -auxbase-strip CMakeFiles/cmTC_9fd31.dir/CMakeCXXCompilerABI.cpp.o -version -fstack-protector-strong -Wformat -Wformat-security -o /tmp/ccZGYNZB.s]
         ignore line: [GNU C++14 (Ubuntu 7.4.0-1ubuntu1~18.04.1) version 7.4.0 (x86_64-linux-gnu)]
         ignore line: [ compiled by GNU C version 7.4.0, GMP version 6.1.2, MPFR version 4.0.1, MPC version 1.1.0, isl version isl-0.19-GMP]
         ignore line: []
         ignore line: [GGC heuristics: --param ggc-min-expand=100 --param ggc-min-heapsize=131072]
         ignore line: [ignoring duplicate directory "/usr/include/x86_64-linux-gnu/c++/7"]
         ignore line: [ignoring nonexistent directory "/usr/local/include/x86_64-linux-gnu"]
         ignore line: [ignoring nonexistent directory "/usr/lib/gcc/x86_64-linux-gnu/7/../../../../x86_64-linux-gnu/include"]
         ignore line: [#include "..." search starts here:]
         ignore line: [#include <...> search starts here:]
         ignore line: [ /usr/include/c++/7]
         ignore line: [ /usr/include/x86_64-linux-gnu/c++/7]
         ignore line: [ /usr/include/c++/7/backward]
         ignore line: [ /usr/lib/gcc/x86_64-linux-gnu/7/include]
         ignore line: [ /usr/local/include]
         ignore line: [ /usr/lib/gcc/x86_64-linux-gnu/7/include-fixed]
         ignore line: [ /usr/include/x86_64-linux-gnu]
         ignore line: [ /usr/include]
         ignore line: [End of search list.]
         ignore line: [GNU C++14 (Ubuntu 7.4.0-1ubuntu1~18.04.1) version 7.4.0 (x86_64-linux-gnu)]
         ignore line: [ compiled by GNU C version 7.4.0, GMP version 6.1.2, MPFR version 4.0.1, MPC version 1.1.0, isl version isl-0.19-GMP]
         ignore line: []
         ignore line: [GGC heuristics: --param ggc-min-expand=100 --param ggc-min-heapsize=131072]
         ignore line: [Compiler executable checksum: 38816e3807cdcb3c59571e251bd6c090]
         ignore line: [COLLECT_GCC_OPTIONS='-v' '-o' 'CMakeFiles/cmTC_9fd31.dir/CMakeCXXCompilerABI.cpp.o' '-c' '-shared-libgcc' '-mtune=generic' '-march=x86-64']
         ignore line: [ as -v --64 -o CMakeFiles/cmTC_9fd31.dir/CMakeCXXCompilerABI.cpp.o /tmp/ccZGYNZB.s]
         ignore line: [GNU assembler version 2.30 (x86_64-linux-gnu) using BFD version (GNU Binutils for Ubuntu) 2.30]
         ignore line: [COMPILER_PATH=/usr/lib/gcc/x86_64-linux-gnu/7/:/usr/lib/gcc/x86_64-linux-gnu/7/:/usr/lib/gcc/x86_64-linux-gnu/:/usr/lib/gcc/x86_64-linux-gnu/7/:/usr/lib/gcc/x86_64-linux-gnu/]
         ignore line: [LIBRARY_PATH=/usr/lib/gcc/x86_64-linux-gnu/7/:/usr/lib/gcc/x86_64-linux-gnu/7/../../../x86_64-linux-gnu/:/usr/lib/gcc/x86_64-linux-gnu/7/../../../../lib/:/lib/x86_64-linux-gnu/:/lib/../lib/:/usr/lib/x86_64-linux-gnu/:/usr/lib/../lib/:/usr/local/cuda/lib64/stubs/:/usr/lib/gcc/x86_64-linux-gnu/7/../../../:/lib/:/usr/lib/]
         ignore line: [COLLECT_GCC_OPTIONS='-v' '-o' 'CMakeFiles/cmTC_9fd31.dir/CMakeCXXCompilerABI.cpp.o' '-c' '-shared-libgcc' '-mtune=generic' '-march=x86-64']
         ignore line: [Linking CXX executable cmTC_9fd31]
         ignore line: [/opt/conda/envs/danspeech/bin/cmake -E cmake_link_script CMakeFiles/cmTC_9fd31.dir/link.txt --verbose=1]
         ignore line: [/usr/bin/c++      -v -rdynamic CMakeFiles/cmTC_9fd31.dir/CMakeCXXCompilerABI.cpp.o  -o cmTC_9fd31 ]
         ignore line: [Using built-in specs.]
         ignore line: [COLLECT_GCC=/usr/bin/c++]
         ignore line: [COLLECT_LTO_WRAPPER=/usr/lib/gcc/x86_64-linux-gnu/7/lto-wrapper]
         ignore line: [OFFLOAD_TARGET_NAMES=nvptx-none]
         ignore line: [OFFLOAD_TARGET_DEFAULT=1]
         ignore line: [Target: x86_64-linux-gnu]
         ignore line: [Configured with: ../src/configure -v --with-pkgversion='Ubuntu 7.4.0-1ubuntu1~18.04.1' --with-bugurl=file:///usr/share/doc/gcc-7/README.Bugs --enable-languages=c,ada,c++,go,brig,d,fortran,objc,obj-c++ --prefix=/usr --with-gcc-major-version-only --program-suffix=-7 --program-prefix=x86_64-linux-gnu- --enable-shared --enable-linker-build-id --libexecdir=/usr/lib --without-included-gettext --enable-threads=posix --libdir=/usr/lib --enable-nls --with-sysroot=/ --enable-clocale=gnu --enable-libstdcxx-debug --enable-libstdcxx-time=yes --with-default-libstdcxx-abi=new --enable-gnu-unique-object --disable-vtable-verify --enable-libmpx --enable-plugin --enable-default-pie --with-system-zlib --with-target-system-zlib --enable-objc-gc=auto --enable-multiarch --disable-werror --with-arch-32=i686 --with-abi=m64 --with-multilib-list=m32,m64,mx32 --enable-multilib --with-tune=generic --enable-offload-targets=nvptx-none --without-cuda-driver --enable-checking=release --build=x86_64-linux-gnu --host=x86_64-linux-gnu --target=x86_64-linux-gnu]
         ignore line: [Thread model: posix]
         ignore line: [gcc version 7.4.0 (Ubuntu 7.4.0-1ubuntu1~18.04.1) ]
         ignore line: [COMPILER_PATH=/usr/lib/gcc/x86_64-linux-gnu/7/:/usr/lib/gcc/x86_64-linux-gnu/7/:/usr/lib/gcc/x86_64-linux-gnu/:/usr/lib/gcc/x86_64-linux-gnu/7/:/usr/lib/gcc/x86_64-linux-gnu/]
         ignore line: [LIBRARY_PATH=/usr/lib/gcc/x86_64-linux-gnu/7/:/usr/lib/gcc/x86_64-linux-gnu/7/../../../x86_64-linux-gnu/:/usr/lib/gcc/x86_64-linux-gnu/7/../../../../lib/:/lib/x86_64-linux-gnu/:/lib/../lib/:/usr/lib/x86_64-linux-gnu/:/usr/lib/../lib/:/usr/local/cuda/lib64/stubs/:/usr/lib/gcc/x86_64-linux-gnu/7/../../../:/lib/:/usr/lib/]
         ignore line: [COLLECT_GCC_OPTIONS='-v' '-rdynamic' '-o' 'cmTC_9fd31' '-shared-libgcc' '-mtune=generic' '-march=x86-64']
         link line: [ /usr/lib/gcc/x86_64-linux-gnu/7/collect2 -plugin /usr/lib/gcc/x86_64-linux-gnu/7/liblto_plugin.so -plugin-opt=/usr/lib/gcc/x86_64-linux-gnu/7/lto-wrapper -plugin-opt=-fresolution=/tmp/ccdLBfXI.res -plugin-opt=-pass-through=-lgcc_s -plugin-opt=-pass-through=-lgcc -plugin-opt=-pass-through=-lc -plugin-opt=-pass-through=-lgcc_s -plugin-opt=-pass-through=-lgcc --sysroot=/ --build-id --eh-frame-hdr -m elf_x86_64 --hash-style=gnu --as-needed -export-dynamic -dynamic-linker /lib64/ld-linux-x86-64.so.2 -pie -z now -z relro -o cmTC_9fd31 /usr/lib/gcc/x86_64-linux-gnu/7/../../../x86_64-linux-gnu/Scrt1.o /usr/lib/gcc/x86_64-linux-gnu/7/../../../x86_64-linux-gnu/crti.o /usr/lib/gcc/x86_64-linux-gnu/7/crtbeginS.o -L/usr/lib/gcc/x86_64-linux-gnu/7 -L/usr/lib/gcc/x86_64-linux-gnu/7/../../../x86_64-linux-gnu -L/usr/lib/gcc/x86_64-linux-gnu/7/../../../../lib -L/lib/x86_64-linux-gnu -L/lib/../lib -L/usr/lib/x86_64-linux-gnu -L/usr/lib/../lib -L/usr/local/cuda/lib64/stubs -L/usr/lib/gcc/x86_64-linux-gnu/7/../../.. CMakeFiles/cmTC_9fd31.dir/CMakeCXXCompilerABI.cpp.o -lstdc++ -lm -lgcc_s -lgcc -lc -lgcc_s -lgcc /usr/lib/gcc/x86_64-linux-gnu/7/crtendS.o /usr/lib/gcc/x86_64-linux-gnu/7/../../../x86_64-linux-gnu/crtn.o]
           arg [/usr/lib/gcc/x86_64-linux-gnu/7/collect2] ==> ignore
           arg [-plugin] ==> ignore
           arg [/usr/lib/gcc/x86_64-linux-gnu/7/liblto_plugin.so] ==> ignore
           arg [-plugin-opt=/usr/lib/gcc/x86_64-linux-gnu/7/lto-wrapper] ==> ignore
           arg [-plugin-opt=-fresolution=/tmp/ccdLBfXI.res] ==> ignore
           arg [-plugin-opt=-pass-through=-lgcc_s] ==> ignore
           arg [-plugin-opt=-pass-through=-lgcc] ==> ignore
           arg [-plugin-opt=-pass-through=-lc] ==> ignore
           arg [-plugin-opt=-pass-through=-lgcc_s] ==> ignore
           arg [-plugin-opt=-pass-through=-lgcc] ==> ignore
           arg [--sysroot=/] ==> ignore
           arg [--build-id] ==> ignore
           arg [--eh-frame-hdr] ==> ignore
           arg [-m] ==> ignore
           arg [elf_x86_64] ==> ignore
           arg [--hash-style=gnu] ==> ignore
           arg [--as-needed] ==> ignore
           arg [-export-dynamic] ==> ignore
           arg [-dynamic-linker] ==> ignore
           arg [/lib64/ld-linux-x86-64.so.2] ==> ignore
           arg [-pie] ==> ignore
           arg [-znow] ==> ignore
           arg [-zrelro] ==> ignore
           arg [-o] ==> ignore
           arg [cmTC_9fd31] ==> ignore
           arg [/usr/lib/gcc/x86_64-linux-gnu/7/../../../x86_64-linux-gnu/Scrt1.o] ==> ignore
           arg [/usr/lib/gcc/x86_64-linux-gnu/7/../../../x86_64-linux-gnu/crti.o] ==> ignore
           arg [/usr/lib/gcc/x86_64-linux-gnu/7/crtbeginS.o] ==> ignore
           arg [-L/usr/lib/gcc/x86_64-linux-gnu/7] ==> dir [/usr/lib/gcc/x86_64-linux-gnu/7]
           arg [-L/usr/lib/gcc/x86_64-linux-gnu/7/../../../x86_64-linux-gnu] ==> dir [/usr/lib/gcc/x86_64-linux-gnu/7/../../../x86_64-linux-gnu]
           arg [-L/usr/lib/gcc/x86_64-linux-gnu/7/../../../../lib] ==> dir [/usr/lib/gcc/x86_64-linux-gnu/7/../../../../lib]
           arg [-L/lib/x86_64-linux-gnu] ==> dir [/lib/x86_64-linux-gnu]
           arg [-L/lib/../lib] ==> dir [/lib/../lib]
           arg [-L/usr/lib/x86_64-linux-gnu] ==> dir [/usr/lib/x86_64-linux-gnu]
           arg [-L/usr/lib/../lib] ==> dir [/usr/lib/../lib]
           arg [-L/usr/local/cuda/lib64/stubs] ==> dir [/usr/local/cuda/lib64/stubs]
           arg [-L/usr/lib/gcc/x86_64-linux-gnu/7/../../..] ==> dir [/usr/lib/gcc/x86_64-linux-gnu/7/../../..]
           arg [CMakeFiles/cmTC_9fd31.dir/CMakeCXXCompilerABI.cpp.o] ==> ignore
           arg [-lstdc++] ==> lib [stdc++]
           arg [-lm] ==> lib [m]
           arg [-lgcc_s] ==> lib [gcc_s]
           arg [-lgcc] ==> lib [gcc]
           arg [-lc] ==> lib [c]
           arg [-lgcc_s] ==> lib [gcc_s]
           arg [-lgcc] ==> lib [gcc]
           arg [/usr/lib/gcc/x86_64-linux-gnu/7/crtendS.o] ==> ignore
           arg [/usr/lib/gcc/x86_64-linux-gnu/7/../../../x86_64-linux-gnu/crtn.o] ==> ignore
         collapse library dir [/usr/lib/gcc/x86_64-linux-gnu/7] ==> [/usr/lib/gcc/x86_64-linux-gnu/7]
         collapse library dir [/usr/lib/gcc/x86_64-linux-gnu/7/../../../x86_64-linux-gnu] ==> [/usr/lib/x86_64-linux-gnu]
         collapse library dir [/usr/lib/gcc/x86_64-linux-gnu/7/../../../../lib] ==> [/usr/lib]
         collapse library dir [/lib/x86_64-linux-gnu] ==> [/lib/x86_64-linux-gnu]
         collapse library dir [/lib/../lib] ==> [/lib]
         collapse library dir [/usr/lib/x86_64-linux-gnu] ==> [/usr/lib/x86_64-linux-gnu]
         collapse library dir [/usr/lib/../lib] ==> [/usr/lib]
         collapse library dir [/usr/local/cuda/lib64/stubs] ==> [/usr/local/cuda/lib64/stubs]
         collapse library dir [/usr/lib/gcc/x86_64-linux-gnu/7/../../..] ==> [/usr/lib]
         implicit libs: [stdc++;m;gcc_s;gcc;c;gcc_s;gcc]
         implicit dirs: [/usr/lib/gcc/x86_64-linux-gnu/7;/usr/lib/x86_64-linux-gnu;/usr/lib;/lib/x86_64-linux-gnu;/lib;/usr/local/cuda/lib64/stubs]
         implicit fwks: []




       Detecting CXX [-std=c++1z] compiler features compiled with the following output:
       Change Dir: /warp-ctc/build/CMakeFiles/CMakeTmp

       Run Build Command(s):/usr/bin/make cmTC_3e8c6/fast 
       /usr/bin/make -f CMakeFiles/cmTC_3e8c6.dir/build.make CMakeFiles/cmTC_3e8c6.dir/build
       make[1]: Entering directory '/warp-ctc/build/CMakeFiles/CMakeTmp'
       Building CXX object CMakeFiles/cmTC_3e8c6.dir/feature_tests.cxx.o
       /usr/bin/c++    -std=c++1z -o CMakeFiles/cmTC_3e8c6.dir/feature_tests.cxx.o -c /warp-ctc/build/CMakeFiles/feature_tests.cxx
       Linking CXX executable cmTC_3e8c6
       /opt/conda/envs/danspeech/bin/cmake -E cmake_link_script CMakeFiles/cmTC_3e8c6.dir/link.txt --verbose=1
       /usr/bin/c++       -rdynamic CMakeFiles/cmTC_3e8c6.dir/feature_tests.cxx.o  -o cmTC_3e8c6 
       make[1]: Leaving directory '/warp-ctc/build/CMakeFiles/CMakeTmp'


           Feature record: CXX_FEATURE:1cxx_aggregate_default_initializers
           Feature record: CXX_FEATURE:1cxx_alias_templates
           Feature record: CXX_FEATURE:1cxx_alignas
           Feature record: CXX_FEATURE:1cxx_alignof
           Feature record: CXX_FEATURE:1cxx_attributes
           Feature record: CXX_FEATURE:1cxx_attribute_deprecated
           Feature record: CXX_FEATURE:1cxx_auto_type
           Feature record: CXX_FEATURE:1cxx_binary_literals
           Feature record: CXX_FEATURE:1cxx_constexpr
           Feature record: CXX_FEATURE:1cxx_contextual_conversions
           Feature record: CXX_FEATURE:1cxx_decltype
           Feature record: CXX_FEATURE:1cxx_decltype_auto
           Feature record: CXX_FEATURE:1cxx_decltype_incomplete_return_types
           Feature record: CXX_FEATURE:1cxx_default_function_template_args
           Feature record: CXX_FEATURE:1cxx_defaulted_functions
           Feature record: CXX_FEATURE:1cxx_defaulted_move_initializers
           Feature record: CXX_FEATURE:1cxx_delegating_constructors
           Feature record: CXX_FEATURE:1cxx_deleted_functions
           Feature record: CXX_FEATURE:1cxx_digit_separators
           Feature record: CXX_FEATURE:1cxx_enum_forward_declarations
           Feature record: CXX_FEATURE:1cxx_explicit_conversions
           Feature record: CXX_FEATURE:1cxx_extended_friend_declarations
           Feature record: CXX_FEATURE:1cxx_extern_templates
           Feature record: CXX_FEATURE:1cxx_final
           Feature record: CXX_FEATURE:1cxx_func_identifier
           Feature record: CXX_FEATURE:1cxx_generalized_initializers
           Feature record: CXX_FEATURE:1cxx_generic_lambdas
           Feature record: CXX_FEATURE:1cxx_inheriting_constructors
           Feature record: CXX_FEATURE:1cxx_inline_namespaces
           Feature record: CXX_FEATURE:1cxx_lambdas
           Feature record: CXX_FEATURE:1cxx_lambda_init_captures
           Feature record: CXX_FEATURE:1cxx_local_type_template_args
           Feature record: CXX_FEATURE:1cxx_long_long_type
           Feature record: CXX_FEATURE:1cxx_noexcept
           Feature record: CXX_FEATURE:1cxx_nonstatic_member_init
           Feature record: CXX_FEATURE:1cxx_nullptr
           Feature record: CXX_FEATURE:1cxx_override
           Feature record: CXX_FEATURE:1cxx_range_for
           Feature record: CXX_FEATURE:1cxx_raw_string_literals
           Feature record: CXX_FEATURE:1cxx_reference_qualified_functions
           Feature record: CXX_FEATURE:1cxx_relaxed_constexpr
           Feature record: CXX_FEATURE:1cxx_return_type_deduction
           Feature record: CXX_FEATURE:1cxx_right_angle_brackets
           Feature record: CXX_FEATURE:1cxx_rvalue_references
           Feature record: CXX_FEATURE:1cxx_sizeof_member
           Feature record: CXX_FEATURE:1cxx_static_assert
           Feature record: CXX_FEATURE:1cxx_strong_enums
           Feature record: CXX_FEATURE:1cxx_template_template_parameters
           Feature record: CXX_FEATURE:1cxx_thread_local
           Feature record: CXX_FEATURE:1cxx_trailing_return_types
           Feature record: CXX_FEATURE:1cxx_unicode_literals
           Feature record: CXX_FEATURE:1cxx_uniform_initialization
           Feature record: CXX_FEATURE:1cxx_unrestricted_unions
           Feature record: CXX_FEATURE:1cxx_user_literals
           Feature record: CXX_FEATURE:1cxx_variable_templates
           Feature record: CXX_FEATURE:1cxx_variadic_macros
           Feature record: CXX_FEATURE:1cxx_variadic_templates


       Detecting CXX [-std=c++14] compiler features compiled with the following output:
       Change Dir: /warp-ctc/build/CMakeFiles/CMakeTmp

       Run Build Command(s):/usr/bin/make cmTC_648f0/fast 
       /usr/bin/make -f CMakeFiles/cmTC_648f0.dir/build.make CMakeFiles/cmTC_648f0.dir/build
       make[1]: Entering directory '/warp-ctc/build/CMakeFiles/CMakeTmp'
       Building CXX object CMakeFiles/cmTC_648f0.dir/feature_tests.cxx.o
       /usr/bin/c++    -std=c++14 -o CMakeFiles/cmTC_648f0.dir/feature_tests.cxx.o -c /warp-ctc/build/CMakeFiles/feature_tests.cxx
       Linking CXX executable cmTC_648f0
       /opt/conda/envs/danspeech/bin/cmake -E cmake_link_script CMakeFiles/cmTC_648f0.dir/link.txt --verbose=1
       /usr/bin/c++       -rdynamic CMakeFiles/cmTC_648f0.dir/feature_tests.cxx.o  -o cmTC_648f0 
       make[1]: Leaving directory '/warp-ctc/build/CMakeFiles/CMakeTmp'


           Feature record: CXX_FEATURE:1cxx_aggregate_default_initializers
           Feature record: CXX_FEATURE:1cxx_alias_templates
           Feature record: CXX_FEATURE:1cxx_alignas
           Feature record: CXX_FEATURE:1cxx_alignof
           Feature record: CXX_FEATURE:1cxx_attributes
           Feature record: CXX_FEATURE:1cxx_attribute_deprecated
           Feature record: CXX_FEATURE:1cxx_auto_type
           Feature record: CXX_FEATURE:1cxx_binary_literals
           Feature record: CXX_FEATURE:1cxx_constexpr
           Feature record: CXX_FEATURE:1cxx_contextual_conversions
           Feature record: CXX_FEATURE:1cxx_decltype
           Feature record: CXX_FEATURE:1cxx_decltype_auto
           Feature record: CXX_FEATURE:1cxx_decltype_incomplete_return_types
           Feature record: CXX_FEATURE:1cxx_default_function_template_args
           Feature record: CXX_FEATURE:1cxx_defaulted_functions
           Feature record: CXX_FEATURE:1cxx_defaulted_move_initializers
           Feature record: CXX_FEATURE:1cxx_delegating_constructors
           Feature record: CXX_FEATURE:1cxx_deleted_functions
           Feature record: CXX_FEATURE:1cxx_digit_separators
           Feature record: CXX_FEATURE:1cxx_enum_forward_declarations
           Feature record: CXX_FEATURE:1cxx_explicit_conversions
           Feature record: CXX_FEATURE:1cxx_extended_friend_declarations
           Feature record: CXX_FEATURE:1cxx_extern_templates
           Feature record: CXX_FEATURE:1cxx_final
           Feature record: CXX_FEATURE:1cxx_func_identifier
           Feature record: CXX_FEATURE:1cxx_generalized_initializers
           Feature record: CXX_FEATURE:1cxx_generic_lambdas
           Feature record: CXX_FEATURE:1cxx_inheriting_constructors
           Feature record: CXX_FEATURE:1cxx_inline_namespaces
           Feature record: CXX_FEATURE:1cxx_lambdas
           Feature record: CXX_FEATURE:1cxx_lambda_init_captures
           Feature record: CXX_FEATURE:1cxx_local_type_template_args
           Feature record: CXX_FEATURE:1cxx_long_long_type
           Feature record: CXX_FEATURE:1cxx_noexcept
           Feature record: CXX_FEATURE:1cxx_nonstatic_member_init
           Feature record: CXX_FEATURE:1cxx_nullptr
           Feature record: CXX_FEATURE:1cxx_override
           Feature record: CXX_FEATURE:1cxx_range_for
           Feature record: CXX_FEATURE:1cxx_raw_string_literals
           Feature record: CXX_FEATURE:1cxx_reference_qualified_functions
           Feature record: CXX_FEATURE:1cxx_relaxed_constexpr
           Feature record: CXX_FEATURE:1cxx_return_type_deduction
           Feature record: CXX_FEATURE:1cxx_right_angle_brackets
           Feature record: CXX_FEATURE:1cxx_rvalue_references
           Feature record: CXX_FEATURE:1cxx_sizeof_member
           Feature record: CXX_FEATURE:1cxx_static_assert
           Feature record: CXX_FEATURE:1cxx_strong_enums
           Feature record: CXX_FEATURE:1cxx_template_template_parameters
           Feature record: CXX_FEATURE:1cxx_thread_local
           Feature record: CXX_FEATURE:1cxx_trailing_return_types
           Feature record: CXX_FEATURE:1cxx_unicode_literals
           Feature record: CXX_FEATURE:1cxx_uniform_initialization
           Feature record: CXX_FEATURE:1cxx_unrestricted_unions
           Feature record: CXX_FEATURE:1cxx_user_literals
           Feature record: CXX_FEATURE:1cxx_variable_templates
           Feature record: CXX_FEATURE:1cxx_variadic_macros
           Feature record: CXX_FEATURE:1cxx_variadic_templates


       Detecting CXX [-std=c++11] compiler features compiled with the following output:
       Change Dir: /warp-ctc/build/CMakeFiles/CMakeTmp

       Run Build Command(s):/usr/bin/make cmTC_cfa98/fast 
       /usr/bin/make -f CMakeFiles/cmTC_cfa98.dir/build.make CMakeFiles/cmTC_cfa98.dir/build
       make[1]: Entering directory '/warp-ctc/build/CMakeFiles/CMakeTmp'
       Building CXX object CMakeFiles/cmTC_cfa98.dir/feature_tests.cxx.o
       /usr/bin/c++    -std=c++11 -o CMakeFiles/cmTC_cfa98.dir/feature_tests.cxx.o -c /warp-ctc/build/CMakeFiles/feature_tests.cxx
       Linking CXX executable cmTC_cfa98
       /opt/conda/envs/danspeech/bin/cmake -E cmake_link_script CMakeFiles/cmTC_cfa98.dir/link.txt --verbose=1
       /usr/bin/c++       -rdynamic CMakeFiles/cmTC_cfa98.dir/feature_tests.cxx.o  -o cmTC_cfa98 
       make[1]: Leaving directory '/warp-ctc/build/CMakeFiles/CMakeTmp'


           Feature record: CXX_FEATURE:0cxx_aggregate_default_initializers
           Feature record: CXX_FEATURE:1cxx_alias_templates
           Feature record: CXX_FEATURE:1cxx_alignas
           Feature record: CXX_FEATURE:1cxx_alignof
           Feature record: CXX_FEATURE:1cxx_attributes
           Feature record: CXX_FEATURE:0cxx_attribute_deprecated
           Feature record: CXX_FEATURE:1cxx_auto_type
           Feature record: CXX_FEATURE:0cxx_binary_literals
           Feature record: CXX_FEATURE:1cxx_constexpr
           Feature record: CXX_FEATURE:0cxx_contextual_conversions
           Feature record: CXX_FEATURE:1cxx_decltype
           Feature record: CXX_FEATURE:0cxx_decltype_auto
           Feature record: CXX_FEATURE:1cxx_decltype_incomplete_return_types
           Feature record: CXX_FEATURE:1cxx_default_function_template_args
           Feature record: CXX_FEATURE:1cxx_defaulted_functions
           Feature record: CXX_FEATURE:1cxx_defaulted_move_initializers
           Feature record: CXX_FEATURE:1cxx_delegating_constructors
           Feature record: CXX_FEATURE:1cxx_deleted_functions
           Feature record: CXX_FEATURE:0cxx_digit_separators
           Feature record: CXX_FEATURE:1cxx_enum_forward_declarations
           Feature record: CXX_FEATURE:1cxx_explicit_conversions
           Feature record: CXX_FEATURE:1cxx_extended_friend_declarations
           Feature record: CXX_FEATURE:1cxx_extern_templates
           Feature record: CXX_FEATURE:1cxx_final
           Feature record: CXX_FEATURE:1cxx_func_identifier
           Feature record: CXX_FEATURE:1cxx_generalized_initializers
           Feature record: CXX_FEATURE:0cxx_generic_lambdas
           Feature record: CXX_FEATURE:1cxx_inheriting_constructors
           Feature record: CXX_FEATURE:1cxx_inline_namespaces
           Feature record: CXX_FEATURE:1cxx_lambdas
           Feature record: CXX_FEATURE:0cxx_lambda_init_captures
           Feature record: CXX_FEATURE:1cxx_local_type_template_args
           Feature record: CXX_FEATURE:1cxx_long_long_type
           Feature record: CXX_FEATURE:1cxx_noexcept
           Feature record: CXX_FEATURE:1cxx_nonstatic_member_init
           Feature record: CXX_FEATURE:1cxx_nullptr
           Feature record: CXX_FEATURE:1cxx_override
           Feature record: CXX_FEATURE:1cxx_range_for
           Feature record: CXX_FEATURE:1cxx_raw_string_literals
           Feature record: CXX_FEATURE:1cxx_reference_qualified_functions
           Feature record: CXX_FEATURE:0cxx_relaxed_constexpr
           Feature record: CXX_FEATURE:0cxx_return_type_deduction
           Feature record: CXX_FEATURE:1cxx_right_angle_brackets
           Feature record: CXX_FEATURE:1cxx_rvalue_references
           Feature record: CXX_FEATURE:1cxx_sizeof_member
           Feature record: CXX_FEATURE:1cxx_static_assert
           Feature record: CXX_FEATURE:1cxx_strong_enums
           Feature record: CXX_FEATURE:1cxx_template_template_parameters
           Feature record: CXX_FEATURE:1cxx_thread_local
           Feature record: CXX_FEATURE:1cxx_trailing_return_types
           Feature record: CXX_FEATURE:1cxx_unicode_literals
           Feature record: CXX_FEATURE:1cxx_uniform_initialization
           Feature record: CXX_FEATURE:1cxx_unrestricted_unions
           Feature record: CXX_FEATURE:1cxx_user_literals
           Feature record: CXX_FEATURE:0cxx_variable_templates
           Feature record: CXX_FEATURE:1cxx_variadic_macros
           Feature record: CXX_FEATURE:1cxx_variadic_templates


       Detecting CXX [-std=c++98] compiler features compiled with the following output:
       Change Dir: /warp-ctc/build/CMakeFiles/CMakeTmp

       Run Build Command(s):/usr/bin/make cmTC_df7be/fast 
       /usr/bin/make -f CMakeFiles/cmTC_df7be.dir/build.make CMakeFiles/cmTC_df7be.dir/build
       make[1]: Entering directory '/warp-ctc/build/CMakeFiles/CMakeTmp'
       Building CXX object CMakeFiles/cmTC_df7be.dir/feature_tests.cxx.o
       /usr/bin/c++    -std=c++98 -o CMakeFiles/cmTC_df7be.dir/feature_tests.cxx.o -c /warp-ctc/build/CMakeFiles/feature_tests.cxx
       Linking CXX executable cmTC_df7be
       /opt/conda/envs/danspeech/bin/cmake -E cmake_link_script CMakeFiles/cmTC_df7be.dir/link.txt --verbose=1
       /usr/bin/c++       -rdynamic CMakeFiles/cmTC_df7be.dir/feature_tests.cxx.o  -o cmTC_df7be 
       make[1]: Leaving directory '/warp-ctc/build/CMakeFiles/CMakeTmp'


           Feature record: CXX_FEATURE:0cxx_aggregate_default_initializers
           Feature record: CXX_FEATURE:0cxx_alias_templates
           Feature record: CXX_FEATURE:0cxx_alignas
           Feature record: CXX_FEATURE:0cxx_alignof
           Feature record: CXX_FEATURE:0cxx_attributes
           Feature record: CXX_FEATURE:0cxx_attribute_deprecated
           Feature record: CXX_FEATURE:0cxx_auto_type
           Feature record: CXX_FEATURE:0cxx_binary_literals
           Feature record: CXX_FEATURE:0cxx_constexpr
           Feature record: CXX_FEATURE:0cxx_contextual_conversions
           Feature record: CXX_FEATURE:0cxx_decltype
           Feature record: CXX_FEATURE:0cxx_decltype_auto
           Feature record: CXX_FEATURE:0cxx_decltype_incomplete_return_types
           Feature record: CXX_FEATURE:0cxx_default_function_template_args
           Feature record: CXX_FEATURE:0cxx_defaulted_functions
           Feature record: CXX_FEATURE:0cxx_defaulted_move_initializers
           Feature record: CXX_FEATURE:0cxx_delegating_constructors
           Feature record: CXX_FEATURE:0cxx_deleted_functions
           Feature record: CXX_FEATURE:0cxx_digit_separators
           Feature record: CXX_FEATURE:0cxx_enum_forward_declarations
           Feature record: CXX_FEATURE:0cxx_explicit_conversions
           Feature record: CXX_FEATURE:0cxx_extended_friend_declarations
           Feature record: CXX_FEATURE:0cxx_extern_templates
           Feature record: CXX_FEATURE:0cxx_final
           Feature record: CXX_FEATURE:0cxx_func_identifier
           Feature record: CXX_FEATURE:0cxx_generalized_initializers
           Feature record: CXX_FEATURE:0cxx_generic_lambdas
           Feature record: CXX_FEATURE:0cxx_inheriting_constructors
           Feature record: CXX_FEATURE:0cxx_inline_namespaces
           Feature record: CXX_FEATURE:0cxx_lambdas
           Feature record: CXX_FEATURE:0cxx_lambda_init_captures
           Feature record: CXX_FEATURE:0cxx_local_type_template_args
           Feature record: CXX_FEATURE:0cxx_long_long_type
           Feature record: CXX_FEATURE:0cxx_noexcept
           Feature record: CXX_FEATURE:0cxx_nonstatic_member_init
           Feature record: CXX_FEATURE:0cxx_nullptr
           Feature record: CXX_FEATURE:0cxx_override
           Feature record: CXX_FEATURE:0cxx_range_for
           Feature record: CXX_FEATURE:0cxx_raw_string_literals
           Feature record: CXX_FEATURE:0cxx_reference_qualified_functions
           Feature record: CXX_FEATURE:0cxx_relaxed_constexpr
           Feature record: CXX_FEATURE:0cxx_return_type_deduction
           Feature record: CXX_FEATURE:0cxx_right_angle_brackets
           Feature record: CXX_FEATURE:0cxx_rvalue_references
           Feature record: CXX_FEATURE:0cxx_sizeof_member
           Feature record: CXX_FEATURE:0cxx_static_assert
           Feature record: CXX_FEATURE:0cxx_strong_enums
           Feature record: CXX_FEATURE:1cxx_template_template_parameters
           Feature record: CXX_FEATURE:0cxx_thread_local
           Feature record: CXX_FEATURE:0cxx_trailing_return_types
           Feature record: CXX_FEATURE:0cxx_unicode_literals
           Feature record: CXX_FEATURE:0cxx_uniform_initialization
           Feature record: CXX_FEATURE:0cxx_unrestricted_unions
           Feature record: CXX_FEATURE:0cxx_user_literals
           Feature record: CXX_FEATURE:0cxx_variable_templates
           Feature record: CXX_FEATURE:0cxx_variadic_macros
           Feature record: CXX_FEATURE:0cxx_variadic_templates
       Determining if the include file pthread.h exists passed with the following output:
       Change Dir: /warp-ctc/build/CMakeFiles/CMakeTmp

       Run Build Command(s):/usr/bin/make cmTC_e3368/fast 
       /usr/bin/make -f CMakeFiles/cmTC_e3368.dir/build.make CMakeFiles/cmTC_e3368.dir/build
       make[1]: Entering directory '/warp-ctc/build/CMakeFiles/CMakeTmp'
       Building C object CMakeFiles/cmTC_e3368.dir/CheckIncludeFile.c.o
       /usr/bin/cc   -fPIC    -o CMakeFiles/cmTC_e3368.dir/CheckIncludeFile.c.o   -c /warp-ctc/build/CMakeFiles/CMakeTmp/CheckIncludeFile.c
       Linking C executable cmTC_e3368
       /opt/conda/envs/danspeech/bin/cmake -E cmake_link_script CMakeFiles/cmTC_e3368.dir/link.txt --verbose=1
       /usr/bin/cc -fPIC     -rdynamic CMakeFiles/cmTC_e3368.dir/CheckIncludeFile.c.o  -o cmTC_e3368 
       make[1]: Leaving directory '/warp-ctc/build/CMakeFiles/CMakeTmp'


       Determining if the function pthread_create exists in the pthread passed with the following output:
       Change Dir: /warp-ctc/build/CMakeFiles/CMakeTmp

       Run Build Command(s):/usr/bin/make cmTC_78d9b/fast 
       /usr/bin/make -f CMakeFiles/cmTC_78d9b.dir/build.make CMakeFiles/cmTC_78d9b.dir/build
       make[1]: Entering directory '/warp-ctc/build/CMakeFiles/CMakeTmp'
       Building C object CMakeFiles/cmTC_78d9b.dir/CheckFunctionExists.c.o
       /usr/bin/cc   -fPIC -DCHECK_FUNCTION_EXISTS=pthread_create   -o CMakeFiles/cmTC_78d9b.dir/CheckFunctionExists.c.o   -c /opt/conda/envs/danspeech/share/cmake-3.14/Modules/CheckFunctionExists.c
       Linking C executable cmTC_78d9b
       /opt/conda/envs/danspeech/bin/cmake -E cmake_link_script CMakeFiles/cmTC_78d9b.dir/link.txt --verbose=1
       /usr/bin/cc -fPIC -DCHECK_FUNCTION_EXISTS=pthread_create    -rdynamic CMakeFiles/cmTC_78d9b.dir/CheckFunctionExists.c.o  -o cmTC_78d9b -lpthread 
       make[1]: Leaving directory '/warp-ctc/build/CMakeFiles/CMakeTmp'


       The system is: Linux - 4.15.0-96-generic - x86_64
       Compiling the C compiler identification source file "CMakeCCompilerId.c" succeeded.
       Compiler: /usr/bin/cc 
       Build flags: 
       Id flags:  

       The output was:
       0


       Compilation of the C compiler identification source "CMakeCCompilerId.c" produced "a.out"

       The C compiler identification is GNU, found in "/warp-ctc/build/CMakeFiles/3.10.2/CompilerIdC/a.out"

       Compiling the CXX compiler identification source file "CMakeCXXCompilerId.cpp" succeeded.
       Compiler: /usr/bin/c++ 
       Build flags: 
       Id flags:  

       The output was:
       0


       Compilation of the CXX compiler identification source "CMakeCXXCompilerId.cpp" produced "a.out"

       The CXX compiler identification is GNU, found in "/warp-ctc/build/CMakeFiles/3.10.2/CompilerIdCXX/a.out"

       Determining if the C compiler works passed with the following output:
       Change Dir: /warp-ctc/build/CMakeFiles/CMakeTmp

       Run Build Command:"/usr/bin/make" "cmTC_2f556/fast"
       /usr/bin/make -f CMakeFiles/cmTC_2f556.dir/build.make CMakeFiles/cmTC_2f556.dir/build
       make[1]: Entering directory '/warp-ctc/build/CMakeFiles/CMakeTmp'
       Building C object CMakeFiles/cmTC_2f556.dir/testCCompiler.c.o
       /usr/bin/cc    -o CMakeFiles/cmTC_2f556.dir/testCCompiler.c.o   -c /warp-ctc/build/CMakeFiles/CMakeTmp/testCCompiler.c
       Linking C executable cmTC_2f556
       /usr/bin/cmake -E cmake_link_script CMakeFiles/cmTC_2f556.dir/link.txt --verbose=1
       /usr/bin/cc      -rdynamic CMakeFiles/cmTC_2f556.dir/testCCompiler.c.o  -o cmTC_2f556 
       make[1]: Leaving directory '/warp-ctc/build/CMakeFiles/CMakeTmp'


       Detecting C compiler ABI info compiled with the following output:
       Change Dir: /warp-ctc/build/CMakeFiles/CMakeTmp

       Run Build Command:"/usr/bin/make" "cmTC_365c8/fast"
       /usr/bin/make -f CMakeFiles/cmTC_365c8.dir/build.make CMakeFiles/cmTC_365c8.dir/build
       make[1]: Entering directory '/warp-ctc/build/CMakeFiles/CMakeTmp'
       Building C object CMakeFiles/cmTC_365c8.dir/CMakeCCompilerABI.c.o
       /usr/bin/cc    -o CMakeFiles/cmTC_365c8.dir/CMakeCCompilerABI.c.o   -c /usr/share/cmake-3.10/Modules/CMakeCCompilerABI.c
       Linking C executable cmTC_365c8
       /usr/bin/cmake -E cmake_link_script CMakeFiles/cmTC_365c8.dir/link.txt --verbose=1
       /usr/bin/cc     -v -rdynamic CMakeFiles/cmTC_365c8.dir/CMakeCCompilerABI.c.o  -o cmTC_365c8 
       Using built-in specs.
       COLLECT_GCC=/usr/bin/cc
       COLLECT_LTO_WRAPPER=/usr/lib/gcc/x86_64-linux-gnu/7/lto-wrapper
       OFFLOAD_TARGET_NAMES=nvptx-none
       OFFLOAD_TARGET_DEFAULT=1
       Target: x86_64-linux-gnu
       Configured with: ../src/configure -v --with-pkgversion='Ubuntu 7.4.0-1ubuntu1~18.04.1' --with-bugurl=file:///usr/share/doc/gcc-7/README.Bugs --enable-languages=c,ada,c++,go,brig,d,fortran,objc,obj-c++ --prefix=/usr --with-gcc-major-version-only --program-suffix=-7 --program-prefix=x86_64-linux-gnu- --enable-shared --enable-linker-build-id --libexecdir=/usr/lib --without-included-gettext --enable-threads=posix --libdir=/usr/lib --enable-nls --with-sysroot=/ --enable-clocale=gnu --enable-libstdcxx-debug --enable-libstdcxx-time=yes --with-default-libstdcxx-abi=new --enable-gnu-unique-object --disable-vtable-verify --enable-libmpx --enable-plugin --enable-default-pie --with-system-zlib --with-target-system-zlib --enable-objc-gc=auto --enable-multiarch --disable-werror --with-arch-32=i686 --with-abi=m64 --with-multilib-list=m32,m64,mx32 --enable-multilib --with-tune=generic --enable-offload-targets=nvptx-none --without-cuda-driver --enable-checking=release --build=x86_64-linux-gnu --host=x86_64-linux-gnu --target=x86_64-linux-gnu
       Thread model: posix
       gcc version 7.4.0 (Ubuntu 7.4.0-1ubuntu1~18.04.1) 
       COMPILER_PATH=/usr/lib/gcc/x86_64-linux-gnu/7/:/usr/lib/gcc/x86_64-linux-gnu/7/:/usr/lib/gcc/x86_64-linux-gnu/:/usr/lib/gcc/x86_64-linux-gnu/7/:/usr/lib/gcc/x86_64-linux-gnu/
       LIBRARY_PATH=/usr/lib/gcc/x86_64-linux-gnu/7/:/usr/lib/gcc/x86_64-linux-gnu/7/../../../x86_64-linux-gnu/:/usr/lib/gcc/x86_64-linux-gnu/7/../../../../lib/:/lib/x86_64-linux-gnu/:/lib/../lib/:/usr/lib/x86_64-linux-gnu/:/usr/lib/../lib/:/usr/local/cuda/lib64/stubs/:/usr/lib/gcc/x86_64-linux-gnu/7/../../../:/lib/:/usr/lib/
       COLLECT_GCC_OPTIONS='-v' '-rdynamic' '-o' 'cmTC_365c8' '-mtune=generic' '-march=x86-64'
        /usr/lib/gcc/x86_64-linux-gnu/7/collect2 -plugin /usr/lib/gcc/x86_64-linux-gnu/7/liblto_plugin.so -plugin-opt=/usr/lib/gcc/x86_64-linux-gnu/7/lto-wrapper -plugin-opt=-fresolution=/tmp/cc5TQUcL.res -plugin-opt=-pass-through=-lgcc -plugin-opt=-pass-through=-lgcc_s -plugin-opt=-pass-through=-lc -plugin-opt=-pass-through=-lgcc -plugin-opt=-pass-through=-lgcc_s --sysroot=/ --build-id --eh-frame-hdr -m elf_x86_64 --hash-style=gnu --as-needed -export-dynamic -dynamic-linker /lib64/ld-linux-x86-64.so.2 -pie -z now -z relro -o cmTC_365c8 /usr/lib/gcc/x86_64-linux-gnu/7/../../../x86_64-linux-gnu/Scrt1.o /usr/lib/gcc/x86_64-linux-gnu/7/../../../x86_64-linux-gnu/crti.o /usr/lib/gcc/x86_64-linux-gnu/7/crtbeginS.o -L/usr/lib/gcc/x86_64-linux-gnu/7 -L/usr/lib/gcc/x86_64-linux-gnu/7/../../../x86_64-linux-gnu -L/usr/lib/gcc/x86_64-linux-gnu/7/../../../../lib -L/lib/x86_64-linux-gnu -L/lib/../lib -L/usr/lib/x86_64-linux-gnu -L/usr/lib/../lib -L/usr/local/cuda/lib64/stubs -L/usr/lib/gcc/x86_64-linux-gnu/7/../../.. CMakeFiles/cmTC_365c8.dir/CMakeCCompilerABI.c.o -lgcc --push-state --as-needed -lgcc_s --pop-state -lc -lgcc --push-state --as-needed -lgcc_s --pop-state /usr/lib/gcc/x86_64-linux-gnu/7/crtendS.o /usr/lib/gcc/x86_64-linux-gnu/7/../../../x86_64-linux-gnu/crtn.o
       COLLECT_GCC_OPTIONS='-v' '-rdynamic' '-o' 'cmTC_365c8' '-mtune=generic' '-march=x86-64'
       make[1]: Leaving directory '/warp-ctc/build/CMakeFiles/CMakeTmp'


       Parsed C implicit link information from above output:
         link line regex: [^( *|.*[/\])(ld|CMAKE_LINK_STARTFILE-NOTFOUND|([^/\]+-)?ld|collect2)[^/\]*( |$)]
         ignore line: [Change Dir: /warp-ctc/build/CMakeFiles/CMakeTmp]
         ignore line: []
         ignore line: [Run Build Command:"/usr/bin/make" "cmTC_365c8/fast"]
         ignore line: [/usr/bin/make -f CMakeFiles/cmTC_365c8.dir/build.make CMakeFiles/cmTC_365c8.dir/build]
         ignore line: [make[1]: Entering directory '/warp-ctc/build/CMakeFiles/CMakeTmp']
         ignore line: [Building C object CMakeFiles/cmTC_365c8.dir/CMakeCCompilerABI.c.o]
         ignore line: [/usr/bin/cc    -o CMakeFiles/cmTC_365c8.dir/CMakeCCompilerABI.c.o   -c /usr/share/cmake-3.10/Modules/CMakeCCompilerABI.c]
         ignore line: [Linking C executable cmTC_365c8]
         ignore line: [/usr/bin/cmake -E cmake_link_script CMakeFiles/cmTC_365c8.dir/link.txt --verbose=1]
         ignore line: [/usr/bin/cc     -v -rdynamic CMakeFiles/cmTC_365c8.dir/CMakeCCompilerABI.c.o  -o cmTC_365c8 ]
         ignore line: [Using built-in specs.]
         ignore line: [COLLECT_GCC=/usr/bin/cc]
         ignore line: [COLLECT_LTO_WRAPPER=/usr/lib/gcc/x86_64-linux-gnu/7/lto-wrapper]
         ignore line: [OFFLOAD_TARGET_NAMES=nvptx-none]
         ignore line: [OFFLOAD_TARGET_DEFAULT=1]
         ignore line: [Target: x86_64-linux-gnu]
         ignore line: [Configured with: ../src/configure -v --with-pkgversion='Ubuntu 7.4.0-1ubuntu1~18.04.1' --with-bugurl=file:///usr/share/doc/gcc-7/README.Bugs --enable-languages=c,ada,c++,go,brig,d,fortran,objc,obj-c++ --prefix=/usr --with-gcc-major-version-only --program-suffix=-7 --program-prefix=x86_64-linux-gnu- --enable-shared --enable-linker-build-id --libexecdir=/usr/lib --without-included-gettext --enable-threads=posix --libdir=/usr/lib --enable-nls --with-sysroot=/ --enable-clocale=gnu --enable-libstdcxx-debug --enable-libstdcxx-time=yes --with-default-libstdcxx-abi=new --enable-gnu-unique-object --disable-vtable-verify --enable-libmpx --enable-plugin --enable-default-pie --with-system-zlib --with-target-system-zlib --enable-objc-gc=auto --enable-multiarch --disable-werror --with-arch-32=i686 --with-abi=m64 --with-multilib-list=m32,m64,mx32 --enable-multilib --with-tune=generic --enable-offload-targets=nvptx-none --without-cuda-driver --enable-checking=release --build=x86_64-linux-gnu --host=x86_64-linux-gnu --target=x86_64-linux-gnu]
         ignore line: [Thread model: posix]
         ignore line: [gcc version 7.4.0 (Ubuntu 7.4.0-1ubuntu1~18.04.1) ]
         ignore line: [COMPILER_PATH=/usr/lib/gcc/x86_64-linux-gnu/7/:/usr/lib/gcc/x86_64-linux-gnu/7/:/usr/lib/gcc/x86_64-linux-gnu/:/usr/lib/gcc/x86_64-linux-gnu/7/:/usr/lib/gcc/x86_64-linux-gnu/]
         ignore line: [LIBRARY_PATH=/usr/lib/gcc/x86_64-linux-gnu/7/:/usr/lib/gcc/x86_64-linux-gnu/7/../../../x86_64-linux-gnu/:/usr/lib/gcc/x86_64-linux-gnu/7/../../../../lib/:/lib/x86_64-linux-gnu/:/lib/../lib/:/usr/lib/x86_64-linux-gnu/:/usr/lib/../lib/:/usr/local/cuda/lib64/stubs/:/usr/lib/gcc/x86_64-linux-gnu/7/../../../:/lib/:/usr/lib/]
         ignore line: [COLLECT_GCC_OPTIONS='-v' '-rdynamic' '-o' 'cmTC_365c8' '-mtune=generic' '-march=x86-64']
         link line: [ /usr/lib/gcc/x86_64-linux-gnu/7/collect2 -plugin /usr/lib/gcc/x86_64-linux-gnu/7/liblto_plugin.so -plugin-opt=/usr/lib/gcc/x86_64-linux-gnu/7/lto-wrapper -plugin-opt=-fresolution=/tmp/cc5TQUcL.res -plugin-opt=-pass-through=-lgcc -plugin-opt=-pass-through=-lgcc_s -plugin-opt=-pass-through=-lc -plugin-opt=-pass-through=-lgcc -plugin-opt=-pass-through=-lgcc_s --sysroot=/ --build-id --eh-frame-hdr -m elf_x86_64 --hash-style=gnu --as-needed -export-dynamic -dynamic-linker /lib64/ld-linux-x86-64.so.2 -pie -z now -z relro -o cmTC_365c8 /usr/lib/gcc/x86_64-linux-gnu/7/../../../x86_64-linux-gnu/Scrt1.o /usr/lib/gcc/x86_64-linux-gnu/7/../../../x86_64-linux-gnu/crti.o /usr/lib/gcc/x86_64-linux-gnu/7/crtbeginS.o -L/usr/lib/gcc/x86_64-linux-gnu/7 -L/usr/lib/gcc/x86_64-linux-gnu/7/../../../x86_64-linux-gnu -L/usr/lib/gcc/x86_64-linux-gnu/7/../../../../lib -L/lib/x86_64-linux-gnu -L/lib/../lib -L/usr/lib/x86_64-linux-gnu -L/usr/lib/../lib -L/usr/local/cuda/lib64/stubs -L/usr/lib/gcc/x86_64-linux-gnu/7/../../.. CMakeFiles/cmTC_365c8.dir/CMakeCCompilerABI.c.o -lgcc --push-state --as-needed -lgcc_s --pop-state -lc -lgcc --push-state --as-needed -lgcc_s --pop-state /usr/lib/gcc/x86_64-linux-gnu/7/crtendS.o /usr/lib/gcc/x86_64-linux-gnu/7/../../../x86_64-linux-gnu/crtn.o]
           arg [/usr/lib/gcc/x86_64-linux-gnu/7/collect2] ==> ignore
           arg [-plugin] ==> ignore
           arg [/usr/lib/gcc/x86_64-linux-gnu/7/liblto_plugin.so] ==> ignore
           arg [-plugin-opt=/usr/lib/gcc/x86_64-linux-gnu/7/lto-wrapper] ==> ignore
           arg [-plugin-opt=-fresolution=/tmp/cc5TQUcL.res] ==> ignore
           arg [-plugin-opt=-pass-through=-lgcc] ==> ignore
           arg [-plugin-opt=-pass-through=-lgcc_s] ==> ignore
           arg [-plugin-opt=-pass-through=-lc] ==> ignore
           arg [-plugin-opt=-pass-through=-lgcc] ==> ignore
           arg [-plugin-opt=-pass-through=-lgcc_s] ==> ignore
           arg [--sysroot=/] ==> ignore
           arg [--build-id] ==> ignore
           arg [--eh-frame-hdr] ==> ignore
           arg [-m] ==> ignore
           arg [elf_x86_64] ==> ignore
           arg [--hash-style=gnu] ==> ignore
           arg [--as-needed] ==> ignore
           arg [-export-dynamic] ==> ignore
           arg [-dynamic-linker] ==> ignore
           arg [/lib64/ld-linux-x86-64.so.2] ==> ignore
           arg [-pie] ==> ignore
           arg [-znow] ==> ignore
           arg [-zrelro] ==> ignore
           arg [-o] ==> ignore
           arg [cmTC_365c8] ==> ignore
           arg [/usr/lib/gcc/x86_64-linux-gnu/7/../../../x86_64-linux-gnu/Scrt1.o] ==> ignore
           arg [/usr/lib/gcc/x86_64-linux-gnu/7/../../../x86_64-linux-gnu/crti.o] ==> ignore
           arg [/usr/lib/gcc/x86_64-linux-gnu/7/crtbeginS.o] ==> ignore
           arg [-L/usr/lib/gcc/x86_64-linux-gnu/7] ==> dir [/usr/lib/gcc/x86_64-linux-gnu/7]
           arg [-L/usr/lib/gcc/x86_64-linux-gnu/7/../../../x86_64-linux-gnu] ==> dir [/usr/lib/gcc/x86_64-linux-gnu/7/../../../x86_64-linux-gnu]
           arg [-L/usr/lib/gcc/x86_64-linux-gnu/7/../../../../lib] ==> dir [/usr/lib/gcc/x86_64-linux-gnu/7/../../../../lib]
           arg [-L/lib/x86_64-linux-gnu] ==> dir [/lib/x86_64-linux-gnu]
           arg [-L/lib/../lib] ==> dir [/lib/../lib]
           arg [-L/usr/lib/x86_64-linux-gnu] ==> dir [/usr/lib/x86_64-linux-gnu]
           arg [-L/usr/lib/../lib] ==> dir [/usr/lib/../lib]
           arg [-L/usr/local/cuda/lib64/stubs] ==> dir [/usr/local/cuda/lib64/stubs]
           arg [-L/usr/lib/gcc/x86_64-linux-gnu/7/../../..] ==> dir [/usr/lib/gcc/x86_64-linux-gnu/7/../../..]
           arg [CMakeFiles/cmTC_365c8.dir/CMakeCCompilerABI.c.o] ==> ignore
           arg [-lgcc] ==> lib [gcc]
           arg [--push-state] ==> ignore
           arg [--as-needed] ==> ignore
           arg [-lgcc_s] ==> lib [gcc_s]
           arg [--pop-state] ==> ignore
           arg [-lc] ==> lib [c]
           arg [-lgcc] ==> lib [gcc]
           arg [--push-state] ==> ignore
           arg [--as-needed] ==> ignore
           arg [-lgcc_s] ==> lib [gcc_s]
           arg [--pop-state] ==> ignore
           arg [/usr/lib/gcc/x86_64-linux-gnu/7/crtendS.o] ==> ignore
           arg [/usr/lib/gcc/x86_64-linux-gnu/7/../../../x86_64-linux-gnu/crtn.o] ==> ignore
         collapse library dir [/usr/lib/gcc/x86_64-linux-gnu/7] ==> [/usr/lib/gcc/x86_64-linux-gnu/7]
         collapse library dir [/usr/lib/gcc/x86_64-linux-gnu/7/../../../x86_64-linux-gnu] ==> [/usr/lib/x86_64-linux-gnu]
         collapse library dir [/usr/lib/gcc/x86_64-linux-gnu/7/../../../../lib] ==> [/usr/lib]
         collapse library dir [/lib/x86_64-linux-gnu] ==> [/lib/x86_64-linux-gnu]
         collapse library dir [/lib/../lib] ==> [/lib]
         collapse library dir [/usr/lib/x86_64-linux-gnu] ==> [/usr/lib/x86_64-linux-gnu]
         collapse library dir [/usr/lib/../lib] ==> [/usr/lib]
         collapse library dir [/usr/local/cuda/lib64/stubs] ==> [/usr/local/cuda/lib64/stubs]
         collapse library dir [/usr/lib/gcc/x86_64-linux-gnu/7/../../..] ==> [/usr/lib]
         implicit libs: [gcc;gcc_s;c;gcc;gcc_s]
         implicit dirs: [/usr/lib/gcc/x86_64-linux-gnu/7;/usr/lib/x86_64-linux-gnu;/usr/lib;/lib/x86_64-linux-gnu;/lib;/usr/local/cuda/lib64/stubs]
         implicit fwks: []




       Detecting C [-std=c11] compiler features compiled with the following output:
       Change Dir: /warp-ctc/build/CMakeFiles/CMakeTmp

       Run Build Command:"/usr/bin/make" "cmTC_82f41/fast"
       /usr/bin/make -f CMakeFiles/cmTC_82f41.dir/build.make CMakeFiles/cmTC_82f41.dir/build
       make[1]: Entering directory '/warp-ctc/build/CMakeFiles/CMakeTmp'
       Building C object CMakeFiles/cmTC_82f41.dir/feature_tests.c.o
       /usr/bin/cc   -std=c11 -o CMakeFiles/cmTC_82f41.dir/feature_tests.c.o   -c /warp-ctc/build/CMakeFiles/feature_tests.c
       Linking C executable cmTC_82f41
       /usr/bin/cmake -E cmake_link_script CMakeFiles/cmTC_82f41.dir/link.txt --verbose=1
       /usr/bin/cc      -rdynamic CMakeFiles/cmTC_82f41.dir/feature_tests.c.o  -o cmTC_82f41 
       make[1]: Leaving directory '/warp-ctc/build/CMakeFiles/CMakeTmp'


           Feature record: C_FEATURE:1c_function_prototypes
           Feature record: C_FEATURE:1c_restrict
           Feature record: C_FEATURE:1c_static_assert
           Feature record: C_FEATURE:1c_variadic_macros


       Detecting C [-std=c99] compiler features compiled with the following output:
       Change Dir: /warp-ctc/build/CMakeFiles/CMakeTmp

       Run Build Command:"/usr/bin/make" "cmTC_47cfd/fast"
       /usr/bin/make -f CMakeFiles/cmTC_47cfd.dir/build.make CMakeFiles/cmTC_47cfd.dir/build
       make[1]: Entering directory '/warp-ctc/build/CMakeFiles/CMakeTmp'
       Building C object CMakeFiles/cmTC_47cfd.dir/feature_tests.c.o
       /usr/bin/cc   -std=c99 -o CMakeFiles/cmTC_47cfd.dir/feature_tests.c.o   -c /warp-ctc/build/CMakeFiles/feature_tests.c
       Linking C executable cmTC_47cfd
       /usr/bin/cmake -E cmake_link_script CMakeFiles/cmTC_47cfd.dir/link.txt --verbose=1
       /usr/bin/cc      -rdynamic CMakeFiles/cmTC_47cfd.dir/feature_tests.c.o  -o cmTC_47cfd 
       make[1]: Leaving directory '/warp-ctc/build/CMakeFiles/CMakeTmp'


           Feature record: C_FEATURE:1c_function_prototypes
           Feature record: C_FEATURE:1c_restrict
           Feature record: C_FEATURE:0c_static_assert
           Feature record: C_FEATURE:1c_variadic_macros


       Detecting C [-std=c90] compiler features compiled with the following output:
       Change Dir: /warp-ctc/build/CMakeFiles/CMakeTmp

       Run Build Command:"/usr/bin/make" "cmTC_bd937/fast"
       /usr/bin/make -f CMakeFiles/cmTC_bd937.dir/build.make CMakeFiles/cmTC_bd937.dir/build
       make[1]: Entering directory '/warp-ctc/build/CMakeFiles/CMakeTmp'
       Building C object CMakeFiles/cmTC_bd937.dir/feature_tests.c.o
       /usr/bin/cc   -std=c90 -o CMakeFiles/cmTC_bd937.dir/feature_tests.c.o   -c /warp-ctc/build/CMakeFiles/feature_tests.c
       Linking C executable cmTC_bd937
       /usr/bin/cmake -E cmake_link_script CMakeFiles/cmTC_bd937.dir/link.txt --verbose=1
       /usr/bin/cc      -rdynamic CMakeFiles/cmTC_bd937.dir/feature_tests.c.o  -o cmTC_bd937 
       make[1]: Leaving directory '/warp-ctc/build/CMakeFiles/CMakeTmp'


           Feature record: C_FEATURE:1c_function_prototypes
           Feature record: C_FEATURE:0c_restrict
           Feature record: C_FEATURE:0c_static_assert
           Feature record: C_FEATURE:0c_variadic_macros
       Determining if the CXX compiler works passed with the following output:
       Change Dir: /warp-ctc/build/CMakeFiles/CMakeTmp

       Run Build Command:"/usr/bin/make" "cmTC_feee3/fast"
       /usr/bin/make -f CMakeFiles/cmTC_feee3.dir/build.make CMakeFiles/cmTC_feee3.dir/build
       make[1]: Entering directory '/warp-ctc/build/CMakeFiles/CMakeTmp'
       Building CXX object CMakeFiles/cmTC_feee3.dir/testCXXCompiler.cxx.o
       /usr/bin/c++     -o CMakeFiles/cmTC_feee3.dir/testCXXCompiler.cxx.o -c /warp-ctc/build/CMakeFiles/CMakeTmp/testCXXCompiler.cxx
       Linking CXX executable cmTC_feee3
       /usr/bin/cmake -E cmake_link_script CMakeFiles/cmTC_feee3.dir/link.txt --verbose=1
       /usr/bin/c++       -rdynamic CMakeFiles/cmTC_feee3.dir/testCXXCompiler.cxx.o  -o cmTC_feee3 
       make[1]: Leaving directory '/warp-ctc/build/CMakeFiles/CMakeTmp'


       Detecting CXX compiler ABI info compiled with the following output:
       Change Dir: /warp-ctc/build/CMakeFiles/CMakeTmp

       Run Build Command:"/usr/bin/make" "cmTC_5100f/fast"
       /usr/bin/make -f CMakeFiles/cmTC_5100f.dir/build.make CMakeFiles/cmTC_5100f.dir/build
       make[1]: Entering directory '/warp-ctc/build/CMakeFiles/CMakeTmp'
       Building CXX object CMakeFiles/cmTC_5100f.dir/CMakeCXXCompilerABI.cpp.o
       /usr/bin/c++     -o CMakeFiles/cmTC_5100f.dir/CMakeCXXCompilerABI.cpp.o -c /usr/share/cmake-3.10/Modules/CMakeCXXCompilerABI.cpp
       Linking CXX executable cmTC_5100f
       /usr/bin/cmake -E cmake_link_script CMakeFiles/cmTC_5100f.dir/link.txt --verbose=1
       /usr/bin/c++      -v -rdynamic CMakeFiles/cmTC_5100f.dir/CMakeCXXCompilerABI.cpp.o  -o cmTC_5100f 
       Using built-in specs.
       COLLECT_GCC=/usr/bin/c++
       COLLECT_LTO_WRAPPER=/usr/lib/gcc/x86_64-linux-gnu/7/lto-wrapper
       OFFLOAD_TARGET_NAMES=nvptx-none
       OFFLOAD_TARGET_DEFAULT=1
       Target: x86_64-linux-gnu
       Configured with: ../src/configure -v --with-pkgversion='Ubuntu 7.4.0-1ubuntu1~18.04.1' --with-bugurl=file:///usr/share/doc/gcc-7/README.Bugs --enable-languages=c,ada,c++,go,brig,d,fortran,objc,obj-c++ --prefix=/usr --with-gcc-major-version-only --program-suffix=-7 --program-prefix=x86_64-linux-gnu- --enable-shared --enable-linker-build-id --libexecdir=/usr/lib --without-included-gettext --enable-threads=posix --libdir=/usr/lib --enable-nls --with-sysroot=/ --enable-clocale=gnu --enable-libstdcxx-debug --enable-libstdcxx-time=yes --with-default-libstdcxx-abi=new --enable-gnu-unique-object --disable-vtable-verify --enable-libmpx --enable-plugin --enable-default-pie --with-system-zlib --with-target-system-zlib --enable-objc-gc=auto --enable-multiarch --disable-werror --with-arch-32=i686 --with-abi=m64 --with-multilib-list=m32,m64,mx32 --enable-multilib --with-tune=generic --enable-offload-targets=nvptx-none --without-cuda-driver --enable-checking=release --build=x86_64-linux-gnu --host=x86_64-linux-gnu --target=x86_64-linux-gnu
       Thread model: posix
       gcc version 7.4.0 (Ubuntu 7.4.0-1ubuntu1~18.04.1) 
       COMPILER_PATH=/usr/lib/gcc/x86_64-linux-gnu/7/:/usr/lib/gcc/x86_64-linux-gnu/7/:/usr/lib/gcc/x86_64-linux-gnu/:/usr/lib/gcc/x86_64-linux-gnu/7/:/usr/lib/gcc/x86_64-linux-gnu/
       LIBRARY_PATH=/usr/lib/gcc/x86_64-linux-gnu/7/:/usr/lib/gcc/x86_64-linux-gnu/7/../../../x86_64-linux-gnu/:/usr/lib/gcc/x86_64-linux-gnu/7/../../../../lib/:/lib/x86_64-linux-gnu/:/lib/../lib/:/usr/lib/x86_64-linux-gnu/:/usr/lib/../lib/:/usr/local/cuda/lib64/stubs/:/usr/lib/gcc/x86_64-linux-gnu/7/../../../:/lib/:/usr/lib/
       COLLECT_GCC_OPTIONS='-v' '-rdynamic' '-o' 'cmTC_5100f' '-shared-libgcc' '-mtune=generic' '-march=x86-64'
        /usr/lib/gcc/x86_64-linux-gnu/7/collect2 -plugin /usr/lib/gcc/x86_64-linux-gnu/7/liblto_plugin.so -plugin-opt=/usr/lib/gcc/x86_64-linux-gnu/7/lto-wrapper -plugin-opt=-fresolution=/tmp/ccL4xmwq.res -plugin-opt=-pass-through=-lgcc_s -plugin-opt=-pass-through=-lgcc -plugin-opt=-pass-through=-lc -plugin-opt=-pass-through=-lgcc_s -plugin-opt=-pass-through=-lgcc --sysroot=/ --build-id --eh-frame-hdr -m elf_x86_64 --hash-style=gnu --as-needed -export-dynamic -dynamic-linker /lib64/ld-linux-x86-64.so.2 -pie -z now -z relro -o cmTC_5100f /usr/lib/gcc/x86_64-linux-gnu/7/../../../x86_64-linux-gnu/Scrt1.o /usr/lib/gcc/x86_64-linux-gnu/7/../../../x86_64-linux-gnu/crti.o /usr/lib/gcc/x86_64-linux-gnu/7/crtbeginS.o -L/usr/lib/gcc/x86_64-linux-gnu/7 -L/usr/lib/gcc/x86_64-linux-gnu/7/../../../x86_64-linux-gnu -L/usr/lib/gcc/x86_64-linux-gnu/7/../../../../lib -L/lib/x86_64-linux-gnu -L/lib/../lib -L/usr/lib/x86_64-linux-gnu -L/usr/lib/../lib -L/usr/local/cuda/lib64/stubs -L/usr/lib/gcc/x86_64-linux-gnu/7/../../.. CMakeFiles/cmTC_5100f.dir/CMakeCXXCompilerABI.cpp.o -lstdc++ -lm -lgcc_s -lgcc -lc -lgcc_s -lgcc /usr/lib/gcc/x86_64-linux-gnu/7/crtendS.o /usr/lib/gcc/x86_64-linux-gnu/7/../../../x86_64-linux-gnu/crtn.o
       COLLECT_GCC_OPTIONS='-v' '-rdynamic' '-o' 'cmTC_5100f' '-shared-libgcc' '-mtune=generic' '-march=x86-64'
       make[1]: Leaving directory '/warp-ctc/build/CMakeFiles/CMakeTmp'


       Parsed CXX implicit link information from above output:
         link line regex: [^( *|.*[/\])(ld|CMAKE_LINK_STARTFILE-NOTFOUND|([^/\]+-)?ld|collect2)[^/\]*( |$)]
         ignore line: [Change Dir: /warp-ctc/build/CMakeFiles/CMakeTmp]
         ignore line: []
         ignore line: [Run Build Command:"/usr/bin/make" "cmTC_5100f/fast"]
         ignore line: [/usr/bin/make -f CMakeFiles/cmTC_5100f.dir/build.make CMakeFiles/cmTC_5100f.dir/build]
         ignore line: [make[1]: Entering directory '/warp-ctc/build/CMakeFiles/CMakeTmp']
         ignore line: [Building CXX object CMakeFiles/cmTC_5100f.dir/CMakeCXXCompilerABI.cpp.o]
         ignore line: [/usr/bin/c++     -o CMakeFiles/cmTC_5100f.dir/CMakeCXXCompilerABI.cpp.o -c /usr/share/cmake-3.10/Modules/CMakeCXXCompilerABI.cpp]
         ignore line: [Linking CXX executable cmTC_5100f]
         ignore line: [/usr/bin/cmake -E cmake_link_script CMakeFiles/cmTC_5100f.dir/link.txt --verbose=1]
         ignore line: [/usr/bin/c++      -v -rdynamic CMakeFiles/cmTC_5100f.dir/CMakeCXXCompilerABI.cpp.o  -o cmTC_5100f ]
         ignore line: [Using built-in specs.]
         ignore line: [COLLECT_GCC=/usr/bin/c++]
         ignore line: [COLLECT_LTO_WRAPPER=/usr/lib/gcc/x86_64-linux-gnu/7/lto-wrapper]
         ignore line: [OFFLOAD_TARGET_NAMES=nvptx-none]
         ignore line: [OFFLOAD_TARGET_DEFAULT=1]
         ignore line: [Target: x86_64-linux-gnu]
         ignore line: [Configured with: ../src/configure -v --with-pkgversion='Ubuntu 7.4.0-1ubuntu1~18.04.1' --with-bugurl=file:///usr/share/doc/gcc-7/README.Bugs --enable-languages=c,ada,c++,go,brig,d,fortran,objc,obj-c++ --prefix=/usr --with-gcc-major-version-only --program-suffix=-7 --program-prefix=x86_64-linux-gnu- --enable-shared --enable-linker-build-id --libexecdir=/usr/lib --without-included-gettext --enable-threads=posix --libdir=/usr/lib --enable-nls --with-sysroot=/ --enable-clocale=gnu --enable-libstdcxx-debug --enable-libstdcxx-time=yes --with-default-libstdcxx-abi=new --enable-gnu-unique-object --disable-vtable-verify --enable-libmpx --enable-plugin --enable-default-pie --with-system-zlib --with-target-system-zlib --enable-objc-gc=auto --enable-multiarch --disable-werror --with-arch-32=i686 --with-abi=m64 --with-multilib-list=m32,m64,mx32 --enable-multilib --with-tune=generic --enable-offload-targets=nvptx-none --without-cuda-driver --enable-checking=release --build=x86_64-linux-gnu --host=x86_64-linux-gnu --target=x86_64-linux-gnu]
         ignore line: [Thread model: posix]
         ignore line: [gcc version 7.4.0 (Ubuntu 7.4.0-1ubuntu1~18.04.1) ]
         ignore line: [COMPILER_PATH=/usr/lib/gcc/x86_64-linux-gnu/7/:/usr/lib/gcc/x86_64-linux-gnu/7/:/usr/lib/gcc/x86_64-linux-gnu/:/usr/lib/gcc/x86_64-linux-gnu/7/:/usr/lib/gcc/x86_64-linux-gnu/]
         ignore line: [LIBRARY_PATH=/usr/lib/gcc/x86_64-linux-gnu/7/:/usr/lib/gcc/x86_64-linux-gnu/7/../../../x86_64-linux-gnu/:/usr/lib/gcc/x86_64-linux-gnu/7/../../../../lib/:/lib/x86_64-linux-gnu/:/lib/../lib/:/usr/lib/x86_64-linux-gnu/:/usr/lib/../lib/:/usr/local/cuda/lib64/stubs/:/usr/lib/gcc/x86_64-linux-gnu/7/../../../:/lib/:/usr/lib/]
         ignore line: [COLLECT_GCC_OPTIONS='-v' '-rdynamic' '-o' 'cmTC_5100f' '-shared-libgcc' '-mtune=generic' '-march=x86-64']
         link line: [ /usr/lib/gcc/x86_64-linux-gnu/7/collect2 -plugin /usr/lib/gcc/x86_64-linux-gnu/7/liblto_plugin.so -plugin-opt=/usr/lib/gcc/x86_64-linux-gnu/7/lto-wrapper -plugin-opt=-fresolution=/tmp/ccL4xmwq.res -plugin-opt=-pass-through=-lgcc_s -plugin-opt=-pass-through=-lgcc -plugin-opt=-pass-through=-lc -plugin-opt=-pass-through=-lgcc_s -plugin-opt=-pass-through=-lgcc --sysroot=/ --build-id --eh-frame-hdr -m elf_x86_64 --hash-style=gnu --as-needed -export-dynamic -dynamic-linker /lib64/ld-linux-x86-64.so.2 -pie -z now -z relro -o cmTC_5100f /usr/lib/gcc/x86_64-linux-gnu/7/../../../x86_64-linux-gnu/Scrt1.o /usr/lib/gcc/x86_64-linux-gnu/7/../../../x86_64-linux-gnu/crti.o /usr/lib/gcc/x86_64-linux-gnu/7/crtbeginS.o -L/usr/lib/gcc/x86_64-linux-gnu/7 -L/usr/lib/gcc/x86_64-linux-gnu/7/../../../x86_64-linux-gnu -L/usr/lib/gcc/x86_64-linux-gnu/7/../../../../lib -L/lib/x86_64-linux-gnu -L/lib/../lib -L/usr/lib/x86_64-linux-gnu -L/usr/lib/../lib -L/usr/local/cuda/lib64/stubs -L/usr/lib/gcc/x86_64-linux-gnu/7/../../.. CMakeFiles/cmTC_5100f.dir/CMakeCXXCompilerABI.cpp.o -lstdc++ -lm -lgcc_s -lgcc -lc -lgcc_s -lgcc /usr/lib/gcc/x86_64-linux-gnu/7/crtendS.o /usr/lib/gcc/x86_64-linux-gnu/7/../../../x86_64-linux-gnu/crtn.o]
           arg [/usr/lib/gcc/x86_64-linux-gnu/7/collect2] ==> ignore
           arg [-plugin] ==> ignore
           arg [/usr/lib/gcc/x86_64-linux-gnu/7/liblto_plugin.so] ==> ignore
           arg [-plugin-opt=/usr/lib/gcc/x86_64-linux-gnu/7/lto-wrapper] ==> ignore
           arg [-plugin-opt=-fresolution=/tmp/ccL4xmwq.res] ==> ignore
           arg [-plugin-opt=-pass-through=-lgcc_s] ==> ignore
           arg [-plugin-opt=-pass-through=-lgcc] ==> ignore
           arg [-plugin-opt=-pass-through=-lc] ==> ignore
           arg [-plugin-opt=-pass-through=-lgcc_s] ==> ignore
           arg [-plugin-opt=-pass-through=-lgcc] ==> ignore
           arg [--sysroot=/] ==> ignore
           arg [--build-id] ==> ignore
           arg [--eh-frame-hdr] ==> ignore
           arg [-m] ==> ignore
           arg [elf_x86_64] ==> ignore
           arg [--hash-style=gnu] ==> ignore
           arg [--as-needed] ==> ignore
           arg [-export-dynamic] ==> ignore
           arg [-dynamic-linker] ==> ignore
           arg [/lib64/ld-linux-x86-64.so.2] ==> ignore
           arg [-pie] ==> ignore
           arg [-znow] ==> ignore
           arg [-zrelro] ==> ignore
           arg [-o] ==> ignore
           arg [cmTC_5100f] ==> ignore
           arg [/usr/lib/gcc/x86_64-linux-gnu/7/../../../x86_64-linux-gnu/Scrt1.o] ==> ignore
           arg [/usr/lib/gcc/x86_64-linux-gnu/7/../../../x86_64-linux-gnu/crti.o] ==> ignore
           arg [/usr/lib/gcc/x86_64-linux-gnu/7/crtbeginS.o] ==> ignore
           arg [-L/usr/lib/gcc/x86_64-linux-gnu/7] ==> dir [/usr/lib/gcc/x86_64-linux-gnu/7]
           arg [-L/usr/lib/gcc/x86_64-linux-gnu/7/../../../x86_64-linux-gnu] ==> dir [/usr/lib/gcc/x86_64-linux-gnu/7/../../../x86_64-linux-gnu]
           arg [-L/usr/lib/gcc/x86_64-linux-gnu/7/../../../../lib] ==> dir [/usr/lib/gcc/x86_64-linux-gnu/7/../../../../lib]
           arg [-L/lib/x86_64-linux-gnu] ==> dir [/lib/x86_64-linux-gnu]
           arg [-L/lib/../lib] ==> dir [/lib/../lib]
           arg [-L/usr/lib/x86_64-linux-gnu] ==> dir [/usr/lib/x86_64-linux-gnu]
           arg [-L/usr/lib/../lib] ==> dir [/usr/lib/../lib]
           arg [-L/usr/local/cuda/lib64/stubs] ==> dir [/usr/local/cuda/lib64/stubs]
           arg [-L/usr/lib/gcc/x86_64-linux-gnu/7/../../..] ==> dir [/usr/lib/gcc/x86_64-linux-gnu/7/../../..]
           arg [CMakeFiles/cmTC_5100f.dir/CMakeCXXCompilerABI.cpp.o] ==> ignore
           arg [-lstdc++] ==> lib [stdc++]
           arg [-lm] ==> lib [m]
           arg [-lgcc_s] ==> lib [gcc_s]
           arg [-lgcc] ==> lib [gcc]
           arg [-lc] ==> lib [c]
           arg [-lgcc_s] ==> lib [gcc_s]
           arg [-lgcc] ==> lib [gcc]
           arg [/usr/lib/gcc/x86_64-linux-gnu/7/crtendS.o] ==> ignore
           arg [/usr/lib/gcc/x86_64-linux-gnu/7/../../../x86_64-linux-gnu/crtn.o] ==> ignore
         collapse library dir [/usr/lib/gcc/x86_64-linux-gnu/7] ==> [/usr/lib/gcc/x86_64-linux-gnu/7]
         collapse library dir [/usr/lib/gcc/x86_64-linux-gnu/7/../../../x86_64-linux-gnu] ==> [/usr/lib/x86_64-linux-gnu]
         collapse library dir [/usr/lib/gcc/x86_64-linux-gnu/7/../../../../lib] ==> [/usr/lib]
         collapse library dir [/lib/x86_64-linux-gnu] ==> [/lib/x86_64-linux-gnu]
         collapse library dir [/lib/../lib] ==> [/lib]
         collapse library dir [/usr/lib/x86_64-linux-gnu] ==> [/usr/lib/x86_64-linux-gnu]
         collapse library dir [/usr/lib/../lib] ==> [/usr/lib]
         collapse library dir [/usr/local/cuda/lib64/stubs] ==> [/usr/local/cuda/lib64/stubs]
         collapse library dir [/usr/lib/gcc/x86_64-linux-gnu/7/../../..] ==> [/usr/lib]
         implicit libs: [stdc++;m;gcc_s;gcc;c;gcc_s;gcc]
         implicit dirs: [/usr/lib/gcc/x86_64-linux-gnu/7;/usr/lib/x86_64-linux-gnu;/usr/lib;/lib/x86_64-linux-gnu;/lib;/usr/local/cuda/lib64/stubs]
         implicit fwks: []




       Detecting CXX [-std=c++1z] compiler features compiled with the following output:
       Change Dir: /warp-ctc/build/CMakeFiles/CMakeTmp

       Run Build Command:"/usr/bin/make" "cmTC_6ca2f/fast"
       /usr/bin/make -f CMakeFiles/cmTC_6ca2f.dir/build.make CMakeFiles/cmTC_6ca2f.dir/build
       make[1]: Entering directory '/warp-ctc/build/CMakeFiles/CMakeTmp'
       Building CXX object CMakeFiles/cmTC_6ca2f.dir/feature_tests.cxx.o
       /usr/bin/c++    -std=c++1z -o CMakeFiles/cmTC_6ca2f.dir/feature_tests.cxx.o -c /warp-ctc/build/CMakeFiles/feature_tests.cxx
       Linking CXX executable cmTC_6ca2f
       /usr/bin/cmake -E cmake_link_script CMakeFiles/cmTC_6ca2f.dir/link.txt --verbose=1
       /usr/bin/c++       -rdynamic CMakeFiles/cmTC_6ca2f.dir/feature_tests.cxx.o  -o cmTC_6ca2f 
       make[1]: Leaving directory '/warp-ctc/build/CMakeFiles/CMakeTmp'


           Feature record: CXX_FEATURE:1cxx_aggregate_default_initializers
           Feature record: CXX_FEATURE:1cxx_alias_templates
           Feature record: CXX_FEATURE:1cxx_alignas
           Feature record: CXX_FEATURE:1cxx_alignof
           Feature record: CXX_FEATURE:1cxx_attributes
           Feature record: CXX_FEATURE:1cxx_attribute_deprecated
           Feature record: CXX_FEATURE:1cxx_auto_type
           Feature record: CXX_FEATURE:1cxx_binary_literals
           Feature record: CXX_FEATURE:1cxx_constexpr
           Feature record: CXX_FEATURE:1cxx_contextual_conversions
           Feature record: CXX_FEATURE:1cxx_decltype
           Feature record: CXX_FEATURE:1cxx_decltype_auto
           Feature record: CXX_FEATURE:1cxx_decltype_incomplete_return_types
           Feature record: CXX_FEATURE:1cxx_default_function_template_args
           Feature record: CXX_FEATURE:1cxx_defaulted_functions
           Feature record: CXX_FEATURE:1cxx_defaulted_move_initializers
           Feature record: CXX_FEATURE:1cxx_delegating_constructors
           Feature record: CXX_FEATURE:1cxx_deleted_functions
           Feature record: CXX_FEATURE:1cxx_digit_separators
           Feature record: CXX_FEATURE:1cxx_enum_forward_declarations
           Feature record: CXX_FEATURE:1cxx_explicit_conversions
           Feature record: CXX_FEATURE:1cxx_extended_friend_declarations
           Feature record: CXX_FEATURE:1cxx_extern_templates
           Feature record: CXX_FEATURE:1cxx_final
           Feature record: CXX_FEATURE:1cxx_func_identifier
           Feature record: CXX_FEATURE:1cxx_generalized_initializers
           Feature record: CXX_FEATURE:1cxx_generic_lambdas
           Feature record: CXX_FEATURE:1cxx_inheriting_constructors
           Feature record: CXX_FEATURE:1cxx_inline_namespaces
           Feature record: CXX_FEATURE:1cxx_lambdas
           Feature record: CXX_FEATURE:1cxx_lambda_init_captures
           Feature record: CXX_FEATURE:1cxx_local_type_template_args
           Feature record: CXX_FEATURE:1cxx_long_long_type
           Feature record: CXX_FEATURE:1cxx_noexcept
           Feature record: CXX_FEATURE:1cxx_nonstatic_member_init
           Feature record: CXX_FEATURE:1cxx_nullptr
           Feature record: CXX_FEATURE:1cxx_override
           Feature record: CXX_FEATURE:1cxx_range_for
           Feature record: CXX_FEATURE:1cxx_raw_string_literals
           Feature record: CXX_FEATURE:1cxx_reference_qualified_functions
           Feature record: CXX_FEATURE:1cxx_relaxed_constexpr
           Feature record: CXX_FEATURE:1cxx_return_type_deduction
           Feature record: CXX_FEATURE:1cxx_right_angle_brackets
           Feature record: CXX_FEATURE:1cxx_rvalue_references
           Feature record: CXX_FEATURE:1cxx_sizeof_member
           Feature record: CXX_FEATURE:1cxx_static_assert
           Feature record: CXX_FEATURE:1cxx_strong_enums
           Feature record: CXX_FEATURE:1cxx_template_template_parameters
           Feature record: CXX_FEATURE:1cxx_thread_local
           Feature record: CXX_FEATURE:1cxx_trailing_return_types
           Feature record: CXX_FEATURE:1cxx_unicode_literals
           Feature record: CXX_FEATURE:1cxx_uniform_initialization
           Feature record: CXX_FEATURE:1cxx_unrestricted_unions
           Feature record: CXX_FEATURE:1cxx_user_literals
           Feature record: CXX_FEATURE:1cxx_variable_templates
           Feature record: CXX_FEATURE:1cxx_variadic_macros
           Feature record: CXX_FEATURE:1cxx_variadic_templates


       Detecting CXX [-std=c++14] compiler features compiled with the following output:
       Change Dir: /warp-ctc/build/CMakeFiles/CMakeTmp

       Run Build Command:"/usr/bin/make" "cmTC_6b556/fast"
       /usr/bin/make -f CMakeFiles/cmTC_6b556.dir/build.make CMakeFiles/cmTC_6b556.dir/build
       make[1]: Entering directory '/warp-ctc/build/CMakeFiles/CMakeTmp'
       Building CXX object CMakeFiles/cmTC_6b556.dir/feature_tests.cxx.o
       /usr/bin/c++    -std=c++14 -o CMakeFiles/cmTC_6b556.dir/feature_tests.cxx.o -c /warp-ctc/build/CMakeFiles/feature_tests.cxx
       Linking CXX executable cmTC_6b556
       /usr/bin/cmake -E cmake_link_script CMakeFiles/cmTC_6b556.dir/link.txt --verbose=1
       /usr/bin/c++       -rdynamic CMakeFiles/cmTC_6b556.dir/feature_tests.cxx.o  -o cmTC_6b556 
       make[1]: Leaving directory '/warp-ctc/build/CMakeFiles/CMakeTmp'


           Feature record: CXX_FEATURE:1cxx_aggregate_default_initializers
           Feature record: CXX_FEATURE:1cxx_alias_templates
           Feature record: CXX_FEATURE:1cxx_alignas
           Feature record: CXX_FEATURE:1cxx_alignof
           Feature record: CXX_FEATURE:1cxx_attributes
           Feature record: CXX_FEATURE:1cxx_attribute_deprecated
           Feature record: CXX_FEATURE:1cxx_auto_type
           Feature record: CXX_FEATURE:1cxx_binary_literals
           Feature record: CXX_FEATURE:1cxx_constexpr
           Feature record: CXX_FEATURE:1cxx_contextual_conversions
           Feature record: CXX_FEATURE:1cxx_decltype
           Feature record: CXX_FEATURE:1cxx_decltype_auto
           Feature record: CXX_FEATURE:1cxx_decltype_incomplete_return_types
           Feature record: CXX_FEATURE:1cxx_default_function_template_args
           Feature record: CXX_FEATURE:1cxx_defaulted_functions
           Feature record: CXX_FEATURE:1cxx_defaulted_move_initializers
           Feature record: CXX_FEATURE:1cxx_delegating_constructors
           Feature record: CXX_FEATURE:1cxx_deleted_functions
           Feature record: CXX_FEATURE:1cxx_digit_separators
           Feature record: CXX_FEATURE:1cxx_enum_forward_declarations
           Feature record: CXX_FEATURE:1cxx_explicit_conversions
           Feature record: CXX_FEATURE:1cxx_extended_friend_declarations
           Feature record: CXX_FEATURE:1cxx_extern_templates
           Feature record: CXX_FEATURE:1cxx_final
           Feature record: CXX_FEATURE:1cxx_func_identifier
           Feature record: CXX_FEATURE:1cxx_generalized_initializers
           Feature record: CXX_FEATURE:1cxx_generic_lambdas
           Feature record: CXX_FEATURE:1cxx_inheriting_constructors
           Feature record: CXX_FEATURE:1cxx_inline_namespaces
           Feature record: CXX_FEATURE:1cxx_lambdas
           Feature record: CXX_FEATURE:1cxx_lambda_init_captures
           Feature record: CXX_FEATURE:1cxx_local_type_template_args
           Feature record: CXX_FEATURE:1cxx_long_long_type
           Feature record: CXX_FEATURE:1cxx_noexcept
           Feature record: CXX_FEATURE:1cxx_nonstatic_member_init
           Feature record: CXX_FEATURE:1cxx_nullptr
           Feature record: CXX_FEATURE:1cxx_override
           Feature record: CXX_FEATURE:1cxx_range_for
           Feature record: CXX_FEATURE:1cxx_raw_string_literals
           Feature record: CXX_FEATURE:1cxx_reference_qualified_functions
           Feature record: CXX_FEATURE:1cxx_relaxed_constexpr
           Feature record: CXX_FEATURE:1cxx_return_type_deduction
           Feature record: CXX_FEATURE:1cxx_right_angle_brackets
           Feature record: CXX_FEATURE:1cxx_rvalue_references
           Feature record: CXX_FEATURE:1cxx_sizeof_member
           Feature record: CXX_FEATURE:1cxx_static_assert
           Feature record: CXX_FEATURE:1cxx_strong_enums
           Feature record: CXX_FEATURE:1cxx_template_template_parameters
           Feature record: CXX_FEATURE:1cxx_thread_local
           Feature record: CXX_FEATURE:1cxx_trailing_return_types
           Feature record: CXX_FEATURE:1cxx_unicode_literals
           Feature record: CXX_FEATURE:1cxx_uniform_initialization
           Feature record: CXX_FEATURE:1cxx_unrestricted_unions
           Feature record: CXX_FEATURE:1cxx_user_literals
           Feature record: CXX_FEATURE:1cxx_variable_templates
           Feature record: CXX_FEATURE:1cxx_variadic_macros
           Feature record: CXX_FEATURE:1cxx_variadic_templates


       Detecting CXX [-std=c++11] compiler features compiled with the following output:
       Change Dir: /warp-ctc/build/CMakeFiles/CMakeTmp

       Run Build Command:"/usr/bin/make" "cmTC_2af09/fast"
       /usr/bin/make -f CMakeFiles/cmTC_2af09.dir/build.make CMakeFiles/cmTC_2af09.dir/build
       make[1]: Entering directory '/warp-ctc/build/CMakeFiles/CMakeTmp'
       Building CXX object CMakeFiles/cmTC_2af09.dir/feature_tests.cxx.o
       /usr/bin/c++    -std=c++11 -o CMakeFiles/cmTC_2af09.dir/feature_tests.cxx.o -c /warp-ctc/build/CMakeFiles/feature_tests.cxx
       Linking CXX executable cmTC_2af09
       /usr/bin/cmake -E cmake_link_script CMakeFiles/cmTC_2af09.dir/link.txt --verbose=1
       /usr/bin/c++       -rdynamic CMakeFiles/cmTC_2af09.dir/feature_tests.cxx.o  -o cmTC_2af09 
       make[1]: Leaving directory '/warp-ctc/build/CMakeFiles/CMakeTmp'


           Feature record: CXX_FEATURE:0cxx_aggregate_default_initializers
           Feature record: CXX_FEATURE:1cxx_alias_templates
           Feature record: CXX_FEATURE:1cxx_alignas
           Feature record: CXX_FEATURE:1cxx_alignof
           Feature record: CXX_FEATURE:1cxx_attributes
           Feature record: CXX_FEATURE:0cxx_attribute_deprecated
           Feature record: CXX_FEATURE:1cxx_auto_type
           Feature record: CXX_FEATURE:0cxx_binary_literals
           Feature record: CXX_FEATURE:1cxx_constexpr
           Feature record: CXX_FEATURE:0cxx_contextual_conversions
           Feature record: CXX_FEATURE:1cxx_decltype
           Feature record: CXX_FEATURE:0cxx_decltype_auto
           Feature record: CXX_FEATURE:1cxx_decltype_incomplete_return_types
           Feature record: CXX_FEATURE:1cxx_default_function_template_args
           Feature record: CXX_FEATURE:1cxx_defaulted_functions
           Feature record: CXX_FEATURE:1cxx_defaulted_move_initializers
           Feature record: CXX_FEATURE:1cxx_delegating_constructors
           Feature record: CXX_FEATURE:1cxx_deleted_functions
           Feature record: CXX_FEATURE:0cxx_digit_separators
           Feature record: CXX_FEATURE:1cxx_enum_forward_declarations
           Feature record: CXX_FEATURE:1cxx_explicit_conversions
           Feature record: CXX_FEATURE:1cxx_extended_friend_declarations
           Feature record: CXX_FEATURE:1cxx_extern_templates
           Feature record: CXX_FEATURE:1cxx_final
           Feature record: CXX_FEATURE:1cxx_func_identifier
           Feature record: CXX_FEATURE:1cxx_generalized_initializers
           Feature record: CXX_FEATURE:0cxx_generic_lambdas
           Feature record: CXX_FEATURE:1cxx_inheriting_constructors
           Feature record: CXX_FEATURE:1cxx_inline_namespaces
           Feature record: CXX_FEATURE:1cxx_lambdas
           Feature record: CXX_FEATURE:0cxx_lambda_init_captures
           Feature record: CXX_FEATURE:1cxx_local_type_template_args
           Feature record: CXX_FEATURE:1cxx_long_long_type
           Feature record: CXX_FEATURE:1cxx_noexcept
           Feature record: CXX_FEATURE:1cxx_nonstatic_member_init
           Feature record: CXX_FEATURE:1cxx_nullptr
           Feature record: CXX_FEATURE:1cxx_override
           Feature record: CXX_FEATURE:1cxx_range_for
           Feature record: CXX_FEATURE:1cxx_raw_string_literals
           Feature record: CXX_FEATURE:1cxx_reference_qualified_functions
           Feature record: CXX_FEATURE:0cxx_relaxed_constexpr
           Feature record: CXX_FEATURE:0cxx_return_type_deduction
           Feature record: CXX_FEATURE:1cxx_right_angle_brackets
           Feature record: CXX_FEATURE:1cxx_rvalue_references
           Feature record: CXX_FEATURE:1cxx_sizeof_member
           Feature record: CXX_FEATURE:1cxx_static_assert
           Feature record: CXX_FEATURE:1cxx_strong_enums
           Feature record: CXX_FEATURE:1cxx_template_template_parameters
           Feature record: CXX_FEATURE:1cxx_thread_local
           Feature record: CXX_FEATURE:1cxx_trailing_return_types
           Feature record: CXX_FEATURE:1cxx_unicode_literals
           Feature record: CXX_FEATURE:1cxx_uniform_initialization
           Feature record: CXX_FEATURE:1cxx_unrestricted_unions
           Feature record: CXX_FEATURE:1cxx_user_literals
           Feature record: CXX_FEATURE:0cxx_variable_templates
           Feature record: CXX_FEATURE:1cxx_variadic_macros
           Feature record: CXX_FEATURE:1cxx_variadic_templates


       Detecting CXX [-std=c++98] compiler features compiled with the following output:
       Change Dir: /warp-ctc/build/CMakeFiles/CMakeTmp

       Run Build Command:"/usr/bin/make" "cmTC_b801b/fast"
       /usr/bin/make -f CMakeFiles/cmTC_b801b.dir/build.make CMakeFiles/cmTC_b801b.dir/build
       make[1]: Entering directory '/warp-ctc/build/CMakeFiles/CMakeTmp'
       Building CXX object CMakeFiles/cmTC_b801b.dir/feature_tests.cxx.o
       /usr/bin/c++    -std=c++98 -o CMakeFiles/cmTC_b801b.dir/feature_tests.cxx.o -c /warp-ctc/build/CMakeFiles/feature_tests.cxx
       Linking CXX executable cmTC_b801b
       /usr/bin/cmake -E cmake_link_script CMakeFiles/cmTC_b801b.dir/link.txt --verbose=1
       /usr/bin/c++       -rdynamic CMakeFiles/cmTC_b801b.dir/feature_tests.cxx.o  -o cmTC_b801b 
       make[1]: Leaving directory '/warp-ctc/build/CMakeFiles/CMakeTmp'


           Feature record: CXX_FEATURE:0cxx_aggregate_default_initializers
           Feature record: CXX_FEATURE:0cxx_alias_templates
           Feature record: CXX_FEATURE:0cxx_alignas
           Feature record: CXX_FEATURE:0cxx_alignof
           Feature record: CXX_FEATURE:0cxx_attributes
           Feature record: CXX_FEATURE:0cxx_attribute_deprecated
           Feature record: CXX_FEATURE:0cxx_auto_type
           Feature record: CXX_FEATURE:0cxx_binary_literals
           Feature record: CXX_FEATURE:0cxx_constexpr
           Feature record: CXX_FEATURE:0cxx_contextual_conversions
           Feature record: CXX_FEATURE:0cxx_decltype
           Feature record: CXX_FEATURE:0cxx_decltype_auto
           Feature record: CXX_FEATURE:0cxx_decltype_incomplete_return_types
           Feature record: CXX_FEATURE:0cxx_default_function_template_args
           Feature record: CXX_FEATURE:0cxx_defaulted_functions
           Feature record: CXX_FEATURE:0cxx_defaulted_move_initializers
           Feature record: CXX_FEATURE:0cxx_delegating_constructors
           Feature record: CXX_FEATURE:0cxx_deleted_functions
           Feature record: CXX_FEATURE:0cxx_digit_separators
           Feature record: CXX_FEATURE:0cxx_enum_forward_declarations
           Feature record: CXX_FEATURE:0cxx_explicit_conversions
           Feature record: CXX_FEATURE:0cxx_extended_friend_declarations
           Feature record: CXX_FEATURE:0cxx_extern_templates
           Feature record: CXX_FEATURE:0cxx_final
           Feature record: CXX_FEATURE:0cxx_func_identifier
           Feature record: CXX_FEATURE:0cxx_generalized_initializers
           Feature record: CXX_FEATURE:0cxx_generic_lambdas
           Feature record: CXX_FEATURE:0cxx_inheriting_constructors
           Feature record: CXX_FEATURE:0cxx_inline_namespaces
           Feature record: CXX_FEATURE:0cxx_lambdas
           Feature record: CXX_FEATURE:0cxx_lambda_init_captures
           Feature record: CXX_FEATURE:0cxx_local_type_template_args
           Feature record: CXX_FEATURE:0cxx_long_long_type
           Feature record: CXX_FEATURE:0cxx_noexcept
           Feature record: CXX_FEATURE:0cxx_nonstatic_member_init
           Feature record: CXX_FEATURE:0cxx_nullptr
           Feature record: CXX_FEATURE:0cxx_override
           Feature record: CXX_FEATURE:0cxx_range_for
           Feature record: CXX_FEATURE:0cxx_raw_string_literals
           Feature record: CXX_FEATURE:0cxx_reference_qualified_functions
           Feature record: CXX_FEATURE:0cxx_relaxed_constexpr
           Feature record: CXX_FEATURE:0cxx_return_type_deduction
           Feature record: CXX_FEATURE:0cxx_right_angle_brackets
           Feature record: CXX_FEATURE:0cxx_rvalue_references
           Feature record: CXX_FEATURE:0cxx_sizeof_member
           Feature record: CXX_FEATURE:0cxx_static_assert
           Feature record: CXX_FEATURE:0cxx_strong_enums
           Feature record: CXX_FEATURE:1cxx_template_template_parameters
           Feature record: CXX_FEATURE:0cxx_thread_local
           Feature record: CXX_FEATURE:0cxx_trailing_return_types
           Feature record: CXX_FEATURE:0cxx_unicode_literals
           Feature record: CXX_FEATURE:0cxx_uniform_initialization
           Feature record: CXX_FEATURE:0cxx_unrestricted_unions
           Feature record: CXX_FEATURE:0cxx_user_literals
           Feature record: CXX_FEATURE:0cxx_variable_templates
           Feature record: CXX_FEATURE:0cxx_variadic_macros
           Feature record: CXX_FEATURE:0cxx_variadic_templates


