def convert(text):
    text = text.replace(":)", "🙂").replace(":(", "🙁")
    return text

def main():
    usertext = input("")
    result = convert(usertext)
    print(result)

main()
