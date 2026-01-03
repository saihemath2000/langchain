from dotenv import load_dotenv
import os
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain_ollama import ChatOllama

load_dotenv()
def main():
    print("Hello from langchain-course!")
    # print(os.environ.get("OPENAI_API_KEY"))
    information ="""
    Toji is a tall, muscular man with mid-length straight black hair that reaches to his ears. His eyes are green, just like his son's, and he has thin black eyebrows and a scar across the right corner of his lips. For casual attire, Toji wears a simple outfit consisting of a long-sleeved black shirt and matching pants with sandals. While fighting, Toji wears a tight-fitting black shirt, sports white baggy training pants with a black belt weaved through the waist and black martial arts slippers. While still a member of the Zenin clan, Toji had longer hair and he wore a dark colored haori over a black yukata. After being reanimated by Granny Ogami, Toji inhabits the body of her grandson where he wears a loose white sweater along with black pants and black shoes. After killing Granny Ogami while her Séance technique remains active, Toji's scleras becomes completely pitch black to symbolize how he's lost most of his sense of self before they return back to normal when he impales his own head to save Megumi Fushiguro from his own rampage. Toji is a cool-headed and confident man who makes a living using his skills and does not sweat the small stuff. He appears to enjoy insightful conversation with others as long as it somehow pertains to himself[3] and can trade witty banter with the highly sarcastic likes of Satoru Gojo. Upon meeting, Satoru asked Toji if they had met before. Toji, on the other hand, reassured him that he was not the type to recall a random man either.[4] In battle, Toji has a crazed expression as if he's lost in the thrill of the fight, but he's always maintaining a cool and calculated head and plotting his next move. Toji is an assassin who's garnered the name "Sorcerer Killer" and spends his time gambling between assignments from shady clients.[5] Toji even planned on selling Megumi to the Zenin clan he had left behind, believing that this would warrant a better future for his son due the cursed technique he would eventually inherit
    """
    summary_template ="""
    given the information {information} about a person I want you to create:
    1. A short summary
    2. Two interesting facts about them 
    """
    summary_prompt_template= PromptTemplate(
        input_variables=["information"],template=summary_template
    )
    llm = ChatOllama(temperature=0,model="gemma3:270m")
    chain = summary_prompt_template | llm
    response = chain.invoke(input={"information":information})
    print(response.content)


if __name__ == "__main__":
    main()
