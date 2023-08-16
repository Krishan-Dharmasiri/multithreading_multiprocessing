import time
from multiprocessing import Process

from  utilities import perform_search

def main() -> None:
    '''
    Use a new process to perform the search
    Process class takes 2 arguments, 
            "target" => the function to be executed by the new Process
            "args"   => argument to be passed into the "target" function
    '''
   
    # Create a process and assign the task
    new_process = Process(target=perform_search, args=('BINARY',))

    # start the new process
    new_process.start()

    # Wait for the process to finish
    new_process.join()

if __name__ == '__main__':
    start = time.perf_counter()

    main()
    
    finish = time.perf_counter()
    print(f'Total time taken  : {round(finish - start, 2)} seconds')         