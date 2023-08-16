import time
from utilities import perform_search


def main() -> None:
    '''
    Arrange the search operations to be run in a list and execute them
    '''
    searches_to_be_run = [
        'LINEAR',
        'BINARY',
        'GRAPH'
    ]

    # Perform the search operations
    for search_type in searches_to_be_run:
        perform_search(search_type)


if __name__ == '__main__':
    start = time.perf_counter()
    main()
    finish = time.perf_counter()
    print(f'Total time taken  : {round(finish - start, 2)} seconds') 


    # print a message to the caller once the program finishes
    print('PROGRAM EXECUTED SUCCESSFULLY')