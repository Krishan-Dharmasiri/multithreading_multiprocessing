import time
from multiprocessing import Process

from utilities import perform_search

def main() -> None:
    '''
    Use multiple processes to perform the search operations
    Process class takes 2 arguments, 
            "target" => the function to be executed by the new Process
            "args"   => argument to be passed into the "target" function
    '''

    # Create new process and assingn the tasks
    process_1 = Process(target=perform_search, args=('LINEAR',))
    process_2 = Process(target=perform_search, args=('BINARY',))
    process_3 = Process(target=perform_search, args=('GRAPH',))

    # Start the Processes manually
    process_1.start()
    process_2.start()
    process_3.start()

    # Wait until all the processes are done 
    process_1.join()
    process_2.join()
    process_3.join()

if __name__ == '__main__':
    start = time.perf_counter()
    main()
    finish = time.perf_counter()
    print(f'Total time taken  : {round(finish - start, 2)} seconds') 


    # print a message to the caller once the program finishes
    print('PROGRAM EXECUTED SUCCESSFULLY')
