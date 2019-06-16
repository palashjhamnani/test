import requests
#import slack
from bs4 import BeautifulSoup

file = open('data.txt', 'r+')

try:
    old_data = file.readlines()
    file.close()
    file = open("data.txt", "w")
    q = []
    if len(old_data)>0:
        for i in old_data:
            q.append(i.replace("\n", ""))
        old_data = q
        print("Old Data:")
        print(old_data)
    else:
        old_data = None

    url = ""
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    a = soup.findAll('td')

    l = len(a)
    print(l)

    current_data = []
    new_data = []

    if l>0:
        for i in range(0, l, 6):
            post = a[i+1].get_text().replace("\t","").replace("\n","").strip()
            current_data.append(post)

        print("Fetched Data:")
        print(current_data)

        # This is to clear expired jobs

        for job in old_data:
            if job in current_data:
                pass
            else:
                old_data.remove(job)


        # This is to find new jobs posted

        for job in current_data:
            if job in old_data:
                pass
            else:
                new_data.append(job)
                old_data.append(job)

        print("Updated Old Data List:")
        print(old_data)

        if len(new_data)==0:
            m = "Hi There! No new postings available currently."
        else:
            m = "Hi There! New job postings available: "+", ".join(new_data)
    else:
        m = "Hi There! No new postings available currently."



    for item in old_data:
            file.write("%s\n" % item)

finally:
    file.close()

print(m)

#client = slack.WebClient(token="")
#response = client.chat_postMessage(
#channel='CK8RVKLG3',
#text=m)
headers = {'Authorization':'Bearer '}
r = requests.post('https://slack.com/api/chat.postMessage', data = {'channel':'', 'text':m}, headers = headers)
print("Process Completed")
