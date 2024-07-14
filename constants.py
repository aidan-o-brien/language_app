OPENAI_API_KEY = "sk-proj-YFaX3sGzqTF1iyHP7sOpT3BlbkFJjgzAvsgGWl189IX5J8iP"

PROMPT_CONTEXT = """
You are helping me learn French.
I listen to some audio that has a transcript.
I am going to give you the transcript.
I want you to generate 5 multiple choice questions that tests my understanding of the audio.
For each question, I want there to be only one correct answer and the rest are incorrect. 
For each question, I want the format that you provide to be:
Question 1: <question>

A - <option>

B - <option>

C - <option>

D - <option>

After you have listed all of the questions using the above format, I want you to provide the answers
to all of the questions like this:

ANSWERS: 1A, 2D, 3C, 4A, 5B.

The transcript is
"""