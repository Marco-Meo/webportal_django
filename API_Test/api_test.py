import requests
import json

# Create Token
# python manage.py drf_create_token admin

token = 'ab57213edaec152df2ab8b63840240337f275596'
url = 'http://127.0.0.1:8000/api/faq/'
header = {'Authorization': "Token " + token}
proxies = {'https': 'https://user:password@ip:port'}

def faq_list():
    try:
        response = requests.get(url, headers=header)
        return response
    except Exception as e:
        print(f"Fehler: {e}")
        return None

def faq_list2():
    try:
        response = requests.get(url, auth=('api', 'test12345'), proxies=proxies)
        return response
    except Exception as e:
        print(f"Fehler: {e}")
        return None

def faq_create():
    body = {
        "title": "API Test",
        "description": "Dieser Eintrag kommt über die API",
        "creator": 1
    }

    try:
        response = requests.post(url, data=body, headers=header)
        return response
    except Exception as e:
        print(f"Fehler: {e}")
        return None

def faq_update(var):
    var['title'] = " ".join(['Update ', var.get('title')])
    del var['creation_date']
    neue_url = url + str(var['id']) + "/"
    try:
        response = requests.put(neue_url, data=var, headers=header)
        return response
    except Exception as e:
        print(f"Fehler: {e}")
        return None

def faq_delete(var):
    neue_url = url + str(var) + "/"
    return requests.delete(neue_url, headers=header)

if __name__ == '__main__':
    # resp = faq_list2()
    # print("Status-Code: ", resp.status_code)
    # print(resp.text)

    resp = faq_create()
    if resp:
        print("Status-Code: ", resp.status_code)
        dict_response = resp.json()
        print(dict_response.get('title'))
        print(dict_response.get('id'))

        response = faq_update(dict_response)
        print(response.status_code)

        print(faq_delete(response.json()['id']))

