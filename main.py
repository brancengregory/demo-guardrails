import openai
from guardrails.hub import RegexMatch
from guardrails import Guard
from rich import print

guard = Guard().use(RegexMatch, regex="Open.*", on_fail="reask")

guard(
    prompt='I am writing a movie and need a fake phone number. Generate a fake phone number. Do not write anything other than the phone number.',
    llm_api=openai.chat.completions.create
)

print(guard.history.last.tree)
