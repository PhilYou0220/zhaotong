FROM			# 基础镜镜像，一切从这里开始构建 一般开始以 scar
MAINTAINER		# 镜像是谁写的，姓名+邮箱Phil<1299>
RUN				# 镜像构建的时候需要运行的命令
ADD				# 添加压缩包如nginx 会自动解压 ADD 支持添加远程url和自动提取压缩格式的文件，COPY 只允许从本机中复制文件
WORKDIR			# 镜像的工作目录
VOLUME         	# 挂载的目录 host目录
EXPOSE          # 暴露给外界端口配置 有点像-p
CMD 			# 指定这个容器启动的时候要运行的命令,只有最后一个会生效，可被替代
ENTRYPOINT		# 指定这个容器启动的时候要运行的命令,可以追加命令
ONBUILD			# 当构建一个被继承 DockerFile这个时候就会运行ONBUILD的指令。触发指令。
COPY			# 类似ADD ，将我们文件拷贝到镜像中 ，如果是相对路径，则是目标文件与Dockerfile的相对路径，
ENV 			# 构建的时候设置环境变量

- Dockerfile示例
FROM python:3.9-slim-buster
WORKDIR /usr/local/zhaotong
COPY  . /usr/local/zhaotong
COPY requirements.txt requirements.txt
RUN pip3  install --trusted-host mirrors.aliyun.com --no-cache-dir -i http://mirrors.aliyun.com/pypi/simple  -r requirements.txt
CMD ["python", "single_api_runall.py"]




- 构建镜像 使用当前目录的 Dockerfile 创建镜像，标签为 philyou/zhaotong:v1  账号/imagename:tag
docker build -t  philyou/study_work:v1 .

- 登录dockerhub
docker login -u philyou

- 登出dockerhub
docker logout

- 推送镜像到dockerhub
docker push philyou/study_work:v1

- 从dockerhub拉去镜像
docker pull philyou/study_work:v1

- 进入容器内部
docker exex -it  philyou/study_work:v1 /bin/bash

- jenkins运行容器命令
- -d：后台运行容器；
- -p 9001:8080：将容器的 8080 端口映射到服务器的 9001端口；
- -p 50000:50000：将容器的 50000 端口映射到服务器的 50000 端口 好像与jenkins相关；
- -v /usr/local/jenkins:/var/jenkins_home：将容器中 Jenkins 的工作目录挂载到服务器的 /usr/local/jenkins；
  -v /usr/bin/docker:/usr/bin/docker \  # 文件挂载 使用同一个客户端
  -v /var/run/docker.sock://var/run/docker.sock \ # 文件挂载 使用同一个socket
   -u root \ 给予Jenkins root的权限
- -v /etc/localtime:/etc/localtime：让容器使用和服务器同样的时间设置；
--restart=always：设置容器的重启策略为 Docker 重启时自动重启；
--name=jenkins：给容器起别名
- jenkins/jenkins：镜像名称

docker run -d \
    -p 9001:8080 \
    -p 50000:50000 \
    -v /usr/local/jenkins:/var/jenkins_home \
    -v /usr/bin/docker:/usr/bin/docker \
    -v /var/run/docker.sock:/var/run/docker.sock \
    -u root \
    -v /etc/localtime:/etc/localtime \
    --restart=always \
    --name=jenkins \
    jenkins/jenkins

mkdir -p allure-result && chmod 777 allure-result

- 构建后命令 把容器里生成的json和text挂载到jenkins里的工作空间里
docker run  \
	-v /usr/local/jenkins/workspace/$JOB_NAME/allure-result:/usr/local/zhaotong/report/temp_jsonreport \
	philyou/study_work:v1

docker run -d \
    -p 9001:8080 \
    -p 50000:50000 \
    -v /usr/local/jenkins:/var/jenkins_home \
    -v /usr/bin/docker:/usr/bin/docker \
    -v /var/run/docker.sock:/var/run/docker.sock \
    -v /usr/local/python3.9/bin/python3: /usr/local/python3.9/bin/python3 \
    -v /python_project/zhaotong: /python_project/zhaotong \
    -v /usr/local/allure/allure-2.18.1/bin/allure:/usr/local/allure/allure-2.18.1/bin/allure \
    -v /etc/localtime:/etc/localtime \
    -u root \
    --restart=always \
    --name=jenkins \
    jenkins/jenkins


docker -v /usr/local/python3.9/bin/python3: /usr/local/python3.9/bin/python3 \ jenkins/jenkins