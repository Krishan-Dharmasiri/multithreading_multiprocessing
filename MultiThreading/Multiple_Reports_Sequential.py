import time
from utilities import generate_report


def main() -> None:
    '''
    Arrange the reports to be run in a list and execute them
    '''
    reports_to_be_run = [
        {'name' : 'MonthEndReport', 'type' : 'pdf'},
        {'name' : 'QuarterlyReport', 'type' : 'xlsx'},
        {'name' : 'AnnualReport', 'type' : 'docx'}
    ]

    # Run the reports
    for report in reports_to_be_run:
        generate_report(report['name'], report['type'])


if __name__ == '__main__':
    start = time.perf_counter()
    main()
    finish = time.perf_counter()
    print(f'Total time taken  : {round(finish - start, 2)} seconds') 


    # print a message to the caller once the program finishes
    print('PROGRAM EXECUTED SUCCESSFULLY')