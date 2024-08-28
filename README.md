# kafka-grafana

In this repository, I created a docker compose that deploys a set of containers with the goal of monitoring a dockerized kafka cluster. 

Containers that will be created will have these features:

- zookeeper: for the management and coordination of kafka nodes
- kafka1, kafka2, kafka3: kafka containers forming a distributed cluster for collecting, processing and storing event stream data
- prometheus: for the collection and storage of metrics 
- grafana: for creating dashboards with the goal of monitoring the kafka cluster
- kafka exporter: for sending metrics from prometheus to grafana
- python-app-producer: application for sending messages to kafka
- python-app-consumer: app for consuming messages to kafka

After creating a clone of the repository, enter the kafka-grafana-main folder and deploy the environment with this command:

```shell
docker compose up
```

Wait for the containers to deploy and then once the grafana container has gone up you can access the administration interface via the link:

```shell
http://localhost:3000/
```

You will be asked to change your password when you first log in. Once the change is made log in to grafana and click on dashboards. There will be a dashboard already configured called Monitoring Kafka.

Clicking on it will display a dashboard containing the following metrics:

- Broker Online
- Partition Topic
- Topic partition Current Offset
- Partition under replica
- Partition in sync replica
- Topic partition leader
- Consumer Group Lag

Wait about 2 to 3 minutes to see the dashboard updated with the new data

![image](https://github.com/user-attachments/assets/cc9995b9-3946-419b-b2fc-0e36a643e6fe)

If you want, you can customise the metrics and add more!
