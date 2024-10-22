USER_DATA_SCHEMA = {
    "type": "object",
    "properties": {
        "id": {"type":"number"},
        "first_name": {"type":"string"},
        "last_name": {"type":"string"},
        "email": {"type": "string"},
        "avatar": {"type":"string"}
    },
    "required":["id","email","first_name","last_name","avatar"]
}