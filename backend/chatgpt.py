import openai

def query_chatgpt(prompt, api_key):
    try:
        openai.api_key = api_key
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}]
        )
        return response['choices'][0]['message']['content']
    except openai.error.OpenAIError as e:
        return f"OpenAI API error: {e}"
    except KeyError:
        return "Unexpected response format from OpenAI API"
    except Exception as e:
        return f"An unexpected error occurred: {e}"
