from typing import Annotated
from fastapi import status
from .health_check_validator import check_health_validate, increase_health_score_validate

def get_health_status(request, response):
  # Validate the request
  validate_health_check = check_health_validate(request.query_params)
  if not validate_health_check['valid']:
      response.status_code = status.HTTP_422_UNPROCESSABLE_ENTITY
      return { 
          "success": False, 
          "message": validate_health_check['message'], 
      }
  
  # request.model_config = request.query_params
  
  
  # Rest Business logic goes here ...
  
  
  return { 
    "success": True, 
    "health_status": "Healthy", 
    "request_method": request.method,  
  }
  
# def increase_health_score(request, response):
#   # Validate the request
#   body = request
  
#   return
#   validate_increase_health_score = increase_health_score_validate(request.body())
#   if not validate_increase_health_score['valid']:
#       response.status_code = status.HTTP_422_UNPROCESSABLE_ENTITY
#       return { 
#           "success": False, 
#           "message": validate_increase_health_score['message'], 
#       }
      
      
#   # Rest Business logic goes here ...
  
  
#   return { 
#     "success": True, 
#     "health_status": "Healthy", 
#     "request_method": request.method,  
#   }
  