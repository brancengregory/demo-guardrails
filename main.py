from pydantic import BaseModel, Field
from guardrails.hub import ValidChoices
from guardrails import Guard
from rich import print
import openai

val = ValidChoices(choices=["flamingo", "piranha", "platypus"], on_fail="reask")

class Pet(BaseModel):
    pet_type: str = Field(description="type of pet", validators=[val])
    name: str = Field(description="punny name")
    color: str = Field(description="unusual color")
    age: str = Field(description="impossible age")
    temperament: str = Field(description="temperament")
    food: str = Field(description="favorite food")
    hobby: str = Field(description="hobby")
    best_friend: str = Field(description="best friend description")
    life_problem: str = Field(description="current human-like life problem")
    divorcee: str = Field(description="who they are divorced from")
    city: str = Field(description="real human city")
    country: str = Field(description="real human country")
    activity: str = Field(description="what they did today")

prompt = """
    What kind of pet, with what characteristics, should I get?

    ${gr.complete_json_suffix_v2}
"""
guard = Guard.from_pydantic(output_class=Pet, prompt=prompt)

raw_response, validated_response, *rest = guard(
    openai.chat.completions.create,
    model="gpt-4",
    temperature=1.2
)

print(guard.history.last.tree)
