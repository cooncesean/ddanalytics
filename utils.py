from ddanalytics import login_manager
from ddanalytics.models import User


@login_manager.user_loader
def load_user(username):
    " Callback used to reload the user object from the user ID stored in the session. "
    try:
        return User.objects.get(username=username)
    except User.DoesNotExist:
        pass
    return None

