from pydantic import (
    BaseModel,
    ValidationError
)
class Health_Check_Validator(BaseModel):
    show_request_information: bool
    
class IncreaseHealthyScoreValidator(BaseModel):
    daily_boot_time: int
    cool_down: int | None = None
    
    
    
    
    
    
    
def check_health_validate(requestArgs):
    try:
        Health_Check_Validator(**requestArgs)
        return { "valid": True }
    except ValidationError as e:
        return { "valid": False, "message": e.errors()}
    

# def increase_health_score_validate(requestArgs):
#     try:
#         IncreaseHealthyScoreValidator(**requestArgs)
#         return { "valid": True }
#     except ValidationError as e:
#         return { "valid": False, "message": e.errors()}

