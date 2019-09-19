FROM bluedata/centos7:latest
ENV port 11000 
ENV user bluedata 
ENV version 5.1.5
ENV data_dir /home/$user/data 

#RUN yum install -y http://download.fedoraproject.org//pub/epel/epel-release-latest-7.noarch.rpm
RUN yum -y install epel-release
RUN yum -y install https://centos7.iuscommunity.org/ius-release.rpm

RUN yum -y install sudo \
        yum -y install wget \
        yum -y install git \
        yum -y install zip \
        yum -y install unzip \
        yum -y install java-1.8.0-openjdk \
        yum -y install epel-release \
        yum -y install nginx \
        yum -y install freetype \
        yum -y install libgfortran \
        yum -y install libgomp \
        yum -y install python27 \
        yum -y install python27-devel \
        yum -y install python-devel \
        yum -y install python36u \
        yum -y install python36u-pip \
        yum -y install python36u-libs \
        yum -y install python36u-devel 
        

USER $user
WORKDIR /home/$user

# Download DSS, untar distribution and remove tar.gz file
RUN wget -q https://cdn.downloads.dataiku.com/public/dss/${version}/dataiku-dss-${version}.tar.gz
RUN tar xzf dataiku-dss-${version}.tar.gz
RUN rm -rf $version

# run DSS installer
RUN  dataiku-dss-${version}/installer.sh -d $data_dir -p $port

COPY ./dbPlugin.tar.gz .
RUN mkdir /home/$user/dataiku-dss-${version}/resources/plugins/dev
RUN tar xzvf ./dbPlugin.tar.gz -C /home/$user/dataiku-dss-${version}/resources/plugins/dev

USER root
 
