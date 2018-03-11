import requests


urls = []


class Urls:
    def __init__(self,urlcsv,status=0):
        self.urlcsv=urlcsv
        try:
            r = requests.get(urlcsv, timeout=5)
            status = r.status_code
            self.status = status
        except requests.exceptions.Timeout:
            self.status = "incorrect url"
        except requests.exceptions.ConnectionError:
            self.status = "incorrect url"
        urls.append(self)
