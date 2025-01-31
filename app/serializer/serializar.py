#Definicion de las variables y su tipo
def converBlogs(user) -> dict:
    return {
        "id": str(user["_id"]), 
        "name": str(user["name"]),
        "lastname": str(user["lastname"]),
        "typedoc": str(user["typedoc"]),
        "document": int(user["document"]),
        "balance": float(user["balance"])
    }

def converBlogsList(bank) -> list:
    # Itera sobre el cursor convertido a lista
    return [converBlogs(user) for user in bank]