#!/bin/sh
# Aggiungi un ritardo di 30 secondi prima di avviare il Kafka Exporter
sleep 120
# Avvia Kafka Exporter con ciascun broker specificato separatamente
/bin/kafka_exporter --kafka.server=kafka1:9092 --kafka.server=kafka2:9093 --kafka.server=kafka3:9094 --kafka.version=${KAFKA_VERSION} --log.level=${LOG_LEVEL}
