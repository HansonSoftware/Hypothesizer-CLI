import openai
import json
from decouple import config

API_KEY = config("OPENAI_KEY")

openai.api_key = API_KEY

models = openai.Model.list()
print(models)