import time

def perform_search(search_type : str) -> str:
    '''
    Performing the search operation which is a CPU bound Task
    '''
    start = time.perf_counter()
    if search_type == 'LINEAR':
        time.sleep(2)

    if search_type == 'BINARY':
        time.sleep(4)

    if search_type == 'GRAPH':
        time.sleep(6)        

    finish = time.perf_counter()
    time_taken = round(finish - start, 2)
    
    print (f'{search_type} Search Completed Successfully, time taken : {time_taken} seconds' )   

def perform_searches(search_type : str) -> str:
    '''
    Performing the search operation which is a CPU bound Task
    '''
    start = time.perf_counter()
    if search_type == 'LINEAR':
        time.sleep(2)

    if search_type == 'BINARY':
        time.sleep(4)

    if search_type == 'GRAPH':
        time.sleep(6)        

    finish = time.perf_counter()
    time_taken = round(finish - start, 2)
    
    return f'{search_type} Search Completed Successfully, time taken : {time_taken} seconds'      