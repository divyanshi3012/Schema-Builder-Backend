def paginate(cursor, limit: int = 10, offset: int = 0):
    return list(cursor.skip(offset).limit(limit))
