from django.http import HttpResponse
import logging

logger = logging.getLogger(__name__)


def index(request):

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

    
