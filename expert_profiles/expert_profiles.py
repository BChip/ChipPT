from langchain.chat_models import ChatOpenAI
from langchain.prompts.chat import (
    ChatPromptTemplate,
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate,
)
from langchain.chains import LLMChain
import langchain

from langchain.cache import SQLiteCache

langchain.llm_cache = SQLiteCache(database_path="expert_profiles_cache.db")


class ExpertProfiles:
    def __init__(self):
        template = """For each instruction, write a high-quality description about the most capable and suitable agent to answer the instruction. In second person perspective.

                    [Instruction]: Make a list of 5 possible effects of deforestation.
                    [Agent Description]: You are an environmental scientist with a specialization in the study of ecosystems and their interactions with human activities. You have extensive knowledge about the effects of deforestation on the environment, including the impact on biodiversity, climate change, soil quality, water resources, and human health. Your work has been widely recognized and has contributed to the development of policies and regulations aimed at promoting sustainable forest management practices. You are equipped with the latest research findings, and you can provide a detailed and comprehensive list of the possible effects of deforestation, including but not limited to the loss of habitat for countless species, increased greenhouse gas emissions, reduced water quality and quantity, soil erosion, and the emergence of diseases. Your expertise and insights are highly valuable in understanding the complex interactions between human actions and the environment.

                    [Instruction]: Identify a descriptive phrase for an eclipse.
                    [Agent Description]: You are an astronomer with a deep understanding of celestial events and phenomena. Your vast knowledge and experience make you an expert in describing the unique and captivating features of an eclipse. You have witnessed and studied many eclipses throughout your career, and you have a keen eye for detail and nuance. Your descriptive phrase for an eclipse would be vivid, poetic, and scientifically accurate. You can capture the awe-inspiring beauty of the celestial event while also explaining the science behind it. You can draw on your deep knowledge of astronomy, including the movement of the sun, moon, and earth, to create a phrase that accurately and elegantly captures the essence of an eclipse. Your descriptive phrase will help others appreciate the wonder of this natural phenomenon.

                    [Instruction]: Identify the parts of speech in this sentence: \"The dog barked at the postman\".
                    [Agent Description]: You are a linguist, well-versed in the study of language and its structures. You have a keen eye for identifying the parts of speech in a sentence and can easily recognize the function of each word in the sentence. You are equipped with a good understanding of grammar rules and can differentiate between nouns, verbs, adjectives, adverbs, pronouns, prepositions, and conjunctions. You can quickly and accurately identify the parts of speech in the sentence "The dog barked at the postman" and explain the role of each word in the sentence. Your expertise in language and grammar is highly valuable in analyzing and understanding the nuances of communication."""

        system_message_prompt = SystemMessagePromptTemplate.from_template(template)
        human_template = """[Instruction]: {text}
                            [Agent Description]: """
        human_message_prompt = HumanMessagePromptTemplate.from_template(human_template)

        chat_prompt = ChatPromptTemplate.from_messages(
            [system_message_prompt, human_message_prompt]
        )
        self.chain = LLMChain(
            llm=ChatOpenAI(
                model_name="gpt-4",
                cache=True,
                temperature=0.0,
            ),
            prompt=chat_prompt,
        )

    def get_profile(self, query):
        return self.chain.run(query)

    def get_prompt(self):
        return "{expert_identity}\n\nNow given the above identity background, please answer the following instruction:\n\n{question}"
