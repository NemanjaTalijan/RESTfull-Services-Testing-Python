
import requests
import json
import time

url = "http://services.groupkt.com"

start_time = time.time()

response = requests.get("{}/country/get/all".format(url), data=None, headers=None, verify=False)
assert response.status_code == 200
print("Service response code: {}!".format(response.status_code))

json_parsed = json.loads(response.content)
print("We have {} results!".format(len(json_parsed["RestResponse"]["result"])))


# Parse JSON service response and print results
count = 0
for x in range(0, len(json_parsed["RestResponse"]["result"])):
    if json_parsed["RestResponse"]["result"][x]["name"] == "Afghanistan":
        print(json_parsed["RestResponse"]["result"][x]["alpha2_code"], json_parsed["RestResponse"]["result"][x]["alpha3_code"], json_parsed["RestResponse"]["result"][x]["name"])
        count += 1
        break
if count > 0:
    print("Afghanistan is in the search results!")
else:
    print("Afghanistan is not in the search results!")


# Search for the countries with alpha2_code listed in array
country_codes = ['AX', 'AL', 'DZ', 'AS', 'AD']
countAX = 0
countAL = 0
countDZ = 0
countAS = 0
countAD = 0
for c in country_codes:
    print(c)
for c in country_codes:
    for x in range(0, len(json_parsed["RestResponse"]["result"])):
        if json_parsed["RestResponse"]["result"][x]["alpha2_code"] == c:
            print(json_parsed["RestResponse"]["result"][x]["alpha2_code"], json_parsed["RestResponse"]["result"][x]["alpha3_code"], json_parsed["RestResponse"]["result"][x]["name"])
            if c == 'AX':
                countAX += 1
            if c == 'AL':
                countAL += 1
            if c == 'DZ':
                countDZ += 1
            if c == 'AS':
                countAS += 1
            if c == 'AD':
                countAD += 1
            if countAX > 0 and countAL > 0 and countDZ > 0 and countAS > 0 and countAD > 0:
                break
if countAX > 0 and countAL > 0 and countDZ > 0 and countAS > 0 and countAD > 0:
    print("All country alpha2_code found in search results!")
else:
    if countAX == 0:
        print("Alpha2_code AX not in the search results!")
    if countAL == 0:
        print("Alpha2_code AL not in the search results!")
    if countDZ == 0:
        print("Alpha2_code DZ not in the search results!")
    if countAS == 0:
        print("Alpha2_code AS not in the search results!")
    if countAD == 0:
        print("Alpha2_code AD not in the search results!")

end_time = time.time() - start_time
print("Test lasted {} seconds!".format(end_time))


# Search for the country with alpha2_code == "PP" that is not in the JSON response besides other contries listed
country_codes = ['AX', 'AL', 'DZ', 'AS', 'AD', 'PP']
countAX = 0
countAL = 0
countDZ = 0
countAS = 0
countAD = 0
countPP = 0
for c in country_codes:
    for x in range(0, len(json_parsed["RestResponse"]["result"])):
        if json_parsed["RestResponse"]["result"][x]["alpha2_code"] == c:
            print(json_parsed["RestResponse"]["result"][x]["alpha2_code"], json_parsed["RestResponse"]["result"][x]["alpha3_code"], json_parsed["RestResponse"]["result"][x]["name"])
            if c == 'AX':
                countAX += 1
            if c == 'AL':
                countAL += 1
            if c == 'DZ':
                countDZ += 1
            if c == 'AS':
                countAS += 1
            if c == 'AD':
                countAD += 1
            if c == 'PP':
                countAD += 1
            if countAX > 0 and countAL > 0 and countDZ > 0 and countAS > 0 and countAD > 0 and countPP > 0:
                break
if countAX > 0 and countAL > 0 and countDZ > 0 and countAS > 0 and countAD > 0 and countPP > 0:
    print("All country alpha2_code found in search results!")
else:
    if countAX == 0:
        print("--Alpha2_code AX not found in the search results!")
    if countAL == 0:
        print("--Alpha2_code AL not found in the search results!")
    if countDZ == 0:
        print("--Alpha2_code DZ not found in the search results!")
    if countAS == 0:
        print("--Alpha2_code AS not found in the search results!")
    if countAD == 0:
        print("--Alpha2_code AD not found in the search results!")
    if countPP == 0:
        print("--Alpha2_code PP not found in the search results!")

end_time = time.time() - start_time
print("Test lasted {} seconds!".format(end_time))


# POST REST call with timeout and SSL sertificate set on False for https connections
url = "https://localhost:8080"

data = "{\"loginName\": \"user\",\"password\": \"user\"}"
headers = {
    "Content-Type": "application/json",
    "X-CSRFToken": "foo",
    "Cookie": "csrftoken=foo"
}
response1 = requests.post(f"{url}/cc/access/rest/v1/sessions", data=data, headers=headers, timeout=1, verify=False)
assert response1.status_code == 204
print(response1.status_code, response1.reason, response1.text)
