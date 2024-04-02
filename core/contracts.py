USER_DATA_SCHEMA = {
    "type": "object",
    "properties": {
        "id": {"type": "number"},
        "email": {"type": "string"},
        "first_name": {"type": "string"},
        "last_name": {"type": "string"},
        "avatar": {"type": "string"},
    },
    "required": ["id", "email", "first_name", "last_name"],
    "unrequired": ["avatar"]
}
USER_RESOURCE_SCHEMA = {
    "type": "object",
    "properties": {
        "id": {"type": "number"},
        "year": {"type": "number"},
        "name": {"type": "string"},
        "color": {"type": "string"},
        "pantone_value": {"type": "string"}
    },
    "required": ["id", "year", "name", "color", "pantone_value"]
}