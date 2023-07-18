def generate_banner(text):
    letter_art = {
        'A': ["  A  ", " A A ", "AAAAA", "A   A", "A   A"],
        #'A': ["@@@@@", "@   @", "@@@@@", "@   @", "@   @"],
        'B': ["BBBB ", "B   B", "BBBB ", "B   B", "BBBB "],
        'C': [" CCCC", "C     ", "C     ", "C     ", " CCCC"],
        'D': ["DDDD ", "D   D", "D   D", "D   D", "DDDD "],
        'E': ["EEEEE", "E     ", "EEEEE", "E     ", "EEEEE"],
        'F': ["FFFFF", "F     ", "FFFFF", "F     ", "F     "],
        'G': [' GGG ', 'G    ', 'G  GG', 'G   G', ' GGGG'],
        'H': ['H   H', 'H   H', 'HHHHH', 'H   H', 'H   H'],
        'I': ['IIIII', '  I  ', '  I  ', '  I  ', 'IIIII'],
        'J': ['JJJJJ', '   J ', '   J ', 'J  J ', ' JJ  '],
        'K': ['K   K', 'K  K ', 'KKK  ', 'K  K ', 'K   K'],
        'L': ['L    ', 'L    ', 'L    ', 'L    ', 'LLLLL'],
        'M': ['M   M', 'MM MM', 'M M M', 'M   M', 'M   M'],
        'N': ['N   N', 'NN  N', 'N N N', 'N  NN', 'N   N'],
        'O': [' OOO ', 'O   O', 'O   O', 'O   O', ' OOO '],
        'P': ['PPPP ', 'P   P', 'PPPP ', 'P    ', 'P    '],
        'Q': [' QQQ ', 'Q   Q', 'Q   Q', ' QQQQ', '    Q'],
        'R': ['RRRR ', 'R   R', 'RRRR ', 'R  R ', 'R   R'],
        'S': [' SSSS', 'S    ', ' SSS ', '    S', 'SSSS '],
        'T': ['TTTTT', '  T  ', '  T  ', '  T  ', '  T  '],
        'U': ['U   U', 'U   U', 'U   U', 'U   U', ' UUU '],
        'V': ['V   V', 'V   V', 'V   V', ' V V ', '  V  '],
        'W': ['W   W', 'W   W', 'W W W', 'WW WW', 'W   W'],
        'X': ['X   X', ' X X ', '  X  ', ' X X ', 'X   X'],
        'Y': ['Y   Y', ' Y Y ', '  Y  ', '  Y  ', '  Y  '],
        'Z': ['ZZZZZ', '   Z ', '  Z  ', ' Z   ', 'ZZZZZ'],
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
