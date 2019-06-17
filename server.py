from progress.bar import Bar
import re
import numpy as np
import pandas as pd

bar = Bar('Loading', fill='@', suffix='%(percent)d%%')
for i in range(100):
    bar.next()
bar.finish()

def OpenArchive():

    dataSet =[]
    with open('data.txt') as f:
        for i in f.readlines():
            dataSet.append(re.findall(r'[\d]+.[\d]+',i))
    return np.array(dataSet,dtype=float)

    #print (pd.dataSet)

if __name__ == '__main__':

    dataSet = OpenArchive()
    brics = pd.DataFrame(dataSet)
    print(brics)

    ai=dataSet[:,0]
    si=dataSet[:,1]
    jobs = len(ai)
    #print ("###################################################")
    #print (ai)
    #print (si)
    #print ("###################################################")

    Co=0.0
    i=0
    di = []
    ci = []

    while(i<len(ai)):
        a = ai[i] 
        if(a < Co):
            d = Co - a
            di.append(d)
        else:
            d = 0.0
            di.append(d)
        Co = a + si[i] + d
        ci.append(Co)
        i = i + 1

    #print ('\nTiempos de llegada para cada trabajo: ai {} ',(di))
    #print ('\nSalidas para cada trabajo: ci ',(ci))
    print ("#############################################################################################\n")
    avg_di = sum(di) / len(ai)
    avg_ai= ai[(jobs-1)] / len(ai)
    avg_si = sum(si) / len(ai)
    wi =  (avg_di + avg_si)
    # 1/ si promedio
    serviceRate  = 1 / avg_si
    # 1/ ri promedio
    arrivalRate = 1 / avg_ai
    
    print ('\t\t\t Estadisticas de trabajo')
    print ('\nPromedio de tiempos de llegada: ai {0:.2f} '.format(avg_ai),'segundos por trabajo')
    print ('Promedio de servicios: si {0:.2f}'.format(avg_si),'segundos por trabajo')
    print ('Promedio de tiempo de espera en la cola : di {0:.2f}'.format(avg_di),'segundos por trabajo')
    print ('Tiempo de espera en el nodo : wi {0:.2f}'.format(wi),'segundos por trabajo')
    print ('Tasa de servicios es : {0:.3f}'.format(serviceRate),'trabajos por segundo')
    print ('Tasa de llegadas es : {0:.3f}'.format(arrivalRate ),'trabajos por segundo\n')
    q_time_average = (jobs/Co) * avg_di
    x_time_average = (jobs/Co) * avg_si
    #Tambien se puede sumar l = q_time_average + x_time_average
    l_time_average = (jobs/Co) * wi
    print ("#############################################################################################\n")
    print ('\t\t\t Estadisticas de  tiempo')
    print ('\ntime-averaged number in the queue: {0:.3f}'.format(q_time_average))
    print ('time-averaged number in service: {0:.3f}'.format(x_time_average))
    print ('time-averaged number in the node: {0:.3f}'.format(l_time_average))
    print ("#############################################################################################")

bar = Bar('Terminado', fill='@', suffix='%(percent)d%%')
for i in range(100):
    bar.next()
bar.finish()