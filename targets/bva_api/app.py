def validate_username_length(username: str) -> str:
    """
    Validate a username against length rules.

    Returns:
        "200 OK"            if 5 <= len(username) <= 30
        "422 TOO_SHORT"     if len(username) < 5
        "422 TOO_LONG"      if len(username) > 30
    """
    if len(username) < 5:
        return "422 TOO_SHORT"
    elif len(username) > 30:
        return "422 TOO_LONG"
    else:
        return "200 OK"
