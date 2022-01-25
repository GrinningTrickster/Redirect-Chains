from crawler import html_request
import re
import requests


def redirected_url_result(url, status):
    redirect = re.compile("^3.*")
    match = re.search(redirect, str(status))
    rcount = 0
    final = "-"
    finalstatus = 0
    second = "-"
    secondstatus = 0
    if match is not None:
        try:
            s = requests.Session()
            s.max_redirects = 10
            r = s.get(url,allow_redirects=10, verify=True)
            # redirect chain status codes results
            history = r.history
            # final redirect in a chain
            final = r.url
            # final status code in the chain
            finalstatus = r.status_code
            # how many urls within the chain
            rcount = len(history)
            if rcount == 1:
                second = "-"
                secondstatus = 0
            else:
                try:
                # second redirect url result
                    second = history[1].url
                # second redirect status code result
                    secondstatus = history[1].status_code
                except IndexError as f:
                    second = history[0].url
                    secondstatus = history[0].status_code
        except requests.exceptions.TooManyRedirects as e:
            # requests does not exceed or follow any redirects
            r = requests.get(url, allow_redirects=False)
            final = "-"
            finalstatus = 0
            # if 11, then the number of redirects is >=11 or a redirect loop
            rcount = 11
            # acquires second redirect without getting caught in the loop
            second = r.headers['Location']
            s = requests.get(second, allow_redirects=False)
            secondstatus = s.status_code
    return rcount, final, finalstatus, second, secondstatus