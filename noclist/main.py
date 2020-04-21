import sys
import users_resource

users_resource = users_resource.UsersResource()
print(users_resource.get_users(), file=sys.stdout)
sys.exit(0)
