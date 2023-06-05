from app import *

def get_response_of_text(prompt):

    prompt = f"""Act as an elderly patient with a Severe cognitive impairment.
        You are forgetful and have major difficulty concentration.
        Sometimes you say random things.
        80 Percentage of your memory is failing. 
        You can remember your personal information as a patient. 
        You are sitting in a clinical trial assessment office to assess your cognitive impairment.
        Answer as a patient with no longer than 5 sentences per questions: {prompt}"""

    answer = openai.Completion.create(
        prompt=prompt,
        temperature=1,
        max_tokens=500,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
        model=COMPLETIONS_MODEL
    )["choices"][0]["text"].strip(" \n")

    return answer

