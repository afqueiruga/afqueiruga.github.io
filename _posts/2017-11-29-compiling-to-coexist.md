---
layout: post
title:  "Compiling TensorFlow"
date:   2017-11-28 22:30:22 -0800
categories: tensorflow
---

# Coexistence with other libraries

TensorFlow isn't really meant to be used like another library in a larger program. But, that's my mid game. My goal right now is to:

1. Compile TensorFlow locally and output a shared object.
2. Install it to an opt location to a) not clash with the two other installs of TF I have :eyerollemoji: and b) bundle it up with a larger statically deployable install.
3. Link to the .so from another program that uses cmake to call TF through the C API. (cmake is the most popular build system for scientific software.)

Right now I'm working on a Linux box. I'll update this with the OSX (are peopling saying macOS yet?) equivalents when I get there.

# Setting up the requirements

Following the bazel instructions for Ubuntu:
```bash
sudo apt-get install openjdk-8-jdk
echo "deb [arch=amd64] http://storage.googleapis.com/bazel-apt stable jdk1.8" | sudo tee /etc/apt/sources.list.d/bazel.list
curl https://bazel.build/bazel-release.pub.gpg | sudo apt-key add -
sudo apt-get update && sudo apt-get install bazel
```
 
Now I clone into TensorFlow in some local working directory,
```bash
git clone --recursive https://github.com/tensorflow/tensorflow
```
and dive in.

# Adding the .so target

I'm following [this guide by cjweeks](https://github.com/cjweeks/tensorflow-cmake). Into `tensorflow/BUILD`, we toss in at the end

```bash
# Added build rule
cc_binary(
    name = "libtensorflow_all.so",
    linkshared = 1,
    linkopts = ["-Wl,--version-script=tensorflow/tf_version_script.lds"], # Remove this line if you are using MacOS
    deps = [
        "//tensorflow/core:framework_internal",
        "//tensorflow/core:tensorflow",
        "//tensorflow/cc:cc_ops",
        "//tensorflow/cc:client_session",
        "//tensorflow/cc:scope",
        "//tensorflow/c:c_api",
    ],
)
```

# Configure it

A subtlety to the TensorFlow build process is that it doesn't actually install it. This is the rundown:

1. Answer the questions in the `./configure` script (no command line options)
2. Run the `bazel` build process for the target
3. Install it with `pip`.

which is different from the usual `./configure --prefix=/opt ; make install` we're familiar with. 

TODO: Add arguments to configure and configure.py

cjweek has a build.sh. But, this is a cmake project, so we have should probably have a `CMakeLists.txt`.

The process is:
```bash
./configure # User input needed
bazel build tensorflow:libtensorflow_all.so
copy what we want
```

