from pydantic import BaseModel, Field, field_validator
from typing import Literal, Optional

class Bank(BaseModel):
    name: str
    lastname: str
    typedoc: Literal['CC', 'TI', 'CE', 'PAS']
    document: int = Field(..., gt=0)
    balance: float = Field(..., ge=0)
    
    @field_validator('name', 'lastname')
    def no_vacio(cls, validar):
        if not validar.strip():
            raise ValueError('The field cannot be empty')
        return validar
    
    @field_validator('document')
    def document_length(cls, value):
        if len(str(value)) < 5:
            raise ValueError('Document must have at least 5 characters')
        return value
    

class UpdateBankModel(BaseModel):
    name: Optional[str] = None
    lastname: Optional[str] = None
    typedoc: Optional[Literal['CC', 'TI', 'CE', 'PAS']] = None
    document: Optional[int] = None
    balance: float = Field(..., ge=0)
