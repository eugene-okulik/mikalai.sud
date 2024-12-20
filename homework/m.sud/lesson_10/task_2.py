def repeat_me(funk):
    def wrapper(text, count=1):
        for _ in range(count):
            funk(text)

    return wrapper


@repeat_me
def example(text):
    print(text)


example('print me', count=2)
