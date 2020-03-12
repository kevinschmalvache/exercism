def response(hey_bob):
    content = hey_bob.strip()
    question = False
    yell = False
    if not content:
        return "Fine. Be that way!"
    if content[-1] == '?':
        question = True
    if content.isupper():
        yell = True
    if question and yell:
        return "Calm down, I know what I'm doing!"
    if question:
        return "Sure."
    if yell:
        return "Whoa, chill out!"
    return "Whatever."