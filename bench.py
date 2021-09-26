#imports
from multiprocessing import Pool
from multiprocessing import cpu_count
import time
import os

#function for stressing the cpu
def f(x):
    cpi = 300000000
    stb = 0
    while True:
        if cpi <= stb:
            break
        stb = stb + 1
        x*x
    
#starting the test
if __name__ == '__main__':
    #checking the number of cpu cores available for multithreading stress test
    processes = int(cpu_count())

    #prints cores utailizing for multithreading
    print ('utilizing %d cores\nrunning 300 million instances, please wait around 3 min for test to finish' % processes)

    #starts a pool for multithreading by using all available processes or cpu cores
    pool = Pool(processes)

    #gets a time stamp for time spent
    start_time = time.time()

    #opens the pool
    pool.map(f, range(6))

    #gets elaspsed time
    elaspsed_time = time.time() - start_time

    #pool closes and terminates
    pool.close()
    pool.join()

    #calculates multithreaded score
    multithread_score = str(int(3000000000/(elaspsed_time*100000)))
    multitime = elaspsed_time
    
    #starts a pool for singlethread but only on a single core to get single threaded score's
    pool = Pool(1)
    
    #gets a time stamp for time spent
    start_time = time.time()
    
    #opens the pool 
    pool.map(f, range(6))

    #gets the elasped time
    elaspsed_time = time.time() - start_time

    #closes and terminates the pool
    pool.close()
    pool.join()

    #calculates single threaded score
    singlethread_score = str(int(3000000000/(elaspsed_time*100000)))
    singletime = elaspsed_time

    #prints both of the score's
    print ("your single threaded score is = "+ singlethread_score +" time taken in seconds " +str(singletime) +"\nyour multithreaded score is = " + multithread_score+" time taken in seconds " +str(multitime))
    print("\nhigher the number better the score")
