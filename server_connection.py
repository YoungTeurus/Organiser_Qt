import requests


def check_connection(url, username, password):
    payload = {'username': username,
               'password': password,
               'download': 'none'}
    try:
        my_req = requests.get(url, data=payload)
        if my_req.text != payload['username']:
            return my_req.text
        else:
            return 1
    except requests.exceptions.MissingSchema:
        return -1
    except requests.exceptions.InvalidURL:
        return -2
    except requests.exceptions.ConnectionError:
        return -3


def download_file(url, username, password, filename):
    payload = {'username': username,
               'password': password,
               'download': 'yes'}
    if check_connection(url, username, password) == 1:
        # try:
        my_req = requests.get(url, data=payload)
        # print(my_req.content)
        file = open(".\\" + filename, "wb")
        file.write(my_req.content)
        file.close()
        # except BaseException:
        #    pass

def upload_json_file(url, json_file):
    files = {'file': ('data.json', open(json_file, "rb"), 'text/json')}
    try:
        my_req2 = requests.post(url, files=files)
    except requests.exceptions.ConnectionError:
        print("Бяка")


if __name__ == "__main__":
    # print(check_connection("http://localhost:80", "user1","qwerty"))
    download_file("http://localhost:80", "user1", "qwerty", "test.json")
