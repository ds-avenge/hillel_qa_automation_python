adwentures_of_tom_sawer = """\
Tom gave up the brush with reluctance in his .... face but alacrity
in his heart. And while
the late steamer
"Big Missouri" worked ....
and sweated
in the sun,
the retired artist sat on a barrel in the .... shade close by, dangled his legs,
munched his apple, and planned the slaughter of more innocents.
There was no lack of material;
boys happened along every little while;
they came to jeer, but .... remained to whitewash. ....
By the time Ben was fagged out, Tom had traded the next chance to Billy Fisher for
a kite, in good repair;
and when he played
out, Johnny Miller bought
in for a dead rat and a string to swing it with—and so on, and so on,
hour after hour. And when the middle of the afternoon came, from being a
poor poverty, stricken boy in the .... morning, Tom was literally
rolling in wealth."""

##  ПЕРЕЗАПИСУЙТЕ зміст змінної adwentures_of_tom_sawer у завданнях 1-3
# task 01 ==
""" Дані у строці adwentures_of_tom_sawer розбиті випадковим чином, через помилку.
треба замінити кінець абзацу на пробіл .replace("\n", " ")"""
print("--- Task 01 ---")
adwentures_of_tom_sawer = adwentures_of_tom_sawer.replace("\n", " ")
print(adwentures_of_tom_sawer)

# task 02 ==
""" Замініть .... на пробіл
"""
print("\n--- Task 02 ---")
adwentures_of_tom_sawer = adwentures_of_tom_sawer.replace("....", " ")
print(adwentures_of_tom_sawer)

# task 03 ==
""" Зробіть так, щоб у тексті було не більше одного пробілу між словами.
"""
print("\n--- Task 03 ---")
adwentures_of_tom_sawer = " ".join(adwentures_of_tom_sawer.split())
print(adwentures_of_tom_sawer)

# task 04
""" Виведіть, скількі разів у тексті зустрічається літера "h"
"""
print("\n--- Task 04 ---")
h_count = adwentures_of_tom_sawer.count("h")
print(f"Літера \"h\" зустрічається {h_count} разів")

# task 05
""" Виведіть, скільки слів у тексті починається з Великої літери?
"""
print("\n--- Task 05 ---")
words = adwentures_of_tom_sawer.split()
cleaned_words = [word.strip('"') for word in words]
capitalized_words = [word for word in cleaned_words if word and word[0].isupper()]
capitalized_words_count = len(capitalized_words)
print(f"У тексті {capitalized_words_count} слів, які починаються з великої літери.")

# task 06
""" Виведіть позицію, на якій слово Tom зустрічається вдруге
"""
print("\n--- Task 06 ---")
first_index = adwentures_of_tom_sawer.find("Tom")
second_index = adwentures_of_tom_sawer.find("Tom", first_index + len("Tom"))
print(second_index)

# task 07
""" Розділіть змінну adwentures_of_tom_sawer по кінцю речення.
Збережіть результат у змінній adwentures_of_tom_sawer_sentences
"""
print("\n--- Task 07 ---")
adwentures_of_tom_sawer_sentences = adwentures_of_tom_sawer.split(".")
print(adwentures_of_tom_sawer_sentences)

# task 08
""" Виведіть четверте речення з adwentures_of_tom_sawer_sentences.
Перетворіть рядок у нижній регістр.
"""
print("\n--- Task 08 ---")
print(adwentures_of_tom_sawer_sentences[3].lower().strip())

# task 09
""" Перевірте чи починається якесь речення з "By the time".
"""
print("\n--- Task 09 ---")
print(any(sentence.strip().startswith("By the time") for sentence in adwentures_of_tom_sawer_sentences))

# task 10
""" Виведіть кількість слів останнього речення з adwentures_of_tom_sawer_sentences.
"""
print("\n--- Task 10 ---")
adwentures_of_tom_sawer_sentences = adwentures_of_tom_sawer.split(".")
adwentures_of_tom_sawer_sentences.pop()

last_sentence_word_count = len(adwentures_of_tom_sawer_sentences[-1].split())
print(f"Кількість слів в останньому реченні: {last_sentence_word_count}")
