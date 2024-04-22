from fastapi import status
from .health_check_validator import validate

def check_health_status(request, response):
        # Validate the request
        validate_health_check = validate(request.query_params)
        if not validate_health_check['valid']:
            response.status_code = status.HTTP_422_UNPROCESSABLE_ENTITY
            return { 
                "success": False, 
                "message": validate_health_check['message'], 
            }
        
        return { 
          "success": True, 
          "health_status": "Healthy", 
          "request_method": request.method,  
        }