from openai import OpenAI, OpenAIError

try:
    client = OpenAI()
    thread = client.beta.threads.create()
except Exception as e:
    pass


def generate_answer(question):
    prompt = f'''
{question}
    '''

    message = client.beta.threads.messages.create(
        thread_id=thread.id,
        role="user",
        content=prompt
    )
    run = client.beta.threads.runs.create(
        thread_id=thread.id,
        assistant_id="asst_gpszyK5JK37zBQjKdD9jU9Ho",
        instructions=""
    )
    while True:
        run = client.beta.threads.runs.retrieve(
            thread_id=thread.id,
            run_id=run.id
        )
        if run.status == "completed":
            break

    messages = client.beta.threads.messages.list(
        thread_id=thread.id
    )
    first_message_value = messages.data[0].content[0].text.value
    return first_message_value
