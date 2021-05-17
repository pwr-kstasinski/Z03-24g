# flake8: noqa

# import all models into this package
# if you have many models here with many references from one model to another this may
# raise a RecursionError
# to avoid this, import only the models that you directly need like:
# from from openapi_client.model.pet import Pet
# or import this package, but before doing it, use:
# import sys
# sys.setrecursionlimit(n)

from openapi_client.model.jsonapi_error400 import JsonapiError400
from openapi_client.model.jsonapi_error403 import JsonapiError403
from openapi_client.model.jsonapi_error404 import JsonapiError404
from openapi_client.model.jsonapi_error405 import JsonapiError405
from openapi_client.model.jsonapi_error409 import JsonapiError409
from openapi_client.model.jsonapi_error500 import JsonapiError500
from openapi_client.model.message_coll import MessageColl
from openapi_client.model.message_coll1 import MessageColl1
from openapi_client.model.message_inst import MessageInst
from openapi_client.model.message_inst1 import MessageInst1
from openapi_client.model.user_coll import UserColl
from openapi_client.model.user_coll1 import UserColl1
from openapi_client.model.user_incoming_messages_rel_coll import UserIncomingMessagesRelColl
from openapi_client.model.user_inst import UserInst
from openapi_client.model.user_inst1 import UserInst1
