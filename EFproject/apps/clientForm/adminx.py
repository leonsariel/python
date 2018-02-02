
import xadmin
from xadmin import views
from .models import ClientInfo, CaseIntensityRating

class ClientInfoAdmin(object):
    # display list of columns
    list_display = ['clientID', 'caseWorker', 'firstName', 'lastName', 'postCode', 'status']
    search_fields = ['clientID', 'caseWorker', 'firstName', 'lastName', 'postCode', 'status']
    list_filter = ['clientID', 'caseWorker', 'firstName', 'lastName', 'postCode', 'status']




class CIRAdmin(object):
    # display list of columns
    list_display = ['clientID', 'knob', 'knob2', 'knob3', 'knob4']
    search_fields = ['clientID', 'knob', 'knob2', 'knob3', 'knob4']
    list_filter = ['clientID', 'knob', 'knob2', 'knob3', 'knob4']

xadmin.site.register(ClientInfo, ClientInfoAdmin)
xadmin.site.register(CaseIntensityRating,CIRAdmin)