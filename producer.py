import json, time
from kafka import KafkaProducer
from kafka.errors import KafkaError
from random import uniform

producer = KafkaProducer(bootstrap_servers=['ip_kafka_server:kafka_port'], 
						 value_serializer=lambda v: json.dumps(v).encode('utf-8'))
contador=1
while True:
	if(contador==1):
		producer.send('p1-c1', {'time': time.strftime("%X"), 'Nombre': 'Felipe', 
						'Apellido': 'Escobar', 'Placa': 'IYZ054', 'Genero': 'H', 'Edad':'21'})
		producer.send('p2-c2', {'time': time.strftime("%X"), 'Nombre': 'Camila', 
						'Apellido': 'Gomez', 'Placa': 'BOS216', 'Genero': 'M', 'Edad':'20'})
		producer.send('p3-c3', {'time': time.strftime("%X"), 'Nombre': 'Ricardo', 
						'Apellido': 'Alonso', 'Placa': 'GYU316', 'Genero': 'M', 'Edad':'50'})
	elif(contador==2):
		producer.send('p1-c4', {'time': time.strftime("%X"), 'Nombre': 'Valentina', 
						'Apellido': 'Chacon', 'Placa': 'ZZE889', 'Genero': 'M', 'Edad':'19'})
		producer.send('p4-c5', {'time': time.strftime("%X"), 'Nombre': 'Santiago', 
						'Apellido': 'Rangel', 'Placa': 'REP131', 'Genero': 'H', 'Edad':'31'})
		producer.send('p5-c6', {'time': time.strftime("%X"), 'Nombre': 'Nicolas', 
						'Apellido': 'Gonzalez', 'Placa': 'TWQ674', 'Genero': 'M', 'Edad':'23'})
	elif(contador==3):
		producer.send('p2-c7', {'time': time.strftime("%X"), 'Nombre': 'Aspen', 
						'Apellido': 'Avila', 'Placa': 'ZZE889', 'Genero': 'M', 'Edad':'2'})
		producer.send('p4-c8', {'time': time.strftime("%X"), 'Nombre': 'Andres', 
						'Apellido': 'Perez', 'Placa': 'KIO490', 'Genero': 'H', 'Edad':'35'})
		producer.send('p3-c9', {'time': time.strftime("%X"), 'Nombre': 'Mariana', 
						'Apellido': 'Arevalo', 'Placa': 'QWE123', 'Genero': 'M', 'Edad':'17'})
	elif(contador==4):
		producer.send('p1-c10', {'time': time.strftime("%X"), 'Nombre': 'Daniel', 
						'Apellido': 'Donado', 'Placa': 'VBN875', 'Genero': 'H', 'Edad':'50'})
		producer.send('p2-c11', {'time': time.strftime("%X"), 'Nombre': 'Maria', 
						'Apellido': 'Gutierrez', 'Placa': 'LOP465', 'Genero': 'M', 'Edad':'38'})
		producer.send('p3-c12', {'time': time.strftime("%X"), 'Nombre': 'Paula', 
						'Apellido': 'Robayo', 'Placa': 'SAD904', 'Genero': 'M', 'Edad':'41'})
		contador=1

	contador=contador+1
	producer.flush()
	time.sleep(10)
	