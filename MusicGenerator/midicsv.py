import sys
import os
#print("Directorio actual: "+os.getcwd())
#print()
dir1 = r"D:\Ubuntu\MachineLearning\MusicGenerator\MIDI_Data"
os.chdir(dir1) #Directorio donde se ejecutaran los archivos MIDI
#print("Directorio donde estan los archivos: "+os.getcwd())
#print()

#seccion para guardar todos los archivos de tipo MID en un array
import glob
midfiles = []
for file in glob.glob("*.mid"):
    midfiles.append(file)

#Imprimir y eliminar extension todos los archivos del directorio tipo MID
files = [x.replace('.mid','') for x in midfiles]
#print(midfiles)
#print()

#Ejecutar el proceso de MID To CSV
import subprocess 
for i in files:#loop que ejecuta el programa midcsv con cada archivo escaneado y posteriormente guarda la informacion en un txt con el mismo nombre del archivo original
    name = str(i)
    end_file = name+'.txt'
    f = open(end_file,'w')
    errn = name+'_err.txt'
    er = open(errn,'w')
    command = r'midicsv -v '+name+'.mid'
    subprocess.Popen(command,stdout=f, stderr=er)
    f.close()
print()
print("Conversion de Archivos MID a CSV Completada!")
print()

#Al terminar de entrenar el modelo comenzar con un menu para seleccionar si se desea convertir de MIDI a CSV o de CSV a MIDI