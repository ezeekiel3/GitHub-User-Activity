import requests

def search_activiy_user(username=""):
    push_event = 0
    issues_event = 0
    watch_event = 0
    fork_event = 0
    create_event = 0
    if (len(username) == 0):
        print('error please enter a username')
        return
    
    url = f'https://api.github.com/users/{username}/events'

    try:
        response = requests.get(url)
        data = response.json()
    except:
        print('error, user not found')
        return

    for element in data:
        match element["type"]:
            case "PushEvent":
                push_event += 1
            case "IssuesEvent":
                issues_event += 1
            case "WatchEvent":
                watch_event += 1
            case "ForkEvent":
                fork_event += 1
            case "CreateEvent":
                create_event += 1
    print(f'veces que pusheo, {push_event}')
    return
search_activiy_user('randombit')


# PushEvent
# IssuesEvent
# WatchEvent
# ForkEvent
# CreateEvent