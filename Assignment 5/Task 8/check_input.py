def check_input(user_input:str, wanted_type:type = str, check_text:bool = False, target_texts:list[str] = ["yes", "no"]):
    if check_text:
        return user_input in target_texts

    try:
        wanted_type(user_input)
    except ValueError:
        return False

    return True