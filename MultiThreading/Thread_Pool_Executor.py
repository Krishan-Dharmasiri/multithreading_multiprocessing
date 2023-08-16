import time
import concurrent.futures

from  utilities import generate_reports

def main():
    '''
        Using the context manager to manage the threads and  
        using "submit" function to call the long runnnig tasks
        Main difference here relative to the thread pool class is that this returns "futures" 
        A future is not the result but a promise to deliver the result in a later time
        you use the "result()" function to get the result from a future object
    '''
    # Arrange the tasks to be executed 
    reports_to_be_run = [
        {'name' : 'MonthEndReport', 'type' : 'pdf'},
        {'name' : 'QuarterlyReport', 'type' : 'xlsx'},
        {'name' : 'AnnualReport', 'type' : 'docx'}
    ]

    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(generate_reports, report['name'], report['type']) 
                                                        for report in reports_to_be_run]
        
        
    # handle results as tasks are completed
    for future in concurrent.futures.as_completed(futures):
        print(f'Completed Futures : {future.result()}')   


if __name__ == '__main__':
    start = time.perf_counter()
    main()
    finish = time.perf_counter()
    print(f'Time Taken : {round(finish - start, 2)} second(s)')    