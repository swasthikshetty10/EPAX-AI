from howdoi import howdoi


def askhow(query):
    if 'how do i ' in query:
        query = query.replace("how do i ", '')

    if 'how to ' in query:
        query = query.replace("how to ", '')
    if 'how ' in query:
        query = query.replace("how ", '')
    if 'write ' in query:
        query = query.replace("write ", '')
    if 'use ' in query:
        query = query.replace("use ", '')
    # parser = howdoi.get_parser()
    # args = vars(parser.parse_args(query.split(' ')))
    # print(query)
    output = howdoi.howdoi(query)
    return output


#print(askhow("java while loop"))
#print(ask("python while loop")["link"])
