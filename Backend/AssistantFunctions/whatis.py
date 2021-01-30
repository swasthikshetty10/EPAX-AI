import wikipedia


def wiki(query: str):
    if 'who is' in query:
        query = query.replace("who is", '')
    elif 'what is' in query:
        query = query.replace("what is", '')
    results = wikipedia.search(query, results=1)
    result_summary = wikipedia.summary(results[0])
    result_title = results[0]
    result = result_summary.split(".")
    try:
        data = {"summary": f'{result[0]}. {result[1]}. {result[2]}.',
                "title": result_title,
                "result": results}
    except:
        try:
            data = {"summary": f'{result[0]}. {result[1]}.',
                    "title": result_title,
                    "result": results}
        except:
            data = {"summary": f'{result[0]}.',
                    "title": result_title,
                    "result": results}
    if len(data['summary']) > 100:
        return data
    else:
        return result
