import pyshark
#Fuente de captura, IP del dispositivo,red al que esta conectado y filtrado por TCP
capture = pyshark.RemoteCapture('192.168.1.33',interface='en1',bpf_filter="tcp")
#Tiempo de captura
capture.sniff(timeout=50)
capture
capture[3]
#Imprimir informacion de 5 paquetes capturados
for packet in capture.sniff_continuously(packet_count=5):
    print 'Just arrived:', packet
