from django.http import HttpResponse
import logging

from coralogix.handlers import CoralogixLogger

PRIVATE_KEY = "cb5b715f-a7e1-1d67-22c1-bb204afce074"
# APP_NAME = "django-webservice-app"
# SUB_SYSTEM = "django-webservice-sys"
APP_NAME = "pod-django-webservice-app"
SUB_SYSTEM = "pod-django-webservice-sys"

def index(request):
    logger = logging.getLogger("Python Logger")
    
    logger.setLevel(logging.INFO)

    # Get a new instance of Coralogix logger.
    coralogix_handler = CoralogixLogger(PRIVATE_KEY, APP_NAME, SUB_SYSTEM)
    
    # Add coralogix logger as a handler to the standard Python logger.
    logger.addHandler(coralogix_handler)

    try:
      num = int(request.GET.get('num', ''))

      if num > 0:
        logger.info("The number: {0} is a positive number".format(num))  
        return HttpResponse("The number: {0} is a positive number !".format(num))
      elif num == 0:  
        logger.info("The number: {0} is zero".format(num))   
        return HttpResponse("The number: {0} is zero !".format(num))
      else:  
        logger.info("The number: {0} is negative number".format(num))  
        return HttpResponse("The number: {0} is negative number !".format(num)) 
    except Exception as e:
        logger.error(e)  
        return HttpResponse("Imput number is not valid") 

    CoralogixLogger.flush_messages()
    
