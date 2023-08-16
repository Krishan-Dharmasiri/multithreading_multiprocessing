import time


def generate_report(report_name:str, report_type:str):
    '''
    Generate the report by fetching data from the data base
    '''
    if report_type == 'pdf':
        time.sleep(4)

    if report_type == 'xlsx':
        time.sleep(5) 

    if report_type == 'docx':
        time.sleep(3)      

    full_name = "{}.{}".format(report_name, report_type)
    print(f'Report with name : {full_name} generated successfully.')


def generate_reports(report_name:str, report_type:str) -> str:
    '''
    Generate the report by fetching data from the data base
    '''
    if report_type == 'pdf':
        time.sleep(4)

    if report_type == 'xlsx':
        time.sleep(5) 

    if report_type == 'docx':
        time.sleep(3)      

    full_name = "{}.{}".format(report_name, report_type)
    return f'Report with name : {full_name} generated successfully.'