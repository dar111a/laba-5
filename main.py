import re
import langid

def read_first_sentence(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
            # Виділення першого речення
            first_sentence = re.split(r'[.!?]', content)[0].strip()
            print("Перше речення:", first_sentence)
            return first_sentence
    except FileNotFoundError:
        print("Помилка: файл не знайдено.")
        return None
    except Exception as e:
        print(f"Помилка: {e}")
        return None

def process_text(text):
    # Виділення слів та видалення знаків пунктуації
    words = re.findall(r'\b\w+\b', text)

    # Розділення слів за мовами
    langid.set_languages(['uk', 'en'])
    ukrainian_words = [word for word in words if langid.classify(word)[0] == 'uk']
    english_words = [word for word in words if langid.classify(word)[0] == 'en']

    # Сортування та вивід українських слів
    ukrainian_words = sorted(ukrainian_words, key=lambda x: (x.lower(), x))
    print("\nУкраїнські слова (в алфавітному порядку):", ukrainian_words)

    # Сортування та вивід англійських слів
    english_words = sorted(english_words, key=lambda x: (x.lower(), x))
    print("Англійські слова (в алфавітному порядку):", english_words)

    print("\nКількість слів:", len(words))

if __name__ == "__main__":
    file_path = "input.txt"  # Шлях до файлу з текстом
    text = read_first_sentence(file_path)
    if text:
        process_text(text)
