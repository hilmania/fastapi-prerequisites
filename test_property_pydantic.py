from pydantic import BaseModel
from typing import List, Optional

class Comment(BaseModel):
    text: Optional[str]=None

class Blog(BaseModel):
    title: str
    comment: Optional[List[Comment]]
    is_active: bool

print(Blog(title="Our First Blog",comment=[{'text':'My comment'},{'text':'Your comment'},],is_active=True))

#Output: title='Our First Blog' comment=[Comment(text='My comment'), Comment(text='Your comment')] is_active=True
