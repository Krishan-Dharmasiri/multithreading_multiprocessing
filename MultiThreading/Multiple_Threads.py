'''
Import the Thread class from threading module
'''
from threading import Thread
import time

from utilities import generate_report

def main() -> None:
    '''
        Function to run the thread
        Thread class takes 2 arguments, 
            "target" => the function to be executed by the new thread
            "args"   => argument to be passed into the "target" function
    '''
    # Create new threads and assign the target function and the arguments at the same time
    thread_1 = Thread(target=generate_report, args=('MonthEndReport', 'pdf'))
    thread_2 = Thread(target=generate_report, args=('QuarterlyReport', 'xlsx'))
    thread_3 = Thread(target=generate_report, args=('AnnualReport', 'docx'))

    # start the threads MANUALLY
    thread_1.start()
    thread_2.start()
    thread_3.start()

    # wait until the thread is completely executed
    thread_1.join()
    thread_2.join()
    thread_3.join()

    
if __name__ == '__main__':
    start = time.perf_counter()
    main()
    finish = time.perf_counter()
    print(f'Total time taken  : {round(finish - start, 2)} seconds') 


    # print a message to the caller once the program finishes
    print('PROGRAM EXECUTED SUCCESSFULLY')





