FROM ubuntu:22.04

ARG ECCODES_VERSION=2.35.0

WORKDIR /app

ADD https://confluence.ecmwf.int/download/attachments/45757960/eccodes-${ECCODES_VERSION}-Source.tar.gz?api=v2 \
  /usr/local/

RUN apt-get update && apt-get install -y \
  software-properties-common \
  && add-apt-repository -y ppa:ubuntugis/ppa \
  && apt-get update && apt-get install -y \
  gdal-bin \
  cmake \
  gcc \
  gfortran \
  python3 \
  python3-idna \
  python3-dev \
  python3-pip \
  python3-gdal \
  python3-six 

RUN cd /usr/local/ && tar -xzf eccodes-${ECCODES_VERSION}-Source.tar.gz \
  && mkdir build && cd build \
  && cmake -DENABLE_PYTHON=ON /usr/local/eccodes-${ECCODES_VERSION}-Source -DENABLE_AEC=OFF \
  && make \
  && make install \
  && rm -r /usr/local/eccodes-${ECCODES_VERSION}-Source.tar.gz /usr/local/eccodes-${ECCODES_VERSION}-Source \
  && cd /app

RUN pip3 install --no-cache-dir "numpy>=1.18.5,<2" matplotlib scipy pandas requests dnspython eccodes GDAL cdsapi
