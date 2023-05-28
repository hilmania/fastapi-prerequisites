from pydantic import BaseModel, Field, validator

class Blog(BaseModel):
    title: str = Field(..., min_length=5)
    is_active: bool

    @validator("title")
    def validate_no_sql_injection(cls, value):
        if "delete from" in value:
            raise ValueError("Our terms strictly prohibit SQLInjection Attacks")
        return value

print(Blog(title="select * from", is_active=True))
