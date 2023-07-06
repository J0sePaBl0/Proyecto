import gradio as gr
import openai

openai.api_key = "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"

def openai_process_message(user_message):
    
    messages = [
        {
            "role": "system",
            "content": "Act like a personal assistant. You can respond to questions, translate sentences, summarize news, and give recommendations."
        }
    ]
    messages.append({"role": "user", "content": user_message})

    openai_response = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages, max_tokens=100)

    response_text = openai_response.choices[0].message.content
    messages.append({"role": "assistant", "content": response_text})
    
    return response_text
examples = [
    "Que es un chatbot?",
    "podrias definir que es una IA?",
    "dime cual seria una receta para hacer salsa bechamel?",
]
demo = gr.Interface(
    fn=openai_process_message,
    inputs=gr.Textbox(lines=5, label='Pregunta',placeholder='Escribe tu pregunta'),
    outputs=gr.Textbox(label='Respuesta'),
    examples=examples,
    title="Chatbot OpenAI API",
)
if __name__ == "__main__":
    demo.launch()
