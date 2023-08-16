import time
import concurrent.futures

from utilities import perform_searches


def main():
    '''
        Using the context manager and  process pool executor
        Process Pool Executor class immediately returns future(s) 
        A future is not the result but a promise to deliver the result in a later time
        you use the "result()" function to get the result froma future object
    '''

    # Arrange the serach operations to be run
    searches_to_be_run = [
        'LINEAR',
        'BINARY',
        'GRAPH'
    ]

    # Crate the process pool executor and pass the tasks
    with concurrent.futures.ProcessPoolExecutor() as executor:
        futures = [executor.submit(perform_searches, search_type) for search_type in searches_to_be_run]
        
    # Handle results as processes are completed    
    for future in concurrent.futures.as_completed(futures):
            print(f'Result :  {future.result()}')

if __name__ == '__main__':
    start = time.perf_counter()
    main()
    finish = time.perf_counter()
    print(f'Time Taken : {round(finish - start, 2)} second(s)') 