# Download base image ubuntu 22.04
FROM ubuntu:22.04

# Disable Prompt During Packages Installation
ARG DEBIAN_FRONTEND=noninteractive

# Install the key packages
RUN apt-get -y update && apt-get install -y cmake git gcc g++ clang default-jdk python3-dev python3-pip wget net-tools dnsutils iputils-ping iputils-tracepath iputils-arping iputils-clockdiff inetutils-traceroute emacs vim libzmq3-dev protobuf-compiler

# Upgrade pip to the latest version
RUN python3 -m pip install --upgrade pip

# Install any python packages
RUN python3 -m pip install --upgrade grpcio grpcio-tools

WORKDIR /work

# Copy all of the files and directories from current directory
# to the current directory within the container
COPY . .