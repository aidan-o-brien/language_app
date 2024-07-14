def get_video_segments(video_transcript):
    ## Find the nearest start times that are just past 30 seconds intervals
    indexes = []
    interval = 30
    start_times = [part['start'] for part in video_transcript]

    current_threshold = interval

    for i, num in enumerate(start_times):
        if num > current_threshold:
            indexes.append(i)
            current_threshold += interval

    ## Retrieve the section times that we want to show clips in
    section_times = [0]
    section_times += [video_transcript[idx]['start'] for idx in indexes]

    return section_times, indexes


def format_transcript(transcipt):

    text_sections = [section['text'] for section in transcipt]
    joined_text = " ".join(text_sections)
    joined_text = joined_text.replace("\n", " ")
    formatted_transcript = joined_text.replace("  ", " ")

    return formatted_transcript


def get_gpt3_response(client, prompt_context, prompt):
    response = client.chat.completions.create(
        messages=[
            {"role": "system", "content": prompt_context},
            {"role": "user", "content": prompt}
        ],
        model="gpt-3.5-turbo-0125"
    )
    
    return response.choices[0].message.content