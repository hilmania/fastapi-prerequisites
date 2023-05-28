import time
from pydantic import BaseModel,Field
from datetime import datetime

class Blog(BaseModel):
    title: str
    created_at: datetime = Field(default_factory=datetime.now)
    is_active: bool

print(Blog(title="Our First Blog",is_active=True))
time.sleep(3)
print(Blog(title="Our Second Blog",is_active=True))

#Output:
#title='...' created_at=datetime.datetime(2022, 10, 7, 15, 57, 46, 257846) is_active=True
#title='...' created_at=datetime.datetime(2022, 10, 7, 15, 57, 49, 261350) is_active=True
