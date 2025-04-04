import os
import django

# Set up Django settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'psqlconnect.settings')
django.setup()

# Import the User model from your app
from users.models import User

# Insert a user into the database
new_user = User(name="Chel Seriezniy", email="nevasyatunebikuitak.doe@example.com")
new_user.save()
print("User added to the database!")

# Query the database for the user
user = User.objects.first()  # Fetch the first user in the database
print(f"User retrieved: {user.name}, {user.email}")
