import json

from celery import shared_task
import environ
import openai
from django.conf import settings

from ingest.models import FileModel
from generate.models import GenerateExecutionModel, GeneratedQuestionsModel

openai_api_key = settings.OPENAI_API_KEY

@shared_task
def generate_questions(file_options, generation_type, num_questions):
    # Here you would define the logic for your task. 
    # For simplicity, let's just simulate a long running process
    print(f"Processing {num_questions} questions with options: {file_options}, type: {generation_type}")
    

    # Get the file model first
    file_model = FileModel.objects.get(id=file_options)
    source_text = file_model.tesseract_text
    
    # Create the generate model
    generate_execution_instance = GenerateExecutionModel.objects.create(
        file_model_instance=file_model, 
        generation_type=generation_type)
    
    # Generate the questions
    generated_questions = generate_frq_openai(source_text, num_questions)
    
    # Add the generated questions to the database
    for i, question in enumerate(generated_questions):
        GeneratedQuestionsModel.objects.create(
            generate_execution_instance=generate_execution_instance, 
            question_text=question['question'], 
            question_text_context=question['context'],
            answer_text=question['answer'])
    
    return f"{num_questions} questions processed successfully."


def generate_frq_openai(source_text: str, num_questions: int) -> dict[int, dict[str, str]]:
    """ Uses OpenAI Model to generate FRQ questions based on source_text. """    
    client = openai.OpenAI(api_key=openai_api_key)


    example_question = """
        What lesson does the text teach? Text:\
    """
    example_context = """
        The Cat Burgler ran to the store. However, since his old days are behind him, he paid for his items instead of robbing the clerk. Overall he experiences a much happier life now that he is no longer stealing.
    """
    example_solution = """
        Following the law leads to a happier life.
    """
    example_json = {
        "question": example_question,
        "context": example_context,
        "answer": example_solution
    }
    
    questions = []
    for i in range(num_questions):
                    
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            response_format={ "type": "json_object" },
            messages=[
                {"role": "system", "content": "You are a an expert exam author. You have worked for the major exam companies such as LSAT, and the ACT. \
                    You are skilled in compiling Free Response (FRQ) questions. Such questions have a question (\"question\") and an answer (\"answer\").\
                        The question should always provide enough context to answer the question, but should not give away the solution directly.\
                        However, it is CRITICAL that you always respond in JSON so that computers can understand you!"},
                {"role": "user", "content": f"""
                    Generate a free response question. Your response should include a question, some contextual text for the question based on the source provided, and the proposed answer. Here is an example of a sample you could produce (text ommited).:
                    EXAMPLE: {json.dumps(example_json)}
                    Now, based on this following text, generate a question. Don't forget to include context from the source, and the answer, in the format shown in the example. Source text is as follows:
                    {source_text}
                    """},
            ]
        )
        try:
            result = json.loads(response.choices[0].message.content)
            print(json.dumps(result, indent=4))
            questions.append(result)
        except Exception as e:
            raise e
        
    return questions

