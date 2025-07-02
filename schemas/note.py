def noteEntity(item)-> dict:
    return {
        "id":item['_id'],
        "title": item['title'],
        "content": item['content'],
        "important": item['important']
    }   

def notesEntity(items) -> list:
    return [noteEntity(item) for item in items]