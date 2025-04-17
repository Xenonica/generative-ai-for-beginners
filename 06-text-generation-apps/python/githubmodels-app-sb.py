import os
from azure.ai.inference import ChatCompletionsClient
from azure.ai.inference.models import SystemMessage, UserMessage
from azure.core.credentials import AzureKeyCredential

token = os.environ["GITHUB_TOKEN"]
endpoint = "https://models.inference.ai.azure.com"

model_name = "gpt-4o"

client = ChatCompletionsClient(
    endpoint=endpoint,
    credential=AzureKeyCredential(token),
)

prompt = input("Ask your questions on python language to your study buddy: ")
system_message = """
You are an expert on the python language.

Whenever certain questions are asked, you need to provide response in below format.

- Concept
- Example code showing the concept implementation
- explanation of the example and how the concept is done for the user to understand better.

If the question is not related to python language, DO NOT answer the question. Only answer to questions that are in python language only"""

response = client.complete(
    messages=[
        {
            "role": "system",
            "content": system_message,
        },
        {
            "role": "user",
            "content": prompt,
        },
    ],
    model=model_name,
    # Optional parameters
    temperature=1.,
    max_tokens=1000,
    top_p=1.    
)

print(response.choices[0].message.content)