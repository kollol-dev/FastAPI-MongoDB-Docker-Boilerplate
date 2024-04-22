from pydantic import (
    BaseModel,
    ValidationError,
    ValidationInfo,
    ValidatorFunctionWrapHandler,
)

class Health_Check_Validator(BaseModel):
    show_request_information: bool
    
def validate(requestArgs):
    try:
        Health_Check_Validator(**requestArgs)
        return { "valid": True }
    except ValidationError as e:
        return { "valid": False, "message": e.errors()}
    

