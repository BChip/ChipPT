from langchain.chat_models import ChatOpenAI
from langchain.prompts.chat import (
    ChatPromptTemplate,
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate,
)
from langchain.chains import LLMChain
from langchain.schema import BaseOutputParser
import langchain

from langchain.cache import SQLiteCache

langchain.llm_cache = SQLiteCache(database_path=".langchain.db")


class CommaSeparatedListOutputParser(BaseOutputParser):  # type: List[str]
    """Parse the output of an LLM call to a comma-separated list."""

    def parse(self, text: str):
        """Parse the output of an LLM call."""
        return text.strip().split(", ")


template = """You are a helpful assistant who generates comma separated lists.
A user will pass in a category, and you should generate 5 objects in that category in a comma separated list.
ONLY return a comma separated list, and nothing more."""
system_message_prompt = SystemMessagePromptTemplate.from_template(template)
human_template = """[Instruction]: {question}
                    [Agent Description]: """
human_message_prompt = HumanMessagePromptTemplate.from_template(human_template)

chat_prompt = ChatPromptTemplate.from_messages(
    [system_message_prompt, human_message_prompt]
)
chain = LLMChain(
    llm=ChatOpenAI(
        # model_name="gpt-4",
        cache=True,
        temperature=0.0,
    ),
    prompt=chat_prompt,
    output_parser=CommaSeparatedListOutputParser(),
)

# execute nougat --markdown pdf './paper.pdf' -o './' in python
import os

if not (os.path.exists("paper.mmd")) and not (os.path.exists("paper.md")):
    os.system("nougat --markdown pdf './paper.pdf' -o './'")

# Rename paper.mdd to paper.md
if os.path.exists("paper.mmd"):
    os.rename("paper.mmd", "paper.md")

# Transform paper.md to paper.json

import markdown_to_json

# Read paper.md as string value
with open("paper.md", "r") as f:
    value = f.read()

# The simple way:
dictified = markdown_to_json.dictify(value)

# get the first key from dictified
title = list(dictified.keys())[0]


# flatten dictified
def flatten(d, parent_key="", sep="_"):
    items = []
    for k, v in d.items():
        new_key = parent_key + sep + k if parent_key else k

        if isinstance(v, dict):
            items.extend(flatten(v, new_key, sep=sep).items())
        else:
            items.append((new_key, v))

    return dict(items)


from docarray import Document, DocumentArray, dataclass
from docarray.typing import Image, Text
from typing import List


@dataclass
class Paper:
    title: Text
    content: List[Text]
    references: List[Text]


dictified = flatten(dictified)

# get values from dictified
content = list(dictified.values())

# concat content together

references = [
    value
    for key, value in dictified.items()
    if "References" in key or "Cited" in key or "Bibliography" in key
]

paper = Paper(title=title, content=content, references=references)

print(paper.title)
print("")
# loop through content
for c in paper.content:
    print(c)
    print("")

# loop through references
for r in paper.references:
    print(r)
    print("")
