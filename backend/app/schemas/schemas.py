from typing import Dict

from pydantic import BaseModel, constr

TheAlphabet = constr(regex=r".")


class StringCounts(BaseModel):
    """Dict of counts of letters in a string"""

    __root__: Dict[TheAlphabet, int]


class InputText(BaseModel):
    text: str
