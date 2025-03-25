import csv
import json

compromised_users = []

with open(r'C:\Users\om31d\OneDrive\Coding Classes\Python\Files\passwords.csv') as password_file:
    password_csv = csv.DictReader(password_file)
    for password_row in password_csv:
        compromised_users.append(password_row['Username'])

with open('compromised_users.txt', 'w') as compromised_user_file:
    for compromised_user in compromised_users:
        compromised_user_file.write(compromised_user)

with open('boss_message.json', 'w') as boss_message:
    boss_message_dict = {
        'recipient':'The Boss',
        'message':'Mission Successful'
    }
    json.dump(boss_message_dict, boss_message)

with open('new_passwords.csv', 'w') as new_passwords_obj:
    slash_null_sig = r"""
      _ _  ___   __    __   
     / )( \(  __) /  \  (  _ \ 
    ) \/ ( ) _) (  O )  )  / 
    \____/ (___) \__/  (__)

        _  _  __  ___  __ _  ____  ____
       / )( \(  __)/  \ /  \(  _ \(  __)
       ) __ ( ) _)(  O )(  O ))   / ) _) 
       \_)(_/(____)\__/ \__/(__\_)(____)
          ____  __    __  ____  _  _ 
         ___/ ___)(  )  / _\ / ___)( )( \ 
        (___\___ \/ (\/ \/ \ \___ \) __ (
        (____/\____/\_/\_/  (____/\_)(_/
                __ _  _  _  __  __  
               (  ( \/ )( \(  ) (  ) 
               /    /) \/ (/ (_/\/ (_/\
               \_)__)\____/\____/\____/
"""
    new_passwords_obj.write(slash_null_sig)

with open('new_passwords.csv') as new_password_csv:
    new_password = new_password_csv.read()
    print(new_password)