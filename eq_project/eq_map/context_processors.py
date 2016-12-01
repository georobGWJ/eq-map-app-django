from django.conf import settings # import the settings file
import local_settings
# 
# try:
#     import local_settings
# except ImportError:
#     pass

def admin_media(request):
    # return the value you want as a dictionnary. you may add multiple values in there.
    return {'API_KEY': local_settings.API_KEY}
