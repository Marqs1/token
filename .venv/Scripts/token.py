import re


def word_tokenizer(text):
    # Ulepszone wyrażenie regularne, które lepiej radzi sobie z interpunkcją
    pattern = r'\b[\w\'-]+\b'
    tokens = re.findall(pattern, text)
    return tokens


# Testowanie tokenizatora
def test_tokenizer():
    tests = [
        ("Czy to działa? Sprawdźmy!", ["Czy", "to", "działa", "Sprawdźmy"]),
        ("NLP, czyli przetwarzanie języka naturalnego.", ["NLP", "czyli", "przetwarzanie", "języka", "naturalnego"]),
        ("Data 20/04/2021 powinna być tokenem.", ["Data", "20/04/2021", "powinna", "być", "tokenem"])
    ]

    pass_tests = True
    for i, (input_text, expected_output) in enumerate(tests):
        result = word_tokenizer(input_text)
        if result != expected_output:
            pass_tests = False
            print(f"Test {i + 1} FAILED. Input: '{input_text}'\nExpected: {expected_output}\nGot: {result}")

    if pass_tests:
        print("All tests passed successfully!")


# Przykładowe użycie
sample_text = "Tokenizacja: to ważny krok w NLP, np. w analizie sentymentu!"
tokens = word_tokenizer(sample_text)
print("Tokens:", tokens)

# Uruchomienie testów
test_tokenizer()
