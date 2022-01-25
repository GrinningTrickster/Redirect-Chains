import pandas as pd
from crawler import html_request
from redirects import redirected_url_result
from datetime import datetime


if __name__ == '__main__':

    data = []

    date = datetime.today().strftime('%Y-%m-%d')

    # Text file with a list of URLs to be checked.
    filename = 'urls.txt'
    with open(filename) as f:
        content = f.readlines()
    content = [x.strip() for x in content]

    for page in content:
        url, html, status = html_request(page)
        rcount, final, finalstatus, second, secondstatus = redirected_url_result(url, status)
        result = (url, date, status, rcount, final, finalstatus, second, secondstatus)
        data.append(result)

    headers = ('URL', 'Date', 'Status', 'Redirect Count', 'Final Redirect URL', 'Final Redirect Status',
               'Second Redirect URL', 'Second Redirect Status')

    df = pd.DataFrame(data)
    writer = pd.ExcelWriter(date + '-results.xlsx', engine='xlsxwriter')
    df.to_excel(writer, sheet_name='results', index=False, header=headers)
    writer.save()






