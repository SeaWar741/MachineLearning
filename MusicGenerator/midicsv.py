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
#files = [x.replace('.mid','') for x in midfiles]
#print(files)
#print()

#Ejecutar el proceso de MID To CSV ( por arreglar)
nmid = '01AusmeinesHerz'
import subprocess
f = open(r'out.txt','w')
#errfd=open('Err.txt','w')

print('Archivo ',nmid)
subprocess.call(['midicsv','v-',nmid+'.mid'], shell=True, stdout=f)
args = r'midicsv -v 01AusmeinesHerz.mid'
subprocess.call([args], shell = True, stdout=f)
command = 'midicsv -v 01AusmeinesHerz.mid'
subprocess.Popen(command, stdout=f)


#errfd.close()

'''
for i in files:
    name= str(i)
    outfd=open(name+'.txt','w+')
    errfd=open('Err.txt','w+')

    print('Archivo: ',i)
    print()
    #Ejecuta MIDI TO CSV
    subprocess.call(['midicsv','v-',name+'.mid'], stdout=outfd, stderr=errfd)
    outfd.close()
    errfd.close()
'''