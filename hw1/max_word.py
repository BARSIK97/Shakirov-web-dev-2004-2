import re
def remove_punctuation(word):
    return re.sub(r'[^\w\s]', '', word)
def max_word():
    with open("C:/Users/shaki/OneDrive/Рабочий стол/Веб приложения/hw1/example.txt", 'r', encoding='utf-8') as file:
        content = file.read()
        words = re.findall(r'\b\w+\b', content, re.UNICODE) 
        words = [remove_punctuation(word) for word in words] 
        max_length = max(len(word) for word in words)  
        max_words = [word for word in words if len(word) == max_length]  
    for word in max_words:
        print(word)
max_word()