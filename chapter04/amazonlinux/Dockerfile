FROM amazonlinux:2

RUN yum -y install sudo
RUN yum -y install shadow-utils

# sudo
RUN echo "%wheel  ALL=(ALL)  ALL" >> /etc/sudoers.d/wheel

# Root User
RUN echo 'root:password' | chpasswd

RUN useradd ec2-user
RUN gpasswd -a ec2-user wheel
RUN echo 'ec2-user:password' | chpasswd
RUN chown -R ec2-user /home/ec2-user/

USER ec2-user:ec2-user
WORKDIR /home/ec2-user
