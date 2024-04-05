def reverse(text: str) -> str:
    """
    This function takes in a text as input and reverses the text

    Parameters
    ----------
    text: str
        Text to be reversed

    Returns
    -------
    str:
        Reversed word
    """
    # Base case
    if len(text) == 0:
        return ''  

    # Recursion
    return reverse(text[1:]) + text[0]


def is_palindrome(text: str) -> bool:
    """
    This function takes in a text as input and checks if it
    is a palindrome

    Parameters
    ----------
    text: str
        Text to be checked

    Returns
    -------
    bool:
        True if word is palindrome, false if it is not
    """
    text = text.strip("?,.! '").lower()

    # Base case
    if len(text) <= 1:
        return True

    # Recursion
    if text[0] != text[-1]:
        return False
    return is_palindrome(text[1:-1])