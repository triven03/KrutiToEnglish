class KrutidevToUnicode:
    CHARS_KD = [
        "ñ", "Q+Z", "sas", "aa", ")Z", "ZZ", "‘", "’", "“", "”",

        "å", "ƒ", "„", "…", "†", "‡", "ˆ", "‰", "Š", "‹",

        "¶+", "d+", "[+k", "[+", "x+", "T+", "t+", "M+", "<+", "Q+", ";+", "j+", "u+",
        "Ùk", "Ù", "ä", "–", "—", "é", "™", "=kk", "f=k",

        "à", "á", "â", "ã", "ºz", "º", "í", "{k", "{", "=", "«",
        "Nî", "Vî", "Bî", "Mî", "<î", "|", "K", "}",
        "J", "Vª", "Mª", "<ªª", "Nª", "Ø", "Ý", "nzZ", "æ", "ç", "Á", "xz", "#", ":",

        "v‚", "vks", "vkS", "vk", "v", "b±", "Ã", "bZ", "b", "m", "Å", ",s", ",", "_",

        "ô", "d", "Dk", "D", "[k", "[", "x", "Xk", "X", "Ä", "?k", "?", "³",
        "pkS", "p", "Pk", "P", "N", "t", "Tk", "T", ">", "÷", "¥",

        "ê", "ë", "V", "B", "ì", "ï", "M+", "<+", "M", "<", ".k", ".",
        "r", "Rk", "R", "Fk", "F", ")", "n", "/k", "èk", "/", "Ë", "è", "u", "Uk", "U",

        "i", "Ik", "I", "Q", "¶", "c", "Ck", "C", "Hk", "H", "e", "Ek", "E",
        ";", "¸", "j", "y", "Yk", "Y", "G", "o", "Ok", "O",
        "'k", "'", "\"k", "\"", "l", "Lk", "L", "g",

        "È", "z",
        "Ì", "Í", "Î", "Ï", "Ñ", "Ò", "Ó", "Ô", "Ö", "Ø", "Ù", "Ük", "Ü",

        "‚", "ks", "kS", "k", "h", "q", "w", "`", "s", "S",
        "a", "¡", "%", "W", "•", "·", "∙", "·", "~j", "~", "\\", "+", " ः",
        "^", "*", "Þ", "ß", "(", "¼", "½", "¿", "À", "¾", "A", "-", "&", "&", "Œ", "]", "~ ", "@"
    ]

    CHARS_UNICODE = [
        "॰", "QZ+", "sa", "a", "र्द्ध", "Z", "\"", "\"", "'", "'",

        "०", "१", "२", "३", "४", "५", "६", "७", "८", "९",

        "फ़्", "क़", "ख़", "ख़्", "ग़", "ज़्", "ज़", "ड़", "ढ़", "फ़", "य़", "ऱ", "ऩ",
        "त्त", "त्त्", "क्त", "दृ", "कृ", "न्न", "न्न्", "=k", "f=",

        "ह्न", "ह्य", "हृ", "ह्म", "ह्र", "ह्", "द्द", "क्ष", "क्ष्", "त्र", "त्र्",
        "छ्य", "ट्य", "ठ्य", "ड्य", "ढ्य", "द्य", "ज्ञ", "द्व",
        "श्र", "ट्र", "ड्र", "ढ्र", "छ्र", "क्र", "फ्र", "र्द्र", "द्र", "प्र", "प्र", "ग्र", "रु", "रू",

        "ऑ", "ओ", "औ", "आ", "अ", "ईं", "ई", "ई", "इ", "उ", "ऊ", "ऐ", "ए", "ऋ",

        "क्क", "क", "क", "क्", "ख", "ख्", "ग", "ग", "ग्", "घ", "घ", "घ्", "ङ",
        "चै", "च", "च", "च्", "छ", "ज", "ज", "ज्", "झ", "झ्", "ञ",

        "ट्ट", "ट्ठ", "ट", "ठ", "ड्ड", "ड्ढ", "ड़", "ढ़", "ड", "ढ", "ण", "ण्",
        "त", "त", "त्", "थ", "थ्", "द्ध", "द", "ध", "ध", "ध्", "ध्", "ध्", "न", "न", "न्",

        "प", "प", "प्", "फ", "फ्", "ब", "ब", "ब्", "भ", "भ्", "म", "म", "म्",
        "य", "य्", "र", "ल", "ल", "ल्", "ळ", "व", "व", "व्",
        "श", "श्", "ष", "ष्", "स", "स", "स्", "ह",

        "ीं", "्र",
        "द्द", "ट्ट", "ट्ठ", "ड्ड", "कृ", "भ", "्य", "ड्ढ", "झ्", "क्र", "त्त्", "श", "श्",

        "ॉ", "ो", "ौ", "ा", "ी", "ु", "ू", "ृ", "े", "ै",
        "ं", "ँ", "ः", "ॅ", "ऽ", "ऽ", "ऽ", "ऽ", "्र", "्", "?", "़", ":",
        "‘", "’", "“", "”", ";", "(", ")", "{", "}", "=", "।", ".", "-", "µ", "॰", ",", "् ", "/"
    ]

    @staticmethod
    def do_convert(krutidevPart):
        processPart = str(krutidevPart)
        if processPart != "":
            for input_symbol_idx in range(0, len(KrutidevToUnicode.CHARS_KD)):
                idx = 0
                while idx > -1:
                    processPart = processPart.replace(str(KrutidevToUnicode.CHARS_KD[input_symbol_idx]),
                                                      str(KrutidevToUnicode.CHARS_UNICODE[input_symbol_idx]))
                    idx = processPart.find(str(KrutidevToUnicode.CHARS_KD[input_symbol_idx]))

            # Code for Replacing five Special glyphs

            # Code for Glyph1 : ± (reph+anusvAr)

            processPart = processPart.replace(u'±', u"Zं")

            # Glyp2: Æ
            # code for replacing "f" with "ि" and correcting its position too. (moving it one position forward)

            processPart = processPart.replace(u'Æ', u"र्f")

            position_of_i = processPart.find(u'f')
            while position_of_i > -1:
                charecter_next_to_i = processPart[position_of_i + 1]
                charecter_to_be_replaced = u"f" + charecter_next_to_i
                processPart = processPart.replace(charecter_to_be_replaced, charecter_next_to_i + u"ि")
                position_of_i = processPart.find(u'f', position_of_i + 1)

            # Glyph3 & Glyph4: Ç  É
            # code for replacing "fa" with "िं"  and correcting its position too.(moving it two positions forward)

            processPart = processPart.replace(u'Ç', u"fa")
            processPart = processPart.replace(u'É', u"र्fa")

            position_of_i = processPart.find(u'fa')
            while position_of_i > -1:
                charecter_next_to_ip2 = processPart[position_of_i + 2]
                charecter_to_be_replaced = u"fa" + charecter_next_to_ip2
                processPart = processPart.replace(charecter_to_be_replaced, charecter_next_to_ip2 + u"िं")
                position_of_i = processPart.find(u'fa', position_of_i + 1)

            # Glyph5: Ê
            # code for replacing "h" with "ी"  and correcting its position too.(moving it one positions forward)

            processPart = processPart.replace(str(u'Ê'), str(u"ीZ"))

            # End of Code for Replacing four Special glyphs

            # following loop to eliminate 'chhotee ee kee maatraa' on half-letters as a result of above transformation.
            position_of_wrong_ee = processPart.find(str(u"ि्"))
            while position_of_wrong_ee > -1:
                consonent_next_to_wrong_ee = processPart[position_of_wrong_ee + 2]
                charecter_to_be_replaced = u"ि्" + consonent_next_to_wrong_ee
                processPart = processPart.replace(charecter_to_be_replaced, u"्" + consonent_next_to_wrong_ee + u"ि")
                position_of_wrong_ee = processPart.find(u"ि्", position_of_wrong_ee + 2)

            # Eliminating reph "Z" and putting 'half - r' at proper position for this.
            set_of_matras = u"अ आ इ ई उ ऊ ए ऐ ओ औ ा ि ी ु ू ृ े ै ो ौ ं : ँ ॅ"
            position_of_R = processPart.find(u"Z")
            while position_of_R > -1:
                probable_position_of_half_r = position_of_R - 1
                charecter_at_probable_position_of_half_r = processPart[probable_position_of_half_r]
                print("word",charecter_at_probable_position_of_half_r)
                print("processPart",processPart)

                # trying to find non-maatra position left to current O (ie, half -r).
                while set_of_matras.find(charecter_at_probable_position_of_half_r) >=0:
                    probable_position_of_half_r = probable_position_of_half_r - 1
                    charecter_at_probable_position_of_half_r = processPart[probable_position_of_half_r]

                    print("probable_position_of_half 137",probable_position_of_half_r)
                    print("char",charecter_at_probable_position_of_half_r)

                charecter_to_be_replaced = processPart[
                    probable_position_of_half_r : (position_of_R)]
                print("position of r 142 and R", probable_position_of_half_r,position_of_R)
                print("charecter_to_be_replaced 143", charecter_to_be_replaced)

                new_replacement_string = u"र्" + charecter_to_be_replaced

                charecter_to_be_replaced = charecter_to_be_replaced + u"Z"

                print("charecter_to_be_replaced 147", charecter_to_be_replaced)
                print("before",processPart)

                processPart = processPart.replace(str(charecter_to_be_replaced), str(new_replacement_string))
                print("after", processPart)
                position_of_R = processPart.find(str("uZ"))
                print("positio r",position_of_R)

        return processPart

    @staticmethod
    def convert_to_unicode(krutidevString):
        unicodeString = ''

        text_size = len(krutidevString)
        sthiti1 = 0
        sthiti2 = 0
        chale_chalo = 1
        max_text_size = 6000

        while chale_chalo == 1:
            sthiti1 = sthiti2

            if sthiti2 < (text_size - max_text_size):
                sthiti2 += max_text_size
                while krutidevString[sthiti2] != ' ':
                    sthiti2 -= 1
            else:
                sthiti2 = text_size
                chale_chalo = 0

            modifiedSubstring = krutidevString[sthiti1:sthiti2]
            unicodeString += KrutidevToUnicode.do_convert(modifiedSubstring)

        return unicodeString.strip()

    @staticmethod
    def toUnicode(word):
        if not len(word):
            return " "
        # letter = ord(word[0])
        # if 33 <= letter <= 127:
        #     return KrutidevToUnicode.convert_to_unicode(word)
        # else:
        #     return wor
        word= word.replace("-","")
        return KrutidevToUnicode.convert_to_unicode(word)
k = KrutidevToUnicode()
word="lr-h'k"

print(k.toUnicode(word))