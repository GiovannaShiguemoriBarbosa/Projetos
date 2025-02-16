chmod 400 <private_key_file>

ssh -i <private_key_file> ubuntu@<public-ip-address>

sudo apt update

sudo apt install openjdk-21-jdk -y

java -version
javac -version

sudo nano /etc/environment

JAVA_HOME=/usr/lib/jvm/java-21-openjdk-amd64

source /etc/environment

sudo addgroup hadoop
sudo adduser --ingroup hadoop hadoop

sudo adduser hadoop sudo

sudo apt install openssh-server -y

sudo su - hadoop
ssh-keygen -t rsa -P '' -f ~/.ssh/id_rsa

cat ~/.ssh/id_rsa.pub >> ~/.ssh/authorized_keys
chmod 0600 ~/.ssh/authorized_keys

wget https://dlcdn.apache.org/hadoop/common/hadoop-3.3.6/hadoop-3.3.6.tar.gz

tar xzf hadoop-3.3.6.tar.gz

sudo mv hadoop-3.3.6 /usr/local/hadoop

sudo chown -R hadoop:hadoop /usr/local/hadoop

sudo nano /usr/local/hadoop/etc/hadoop/hadoop-env.sh

export JAVA_HOME=/usr/lib/jvm/java-21-openjdk-amd64

sudo nano /usr/local/hadoop/etc/hadoop/core-site.xml

<property>
    <name>fs.defaultFS</name>
    <value>hdfs://localhost:9000</value>
</property>
<property>
    <name>hadoop.tmp.dir</name>
    <value>/home/hadoop/tmp</value>
</property>

sudo nano /usr/local/hadoop/etc/hadoop/hdfs-site.xml

<property>
    <name>dfs.replication</name>
    <value>1</value>
</property>
<property>
    <name>dfs.namenode.name.dir</name>
    <value>/home/hadoop/dfs/name</value>
</property>
<property>
    <name>dfs.datanode.data.dir</name>
    <value>/home/hadoop/dfs/data</value>
</property>

sudo nano /usr/local/hadoop/etc/hadoop/mapred-site.xml

<property>
    <name>mapreduce.framework.name</name>
    <value>yarn</value>
</property>

sudo nano /usr/local/hadoop/etc/hadoop/yarn-site.xml

<property>
    <name>yarn.nodemanager.aux-services</name>
    <value>mapreduce_shuffle</value>
</property>
<property>
    <name>yarn.nodemanager.aux-services.mapreduce.shuffle.class</name>
    <value>org.apache.hadoop.mapred.ShuffleHandler</value>
</property>

sudo mkdir -p /home/hadoop/dfs/name /home/hadoop/dfs/data /home/hadoop/tmp
sudo chown -R hadoop:hadoop /home/hadoop/dfs /home/hadoop/tmp
sudo chmod 750 /home/hadoop/dfs /home/hadoop/tmp

/usr/local/hadoop/bin/hdfs namenode -format

/usr/local/hadoop/sbin/start-dfs.sh

/usr/local/hadoop/sbin/start-yarn.sh

sudo su - hadoop

nano ~/.bashrc

export HADOOP_HOME=/usr/local/hadoop
export PATH=$HADOOP_HOME/bin:$PATH

source ~/.bashrc

sudo su - ubuntu

nano ~/exemplo.txt

sudo su - hadoop

hadoop fs -mkdir /test

hadoop fs -put /home/ubuntu/exemplo.txt /test

hadoop fs -ls /test

/usr/local/hadoop/sbin/stop-dfs.sh
/usr/local/hadoop/sbin/stop-yarn.sh



