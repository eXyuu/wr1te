def generate_banner(text):
    letter_art = {
        'A': ["  A  ", " A A ", "AAAAA", "A   A", "A   A"],
        #'A': ["@@@@@", "@   @", "@@@@@", "@   @", "@   @"],
        'B': ["BBBB ", "B   B", "BBBB ", "B   B", "BBBB "],
        'C': [" CCCC", "C     ", "C     ", "C     ", " CCCC"],
        'D': ["DDDD ", "D   D", "D   D", "D   D", "DDDD "],
        'E': ["EEEEE", "E     ", "EEEEE", "E     ", "EEEEE"],
        'F': ["FFFFF", "F     ", "FFFFF", "F     ", "F     "],
        '.': ["      ", "      ", "      ", "      ", "  .   "],
        ',': ["      ", "      ", "      ", "  ,   ", " .    "],
        ':': ["      ", "  :   ", "      ", "  :   ", "      "],
        ';': ["      ", "  ;   ", "      ", "  ;   ", " .    "],
        # Diğer harfler için gerekli ASCII sanatları ekleyebilirsiniz
    }

    banner_lines = []
    for line in range(5):
        banner_line = ""
        for char in text.upper():
            if char in letter_art:
                banner_line += letter_art[char][line] + " "
            else:
                banner_line += "     "  # Boş alan
        banner_lines.append(banner_line)

    return '\n'.join(banner_lines)

# Kullanıcıdan metin girişini alın
user_input = input("Metni girin: ")

# Metni banner yazı stiline dönüştürün
banner = generate_banner(user_input)

# Bannerı ekrana yazdırın
print(banner)
