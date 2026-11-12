FROM debian:bookworm-slim

# Durante se instala se quitan las interacciones
ENV DEBIAN_FRONTEND=noninteractive

# Se instalan las dependencias necesarias para Hadoop y SSH
RUN apt-get update && apt-get install -y \
    openjdk-17-jdk-headless \
    python3 \
    openssh-server \
    wget \
    && rm -rf /var/lib/apt/lists/*

# Defino variables de entorno para Java y Hadoop
ENV JAVA_HOME=/usr/lib/jvm/java-17-openjdk-amd64
ENV HADOOP_VERSION=3.3.6
ENV HADOOP_HOME=/opt/hadoop
ENV PATH=$PATH:$HADOOP_HOME/bin:$HADOOP_HOME/sbin

# Se descarga e instala Hadoop
RUN wget -q https://archive.apache.org/dist/hadoop/common/hadoop-${HADOOP_VERSION}/hadoop-${HADOOP_VERSION}.tar.gz && \
    tar -xzf hadoop-${HADOOP_VERSION}.tar.gz -C /opt/ && \
    mv /opt/hadoop-${HADOOP_VERSION} /opt/hadoop && \
    rm hadoop-${HADOOP_VERSION}.tar.gz

# Configuracion de SSH sin contraseña
RUN ssh-keygen -t rsa -P '' -f ~/.ssh/id_rsa && \
    cat ~/.ssh/id_rsa.pub >> ~/.ssh/authorized_keys && \
    chmod 0600 ~/.ssh/authorized_keys

# Configurar el demonio sshd para evitar prompts de host
RUN mkdir -p /run/sshd && \
    echo "StrictHostKeyChecking no" >> /etc/ssh/ssh_config && \
    echo "PermitRootLogin yes" >> /etc/ssh/sshd_config

# Crear las carpetas de datos para montar el volumen del CSV
RUN mkdir -p /data/input /data/output

# Iniciar el servicio SSH y mantener el contenedor en ejecucion
CMD ["/bin/bash", "-c", "service ssh start && tail -f /dev/null"]