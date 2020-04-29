users_list = ['deepak', 'satheesh', 'jjc']
confirmed_users = []
while users_list:
    current_user = users_list.pop()
    print(f"Verifying User: {current_user.title()}")
    confirmed_users.append(current_user)
print("\nThe following users have been confirmed:")
for user in confirmed_users:
    print(user.title())
### example 2
# remove a value from list using while
servers = ['app_server', 'db_server', 'db', 'jboss_server', 'db', 'web_server']
while 'db' in servers:
    servers.remove('db')
print(servers)

