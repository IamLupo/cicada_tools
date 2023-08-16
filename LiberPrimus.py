from CicadaUtils import Cicada
import abc

class Translation(abc.ABC):
    """
        Abstract translation.
    """

    @abc.abstractmethod
    def decrypt(self, page):
        """
            Decrypts.
        """

        # Do nothing
        pass

class SimpleTranslation(Translation):
    """
        Represents simple translation.
    """

    def __init__(self, atbash=False, shift=0, prime_substruction=False, skip_indices=None):
        """
            Initializes a new instance.
        """

        # Save members
        self.atbash = atbash
        self.shift = shift
        self.prime_substruction = prime_substruction
        self.skip_indices = set() if skip_indices is None else set([ i+1 for i in skip_indices ])

    def decrypt(self, page):
        """
            Decrypts.
        """

        # Decrypt page
        return Cicada.runes_to_latin(page, atbash=self.atbash, shifts=self.shift, prime_substruction=self.prime_substruction, interrupt_indexes=self.skip_indices)

class VigenereTranslation(Translation):
    """
        Represents Vigenere decryption translation.
    """

    def __init__(self, key, skip_indices=None):
        """
            Initializes a new instancde.
        """

        # Save parameters
        self.key = key
        self.skip_indices = set() if skip_indices is None else set([ i+1 for i in skip_indices ])

    def decrypt(self, page):
        """
            Decrypts.
        """

        # Decrypt page
        return Cicada.vigenere_decrypt(page, key=self.key, interrupt_indexes=self.skip_indices)

class UnsolvedTranslation(Translation):
    """
        Represents an unsolved translation.
    """

    def decrypt(self, page):
        """
            Decrypts.
        """

        # Unsolved
        return '<CURRENTLY UNSOLVED>'

class LiberPrimusPages(object):
    """
        Represents Liber Primus pages and their translation methods.
    """

    PAGES = [
        ('''
ᚱ-ᛝᚱᚪᛗᚹ.ᛄᛁᚻᛖᛁᛡᛁ-ᛗᚫᚣᚹ-ᛠᚪᚫᚾ-/
ᚣᛖᛈ-ᛄᚫᚫᛞ.ᛁᛉᛞᛁᛋᛇ-ᛝᛚᚱᛇ-ᚦᚫᛡ/
-ᛞᛗᚫᛝ-ᛇᚫ-ᛄᛁ-ᛇᚪᛡᛁ.ᛇᛁᛈᛇ-ᚣᛁ-ᛞ/
ᛗᚫᛝᚻᛁᚳᛟᛁ.ᛠᛖᛗᚳ-ᚦᚫᛡᚪ-ᛇᚪᛡᚣ.ᛁᛉ/
ᛋᛁᚪᛖᛁᛗᛞᛁ-ᚦᚫᛡᚪ-ᚳᚠᚣ.ᚳᚫ-ᛗᚫᛇ-ᛁᚳᛖᛇ-ᚫ/
ᚪ-ᛞᛚᚱᚹᛁ-ᚣᛖᛈ-ᛄᚫᚫᛞ.ᚫᚪ-ᚣᛁ-ᚾᛁᛈᛈᚱᛟᛁ-/
ᛞᚫᛗᛇᚱᛖᛗᛁᚳ-ᛝᛖᚣᛖᛗ.ᛁᛖᚣᛁᚪ-ᚣᛁ-ᛝᚫ/
ᚪᚳᛈ-ᚫᚪ-ᚣᛁᛖᚪ-ᛗᛡᚾᛄᛁᚪᛈ.ᛠᚫᚪ-ᚱᚻᚻ-ᛖ/
ᛈ-ᛈᚱᛞᚪᛁᚳ./
        ''', SimpleTranslation(atbash=True)),

        ('''
ᚢᛠᛝᛋᛇᚠᚳ.ᚱᛇᚢᚷᛈᛠᛠ-ᚠᚹᛉ/
ᛏᚳᛚᛠ-ᚣᛗ-ᛠᛇ-ᛏᚳᚾᚫ-ᛝᛗᛡ/
ᛡᛗᛗᚹ-ᚫᛈᛞᛝᛡᚱ-ᚩᛠ-ᛡᛗᛁ-ᚠᚠ-/
ᛖᚢᛝ-ᛇᚢᚫ.ᚣᛈ-ᚱᚫ-ᛁᛈᚫ-ᚳᚫ-ᚫᚾᚹ-ᛒᛉᛗᛞ/
-ᚱᛡᛁ-ᚠᛈᚳ-ᛇᛇᚫᚳ-ᚱᚦᛈ-ᚠᛄᛗᚩ-ᛇᚳᚹᛡ-ᛒᚫᚹ-/
ᛒᛠᛚᛋ-ᚱᚣ-ᛄᚫ-ᚱ-ᛗᚳᚦᛇᚫᛏᚳᛈᚹ-ᛗᚷᛇ.ᚳ/
ᛝᛈᚢ-ᛇᚳ-ᚱᛖᚹ-ᛡᛈᛁ-ᛒᚣᛒᛉ-ᚠᛚᛁᚱ-ᚱᛗ-ᚳᚷ/
ᛒ-ᚣᚱ-ᚳᚠᚢ-ᚦᛈᛡᛄᚹᛏᚠᛠ-ᛄᚷᛒ-ᚫᚦᚠᚠᛠ/
ᛈᚦ-ᛈᚠᚪᛉ-ᛄᛗᛖᛈᛝᛋᚩᛋᛗ-ᚹᛇᛄᛚ-ᚹᛉᚢᚦ/
ᚫᚹᛗᚦ-ᛞᚣᛄᚳ-ᛋᛡᛉᚩᛝᚱᛗᛒᚹ-ᚱᛗᛁ-ᛞᚣᛄ/
ᚳ-ᛉᚻᚢᚣᛈᛚ.ᛄᛝᚣᛗᚠᛄᛈᛇᚢᛡ-ᚹᛇᛄ-ᛞ/
ᚹᛉᚢ-ᚪᛚᚪᛋᛗᛡᛇᛉ-ᚫᛗ-ᛡᛗᛁ-ᛈᚣ-ᚫᛗᚢᚠ/
%
.ᛗᚣ-ᚣᛇ-ᚫᛉᚱᛄᛋᛖ-ᛖᚹᚾ-ᛞᛄᚢᛋᛉᚣᛏ/
ᛖᛏᛗ-ᛇᚱᚣ-ᛞᛋ-ᚾᛖᚫᛞᛡ-ᛈᛒᚢᚾᛠᛝᛄᛡ/
ᚫ-ᛄᚷᛒ-ᛈᚦᛉ-ᛈᚾᚹᚹᛁᛚᛗᚫ.ᛚᛈᛒᚢᚩᛠᛡ-ᚱ/
ᛡᛠᚠ-ᚱᚱᛇᛄᛗ-ᚱᛗᛁ-ᛞᚣᛄ-ᚻᛚᚠᚢ-ᛄᚢᛡᛚᚦ/
ᛠ-ᛇᛄᚩᛇᚱᚱᛗ.ᚢᛗᛋᚳ-ᛠᛇ-ᛚᛁᚫᚫᚳᛚ-ᚹᛁ-ᛚ/
ᛏ-ᛈᛖᚢᛈ-ᛠᛡᛈᚦᛏᛒ-ᛏᛗᛖ-ᚢᛚᚩᛚᛖ-ᛇᛄ/
ᛈ-ᚢᛠ-ᛚᚳᚷ-ᛠᚷᛋᛡᛏᛗ./
&
ᛒᛗᚱᚦᚠᛈ.ᚹᚱᛄ-ᚱᛉᚳ-ᛝ-ᛄᛠᛟ-ᛄᛖ/
ᚣᛗ-ᛞᚣᛄᚳᚫᛡᚢᚠ.ᛈᚠᚪ-ᚳᚳᛠ-ᚱ-/
ᚢᛄᚱ-ᚪᛗᛒᛈ-ᚷᛈᛒᚢᚾᛠᛝᚠ.ᚾᛉᛖ-/
ᚣᚷᛁᛠᛝᚢᛗᛏᚳᚷᛠᛠ-ᛄᚫ-ᛒᛈᚹᛞ.ᚠᚣ/
ᛉ-ᚫᚢᚠ-ᛇᛄᛈ-ᛉᛚᚦᛠᚪ-ᛚᚦ-ᚳᚣᚢᛡ./
ᚳᛖ-ᛚᚫᛇᛁᛉᚦᛋᚫᚻᚫ-ᚦᚣᚠᛚᚳᛖᚱ-ᛈᚠᚪᛉ-ᚱᛒᛖ-ᚫᚳᛒᚠ./''', VigenereTranslation(key='ᛞᛁᚢᛁᚾᛁᛏᚣ', skip_indices={ 62, 102, 115, 181, 217, 218, 333, 566, 596, 625, 689 })),        


        ('''
ᛋᚩᛗᛖ-ᚹᛁᛋᛞᚩᛗ.ᚦᛖ-ᛈᚱᛁᛗᛖᛋ-ᚪᚱᛖ-ᛋᚪᚳ/
ᚱᛖᛞ.ᚦᛖ-ᛏᚩᛏᛁᛖᚾᛏ-ᚠᚢᚾᚳᛏᛡᚾ-ᛁᛋ-ᛋᚪ/
ᚳᚱᛖᛞ.ᚪᛚᛚ-ᚦᛝᛋ-ᛋᚻᚩᚢᛚᛞ-ᛒᛖ-ᛖᚾᚳᚱᚣ/
ᛈᛏᛖᛞ./
&
ᚳᚾᚩᚹ-ᚦᛁᛋ./
272        138     ᛋᚻᚪᛞᚩᚹᛋ     131     151./
ᚫᚦᛖᚱᛠᛚ     ᛒᚢᚠᚠᛖᚱᛋ     ᚢᚩᛁᛞ        ᚳᚪᚱᚾᚪᛚ      18./
226        ᚩᛒᛋᚳᚢᚱᚪ     ᚠᚩᚱᛗ        245     ᛗᚩᛒᛁᚢᛋ./
18     ᚪᚾᚪᛚᚩᚷ      ᚢᚩᛁᛞ        ᛗᚩᚢᚱᚾᚠᚢᛚ        ᚫᚦᛖᚱᛠᛚ./
151        131     ᚳᚪᛒᚪᛚ       138     272./''', SimpleTranslation()),

        ('''
ᚹ-ᚣᛠᚹᛟ.ᚹ-ᛇᚹᛟ-ᚻᛈᚣᛝᚻᛈᚻ-ᛋᛠ-/
ᚫᛠ-ᚹᛟᚻ-ᛏᛋᚢᚻᚳ-ᚪᛝᚠ-ᚹ-ᛇᚹᛏᛋᛈ/
ᛡ.ᛞᛈ-ᚪᛈᛟᛋ-ᛋᛠ-ᚠᛈ-ᚻᛠᛠᛡ-/
ᛠᚦ-ᚠᛈ-ᛇᚹᛏᛋᛈᛡ.ᚪᛞᛠ-ᚹᛡᛈ-ᚳᛠ/
ᚢ-ᚪᛞᛠ-ᚪᛝᛏᛞᛈᛏ-ᛋᛠ-ᛏᛋᚢᚻᚳ-ᛞᛈᛡ/
ᛈ-ᚹᛏᚣᛈᚻ-ᚠᛈ-ᛇᚹᛏᛋᛈᛡ.ᚠᛈ-ᛏᛋᚢᚻᛈ/
ᛟᛋ-ᛋᛠᛄᚻ-ᚠᛈ-ᛇᚹᛏᛋᛈᛡ-ᛞᛝᛏ-ᛟᚹᛇᛈ./
ᚠᚹᛋ-ᛝᛏ-ᛟᛠᛋ-ᚪᛞᛠ-ᚳᛠᚢ-ᚹᛡᛈ-ᚠᚹ/
ᛋ-ᛝᛏ-ᛠᛟᛄᚳ-ᚪᛞᚹᛋ-ᚳᛠᚢ-ᚹᛡᛈ-ᚣᚹᛄ/
ᛄᛈᚻ.ᚪᛞᛠ-ᚹᛡᛈ-ᚳᛠᚢ-ᚪᛞᛠ-ᚪᛝᛏᛞ/
ᛈᛏ-ᛋᛠ-ᛏᛋᚢᚻᚳ-ᛞᛈᛡᛈ-ᛞᛈ-ᚹᛏᚣᛈ/
%
ᚻ-ᚹᚫᚹᛝᛟ.ᚠᛈ-ᛇᚹᛟ-ᚠᛠᚢᚫᛞᛋ-ᚦᛠᛡ-ᚹ-/
ᛇᛠᛇᛈᛟᛋ-ᚹᛟᚻ-ᛡᛈᛖᛄᛝᛈᚻ-ᛝ-ᚹᛇ-ᚹ-/
ᛖᛡᛠᚦᛈᛏᛏᛠᛡ.ᚠᚹᛋ-ᛝᛏ-ᚪᛞᚹᛋ-/
ᚳᛠᚢ-ᚻᛠ-ᛟᛠᛋ-ᚪᛞᛠ-ᚳᛠᚢ-ᚹᛡᛈ-/
ᛡᛈᛖᛄᛝᛈᚻ-ᚠᛈ-ᛇᚹᛏᛋᛈᛡ.ᚪᛞᛠ-ᚹᛡ/
ᛈ-ᚳᛠᚢ-ᚪᛞᛠ-ᚪᛝᛏᛞᛈᛏ-ᛋᛠ-ᛏᛋᚢᚻ/
ᚳ-ᛞᛈᛡᛈ.ᚣᛠᛟᚦᚢᛏᛈᚻ-ᚠᛈ-ᛇᚹᛟ-ᚠ/
ᛠᚢᚫᛞᛋ-ᛏᛠᛇᛈ-ᛇᛠᛡᛈ.ᚦᛝᛟᚹᛄᛄᚳ-/
ᛞᛈ-ᚹᛟᛏᚪᛈᛡᛈᚻ-ᛝ-ᚹᛇ-ᚹ-ᛞᚢᛇᚹᛟ-ᛉ/
ᛈᛁ.ᚠᚹᛋ-ᛝᛏ-ᛠᛟᛄᚳ-ᚳᛠᚢᛡ-ᛏᛖᛈ/
ᚣᛝᛈᛏ-ᛟᛠᛋ-ᚪᛞᛠ-ᚳᛠᚢ-ᚹᛡᛈ.ᚪᛞ/
%
ᛠ-ᚹᛡᛈ-ᚳᛠᚢ-ᚪᛞᛠ-ᚪᛝᛏᛞᛈᛏ-ᛋᛠ-/
ᛏᛋᚢᚻᚳ-ᛞᛈᛡᛈ-ᚹᛏᚣᛈᚻ-ᚠᛈ-ᛇᚹᛏᛋᛈ/
ᛡ-ᚹᚫᚹᛝᛟ.ᚹᚦᛋᛈᛡ-ᚹ-ᛇᛠᛇᛈᛟᛋ-ᛠᚦ-ᚠ/
ᛠᚢᚫᛞᛋ-ᚠᛈ-ᛖᛡᛠᚦᛈᛏᛏᛠᛡ-ᛡᛈᛖᛄ/
ᛝᛈᚻ-ᛝ-ᚹᛇ-ᚹ-ᚣᛠᛟᛏᚣᚱᚢᛏᛟᛈᛏᛏ-ᛝ/
ᛟᛞᚹᛉᛝᛋᛁ-ᚹᛟ-ᚹᛡᛉᛝᛋᛡᚹᛡᚳ-ᛉᛠᚻᚳ/
.ᚠᚹᛋ-ᛝᛏ-ᛇᛈᛡᛈᛄᚳ-ᚪᛞᚹᛋ-ᚳᛠᚢ-ᚹ/
ᛡᛈ-ᛟᛠᛋ-ᚪᛞᛠ-ᚳᛠᚢ-ᚹᛡᛈ.ᚪᛞᛠ-ᚹ/
ᛡᛈ-ᚳᛠᚢ-ᚪᛞᛠ-ᚪᛝᛏᛞᛈᛏ-ᛋᛠ-ᛏᛋᚢ/
ᚻᚳ-ᛞᛈᛡᛈ.ᚠᛈ-ᛇᚹᛟ-ᚪᚹᛏ-ᚫᛈᛋᛋᛁ-ᛝᛡ/
ᛡᛝᛋᚹᛋᛈᚻ.ᛝ-ᚹᛇ-ᛞᛈ-ᛏᛋᚹᛡᛋᛈᚻ-/
%
ᛉᚢᛋ-ᛞᛈ-ᚣᛠᚢᛄᚻ-ᛟᛠᛋ-ᚠᛝᛟᚣ-ᛠᚦ-/
ᚹᛟᚳᚠᛁ-ᛈᛄᛏᛈ-ᛋᛠ-ᛏᚹᚳ-ᛏᛠ-ᛞᛈ-ᛋᛡᚹ/
ᛝᛄᛈᚻ-ᛠᚦᚦ.ᚹᚦᛋᛈᛡ-ᚹ-ᛄᛠᛁ-ᛖᚹᚢᛏᛈ-/
ᚠᛈ-ᛇᚹᛏᛋᛈᛡ-ᛡᛈᛖᛄᛝᛈᚻ-ᚠᛈᛟ-ᚳᛠ/
ᚢ-ᚹᛡᛈ-ᚪᛈᛄᚣᛠᛇᛈ-ᛋᛠ-ᚣᛠᛇᛈ-ᛏᛋᚢ/
ᚻᚳ./
&
ᚹᛟ-ᛝᛟᛏᛋᛡᚢᚣᛋᚱᛟ.ᚻᛠ-ᚦᛠᚢᛡ-/
ᚢᛟᛡᚩᛏᛠᛟᚹᛉᛄᛈ-ᚠᛁᛏ-ᚩᚣᛞ-ᚻᚹ/
ᚳ./''', SimpleTranslation(atbash=True, shift=3)),

        ('''
ᚦᛖ-ᛚᚩᛋᛋ-ᚩᚠ-ᛞᛁᚢᛁᚾᛁᛏᚣ.ᚦᛖ-ᚳᛁᚱᚳᚢ/
ᛗᚠᛖᚱᛖᚾᚳᛖ-ᛈᚱᚪᚳᛏᛁᚳᛖᛋ-ᚦᚱᛖ/
ᛖ-ᛒᛖᚻᚪᚢᛡᚱᛋ-ᚹᚻᛁᚳᚻ-ᚳᚪᚢᛋᛖ-ᚦ/
ᛖ-ᛚᚩᛋᛋ-ᚩᚠ-ᛞᛁᚢᛁᚾᛁᛏᚣ./
&
ᚳᚩᚾᛋᚢᛗᛈᛏᛡᚾ.ᚹᛖ-ᚳᚩᚾᛋᚢᛗᛖ-ᛏᚩᚩ/
-ᛗᚢᚳᚻ-ᛒᛖᚳᚪᚢᛋᛖ-ᚹᛖ-ᛒᛖᛚᛁᛖᚢᛖ-ᚦᛖ-/
ᚠᚩᛚᛚᚩᚹᛝ-ᛏᚹᚩ-ᛖᚱᚱᚩᚱᛋ-ᚹᛁᚦᛁᚾ-ᚦᛖ-ᛞᛖᚳ/
ᛖᛈᛏᛡᚾ./
1-ᚹᛖ-ᛞᚩ-ᚾᚩᛏ-ᚻᚪᚢᛖ-ᛖᚾᚩᚢᚷᚻ-/
ᚩᚱ-ᚦᛖᚱᛖ-ᛁᛋ-ᚾᚩᛏ-ᛖᚾᚩᚢᚷᚻ./
%
2-ᚹᛖ-ᚻᚪᚢᛖ-ᚹᚻᚪᛏ-ᚹᛖ-ᚻᚪᚢᛖ-ᚾ/
ᚩᚹ-ᛒᚣ-ᛚᚢᚳᚳ.ᚪᚾᛞ-ᚹᛖ-ᚹᛁᛚᛚ-ᚾᚩᛏ-/
ᛒᛖ-ᛋᛏᚱᚩᛝ-ᛖᚾᚩᚢᚷᚻ-ᛚᚪᛏᛖᚱ-ᛏ/
ᚩ-ᚩᛒᛏᚪᛁᚾ-ᚹᚻᚪᛏ-ᚹᛖ-ᚾᛖᛖᛞ./
ᛗᚩᛋᛏ-ᚦᛝᛋ-ᚪᚱᛖ-ᚾᚩᛏ-ᚹᚩᚱᚦ-ᚳᚩᚾᛋᚢᛗ/
ᛝ./
&
ᛈᚱᛖᛋᛖᚱᚢᚪᛏᛡᚾ.ᚹᛖ-ᛈᚱᛖᛋᛖᚱᚢᛖ-/
ᚦᛝᛋ-ᛒᛖᚳᚪᚢᛋᛖ-ᚹᛖ-ᛒᛖᛚᛁᛖᚢᛖ-ᚹᛖ-ᚪᚱ/
ᛖ-ᚹᛠᚳ.ᛁᚠ-ᚹᛖ-ᛚᚩᛋᛖ-ᚦᛖᛗ-ᚹᛖ-ᚹᛁᛚᛚ-ᚾᚩ/
ᛏ-ᛒᛖ-ᛋᛏᚱᚩᛝ-ᛖᚾᚩᚢᚷᚻ-ᛏᚩ-ᚷᚪᛁᚾ-ᚦᛖᛗ-/
ᚪᚷᚪᛁᚾ.ᚦᛁᛋ-ᛁᛋ-ᚦᛖ-ᛞᛖᚳᛖᛈᛏᛡᚾ./
%
ᛗᚩᛋᛏ-ᚦᛝᛋ-ᚪᚱᛖ-ᚾᚩᛏ-ᚹᚩᚱᚦ-ᛈᚱᛖᛋᛖᚱᚢ/
ᛝ./
&
ᚪᛞᚻᛖᚱᛖᚾᚳᛖ.ᚹᛖ-ᚠᚩᛚᛚᚩᚹ-ᛞᚩᚷᛗᚪ-/
ᛋᚩ-ᚦᚪᛏ-ᚹᛖ-ᚳᚪᚾ-ᛒᛖᛚᚩᛝ-ᚪᚾᛞ-ᛒᛖ-ᚱᛁᚷᚻ/
ᛏ.ᚩᚱ-ᚹᛖ-ᚠᚩᛚᛚᚩᚹ-ᚱᛠᛋᚩᚾ-ᛋᚩ-ᚹᛖ-ᚳᚪᚾ-/
ᛒᛖᛚᚩᛝ-ᚪᚾᛞ-ᛒᛖ-ᚱᛁᚷᚻᛏ./
ᚦᛖᚱᛖ-ᛁᛋ-ᚾᚩᚦᛝ-ᛏᚩ-ᛒᛖ-ᚱᛁᚷᚻᛏ-ᚪᛒᚩᚢᛏ./
ᛏᚩ-ᛒᛖᛚᚩᛝ-ᛁᛋ-ᛞᛠᚦ./
ᛁᛏ-ᛁᛋ-ᚦᛖ-ᛒᛖᚻᚪᚢᛡᚱᛋ-ᚩᚠ-ᚳᚩᚾᛋᚢᛗᛈᛏ/
ᛡᚾ.ᛈᚱᛖᛋᛖᚱᚢᚪᛏᛡᚾ.ᚪᚾᛞ-ᚪᛞᚻᛖᚱᛖᚾ/
%
ᚳᛖ-ᚦᚪᛏ-ᚻᚪᚢᛖ-ᚢᛋ-ᛚᚩᛋᛖ-ᚩᚢᚱ-ᛈᚱᛁᛗᚪᛚ/
ᛁᛏᚣ.ᚪᚾᛞ-ᚦᚢᛋ-ᚩᚢᚱ-ᛞᛁᚢᛁᚾᛁᛏᚣ./
&
ᛋᚩᛗᛖ-ᚹᛁᛋᛞᚩᛗ.ᚪᛗᚪᛋᛋ-ᚷᚱᛠᛏ-ᚹ/
ᛠᛚᚦ.ᚾᛖᚢᛖᚱ-ᛒᛖᚳᚩᛗᛖ-ᚪᛏᛏᚪ/
ᚳᚻᛖᛞ-ᛏᚩ-ᚹᚻᚪᛏ-ᚣᚩᚢ-ᚩᚹᚾ.ᛒᛖ-/
ᛈᚱᛖᛈᚪᚱᛖᛞ-ᛏᚩ-ᛞᛖᛋᛏᚱᚩᚣ-ᚪᛚᛚ-ᚦᚪᛏ-/
ᚣᚩᚢ-ᚩᚹᚾ./
&
ᚪᚾ-ᛁᚾᛋᛏᚱᚢᚳᛏᛡᚾ.ᛈᚱᚩᚷᚱᚪᛗ-ᚣᚩᚢ/
ᚱ-ᛗᛁᚾᛞ.ᛈᚱᚩᚷᚱᚪᛗ-ᚱᛠᛚᛁᛏᚣ./''', SimpleTranslation()),

        ('''
ᚪ-ᛋᚹᚪᛁ.ᛈᚢᛟᚫ-ᛈ-ᚠᛖᚱᛋᛈᛈ-ᚦᛗ-ᚾᚪᚱ/
ᛚᚹᛈ-ᛖᚩᛈᚢᛠᛁᛁᚻᛞ-ᛚᛟ-ᛠ.ᛄᛖ-/
ᛠ-ᛁᚫ-ᚷᛖ-ᚦᛟᛁᛞᛟ-ᛝᚠ-ᛄᛖ-ᛞᛁᛉᚾᚢ/
ᛚᚠᚻᚱᚹᛈᛞᛡ-ᚻᚹ-ᛋᚳᛉᛞ.ᚻᛡᛖᛡ-ᛠᚱ/
ᛉᛖᛇ-ᛒᚹ-ᛠ-ᛋᛒᛚᛞᚹᛈᚳ-ᚫᚩ-ᚹᛉᛞᚪᚪᛄᛠ/
-ᚹᚣᛠᚳ-ᛄᚪᚳ-ᛗᚾᛈᛏ.ᚩᚻ-ᛗᛈᛗᚳᛡᚱ-ᚱᚪ/
ᛚᛡ-ᛁᛒ-ᚠᛋ-ᛈ-ᚳᛝᛗᚳᚹ-ᛁᛗᛗᛁᚪᚻ-ᚣᛝᚳᛟ-ᛒ/
ᛠᛇ.ᛁ-ᚱᚹᚾᛒ-ᛡᚪᛗᛟ-ᛈ-ᛁᚩᛠᚳᛠ-ᛉ/
ᚾ-ᛚᛏ-ᚻᛒᛡ-ᛚᛇᚢᚪᚻᚣ-ᚷᛖ-ᛏᚷᚢᛇᛟᛡᚫ-/
ᚪᛡᛞ-ᛖᛟ-ᚱᚫᚠᛋᚹᛡ-ᚣᛗᛋ-ᚣᚪᛗᛡ-ᛏᚱ-ᚷᛖ/
ᚾᚪ-ᛚᛡ-ᛗᛈᛋᚣᛟᚱ.ᚩᚻ-ᛗᛈᛗᚳᛡᚱ-ᚱᛏᛈᛒ/
%
ᛈᛗᛈ-ᚦᚹ-ᛗᚳᛁᛞᚹᚾᚣ-ᛠᚾᚪ-ᚳᚪᛠᛡ-ᛚᛡ-/
ᚢᛝᛁᛋᛟ-ᚦᚫᚷ-ᛄᛗᛗᚳ-ᚪᚪᛠᛞ-ᚹᚹᚢ-ᚾᛉᚢ/
ᚹ-ᛈᛝ-ᛁᚩᛠᚳᛠ-ᛉᚾ-ᛡᛟᚢᛟ-ᛇᛒᚩ-ᛁᚱ-ᚦᛠ-/
ᛉ.ᚪᛁᛈ-ᚦᚹ-ᛗᚳᛁᛞᚹᚾᚣᛗ-ᚹᛗᛞᛖ-ᚹᛈᚾ/
ᛗᚷᚣᛏᛠᛈᛖᚪ./''', VigenereTranslation(key='ᚠᛁᚱᚠᚢᛗᚠᛖᚱᛖᚾᚠᛖ', skip_indices={ 68, 81 })),

        ('''
ᚪᚾ-ᛁᚾᛋᛏᚱᚢᚳᛏᛡᚾ.ᚳᚹᛖᛋᛏᛡᚾ-ᚪᛚᛚ-/
ᚦᛝᛋ.ᛞᛁᛋᚳᚩᚢᛖᚱ-ᛏᚱᚢᚦ-ᛁᚾᛋᛁᛞᛖ-/
ᚣᚩᚢᚱᛋᛖᛚᚠ.ᚠᚩᛚᛚᚩᚹ-ᚣᚩᚢᚱ-ᛏᚱᚢ/
ᚦ.ᛁᛗᛈᚩᛋᛖ-ᚾᚩᚦᛝ-ᚩᚾ-ᚩᚦᛖᚱᛋ./
&
ᚳᚾᚩᚹ-ᚦᛁᛋ./
434        1311        312     278     966/
204        812     934     280     1071/
626        620     809     620     626/
1071       280     934     812     204/
966        278     312     1311        434/''', SimpleTranslation()),

        ('''
ᛋᚻᛖᚩᚷᛗᛡᚠ-ᛋᚣᛖᛝᚳ.ᚦᛄᚷᚫ-ᚠᛄᛟ-/
ᚩᚾᚦ-ᚾᛖᚹᛒᚪᛋᛟᛇᛁᛝᚢ-ᚾᚫᚷᛁᚦ-ᚻᛒᚾᛡ-/
ᛈᛒᚾ-ᛇᛄᚦ-ᚪᛝᚣᛉ-ᛒᛞᛈ-ᛖᛡᚠᛉᚷᚠ-/
ᛋᛈᛏᚠᛈᚢᛝᚣᛝᛉᛡ-ᚣᚻ-ᛒᚢ-ᚷᚩᛈ-ᛝᚫᚦ-ᛁ/
ᚫᚻᛉᚦᛈᚷ-ᚣᚠᛝᚳᛄ-ᚦᚪᛗᛁᛝᛁᛡᚣ-ᚻᛇ-ᛏᚻᚫ/
ᛡ-ᛉᚣ-ᛖᚢᛝ-ᚳᚠᚾ-ᛇᚦᛄᛁᚦ-ᚦᛈ-ᚣᛝᛠ-ᚣᚾ/
ᛖᚣ-ᛞᛉᛝᚹ-ᛒᚳᛉᛞᛒᚠ-ᛗᛏᚾᛖ-ᛠᛄᚾᛚᚷ/
ᛒ-ᛉᚷᚦ.ᚣᛁᛞᚪ-ᛝᚷᛗᛄᚱᚩᛚᛇ-ᚣᛏᛈᛁᚦᛞᛄ-/
ᛟᚻᛚ-ᛠ-ᚠᛉᚫᛈᚷᛉ-ᚠᛚᚹᛇᛏᚫ-ᚠᚷᚾ-ᛗᛇᛚᚾ-/
ᛝᛗᚠᚱᛡ-ᚪᛋ-ᛠᛗᛝᛉᛉᛇᛞᛒ-ᛟᛞᛗᚩ-ᛠ/
ᛇᚻ-ᛞᛝᚷ-ᛟᛝᛚᚢᚱᚾᛏ-ᚫᛋᚣᚢᚻᚱᛏ-ᚻᚳ-ᛋᛟ/
ᛏᛟᛝᚢᚱ-ᛋ-ᚠᚩᛖᚹᛠᛟᛚᚠᚫ-ᛗᚱᛝ-ᛞᚪᛗᚱ-ᚹ/''', UnsolvedTranslation()),

        ('''
ᚪᛁᛗᛋᚾ-ᛋᛟᚱᚢᚹᛋᛚᛡ.ᛟᚪᚫᛝᛋᛞᛈᛏ-ᚳᚱᚦ/
ᛡ-ᚱᛒᚩᛞᚦᚠ-ᚣᛉᛁᛏ.ᛟᛁ-ᚠᛚᚩ-ᚠᛠ-ᚱᚩᛟᛗᚻ/
ᛗᚷᛈᚻ-ᚫᚻᚾᚩᚻᚣ-ᛟᛋᛚ-ᚾᚷ-ᚫᚣ-ᛟᚳᛒᛚᛄ-ᛝ/
ᛚᛟ-ᚫᛄᛠᚹ-ᛠᚦᚩ-ᛒᛟᚣ-ᚳᚠᚳᛄ-ᛚᚫ.ᚾ-ᚦᛈ-/
ᚢᛉ-ᛟᛉᚷ-ᛈᚠᛋᛇᚫᛟ-ᛝᛈᛇᚩᛖᚪ-ᚷᚫᛡᛝᚦᚩ/
-ᛈᚪᛟᚦᚱᛝᚫ-ᚳᛋᛒᛇᚣᚻ-ᛏᛉᛖᛚᚱ.ᚷᚹᚣ-ᛄᚠ/
ᛁᚾᛡᚳᚣᛠᛁᛡ-ᚩᚦ-ᛖᚳᚫᚳᛉᛡᛠ-ᚩᛚᚳ-ᚠᚱ/
ᛞᛝᛖᚢ-ᛞᚳᛚᛠᛋᛉᚳᚷᛡ.ᚹᛋᚦ-ᚠᛞᛝ-ᛁᛡ/
ᛗᚪᚫᚷ-ᚹᛋ-ᚾᛞ-ᚳᛈᚦᛉᛈᛠᛠ-ᚹᚢ-ᛠᚹ-ᚠᚹ/
ᛄᚣ-ᛉᛞᚹᚳᚷᚳᛟ-ᛞᛉᛟ-ᚱᛡᚷ-ᚾᛈᚪᚣᛈ-ᚳ/
ᚣᚻ-ᚠᛖᛄᛠᚾ-ᛟᚫ-ᚢᚪ-ᚻᚱ-ᛖᛠᚦᚠᛄᚪ-ᛚᛉ/
ᛋᛏ-ᛗᚠᛚᚠᛏ-ᚷᛁᚦ-ᚢᛚᚷ-ᛉᛠᛏᛋᛚᛄᛈ-ᛚᛉᛁ/''', UnsolvedTranslation()),

        ('''
ᛟᛗ-ᚢ.ᚻᛏ-ᛒᛇᛚᛞᚻᛒᛗ-ᛠᚱᛒ-ᚾᚻᛒᛖᚷᛇ-/
ᛞᛚᚹᛇᛡᛈᚩ-ᚻᛖᛠ-ᚹᛁᚱᛁᚻ-ᚢᚦᚻᚣ-ᚾᛉᛒᚷᛄ/
ᛈᚢ-ᛝᛠᚠᚾᛁᛖᛞᛡᛝᚱ-ᛞᛒᛄᛡᛟᛗᛁ-ᚠᛏ-ᛄ/
ᛞᛁᚦᚱᛚᛋ-ᛖᛇᚩᚷᛒᛏᛞ-ᚦᚪᚾᚳᚣ-ᛡᛋᚦᛞ-ᛝᚠᛚ/
ᛖᚷᚻᚳ-ᛖᚩᛁᛏᚾᛉ-ᛈᛏᚠᚻᚱᛞᛖᚠᛏ-ᚫᚹᚻ-ᛒ/
ᚳ-ᚠ-ᛈᚪᛚᚢᛠᚾᛚᛄ-ᛄᚳᛚᚹᛠᛞᚢᛞᛇ-ᛠᛉ/
ᛞᚹᚻᛠ-ᚦᛡᚫᚳᛚᛏᚹᛖᛁᚳ-ᛈᛟᛞᚳ-ᚾᚻᚪ-ᚱᛁᚷ/
ᚦᛠᛖᛏᚷ-ᚦᚻᚩᛡᚹᚫᛄᛖ-ᛝᛠᛞ-ᚩᚫ-ᚪᛚ-ᛒᛄ/
ᚳᚢᛉᛏᚪᛒᛄᛈ-ᚠᛠ-ᚻᛞᚾᛡᚢᛈᛋᚢᚹ./
&
$''', UnsolvedTranslation()),

        ('''
ᛚᛄ-ᛇᚻᛝᚳᚦᛏᚫᛄᛏᛉᚻ-ᛏᚢᛟ.ᛋᛈᚱᚷ/
-ᚣᚾᚪᚷᛇᛝᚾ-ᚹᚠᚣᚾᛒᛠᛡ-ᛈᚾᚣᚪᛋᛗ/
ᛒ-ᛡᛠᛡᛁ-ᚩᛒᚱᚾᛚᛠ-ᚱᛚᛚᛖᛒᚹᚾᚻᛗᚠ/
ᛟᛒ-ᛝ-ᚱᚪᛡᚷᛟᛇᛏᛗᛉ-ᛞᛇ-ᛗᚣᚻᛠ-ᛁᛚᛋ-ᚾ/
ᚹᚳᚠᛈᛗᛈᛚ-ᛠᛋᚦᚠᛟᛡ-ᚦᛖᚣ-ᚳᛄᛚᚳᛡᛗ-/
ᛒᛞᚳᛇ-ᛄᛁᛏᛟ-ᛞᛠᛖᛡᚾᛏ./
&
ᛈᛞᚦ.ᛇᛞᛇ-ᚫᛚᚳ-ᛡᛇ-ᛠᚻ-ᚹᛗᚣᚦ/
ᚢ-ᚻᛏᚦᚱᚻᛝ-ᛚᛝᛋ-ᚾᚫᛠᚷᛋᛚ-ᛋᛉ/
ᚩᚻᚹᛞᛗᛖᛗᚪᚠ-ᚳᚣᚳᚫᚾ-ᛏᚦᚷ-ᛁᛄᛁ/
-ᚳᛞᛡᛉ-ᚻᚫᚫᛠᚷ-ᛠᛝ-ᚠᛏᚩᚱᛞᚳᛇ-ᚠᚢ/
ᛉᛠᛒᚩ-ᛉᛁᚣᚷᛋᛋᛒᛠ-ᚩᛁᛈ-ᛁᛄᛁᚩᛖ-ᚻᛠᚻ/''', UnsolvedTranslation()),

        ('''
ᛚᛡ-ᚣᛈᛉᛁᚹᛗᚳᛁ-ᛚᚷᚠᚾᛡᚳᛉ-ᛈᚩᚱᛡ-ᚻ-ᛄ/
ᛗ-ᛟᛉᛝ-ᚢᛗᛇᛠᚷᛝ-ᛝᚹᚳ-ᛚᛝᚢ-ᛉᛄᚠᛟ/
ᚢ-ᚷᛠ-ᛗᛉ-ᚪᚹ-ᛚᚢᛉᚫ-ᛗᛞᛝᚻᚱᚣ-ᚻᚪ-ᚷᛁ/
ᚠᚷᚳ-ᚫᛝᛄᛇᛉᛡ-ᚾᚦᛒᚢᛄᚱ.ᚹ-ᚷᛚᛟᚷ-ᚦᛇᚠ-/
ᚦᛠᛁ-ᛋᚷ-ᚷᚣ-ᛠᛡᛈ-ᛡᚫᛚ.ᚦᛠᛉᚫ-ᛖᛗ/
ᛖᛏᛟᛏ-ᛠᚳᚠ-ᚳᛠᚷ-ᚦ-ᛈᛁᚳᚾ.ᛇᚣᛝᛄᛝ/
ᛗᚹᚳᚾ-ᛒᚣᛠ-ᚩᛟᚷᚱ-ᛗᚱᛗᛈᛡᚹ-ᚫᛟᚦᛟ-ᛈ/
ᛉᛄᛚ-ᚱᛚᚱᛒᚪᛈᛏᛉᛚᛏ-ᛗᛉᛁᚹ.ᛄᛋᛟᛗᚾᚱ/
ᛖᛒᛋ-ᚳᛏᛚᛟ-ᛋᛒᚠᛉᚦᚪᛠᚢ-ᛇᛉ-ᚱᚷᛏᛇᛠ/
ᛁᛄᛒᛟ-ᛉᚷᛄᛝ-ᛠᚦ-ᚱᛝᛒ-ᚾᚢᚪᛝᛒᛈᛋᛠ-ᛈ/
ᚹᚩᚻᛖ-ᚫᛇᚷᚾᚫᛋᛇ-ᚩᛈᛗ-ᛖᛉᛡᛒᚹ-ᚢᛖᛁᛞ-/
ᛈᚪᛇᚷᛋᚳᚷᛞᛈᚣ-ᛡᛚᚦᚱ-ᚳᚢᚠᛇᚦ-ᛉᛖᛚ-ᚢ/''', UnsolvedTranslation()),

        ('''
ᚱᚫ-ᛉᚻᛄᚫᛗᛚᚠ-ᚳᛝᛞ-ᛁᛝᚩ-ᚳᛋᛟᛖᚣᛟᚻᚢ-/
ᚷᛞᚹᚪ-ᛖᛋᚷᛝᚠᛉ-ᛞᛉᛄ-ᛠᚻᛁ-ᚦᛈᛉᚣ-ᛡ-/
ᛇᛞᛇᛝᛇᛝ-ᛖᛠᛞᚱ-ᛚᛇᛏ-ᛉᛏᚣ-ᚱᛇ-ᛈᛝᛇ/
ᛈᚩᛁᛚᛖᚠ-ᛇᚫᚪ-ᚣᛝᚠᚣ-ᚠᛞᚾᛚ-ᛉᛏᚾᚫᛋ.ᛁᚩ/
ᚳᚢ-ᚣᛠᚾᛏᚷᚳᚪ-ᛉᛡᛇ-ᚦᛄᚣᛄᛚᛟᛖᛚ-ᚣ./
ᛈᛡ-ᛖᚹᛟ-ᛇᚾᚪ-ᚻᛞᛇᛋ-ᚦᚣᛇᚦᛄᚦᚱᚢ-ᚳᛠ/
ᚪ-ᚢᛄᛡᛈ-ᚣᚫᛇᛋ-ᚻᛠᛏᚣᛞᚣᚫᚠᚻᚩ-ᛟᛗ/
ᛉᛟᛄᚷ-ᚢᛡᚱᛡᚳ-ᛁᚠᛟ-ᛁᛄᛈᛒ-ᛖᛝᚣᚦᚩᚫᚣ-/
ᛠᛉᛡᛖᛚ-ᛁᚱᚣᛞᛠᛄ-ᚫᚳ-ᛗᚷᛁᚫᚢᚪᚫ-ᛄᚪ/
ᚻᛈ-ᚠᛞᛚᛁᛠᛈᛟᚣᚩ-ᚢᛒᚷᛝᛟᚢᛝᛋᚢᚳ-ᛏ/
ᛞ.ᚫᛈᚩᛄ-ᛒᚻᚱᛁᚷᚻᛄ-ᚣᚹᛗᛇᚾᚫ-ᛞᛝᛇ-ᛟᛄ/
ᛝᚳᛖᛠ-ᛉᚪᚱᚣ-ᚪᚢᛏ-ᚳᛈᚳ-ᚩᛇᛟ-ᚫᛈ-ᛏ/''', UnsolvedTranslation()),

        ('''
ᛉᚳᛏᚻᛞᛇ-ᛉᛒᛠ-ᚫᚾᛄ-ᛠᚪᛒ-ᛖᛠᚹ-ᛡᛚ-/
ᚹᛁᛡᛋᛈᛚᚦᚪᛋᛄ-ᛡᛞᚣᚱᛞᛟ-ᚦᚱᛉᛟᚹ-ᚣᛞᛏ-/
ᚷᛚᛡᚻᚹᛗᚱ-ᛝᚠᚳ-ᚱᚫᛁᛒᚷᛈᚣ-ᛞᚪᚱᚪᛉᛟ-ᚢ/
ᚩᛁᛠ./
&
ᚪᛏᛉᛒ-ᛗ-ᚷᛡᛋᛒ-ᛉᛇ.ᚷᚾᛠᚫᚷᛝᛞ-/
ᛉᛖᛏᚩᚷᛡ-ᛝᚻᛏ-ᚳᛁᚣ-ᛄᛏ-ᛟᚩᚻᚱᛄ-/
ᚳᛖᛡᚩ-ᛞᚪᛏᚣᚢᚾᚱᛇ-ᚫᚫᛁᛖᚠᛝᚦᚻ-/
ᛉᛁᛟᛋᛁ-ᛗᚪ-ᚢᛄᚳᛋᚹᚾᚣ-ᚩᛈᛉᚱ-ᛚᚫᛟᛏᛡ-ᛄ/
ᛈᛗ-ᛞᛋᚠᛗ-ᛟᚹ-ᛞᛚᛏ-ᚷᚱ-ᚩᚢᛋᚻᚪ-ᚣᛇᛡᛚ/
ᚢᚻ-ᛈᚹᛄᛚᚷᛒ-ᛗᚢᛄᛗ-ᛇᚾᛇ.ᚫᛚᚪᛚᚷᚪ-ᛋ/''', UnsolvedTranslation()),

        ('''
ᚻᛝ-ᛚᚦᛒ-ᛋᚳᚢᚳᚩᛡ-ᛚᚳᛄ-ᛉᚪᚾᛇᛉ.ᛠ/
ᛗᛈᚢ-ᛗᚠᛚᛠᛝ-ᛒᛉᛁ-ᛚᚦᚱ-ᛠᛡᛁᚳ-ᚩᛉᛖ/
ᛞᛡ-ᛏᛋᛗᛠᛄᛈ-ᛠᛟ-ᛡᚫᚦᚹᚻᛈᛇᚪᚷᛈᚻ/
ᛠ-ᚳᛚᛠᛈ-ᛡᚣᚾᛁ-ᛚᛡᛁᚳ-ᚫᛇᚾ-ᚫᚳᛡᚱᛡᛚ/
ᛞ-ᛒᛟᛝᛡ-ᛉᛗᛝ-ᚳᚻᛟᛠᚾᛈᚳᚦ-ᛁᛇᚦ-ᛇᚢᚩ/
-ᚦᛈᚪ-ᛡᛚᛟᚹᛡᛈ-ᛄᛗ-ᚷᛒᛈᛋᚾᛇ-ᛏᚩᚷᚢᚾᚫ/
ᛖ-ᚾᚣᛁᛖ-ᛞᛝ-ᛞᛝ-ᛚᚢᛚᛉ-ᚪᚾᛝ-ᛇᚪᛄ-ᚻ-ᛞ/
ᚹᛈᚫᚹᚫ-ᛇᛁᛚᛝ-ᚦᚾᚳ.ᛒᛁᛏ-ᛠᚳᚩᛇᛖᛝ-ᚳᚻ/
ᛟᚻᚫᛄ-ᛟᛉ-ᛁᚳᛖᛏᛋᚹᛖᚾᛡᚣᛄᛗ-ᛖᚳᚪ./
&
ᛞᚩ-ᛟᛏᚦᚫ.ᚳᚹᛄ-ᛉᛠ-ᚷᛠᛗ./
&
$''', UnsolvedTranslation()),

        ('''
ᛉᛁᛉᛗ-ᚢᛉᛗᚳᚦᛈᚩᛒ.ᛡᚾᛏ-ᛠᛉ/
-ᛈᚱᚣ-ᚩᚳᛠᛗᛝᚷᛉᛚᚢ-ᛝᛁᛏᚩ-/
ᛄᚠᛝ-ᛋᛚᚾᛞ.ᚩᛗ-ᛇᚫ-ᚱᛞᚹᛏᛄᚦ-/
ᚣᚦᛋ-ᚫᚣᛖᛋᛉᛟᛒ-ᛠᚱᛇ-ᛈᛝᚢᛈ-ᚩᚦᛉ-ᚪᚻ/
ᛟᚱᛝᚢᛖᚱ-ᚣᛚᛉᛚ-ᛡᛚᚱ-ᛈᚹᛇᚾ-ᛠᚪᚱᛉᛝ-/
ᚣᛋᚻᚢᛚ-ᛋᚣ-ᚷᚾᚢ-ᛇᚫᚾᚾ-ᚩᚫᛖᛞ-ᚪᚩᛄᛡᚢ/
ᚪᛉ-ᚱᛉᛡᛟᛄ-ᛗᛁᛇᛚᛠᚻᚦᛗᛠᚣ.ᚷᛒᚳᛈ/
ᛉᚳ-ᚾᛟᛟᛋᚷᛗᛈᛖᛏᛚᚾᛄ-ᛄᚳᛝᚩ-ᛁᚹᛚᛠᛒ-/
ᚠᚪᛖ-ᛏᛝ-ᚾᛈᛠᚩᛏᚦ-ᚻᛝᛉᛈᚻᛈᚳᛈᚱᚢ-ᛚ/
ᚠᛖᛟ-ᚷᚪᛒᚠᛁᚫᚠᚢᛟ-ᛗᚠᚣᛝᛄᚳ-ᚻᛏᚠᛚᚫ-ᛖ/
ᚦᛋᛚᚩᚢ-ᚫᚩᚪᛗᛟᚢᚹᛇ.ᛒᚾᛋᛚᛝᛄᛟᚾ-ᛗᛚᛒ-/
ᛟᛏ-ᚾᛞᛒᚩᚾᚦᛡᚻᛟ-ᚱᛈᚾᚠᛈᛞ-ᛋᚩᛁᛠᚣᚾ-ᛇ/''', UnsolvedTranslation()),

        ('''
ᚣᚹᚫᚷᛄ-ᛝᛗᚪᚹᛈ-ᚪᚢᚾ-ᛈᛡᛗᛖᛞᛟ.ᛁ-ᛉ/
ᛡᛗ-ᚠᛈᚩ-ᚦᛉᛞ-ᚩᛞ-ᛋᛈᛉᛡᚷ-ᛟᚻᚠᚦᛉᛄ/
ᛟᛋᚦᚣᚦ-ᛏᚻᛋᚣ-ᚻᛠᚷᛚᚫᚱᛏ-ᚢᛋᛟ-ᚦᚠᚠᚣ/
ᛟᛡ-ᛇᚳᚣᛒᛚᛝ-ᛠᚱᚻᛞ-ᛄᚣᛏᚫ-ᚻᛞᚳᛋ-ᛉ/
ᚠᛞ-ᚦᛗ-ᚳᛇᛝ-ᚫᚾᛡᛠᚹᛁᛡ-ᛒᛗᛝ-ᚷᛈᛁᚳ-ᛠ/
ᛚᚷᛉᚣᚣᚱᛄ-ᛉᛁᛄᚢ-ᛖᚣ-ᚪᛝᛈ-ᛡᚫᚳ-ᛖᛠ/
ᚹᛒᚦᛟᚠᛗ-ᚫᚱᚠᚩᛏ-ᛝᛉᛞ-ᛗᛖᛡ-ᚩᛈᛋ-ᛇᛞ-/
ᛇᛟᚫᚾ-ᚷᛗᚣᛁᚫᛁᛄ-ᛈᛄᚩᛡᚷ-ᛈᚳᛄ-ᛚᛖᛡᚻᛚ/
ᚷᚱᛇ-ᛟᚣ-ᛠᚣᛗᚹᚾᚹ-ᚠᛁᛄᚢᛗᚫᚾᚳᛗᛠᛁ./
ᚩᛇ-ᛒᛚᛞ-ᚾᚹᚠᚾᛒᚱ-ᛋᛟᚦᛡ-ᚪᛡᛏᚷᚷᚹ-ᚪᛋᛡᚦ/
ᛋᚦᛋᚠᛗᚷᛞᛠ-ᛝᛈᚩᚪᚣᛝᛈᛋ-ᛟᚾᛇᚪᛖ-ᚻᚢ/
ᚷ-ᚩ-ᚢᚦᛏ-ᛒᚷᚣᛝᚠᚣᛁᚻ-ᚹᛡᛠᚱᚫᚹᛡᛞᚪᚦ/''', UnsolvedTranslation()),

        ('''
ᚳ-ᛉᚢ-ᛈᛏᛋᚢᛖ-ᚷᚦᛡᛚ-ᛖᛋᛠᛝᛉᛈᛉ-ᚾ/
ᛟ-ᛞᛟᛒ-ᚾᚹᚢᛁᛇᛚᛞ-ᛁ-ᚦᚣᚷ-ᛟᛈᛡ-ᛖᚪ.ᚠᛋᛉ/
ᛞ-ᛖᚷᚦᛠ-ᚾᛋ-ᛞᛟᛗᛖ-ᛗᚾᛉ-ᚹᛒᛠᛈᛟ-ᛗ/
ᛉᚫ-ᛄᚩᛞᚻᛡᚷᚠ-ᚣᛗ-ᛁᚷᛉᚻᚹ-ᚾ-ᛋᛗᚷᛠ-/
ᚣᛚᚱᛄᛗᛉᚣ-ᛇᚱᚢᛟ-ᚣᚦᚢᛟᚩ-ᚱᚢᚹ-ᛁᛒᚳ./
ᛠᛏᛞ-ᛚᛖᛋᛄ-ᚳᛟ-ᚷᛞᛡ-ᚢᚹᛝᚻᚫᚢᛈ-ᛏᛈ/
ᚩᚣ-ᚾᛇᚦᛟᛏᛇᚳᚠ-ᛒᚪᚾ-ᛗᚦᛝ-ᛟᛠᚢᛁᚪ-ᚾᚻᛝ/
ᛉᚩ-ᛇᛁᛡᚠᛟᛒᚦᚠ-ᛋᛒ-ᚠᛞᛇ-ᚩᚦᛏ-7-ᚷ-ᛚᛄᛖᚫ/
.ᚣᛁᚫᚹᚻ-ᚫᛏ.ᛁᛉ-ᛉᚻᛞᚩᛠ-ᚫᛋᛝᛚᛝ-ᛖᚩ/
ᚻᛗᚩᛟᛒᚦ-ᚱᛚᛋ-ᚳᚻ-ᚪᛡᚾᛇᚱᛉᚦ-ᚣᛉᚻ-ᛡᚾ/
ᚢ-ᛗᛉᚹ-ᛖᛈᛖ-ᚩᚳᛈᚳᛞᚪᛉᚢᛗᛝᛟ-ᛋᚾᛟ/
ᛉ-ᚠᚱᚳᛒᚢᛄᚱᚫᛝ-ᛒᛋᛟᛠᛡᚪᛚ-ᛏᛟᚾᚫᛟᚪ-ᛁ-/''', UnsolvedTranslation()),

        ('''
ᛡᛋᚳᛖ-ᚹᛒ.ᚾᛚᛝ-ᚦᚾᛁᛠ-ᛒᛡᚱᚠᛖᛁᚹ-ᚾᚠᛗᚢ/
ᚷᚾ-ᛄᛚᚳᚱ.ᛝᚣᛉᛋᚪᛟᚱᛉᚳ-ᛒᚫ-ᚠᚢᚪᛖᚪᚹ-/
ᛚᚾ-ᛄᛉ-ᚻᚦᛉ-ᛗᛚᚾᛖ-ᛏᛝᚦᚪᚩᚢᛗᚣ-ᚠᛝᚪ-/
ᚻᛡᛇᛡ-ᛚᛏᛁ-ᛇᛁ-ᚳᚢᚢᛖ-ᚳᛒ-ᚫᛇᚠᚦᚳᛚᚩᛉᛚ/
ᚩᛚ-ᚠᚳᛠ-ᚪᚠᛟᚫᚠ-ᚾᚳ-ᚢᛒᚱ-ᚾᛇᚩᛉ-ᛁᚳᛟ-ᛞ/
ᛉᛠᛝᚠᚱᛡᚳᛇ-ᛉᛟᛈᛗᛞᚳᚦᚹᛈ.ᛡᚻ-ᚾᚦ/
ᛇᛏᚹᛖᚢ-ᚫᛇᚦ-ᛝᛟᛏᚳᚷᛒᛠ-ᚪᚳᛒᚪᚩᚹᚫ-ᛉ/
ᚢ-ᚫᛖᛒ.ᛇᛏᚢᚩ-ᛟᛞᚠᚢᛋ.ᛡᛄᛗᚦᛠᛏᚪ-ᛒ/
ᚹᚣ-ᛏᛄᚻᚦᚫ-ᛚᚪᚱᚫᛟᚦᚩᚾᛟᛁᛖ-ᛡᚠᚷ-ᛋᚠᚦᛏ-/
ᛠᛡᛠᛁᚢᛡᛇᛝᛞ-ᛉᛏᚠᛒᚻᚢᛋᚳᚱᛇᚹ-ᛇᛈ/
ᛋᚢᛚᚪᛈᚢᚳᛖᚠᛞᛉ-ᚦᛠᛇᛝᚻ-ᚣᚱᛗ-ᛟᚾᛚ./
ᛈᚹᛞᚱᛄ-ᚪᛝᛞ-ᛁᚦᛏᚷᚢᚹᚳᚻᛖᚩᚪᛖ-ᛉᚪᚢ-/''', UnsolvedTranslation()),

        ('''
ᚳᛁ-ᚱᚳᚹ-ᛠᛇᛏ-ᚦᚳᚻᚢ.ᛡᚹᛟ-ᚷᛇᛈ-ᚢᛈᚦ-/
ᚷᚣᚢᚪᛗ-ᚹᚳᛖᛝᚱᛠᛞᛏᚻ-ᛄᛁᛈᚻᚠᛉᛝᛈ/
ᚾ-ᛒᚳᚪᚷᛋᛟ-ᛉᛠᛈᚪᚩᚷᚠᚳᛡᛄ-ᛠᚢᚠᛋᛚ-/
ᚣᛚ-ᚢᛒ-ᛉ.ᚱᚣᚾ-ᛁᛠ-ᛚᚹᛋ-ᚠᚦᚪᛠ-ᛈᚷ.ᛏ/
ᚷᛡᛟᛠᛡᛒ-ᛉᛄᛒ-ᛖᚾ-ᛞᚠᛠᛗ-ᚦᚪᛗᚠᚪ./
ᚻᛡ-ᛗᛁᛏᛟ-ᚻᚣᚹᛏ-ᚠᛒᛁ-ᚫᛖ-ᛝᛒ-ᛚᛏᛠᛉ-ᛟ/
ᛋᚾᛉ-ᚹᛏᛠᛏ-ᛖᚢᛡᛖ-ᛉᚾᛇ-ᛟᚳᚾᚠᚩᚾᚠ-ᚳ/
ᚪ-ᚷᚱᚩ-ᛠᚦᚹᚣ-ᛒᛁ-ᛝᛇᛟ-ᚣ-ᚷᛗᚩ-ᛁᚷᛄ-ᚩᛇ-ᚢ/
ᛁᛉᛝᚪᚱᛉ-ᛏᛄᛞᛈ-ᚾᛝᚷᛏᚢ-ᛚᚷᚳᛏ-ᚢᛒᛇ-/
ᛈᚩᚣᚢᛏ-ᛡᚫᛏᚹᛏᛇ-ᛡᚫᚫ-ᚦᛏᛝ.ᛠᚳᛁᛉ/
ᚻᚦᚣ-ᚻᛚᚾᛋᚱᛡᚫᛚᚫ-ᛖᚷᚻ-ᛞᚾᚻᛠ-ᚠᚪᚹᛖᚠ/
ᛄ-ᛒᛇᚱᚹᛏᛉᚾᛠᛖᛁ-ᚠᚾᛡᚳ.ᛋᛟᚹ-ᛈᚷᛝᛟ-/''', UnsolvedTranslation()),

        ('''
ᚷᚦᚠᛄᚷᚳ-ᛒᛁᛗᛚᛇᛠᚹ-ᚾᚫᚹᚷ.ᚩᚻᚪᛏᚾᛄ-ᚣ/
ᛝᛏᛡᛝ-ᚢ-ᚩᚠᚣ-ᛗᚢᛒ-ᛏᚠᛈ.ᚱᚩ-ᛉᚩᛝᛒ-ᛖ/
ᛏᚩᛉ-ᚣᛗᚠᛉ-ᛖᚩᚫᚷᚣᛚ-ᚩᛇ-ᚠᛋᚫᛇᛗ-ᛡᛟᚹ/
ᚾᚩᚢᚹᛖᛁ-ᚾᚦᚫᛠᚪ-ᛠᛚ-ᚹ-ᛡᚩ-ᚢᚦᛗ-ᛝᛚᚪᚠ/
ᛝ-ᛚᚠᛚᚳᛒᚢᛝᛉ-ᚣᛡᚪᚷ-ᚹᛟᚪᚻᚹᚢ-ᛖᛠᚷ-/
ᛁᚪᛏᛄᛗ-ᛏᛖᛁ-ᚣᛡ-ᚦᚾᚠᚦ-ᚩᛈᚻᚪ-ᚻᛋᛠ-ᛡᛉ/
ᚪᚫ-ᚠᚣᛞᛠᛇᚠᚫ-ᛏᛗ-ᚳᛡᚷ-ᚱᚢᛞ-ᛄ-ᛋᛡᛇᚩ/
-ᛚᛟ-ᚦᚱᚫᛒᛚᚦ-ᛖᚪᚦᛗᛚ-ᚦᛉᚪᚱ-ᛟᛖᛒᛄᚱᛄᛖᛁ/
ᛈ-ᚪᛖᛠᚠᛄᚢ-ᛞᚹᚦᚣ-ᛉᚷᚩᚳᛡ-ᛇᛗᛞᚳᛏ-/
ᚻᛚᚦᛝᛖᛗᚱ-ᛒᚷᛞᛉᛗᛒᛉᚳᛝᚦᚣᛞᚫᛠ-ᛋ/
ᛏᛗᛏᚻᚹ-ᛇᚳᚪᛞ-ᛠᚢᛒᛉ-ᛡᛁᛡᛚ-ᚷᛋᚦᛞ-ᚠ/
ᚢᚩᛠ-ᛚᛋᚣᛏ-ᛋᚪᛞᚫᚹᛄᛞ-ᛋᛈᛋᛄ-ᚪᛖᛁᛇᛒᛟ/''', UnsolvedTranslation()),

        ('''
-ᛏᛄ-ᚠᚩᛚᛞ-ᚾᚷᚳ-ᛚᚷᛗ-ᛠᚦᚢ-ᛟᚻᚾᛟᚣᛡ./
ᛇᚻᚣᚪᛈ-ᚾᛋ.ᛞᚫᛠᚳᛉᛄ-ᚦᚹᛋᚱᚦᚫᚾ-ᛡᛚᚣ/
ᚫᛋᛖ-ᛟᚣᛝᛡ-ᚦᚣᚷᛇᚱ-ᛋᛠᛏ-ᛡᚳᛉ-ᛠᚷ-/
ᚳᛒᛋ-ᚹᚾᚻᛖᛝᛋ-ᚩᛡᛗᛉᛝ-ᛉᚦ-ᛠᛞᚳᛒᚷ/
ᛉᚹᛝᚢ-ᛉᛞᛈ.ᛉᛡᛈᛟ-ᚾᛡᚠᛡᚢᛋ-ᛉᚪᛖ/
ᚻᚱᚣᛠᛇ-ᛒᛟ-ᚪᛝᛡ-ᚳᚱᚳᛈᚩᛏ-ᚻᚣᚫᛁᛋᚩᚦᛚ/
-ᛟᛚ-ᛋᚪᚢᚪᛈᚻ./
&''', UnsolvedTranslation()),

        ('''
ᚠᚢᛚᛗ-ᚪᛠᚣᛟᚪ./
3258    3222    3152    3038/
3278    3299    3298    2838/
3288    3294    3296    2472/
4516    1206    708 1820/
&
$
ᛚᚢᛝᚾ-ᚳᚢ-ᛒᚾᛏᚠᛝ.ᛁᚢᛁᚢ-ᛟᚫᛄᚠᚫ-ᚢ/
ᚷᛉᛇᛈᛉ-ᚣᛠᛚᚪᛉ-ᛟᛉᛡᚦᚻᛠ-ᚾ/
ᚪᚳ-ᚢᚷᚾ-ᛈᛖᚾᚦᚩᚢᛁᛡᚱ-ᛏᛁᛒᛇᚳᚠᚷ-ᚩ/
ᚦᚪ-ᛁᛈᚻᛡᛒ-ᚹᛈᚻᚱᛞᛉᛏᚢ-ᚣᛒ-ᚠᛋᛉᚢ-ᛗᛁ-/
ᛡᚱ-ᛝᚢᚠᚦᛝ-ᛈᛟᛒ-ᚻᚷᚻᛡᛚ-ᚩᛞᚪᚳ-ᚦᛈᛞᛋ/
ᛡᚻᛇᛚ-ᚢᛏᛋᛞ-ᚦᚢᛞᛝ-ᛚᛉᛝ-ᛏᚩᛚ-ᚪᛚ-ᚣ-ᛟ/
ᛡᛉᚣ-ᛒᚻᚫᛄᛡᛁ-ᚱᚦᛚᚠ-ᛠᚾᛝ-ᛉᛗᛒᚩᛠᛈ-/''', UnsolvedTranslation()),

        ('''
ᛖᛞᚪᚫᛏᚩᛠᛖᛠᛉᚳᛠᛏ-ᚩᛞᚳᛠᚾᚳᚦ/
ᛗ-ᛞ-ᚷᛁᚳᚹᛟ-ᚪᚢᛒᚳᚫ-ᚦᚱ-ᛋᚣᚪ-ᛏᚦᛒ-ᛝᚹᛋᚱᛁ/
ᛝ-ᛒᛁᚪᚫᛚ-ᛏᚱᛡᚫᚠᛞ-ᛝᛄᚩ-ᛡᛠᛉ-ᚪᛡᚻ-ᚱᛒ/
ᛁ-ᛞᛡᛄᚪᛈᚱᛋ-ᚢᛡ-ᚻᚷ-ᛚᛟᚠ-ᚻᚷᚫᛋ.ᛈᚹᚷᚷ/
-ᛗᛟᚪᚾᚱ-ᚩᛟᛞ-ᚷᛟᚠᛠ-ᛡᚷᚳ-ᛉᛠᚠᛚ-ᛒᚫ/
ᛈ-ᚩᛄᛈ-ᛄᛗᛠ-ᚾ-ᛉᚪ.ᛡᛖᛋᚷᚫᚦ-ᛄᚷᛉᚩᚦ/
ᛄᚳᚣ-ᚢᛄᚦᛄᚪᚾᛏᛒ-ᚳᛈᛡᛄᛋᚫ-ᛋᛗ-ᚻᛞᛠ/
ᛉᚢᛗ-ᛏᛠᛖᚣᚠ-ᛄᛏᛋᛗᛞᛟᛁᛝᚪᛉᛖᛈ-ᛚ/
ᛇᛞᚦ-ᚪᛋᛉ-ᚳᛒᚢᛟᚳᛒᛚᚾᛟᛝᛉᚩ-ᛖᚳ-ᛝᛟ/
ᚳᛁᛒᛈᚫ-ᚣᛖᛄᛝ-ᛞᚢᚱ-ᛉᛟᚩ-ᚠᚹᚩ-ᚣᛁᚠᚢᛇ-ᛚ/
ᛏᛈᛒᛗ-ᛇᛝ-ᚢᚳᚱᛡ-ᛖᚩᛁᚣᛄᛏᛡ-ᛖᚠᛇᚠᛚ-ᛁ/
.ᚣᚷᚠᛝᛡᛈᚷᛒ-ᛡᚩᚷᛡ-ᛟᚾᚹᛡᛈᛟ-ᚦᛈ-ᛟᚷ/''', UnsolvedTranslation()),

        ('''
ᛚᚦ-ᛈᛞ-ᚦᛇᛒ-ᛡᚪᛒᚪ-ᚾᛗ-ᚳᚾᛖᛡᚹᛝᛏᚱ-ᛝᚫ/
ᛚᛟᛁᛇᚣ-ᛝᛡᚾᛏ-ᚱᛁ-ᛋᚪᛖ-ᛇᚢ-ᛝᛞᛄ-ᚠᚱᛠᛗ/
ᛠᚪ-ᚫᛈ-ᛏᚠ-ᛖᛏᚷᚾᚠᛁᚠ-ᚱᚻᚱᛇᛒ.ᚻᛈᛏ-ᛇᚱ/
ᛝᛡᛒᚹᛚᛏ-ᛗᛉᚦ-ᚾᛄᚳᚫ-ᚷᛈ-ᛋᛖᚩ-ᚢᛝᚩ-ᛏ/
ᛈᛁᚣᚾᚪ-ᛏᚹ-ᚠᛗᚾᛟᚾᚳᛒ.ᛄᛉᛡ-ᛟᚪᛁᚫᛝ-ᛒ-/
ᛉᛏᛄᛁᛋ.ᛠ-ᚳᛖᚱᚦᚣᚩᚣ-ᛈᚫᚷ-ᛡᛄᛁᚩ-ᚱᚦ/
ᛠ-ᛇᚦᚩᛉ-ᚾᚱᚾᚫᛁᛉ-ᛁ-ᛝᚣᚫᛡᚫᛗ-ᚹᛖ-ᛇᚷᚻ/
ᛖᛗ-ᚷᚢᛞᚹ-ᛄᚻ.ᛉᚱᚢᛄᚢᚾᛈ-ᛋᚣᛄᚫ-ᛈᚳ/
ᚣᚳᛒᛡ-ᚫᛟᚪᚠ-ᛏ-ᚷᚩᛇᛟ-ᛁᚱᛗ-ᛖᛉᛟ-ᛗᛇᚫᛟ/
ᚦ-ᚱ-ᛞᛁᚢᚦᚻᛗᛡᚾ-ᛁᚦᚻᛚ.ᛏᚳ-ᚪᚦ-ᚠᚪᚫᚣᚻ/
ᛠ-ᚦᚠᛋᚠᛝᚷᚱᛈ-ᛏᛄᛉᛟ-ᚷᛚᚻ-ᚩᚪᚦᛏᚳᛁ-ᚠ/
ᚣᚢᛁᚹ-ᛟᚪᚣᛁᛠᛄᚪ-ᛟᛝᚦ-ᛟᚠᚦᚾ-ᛇᚷ-ᛠᛚᛒᚠ/''', UnsolvedTranslation()),

        ('''
-ᛠᚪᛄᛇᛠᛚ-ᚱᚷᛋ-ᚹᚩᛒᛁ-ᛠᚳ-ᛁᛞᛄ-ᛖᛗᚱ-ᚷ/
ᚪᚻᛠᛚᚷᚩ-ᛉᚻ-ᛡᛝ-ᛞᚱᚹᚩᛈᛡ-ᚣᚳᚦ-ᛁᛇᚢᛁ-/
ᛟᚦᚠᚳᚻ-ᚩᛁ-ᛝᚾᛁᛞ-ᛏ-ᚫᚱᛝᚫᛈ-ᛠᛞᛇᛉᚳ/
ᛠᚩᛟᛖ.ᛗᛈᛒᚦᛝᛋᚢᛡ-ᚻᛡᛏ-ᛉᛇᚷᚠᛡᛡ/
ᛟᚢ-ᛡᚦᚣᛞᚪᚫᛝᛒ-ᚳᚩᚷ-ᛏᛞᚦᛁ-ᚠᛒᛖ-ᚦᛟᚳ-/
ᚠᚻ-ᛞᚠᚣᛋᚾᛟ-ᛠᛇᛄ-ᛖᛉ-ᚩᛈᛠᛚᚪ-ᛟᚩᚾ-/
ᛄᛉᛋ-ᚣᚫᚷᛖᚩᛟᚢᚱᚹᚢ-ᛟᛡᛄᛇᚢᛞᛉ-ᛒᛇ/
ᚳ-ᛝᛚᛗᛠᛗ-ᚪᚱᛡᛗᛒᚩᚹ-ᛋᛖᚾᚻᚣ-ᛈ-ᛞᛚᛞ/
-ᛈᛏ-ᚪᛞᛚᛉ-ᛟᚱᚾᚹ.ᛠᚠᛁ-ᛟᚾᛒ-ᛇᛟᛖᛝᚳᚠ/
ᛏᛞᛏ-ᛇᚫ-ᛝᚢ-ᛠᛡᚫᛖᛟᛞᛝᛠ-ᚠᛗᛒᛚ-ᛏ/
ᚢ-ᛈᚱᚹᛟᛇᛉ-ᚳᛟᛈᛏ-ᚢᚠᚳᛞ-ᛄᛋᛞᛈᛚ-ᚠᛝ/
ᚱᛄᚣ-ᛞᛗᛖᚣ-ᚢᛖᛝᛠᚳᛞᛈᚩᛠ-ᛏᛒᚳ-ᚷ/''', UnsolvedTranslation()),

        ('''
ᚾᚩᛟᚾᚠ-ᚩᛁᚠᚢᛋᚾ-ᛞᚹᛠᛇᛈ-ᚱᚩᚩᛄ-ᚪᛟ-ᛇᛠ/
ᛄᛁ-ᛟᛄᛞᚢᚳᛝᚩ-ᚱᛝᛋ-ᛄᛁᛈᛉᛖ-ᛞᛁᚾᛗᛗᚳ/
.ᛉᚩᛁᛄᛞᚳ-ᚢᚪᛇ-ᚦᛡᛇᚻᛠᚣ-ᛠᚻ-ᚠᚩ-ᛡ/
ᛠᛋᛟᚪ-ᚹ-ᚫᚻᚩᛄᚢᚱᚩᚣ-ᛏᚫᚪᛡᚷ-ᛄᛚᛄ-ᛝᛏ/
ᛖᛒᛚᛉᚻ-ᚱᚩᚫᛇᛈᛄᛠ-ᚳᛈᛚᚣᛈ-ᚪᛠᚻᚻᛋ/
ᚫ-ᚩᛝᚹ-ᛋᛞᚠᚳᛠ-ᚩᛇᚫᚪᚩᚹᛗᚪ-ᚣᚫᚷᚫᛄᚱᚹ/
ᛞ-ᚱ-ᚦᚷᚳᚹ-ᚾᚷᛡ-ᛚᛒᚳ-ᛄᚷᚹᚹ.ᚱᛁᚠᛏ-ᚠᛚ-ᛋᛄ/
ᛚᚪᛄᚱᛏ-ᛞᚷᚫᛠᚠᛉᛞ-ᚫᚷᚻᛏ-ᛗᚣᛈ-ᛏᛒᛟ/
ᛝ-ᛄᛋᚾ-ᛝᛁᚹ-ᚦ-ᛠᛝᛞᚾᛟᚷᚫ-ᛁᛗ-ᛝᛉᚱᛞᛋ/
ᛗ-ᚠᚫᚹ-ᛟᛋ-ᚦᛞᛞᛈᛝ-ᛞᛡᚷᛒ-ᚪᛟ.ᚦᛡᛒ-ᚪᚹ-/
ᚾᛉᚫ-ᛚᛈᛁ-ᛒ-ᚠᚾᚠ-ᛡᚩᛏᛞᚾᛋᛖᚳᚻ-ᛖᚻ-ᚢᛟ-/
ᚪᛖᛗᛝ-ᛠᚫ-ᛈᚩᚪᛞ-ᚠᚫᚻ-ᚠᛏᚦᛄᛚᛄᛒ-ᛗᛇ/''', UnsolvedTranslation()),

        ('''
ᛈ-ᛄᚢᛒ-ᚷᛁᛇ-ᛈᛉᚣ-ᛈᛟᚦᛞᚱᛠᚪᛡ-ᛝᛡᛒᛚ/
ᚻᚦᚫᛉ-ᛟᚫ-ᚪᛇ-ᛉᚳ-ᛠᚠᚫ-ᚢᚣᚦᛋ-ᚠᛝᚠᚱᚹ-/
ᛟᛒᛗᚷᛞᚾᛡ-ᛞᚪ-ᚻᚣᛇ-ᚱᛚ-ᛖᚣᛇᚻᛠᚩ-ᚢ/
ᚳᚱᚻ-ᛡᛟᛗᛠᛝᛄᚦ-ᛄᚢᛁᛇ-ᛄᛁ-ᛖᚷᛁ-ᚪᛇᛏ-ᛝ/
ᛡᚳᛚ-ᛇᚠᛗᚪ-ᚷᛚᛒᛋ-ᛉᛞᚫᛟᛋᛚ-ᚹᛏᛠᛗ-ᛚᚦ/
ᛗ-ᛝᚦ-ᚣᛈᚠ-ᚪᛞᛚᚪᛖᛚᚩ-ᚱᚷ-ᛚᚳᛇᛏᚷᚣᛟᛗ./
ᚪᛁ-ᚷᛄᛒᛡᛗ-ᛞᛈᚪᚳᛠᚷᛋ-ᛏᛈ-ᚩᛋᛏᛗᚱᚣ/
ᛋᛉ-ᛁᛄᛚᛝᛚᛁ-ᛉᚢᛠᛗᛇᚢᛋᚻ-ᚳᛉᛄᚩ-ᚠᛄᚠ-/
ᛁᚣᛁᛟ-ᛏᚷᚱᚦ-ᛡᛒᛋᚳ-ᛇᚢᚷ-ᛚᚱ-ᛁᛗᚱ-ᛗᛝᚻᛈ/
ᚫ-ᛝᛋᚫ-ᛖᛈᛁ-ᛒᛇᚹᚫᚢᛄᚳᛒ-ᚦᛋᚹᚦᚫ-ᛡᛟᚷᛚ-/
ᛞᛚᚢᛟᛡ-ᚱᛞᚱᛒᛄᚳᚢᛠ-ᚩᛉᛉ-ᛝᛡᛄ-ᛁᚫᛟ/
-ᛖᛗᚹ-ᛖᛉᚦᛗᚪᛋᛉ-ᛞᚦ-ᛡᚢ-ᛉᛗᚫᛋᚳᛖ-/''', UnsolvedTranslation()),

        ('''
ᚳᚫᛠ-ᛞᚳᚷ-ᚩᛁᛇ-ᚾᛟᚷᚣᚳᚦᚳᚦ-ᛗᚣ-ᛈᚪᛒ/
ᛈ-ᚻᚢᚻᚾᛏᚫᛒᛇᚩᛁᛈ-ᚫᚩᚣ-ᛡᚣᛗᚷ-ᚠᚱᛡᛚ/
ᛏ-ᛖᛟᚩᛈᛚᚩᚷᛁᛟᛠ-ᛞᛖᚳᛗᛁᚣ-ᛈᛚ-ᛁᚹᛋᛄᚹ-/
ᛟᛡᚪ-ᚦᛖᚩᛄᚷᛋᛝᚣᛗᛟᚻ-ᛗᚠᚦᛉᚦᚫᛋᛈᚣᚩ/
ᚠ-ᛈᛟᛋᛖᚫᛇᛗᛚᛈᚾ-ᛡᚠᚳᚾᚩᛄᛋᛡ-ᚫᛄᚦᚪᛠ/
-ᛈᚻᛋᛟ-ᛗᚹ-ᚱᚣᛁᚢ-ᛉᚹᛋᚱ-ᛞᛈᚦᛈᚩ-ᛞᛄᚩ-/
ᚢᛈᛖᚪᚫᛉᚫ-ᛏᚱᛟᛏᛒ-ᛠ-ᚫᚳᚾ-ᛖᛝᚦᛄᛄᚠ/
ᛚᚾᚩᛒ-ᛉᚷ-ᚪᚩᛚ-ᚪᚢ-ᛞᚻᚳᚹᛚᛡᛞᛇ-ᛟᚩᛡᛚᚳ/
-ᛡᚳᛉ-ᛝᛠᛝᚷᛝᛞᛄᛏ-ᛠᛈ-ᚹᛈᛗ-ᛈᚱ-ᚫ/
ᛏᛖᚢᛝᚫᛡ-ᚾᛁᛠᚻᚦᚣᛠ-ᚫ-ᚩᛉᛋᚩ-ᛄᚠᛏᚷ-/
ᚹᛁᚪᛁᚩᛁ-ᛝᛠ-ᚾ-ᚷᛗᚹᚦᛖ.ᚷᛟᚪᚹᛞᚻᚢ-ᛡᚹ-/
ᚣᚷᛉᛒᚪᚾᛝᛡᛄᛡ-ᚠᚷᛈᚦᚠᚦ-ᛁᛈᚪᛝᛋᛞᛟᚩ/''', UnsolvedTranslation()),

        ('''
ᛝᛗ-ᛁᚷ-ᛄᚷ-ᚳᚩᚦᛖᚦᛄ-ᚣᚠ-ᚦᚳᛄᛡᛖᚢ-ᛉᛄ/
ᚳᚻᛄᚱᛄ-ᚪᚻᚾᚦ-ᛚᚷ-ᚱᚦ.ᛒᚪᚩᛖᚢᛡᛄᚹᛏᚱᚹ/
ᛟ-ᚦᚳᛗᚦᚠᚫᚻ-ᛡᚠᛠᚣᚪᚦᛚᛏᛒᚢᛝ-ᛖᛋᛗᚱ-/
ᚪᚹᛒ-ᚹᛒᛗᚱᚾᛗᚻᛗᛁᚾᚪᛞ-ᛡᛖᚩ-ᚾᚹᛡ-ᚢᛄ/
ᚦᛠ-ᛚᚳᚷᛚᛇ-ᛟᛠᛠᚪ.ᛇᛉᚣᚪ-ᚷᛏᚩ-ᛖ/
ᚹᛒᛈᚷᛝᛒ.ᛡᚦᚠᛋᚾ-ᛒᚦᚠ-ᛇᛝᛠ-ᚠᚾᛉ./
&
$''', UnsolvedTranslation()),

        ('''
ᚢᚪ-ᚹᛝᚷᛉᛞᚷ-ᛁᛒᛁ-ᛇᛏᛒᛁᚣ.ᛠᚷᛋᚫ/
ᛈᚹᛗᛠ-ᛇᛄᛇ-ᚹᚻᛁ-ᚷᛠᛒᚢᚣᚻᚣ-/
ᛝᚹᚢᚱᛋ-ᚩᛡᚠᛡᛠ-ᛞᛟᚦᛗᚳᚾᛉ-/
ᛞᚦᛖᚱᛇᚳ-ᚪᛄᛋᛟ-ᚢᚹᚱᛏ-ᛋᛖᛋᛏ-ᚣᚱᛠᚫᚾ/
ᛞ-ᛈᛒᛡᛋᚢᛞᛖᚣᚦ-ᛚᚹᛟᛋ-ᚷᛚᛄ-ᚫᛖᚩᚳᚦᚹ/
ᛗ-ᚢᚩᚷ-ᚠᚪᚩᛡᛝᛒᛠᚦᚳᚪ-ᚱᛡᛏ-ᛟᚹᚠᚣᛝᚢ/
ᚣᛁ-ᛚᛏᚫᚫ-ᚪ-ᚱᛈᚠᛗᚹᚩᛞ-ᛠᛒᛈ-ᛝᛟ-ᚾᚷᛗ-/
ᛡᛖᚩ-ᚾᛚᛉᛝ-ᛁᛡᚫᛗ-ᚻᛖᚹᛗ-ᛝᛈᛇᛗᛡᛄ-ᚫ/
ᚩᛡ-ᚠᚣᛉᛟᚫᚦ-ᚫᛒᚩ-ᚪᚦᛄᚱᛄᚾᚦ-ᛡᚠᚪᛏᚾᚻ-ᚷ/
ᚢ-ᛞ-ᚳᚦᚢᚱᚢᛟ-ᛞᚻᚱ-ᚷᚹᛏᛈᛖᚠ-ᚪᚻᛠᚦ/''', UnsolvedTranslation()),

        ('''
ᛞᚱᚠ-ᛖᛄᚫ-ᚾᚳᚻᚹ-ᛇᛡᛈᛠᚹ-ᛗᛚ-ᚹᛟᚹᛠ-ᚪ/
ᚾᚪ-ᚳᚪ-ᚷᛚᚦᛒᚩᚹᚢ-ᚷᛚᚠᛋᚻ-ᚾᛉᛝᛗ-ᛖᚦᚢᛝ/
ᛡ-ᛈᚣᚢ-ᛉᚷᚷ-ᚹᛞᛁᛋ-ᚦᛡᛡᛈᚳᚪᚩ-ᚢᛗᚢ/
ᛉᚩᚣᚻᛏ-ᚩᚫᛗᚢ-ᚩᚾᛏᛠᛒᛟᛒᚠᛁᛈ-ᛚᛋᛝᚫᚳ/
-ᚫᛟᛏ-ᚢᚩᛉᚾᛡᛋᚠᛖ-ᛉᚱ-ᛗᚩᚩᚫ-ᚠᚢᚦᛖᛞᚾ/
ᚣ-ᛡᛋ-ᛋᚱᛚᛟ-ᚢᚻ.ᚢᚾᛈ-ᛁᚻ-ᛖᛉ-ᚦᛞᛗ-ᛈᛟ/
ᚠ-ᛈᚠᛝᚫᛝᛋ-ᛟᛄᚹ-ᛠᛒᚣ-ᛟᚹᛞ.ᚠᚣᛄᛁᛏᛉ/
ᛚ-ᚩᚦᛝ-ᚠᚪᛋᛡᛁᚻᛒᚱ-ᚪᚢᚣ-ᚫᚢ-ᛟᛠᚪᚣ-ᛖᛟ/
ᚫ-ᛖᛈᚠᛒ-ᛈᛄᛁ.ᛋᛝᛒ-ᚱᚦᚳᛇ-ᛚᛁᚢᛈᛏᚳᛒᛉ-/
ᛖᚪᚣᚠᛗᚳᚣᚱ-ᚻᚹᛏᚾᛡᛉᚫᚦᛟ-ᚳᚹ-ᛠᚠ-ᛏ/
ᛠ-ᛝᚩᚻ-ᛡᛠᛒᛋᚻᛟ-ᚫᛁ-ᛠᛏᛁᛋ-ᛏᚫᚻᚱ-ᚻᛄ/
ᛋᛡᚹᚾᚾᛡᚹᛚ-ᚢᛖ-ᛏ-ᚱᛝᚳᚣ-ᚪᛉᛇᛝᛋᛖᛇᛁ/''', UnsolvedTranslation()),

        ('''
ᚻᚾ-ᚷ-ᚹᛉᚳᛉᚣ-ᛋᛈᚳᛟᚱ-ᛒᚣᛄᛝᛖᛁ-ᚾᚷᚪ-/
ᚣᚷ-ᛚᛒ-ᚢᛄᚩ-ᛝᛉᛉᚪᛖ-ᛒᚦᛉᛡᚱ.ᛏᚷᚹᛄᛋ/
ᛁᚠ-ᛠᛁᛡᚦᛝᚾᛖᚾᚠᚩᛗᛖᚣᚪ-ᚳᛖᚳᚹᚪᚫᚹ-ᛇ/
ᚢᚦᚻᛉᚢᚾ-ᛠᛚᚢᚾᚦᛈᛋᚢᛈᚱ-ᛞᚫᛟᚱᛡᚫᚪ/
ᚢ-ᚢᛗᛚᚦᛠ-ᛚᛝᛈᚣ-ᚩᛋᛟᚪᚱᛗᚦᛟᛈ-ᛚᛋ-ᛏᛁ/
ᚠᛋᛖᚹᛝ-ᛗᛞᚩ-ᛠᚫᛡᛒᛏᚩᛋ-ᛖᛏᚪᚠ-ᚫᛒ-ᛚᚾ-/
ᛋᚪᛉᛟ-ᚾᛚᚹᛖ-ᚩᛚᛁᛄᛏ-ᛒᚪᚠᛉᛏ-ᚩᛟᛄ-ᚾᚷᛋ-/
ᚷᛚᚷᛠ-ᛒᚷᛖᚩᚪᚩᛖᛞ-ᚷᛇᛗ-ᚳᚱᚷ-ᛈᛞᚩᚠᚹ/
ᛇ-ᛠᛞᚣᛝ-ᚾᛁᚠᛈᛚ.ᛖᛟ-ᚢᚳᛗ-ᛚᚫᛏᛉᛄᚱ/
ᛉ-ᛁᛠᚷᛚ-ᚷᚳᛋᚩᛝ-ᚫᚦ-ᛗᚻᛟᚠ-ᚱᛋᚳᚦ-ᚣᚩ-ᛒᛁ/
ᚫᚻᛖᚢᛏᛚᛚ-ᛇᚷᛟᚣ-ᛒᚾᚦᚻ-ᛠᛖᛄᛒᚾᛁᛚᛠ/
ᚱ-ᛄᚠᚳᛋᛝᚳᛈ-ᚷᚻᛋᛗ-ᛇᛞᛇ-ᚣ-ᛡᛖᛏᛠᚢ/''', UnsolvedTranslation()),

        ('''
ᛡ-ᚩᚾᛠᚩ-ᛄᚣᛇᛉᛠᚪᛡ-ᚾᛞᛝᚻ-ᛈᛠᚻᛡ/
ᚢ-ᛝᚻᚦᛈ-ᛉᚢ-ᛠᚣᛈᛟᚦᛋᚣᛈ-ᚠᛏ-ᛒᛁᛟᚪᚷ/
ᛚ-ᛠᚻ-ᛝᛁᛡᛚᛝᚾᛞᚪᛈᚷ-ᚾᛏᚦᛋᛒ-ᛋᛋᛠ-ᚷᚳ/
-ᛠᛗᚢ-ᛖᛉᛒᚷᚫᚠᚩᛁᛉ.ᚠᚪ-ᛠᚱᛇ-ᚩᛁᛞᛋᛚ/
ᚦᛖᛒᛇ-ᛟᚷᚣᚷᚾᚷ-ᚦᚠᚳᛗ-ᚩᛖᛖ-ᚩᚠᛒᚻᛝ-ᚳᛁ/
ᛄᚪᚾᚩᚪ-ᛈᚻᚱᛗ-ᚱᛗᛟ-ᚦᚷᛄ-ᛒᚱᚦᚪᛠ-ᛉᛖᛡ/
ᛞᚦ-ᚱᛝᛄᛒ-ᚾᛏᚣ-ᛏᛋᛒᚾᚫ-ᚢᛖᛁᚩᛡ-ᛄᛇᚢᚦᛚ/
ᚳᛖ-ᛚᛁ-ᛒᚢᚠᚪᚱᛠ-ᛗᛒ-ᛞᛉᛗ-ᚢᛠᛏᚣ-ᚪᛄ/
ᛈᚢᛈᛠᚣᚷ-ᛗᛡᛗᚢᚪᛗᛝ-ᚣᛡ.ᚪᛖᛏ-ᛖ/
ᛋᚪᛟ-ᚳᚻᛁᛋᚠᛁᚾ-ᛈᛟᛝ-ᛇᚦᚣᛏᚫᛉ-ᛖᛟᛏ-ᛞᛡ/
ᛚᛖᛈᛏᚪ-ᛏᚠᚱᚾ-ᚪᛠᚱ-ᛠᚳ-ᚾᚻᚹᛒᛇᛋ-ᛁᚻᚣ/
ᛋᚹᚩᛉᚹ-ᚩᛝᚢ-ᚻᛝᛟ-ᛏᛚᚠ-ᛄᚷᛏᛝᛄᛝ./
&
$''', UnsolvedTranslation()),

        ('''
ᛗᛈᚣ-ᛚᛋᚩᚪᚫᚻᛚᛖᛇᛁᛗᛚ-ᛚᛋᚳᛈ.ᚾ/
ᚻᚷᚢᛡᚻᚢ-ᛒᚠ-ᛞᛄᚢ-ᛒᛖᛁ-ᚫᚠ-ᛈ-/
ᚫᛈᚦ-ᚱᛗᛚᚳ-ᛒᚷᚣᛗᛠᛒᚫ-ᚾᚦ-ᛗᚠ/
ᛡᛠᚳᛒᚷᚫᚠ-ᛖᛄᚱᚩ-ᛈᛒ-ᚠᛒᚩ-ᛇᚱᛠᚱ-ᛠᚷ/
ᛖᛚ-ᛇᚱᚾᛋᚩᚩᚳᚪᛖᚣᛖᛖ-ᛏᚱ-ᚢᚣ-ᛟᛄᛉ-/
ᛠᚷᛝ-ᚣᛏᛝᚾ-ᚪᛏᛋ-ᛝᚪᛄ-ᚠᛚᛋᚢ-ᚹᛠᛈᛁᛏ-/
ᛁᚾ-ᚱᚱᛝᛗ-ᚣᛗᚠᛁᚫᛁᚪ-ᚢᛟᛒᚹ-ᛗᛁᚻᚣᚹᛞᛚ.ᛟ/
ᛏᛞ-ᛟᚳᛒ-ᛡᛒ-ᚪᛏ-ᚹᛏᛈ-ᚹᛠᚩᚱᚩᛖ-ᚣᛚᛋ./
ᚢᛡᚱᚠᛄᛇᚱᛡᚦᛖᚢᛏ-ᛝᚫ-ᚾᚪᛠᚩᚪᚾᚪᚦᚷᚩ-/
ᚫᛉᛒᛏᛖᛠᛗᚷᚱᛗ-ᚣᛝᚠᛒ-ᛞᛟᛞᚪ-ᛠᚱᚳᛁ/
ᛈᛞᚠᛗᛝᚻ-ᛋᚩ-ᛞᛈᛉᚾ-ᛟᚱᛡᚾᚳᚳᛏ-ᚾᛈᚠ/''', UnsolvedTranslation()),

        ('''
ᛈᚳ-ᛄᚦᛒᛁᚹ-ᛞᚹᛝᛠᛡᚹᛚ-ᚹᛄᚾᚪᛟ-ᛏᛞᛉᚣ/
ᛖᚱᛞ-ᚱᛏᛇᛁᚳᛈ-ᛝ-ᚦᛟᚷᛄᚦ-ᚣᛋ-ᛠᚻ-ᚠᛒᛚ-ᛁ/
ᚫᛚᛞᛉᚪ-ᛁᚹᚷ-ᛒᚩᚹᚾᛠ-ᛋᛖᛗᛒᛋ-ᚳᚹᚦᛟᚠᚻᚫ/
-ᛞᚢᛁᛒᛞ-ᛇᛝᛈᚠᛁ-ᛟᚢᚣᛏ-ᚻᚱᛖᚾᚳᛈᛡᛈᛞ/
ᛄ-ᛁᛏᛗᛋᚫᛉᚩᚣ-ᚪᛄᛗᛡᛖ-ᛇᛄᚠᛗᚱ.ᛞᛟᚪᛒ/
ᛞᚻ-ᚾᛈᚪ-ᛇᚱᚻᚾᛝᛠᚠᚾᚠ-ᚩᛗᛋᚾ-ᛠᚪᛁᚢᛚ-/
ᚪᚫ-ᛄᛉᛡᚠ-ᛁᛖᛈᛠᚻ-ᚠᛇᚩᚹ-ᛠᛄᛇᛁᛠᚫ-ᛄ/
ᛒ-ᛋ-ᚠᛖᚷ-ᛋᛁ-ᛟᛗᛒᛁᛝᛏᚪᚢᛁᚦ-ᚩᛝᛗᚠ-ᚹᛟᛒᛟ/
ᛡ-ᚠᚣᛝᚩᛠ-ᚳᛚᛈᚱ-ᛞᛄᚩᛝᛄ-ᚪᛖᛗᛈᚾ-ᚠ/
ᛠᚷᛞᛒ-ᚩᛉᚷᚾᚣᚷ-ᛠᛈᛄᛞᚾᛟᚩᚢᚾᚹᛗ./
ᛄ-ᚢᚷᛠ-ᛗ-ᛇᚪ.ᚻᚦᛡ-ᛝᛈᛞᛒ-ᚳᛉᚳ-ᛠ/
ᛉ-ᛟᚣ-ᛒᚦᛁᛄᛚᛡᛝᛡ-ᚹᛄᚫ-ᛋᛗᚪᛡᛠᛇᛝᛏ-/''', UnsolvedTranslation()),

        ('''
ᚦᛞᚷ-ᚢᛏᛚᛏᚣ-ᚢᛝ-ᚷᛟᚪᛏ-ᛄᚦᚣ-ᚫᚻᚪ-ᛒᛝ-/
ᚦᚢᚱᚪᚾᛞ-ᛁᛝᚫ-ᛚᚫᚷ-ᚹᛁᛒᚣ-ᚾᚫᚠ-ᛚᛋᛒ-ᛈᛟᚪᛟ/
ᛞᚷᛟᚣᛉᚷᛚ-ᛋᛠᛁ.ᚳᛟᛁᚦᛈᚹᛉ-ᛖᚢ-ᛟᛄᛝ/
ᛋᚢᛝ-ᚳᛡᛠ.ᛚᛇ-ᛚᚷᚢᛁᛏᛒᛋ-ᛞᛁ-ᚠᚠᚷᚠ-ᚦᛄ/
ᚳ-ᚫᛟ-ᛁᛗᛡᛁᛇᚦ-ᚩ-ᚢᛈᛒ-ᚻᛋ-ᛄᚣᛄᛖ.ᛒᛇᛇᚱ-/
ᚹᛄᛏᛡ-ᚳᚪᚫ.ᚩᛈᚱ-ᛡᚾᛗᛁᛝ-ᚻᚹᚦ-ᛡᚦᚻᚦ-ᛉ/
ᚫᚫᛋᚳᛡᚾᛇ-ᛟᛉᚢ-ᚱᛄᛖ-ᛚᚾᛞ-ᛗ-ᛏᚱᛟᚦ-ᛁᛝ/
ᛡᛒ-ᚳᚩᚹᛟ-ᛏᛗᛋᚱᚷ-ᚱᛚᛞᛚ-ᚩᚣ-ᛞᚳᚪᛖᛞᚠ/
ᚳ-ᛇᛖᛉᛚᚫ-ᛖᚩᛁᛋ-ᛡᛁᛟᛋᚪᛒᛗ-ᛗᚣᚹᛄ-ᛖᚫᛝ/
ᛚ-ᛄᚱᛇ-ᛈᛚᚩᚻ-ᚪᛞ-ᛡᛄ-ᛞᚠᚹᛞᛄᚳ-ᚾᚦᛉ-ᛄ/
ᚻ-ᚷᛚ-ᚠᛖᚦ-ᛇᚻ-ᛝᛖᛒᛚᛞᛁᛗᚠ-ᚹᛒᛗᛟᛁᛖᛁᛠ-/
ᛈᚻᛝᛖᛞᛟᚩᚻᛄ-ᚹᚩᚾᛄᛈᛗ-ᛖᚳ-ᛖᛇ-ᚷᚻᛗ/''', UnsolvedTranslation()),

        ('''
ᛞᚪᛈᛖ-ᛗ-ᛉᚫᛒᛇᚱ-ᛖᚣᛟᚣ-ᚱᛠᛈᚢᛠ-ᚣ/
ᛖᚪᚻ-ᚩᛉᛠᚢᚻᛡᛟ-ᚷᚫᚩᛒᛉ-ᚫᚱᛞᛋᚩᚱ-ᚷ/
ᛠ-ᛉᚻᛁ-ᚷᚳᛞᛠᛡᚳ-ᛄᛠᛉᛇᚻᛋᚹ-ᛝᛡᚷ/
ᛖᛡᚣ-ᛠᚩᚷ-ᚱᚦᚠᛟᚩᚦ-ᚦᛁᛏᚱ-ᛇᛉᛇ-ᚢᚷᛠ-/
ᛟᛏ-ᚩᚠᛚ-ᛟᛝᛈ-ᚱᛡᚪᚩᛏ-ᚩᛠᚷᚫᛗ-ᛈᛋᚱ-ᛖ/
ᚦᚠ-ᛞᚹᚾᛚ-ᛝᚩᛇᛄ-ᚳᛚᚢᚹᛏ-ᚩᛖᛏᚠᚪᛚ-ᛟᛇᛟ-/
ᛠᚱᛇ-ᚢᚪᚦᛈᛟᛡᛉ.ᛡᛒᚱᛒᚠᚢᛚᚢᛟ-ᛒᛇᛒ-/
ᛉᚦᚹ-ᛝᚣᛖ-ᚳᚫᚣᛟ-ᚹᛁᛝᚫᛏ-ᚫᛇᛈᛡᛟᚠ-ᛚ-ᛝ/
ᚠᛡ.ᛞᚪᛚᛈ-ᛋᛁ-ᚢᚣᚪᛚᛠᛝᚹ-ᚪᛏᛈᚳᚣ-ᛝᚫ/
ᚻᛗᛞᚷᛚ.ᛠᛉᛒ-ᛇᛡᛋᛖ-ᚣᛁᛚ-ᚣᛠᚣ-ᚻ./
ᚣᛉᚾᛏᚫᛉᛋᚦᚪᚹᛗ-ᚪᚱ-ᚪᚩᚻ.ᛗᛖᚫᛞᛠᛁᛗ/
-ᛒᛟᚾᚳᚩᚱᛉ-ᛋᚹᚫ-ᚻᛖ-ᛋᚠᚾ-ᚢᚦᛟᚷᛖᚪᛟᛇᛇ-/''', UnsolvedTranslation()),

        ('''
ᚦᚳᛒᛝᛏᛉᛡᛞ-ᛋᛡ-ᚩᚠ.ᛈᛖᛞᛋᛁ-ᛚᛁᚻᚾᛝᚱ-/
ᚻᛈ-ᛇᚢᚫᛞ-ᛚᚻᛉᚳᛈ-ᛁᛗᛉᚳ.ᛄᚫᚾᛞᛋ-ᛏᛚ/
ᛡᚩᛋᛗ-ᛚᛞᚾ-ᛈᚫᛏᚷᛈ-ᚫᚦᛄᛗ-ᛒᚻᚩᚻᛁᚷᚻᚳ-/
ᛚᚹᛋᚱᛇᛗᛏ-ᛄᚳᛁ-ᛠᚦᛞ-ᛏᛚ-ᚱᛖᛠᛒᚪ-ᛒᚠᛒ-ᛁ/
ᛒᛡᛇᛏᚣ-ᛏᛖᚣᚳᚱᛋᚠ-ᛁᚦᚪᛉ-ᚪᚣᚫᛠ-ᛄ-ᛈ/
ᛗ-ᚠᛋ-ᚪᛒᚱ.ᛉᚣᚻ-ᚦᚩ-ᛇᛞᚢ.ᚠᛁ-ᚻᚩᚫᚠᚣᚷ/
ᚱᚪᛄ-ᛏᛉᛇ-ᛖᛠᛞ-ᛏᚠᚢᛝ-ᚫᛄᛖᛈᚳᛒᚦᚢ/
ᛝ-ᛡᛒᚹᚱ-ᛖᚾᛈᛇᚣᛇ-ᛉᚱᚹ-ᛒᛡᛞ-ᛖᚱᚩᚻᚣ/
ᛠᛈᚦ-ᛗᛁᚷᛚ-ᚹᛉᚫ.ᚠᛞᚾ-ᛄᛟ-ᚻᛚᛡ-ᛗᛖᚷ-/
ᛟᛁᛡ-ᚻᛟᚱᛇᚹᚣᚠ-ᛈ-ᛄᚷᚦ-ᚪᛒᛝ-ᛈᛒᚪᛖ-ᚢᚹᚻ/
ᚩᛒᛋᛉ-ᚹᛞ.ᚦᛇᚱᛖ-ᛄᚾᛞᛝᚹᚪ-ᚻᛖᚹ-ᛟᛡᛄ/
ᛡᛟᛝᛄᛉᛚᛄ-ᛞᛉᛟᛈ-ᚱᚪᛁᛏᚷᛉᛝᛇ-ᛠᛗᚩ/''', UnsolvedTranslation()),

        ('''
ᛚ-ᚦᚫᚹ-ᚫᚢᛈᛡᚳ-ᚹᛝᚻᚹᛒᛗᛋᛟᛖᛁᛡ-ᛟᚹᚦᚻᛒ/
-ᛡᚱᛏᚦᚠ-ᚠᚩᚦ.ᚻᚩᛗᛖᛉᚹᛞᛋᛚᚠᛞ-ᛝᛒᛇᛡ/
ᛚᚪ-ᚹᛞᚾᚫᛉᛏᚣᛗᚷ-ᚦᚹᛉᛡᚦ-ᚹᛒᛋᚱᛉᛡᛉ/
ᚪ-ᚢᛒᚻᛠ-ᚹᛝᚢᚻᛇᛝᛡᛠᛄ-ᛋᛈᚦᛏ-ᛟᛝᚩ/
ᛗᛒᚢᛞᛋ-ᛒᛄ-ᛠᚱᛟ-ᛖᚾ-ᚾᚹᚷᚢᛚᚪᚩᚣ-ᚢᛏ/
ᚠᛄᛏ-ᚪᚷᛒᛇ./
&
$''', UnsolvedTranslation()),

        ('''
ᛞᛇ-ᛉᚳᚠᛁᚪᚹᚻᚷ.ᛇᛟ-ᚠᛏᛖᛟᛠᚪ/
ᛡᛋᚷ-ᚣᛠᚾᚦᚫᚱ-ᚩᛡᛗ-ᚹᛉᛗ-ᚣ/
ᛞᛒᛏᚱ-ᚢᛄᚻ-ᚫᛟ-ᛡᛝᚹᚻᛋᚠᛡ-ᛚᚦ/
ᛏ-ᛁᚹᛏ-ᚩᚢᚾᚹᛗᛚ-ᛋᚦᛠᚹᛄ-ᚪᛄᚫᚷᚣᛗᚹᛞ-/
ᛈᛡ-ᛖᛄᚹ-ᛖᚢ-ᚻᚹ-ᛝᛁ-ᛋᚫᚷ-ᛄᛚ./
&
ᛝᚦᛇ-ᛁᚠᚳᛟᛇ.ᛞᛒᚣᛡᚣᚢ-ᚣᚾᚦᚱᛖ/
ᛗᛁ-ᛇᛞᚱᚹ-ᛉᛒᚻ-ᚳᛄᛡᚪ-ᚾᚹ-ᚾᛗ-ᚠ/
ᛇᛁ-ᛇᚪ-ᚩᛋᛒᛟ-ᛏᛄ-ᛈ-ᛖᛈᛄᚩᚹᚢᛠ/
ᛝᚹ-ᛗᚳᚩᛏᛏᚠᚢᛄ-ᛞᛠᛉᚩ-ᛉᚦᚷᛞ-ᛒᚩᛏᛚ/
ᛇᛁᛒᛡᚪ-ᛖᚠᛠᚢᛖ-ᛈᛋᚹᛞᛞ-ᛋᛡ-ᚹᚦᛞᛋ-ᛝ/
ᛄ-ᛚᚷᚢᛡ-ᚾᛉᚠ-ᚱᚪᚣᛗᚠᚦᚻ-ᚱᚪᚱ-ᚫᚪᚷᛟᛞ-ᛒ/''', UnsolvedTranslation()),

        ('''
ᛗᛒ-ᚾᚻ-ᛇᛞ-ᚻᛗᛚᛁ.ᛠᚾᛁ-ᚫᛖᚢ.ᛏᚦᛇᛋᛈᚻ/
-ᚻᛇᚳᛠᚫ-ᛞᛚᛋᛝ-ᛁᚹ-ᚪᚳᚩᛏᛇᛝᚷ-ᚳᚦᛋᛠᚠ/
ᚢᛝᛚᚻ-ᚹᚩᛇᚪᛈᚷ-ᛇᛗᛚᛄᛋᛏ-ᛚᚳᛈ-ᚾᛋᛝ-ᚳᚪ/
ᚳ-ᚾᛉ-ᚾᚢᛉᚫᛗᛏᛞᛏᚫ-ᛟᛗᛋᛉ-ᛏᚣᛉ-ᛇ/
ᛠᚷ-ᚻᛒᚾᚷᛇᚢᛟ-ᛄᚦᛉᚩ-ᚾᚪ-ᛞ-ᚩᛈ-ᛠᛚᛋ/
ᛏ-ᛒᚷᛁᚢᛟᛖᛁ-ᛄᚦᛖᚻᚹ-ᛄᚫᛄᚾᚻᛉᚹ-ᛒᚪᛋ-ᚠᚱ/
ᚱᛁᛉᚢᚦᚻ-ᚢᛗᚪ-ᛞᛝᛠᚪ-ᚫᛉᛖᚾᚹ-ᛟ.ᛝᛞ/
ᚾ-ᛈᚫᚳᛡ-ᛈᚠᛉᚩ-ᛒᚷᛗᚫ-ᛚᚻᛞᚣᛖᛉᛒ-ᛄᚹ/
ᛇ-ᛈᚩᛁᚦᚠ-ᚷᚾᛈᛞᛝᛏᛖᚪ-ᛄᛋᛠ-ᛈᛝᚢ-ᛒᚷ/
ᚳᛉ-ᚪᚢᛈᛚ-ᛄᚱᚷᚣᚪ.ᚪᚠ-ᛗᛝᚣᚳᛟ-ᚹᚣᚷ/
ᛈ-ᛗᛖᚩᚹᚢ-ᛟᛞᛋᚱ-ᚣᛞᛋᚳᛡᛉ-ᚻᚦᚹᛚᛞ/
ᛠᚩᛞᛠᚢᛟᛖ.ᛠᚹ-ᛉᚻᛡᚹᛞ-ᚪᛗ-ᚠᚦᛈ-/''', UnsolvedTranslation()),

        ('''
ᛝᛏᚳᚪ-ᛠᚣᚷ-ᚳᚦᛖᚾᚢᛁᚫᛁᚢᛡ-ᚹᛚᚳ-ᚻᛈ-ᛞ/
ᛄᚳ-ᛗᛒ-ᛗᚪᛄ-ᚩᚪᛞᛁ-ᚩᚱᛟᚠᛖᚣᛟᛁ.ᛇᛟ-ᛁᛈᚣ/
ᛚᚪᛡ-ᚳᛏᛠᛋᛖᛒᛝ-ᚫᛟᚫᛞᛖᛞᚣᛡ-ᛠᚪᛖ/
ᚦᛚᚫ-ᚳᛋᚪᚩᚷᚹᛚ.ᛈᛖᛏ-ᛄᛉᛝᛚ-ᛏᛉᚩᚣᛝ/
ᚠᚩᚣ-ᛁᚻ-ᛟᚫᚷᛄᛝᛡᚾᛗᚣᛟᛡ-ᛝᚷᛖᛉ-ᛟᛉ/
ᛈᛚᛋᛉᛠ-ᛚᛡ-ᚱᚪᛞ-ᛠᚷ-ᚱ-ᚳᛇᚻ-ᛗᚪᛟᚷ-/
ᛞᚪᛋᛡᚻ-ᛈᚷᛖᚳᛟᚱᛟᚢ-ᛁᚫᛟᚦ-ᛄᚱᛡ-ᚱᛖᚦ/
ᚣᛏᛝᛡᚩᛒ-ᛏᚦᚳ-ᛉᚳ-ᛋᚪᚫ-ᛗᚠᛄᚱᛖ-ᛡᛇᛁᛇ/
ᛟᛉᚳᚹᚪᛖ-ᛋᚢᛉ-ᛋᛟᛚ-ᛄᚾ-ᛈᛇᛒ-ᚦᚦ-ᛁᚫᛚᛋᛝ/
ᛄᛄᛡ-ᛟᚻᛇᚢᛚ-ᛁᚱ-ᛡᚻᛚᛏᚹᛉᛇ-ᚱᛏᛠ-ᛁᚫᛚ/
ᛗ-ᛁᚱᚷᛏᛠ-ᛇᛟᚻᛟᚳᛋᛏᚾᚩ-ᛁᚱᚷ-ᚹ-ᛞᚢᚣᛚᛁ/
ᛗᛒᚢ-ᛚᚱ-ᛏᛁᚢ-ᚷᚳᚠᛇ-ᛚᛇᚣᛏ-ᛏᚫᚢ-ᚫᛠᛇ/''', UnsolvedTranslation()),

        ('''
ᚣᚾ-ᚢᚹᛝᚻ-ᚷᚣᚱ-ᚩᛁ-ᛚᚾᛉ-ᚾᚩᛈ-ᚠᛠᚫᚫᚩ-ᛉ/
ᚾᛋᛟᚫᛚ-ᚾᚫ-ᚦᚢᛠᚣᚫ-ᛈᛁᛇᚢᚱᛄ-ᛈᛟᛄᚪᛝᛈ/
ᚦᛈᚪᛝ-ᚣᛗᛟ-ᛉᛒᚢᛏᛇᛗᛈᚫᚣ-ᛉᚫᚣᚱᚫᚣ/
ᚠᚠᛗᛡ-ᛉᛖ-ᚱᚢᛏᚷᚢᚣᚱ-ᛡᚢᚩᛇᛁ-ᛄᚠᛈᛄ/
ᛞ-ᛁᚦᚩᚻᛡᚷᚻ./
1-ᛚᚦᛇᛟ-ᚪᚫᛠ-ᛗᛉᚻᚳᛉᚪᛏᚦ-ᚫᛉ-ᚩᛋᚳᛞ/
ᛏ-ᚣᚹᚾ-ᛟᛏᛉ-ᚹᛁᛟᛄᚠᛁᚩ-ᛁᚱᛋ-ᛉᚾᛗᚪᛡ-ᚱᛈᛋ/
ᛞ-ᛁᛟ-ᚻᛖᛏᚢᚹ-ᛠᛟᛞᛟᛄᛁᛝᛡ-ᛄᚱᛞᛗᛒ-ᚩ/
ᚳᚩ-ᚦᛟᚱᚢᛚ-ᚢᚦᛋᚢᛞᛚ-ᚷᛁᚣᛝᚩᛟ-ᛁᛖᚣ-ᛖᚠ-/
ᛇᛝᛒᛚᛁᚢᚣᚠᛟᚾᛟ-ᛒᛟᚷᛄᚪᚾᛗᚫ-ᚣᚦᚠ-ᛁᛒᛝᛈ/
ᚾᛁᚱᚷ-ᛄᛇᚫ-ᚻᚪ-ᚱᛉᛉ-ᚩᛚᚾᚫ-ᛞᚣᛒᚾᚪ./''', UnsolvedTranslation()),

        ('''
2-ᚾᚣᛖᛉ-ᚾᚢᛉᛁ-ᛝᛏᛈᚹᛋᚣ-ᛏᛠᛈᛉ-ᚪᛁ/
ᛄᛋᚱᚪᛏᛋᛝᛏ-ᚳᚷᚳᚻ-ᛖᛟᚱᚪᛡᚻᚳ-ᛝᛒᛖᚱ/
ᛠᚪ-ᛚᛟᛖᛚᚪ-ᚦᛋ-ᚳᚹᚱᚹ-ᚩᚻᚣ-ᚢᛝᚩ-ᛈᛚᛁᛏᚪ/
-ᚠᛋᛝᛞ-ᚳᚪᚱᛒ-ᚹᛈ-ᚾᚩᚦᚳᚦᚾᛗᚩᛖ-ᚣᛇᚾ-ᚠᛒ./
3-ᛞᚢᛈ-ᚹᚾᛖᚪ-ᚱᛚᛁᚹ-ᚫᛉ-ᛝᚠᛞᚪᚠ-ᛒᛄᛉ-ᛞ/
ᛄᛝᚣᛇᚪ-ᚫᛄ-ᛝᛈᚪ-ᚢᛠ-ᛇᛏᚱ-ᛖ-ᚫᛗ-ᚫᛠ/
ᚻ-ᛁᚫᛟ-ᛠᚹᚳᛄᚦᚻ-ᛡᚩᚢ-ᚩᚦᚷᛡ-ᚻᛋᚷᚪᛁᛟᛞ/
ᚪᛄ-ᛁᚹᛡᛒ-ᛗᛝᛡᛞᚠᛒᛋᛏ-ᛒᚷᚠ-ᚷᛟᚢᚳᚫᛏᛁ/
ᛖ-ᚱᚷᛗᚣ-ᚪᚷᚹ./
4-ᛝᛄᛋᛄᛗᚱᛗ-ᚾᛒᛋᛗᛉᛞᚻᛉᛁ-ᚣᛡᚻᚣ/
ᛠᛉᚻ-ᛞᛖ-ᚹᛖᚦ-ᚢᚳ-ᛉᛗᚪᚣᛠ-ᚹᚫᚪᚳ-/''', UnsolvedTranslation()),

        ('''
ᚢᚫᚳᛇᚳᚣ-ᛡᚫᛏᛖᚳᚠ-ᛋᚻ-ᛋᚱᚢᚦ-ᛁᛋᛝᛗᛞ/
ᚫᚢᛠᚢᚪ.ᚾᛝᚳ-ᛖᛈᚹᛉ-ᚢᛉᚫ-ᚾᛈᚳᚻᚱᚣ/
ᚹᛚᛉᚱᛒ-ᛗᚫᛟᚣᚩ-ᚳᛇᛗ./
5-ᚻᚫᛉᚦᛒᛟ-ᛏᛟᚹᛄ-ᚫᛠᛗᚠᚫᚳᚷ-ᛇ-ᚻᚹᛗ/
ᚻᛝᚣ-ᛁᚩᛁ-ᛏᛁᛖᛡᛄ-ᛗᚣᛚ-ᚻᚱᚩᛞᛒᛡᛈᛠᛗ-/
ᚳᛠ-ᛖᛒᚢ-ᚷᛁᚦ-ᛟᚫ-ᛡᚻᛝᛖᚾ-ᚱᛠᛡᛋ-ᚻᛏ/
ᛝᚻᚪᚷᚩᛝᚫ-ᚹᛚᛏᚱ-ᚷᛁᚾ-ᛖᛠᛄᛡᛞᛋᚻ-ᛝᚾ/
ᚳᛋᚾᛞᛇᚾᛋᛁᚳᛡ-ᚱᛝᛚᚫᚣᛇᛚᚩ-ᚳᛞᚾ-ᛝᚷᛡ./
ᛝᛄ-ᚻᛄᛚᛠᛟ-ᛄᛏᚷ-ᛚᛒᛝᚢᛏ-ᚻᚳ./
&
ᚫᛞᛟᚫᛟᛗ-ᛟᚫᚪᚻᚱᛗᚢ-ᚣᚢᚣ-ᛈᛗ-ᚪᛄᚫᛟ/
ᛠᛚᚠᛖᛡᚢ-ᛉᚻ-ᚪᚩᛡᛒᛠᚢᚷ-ᚻᛏᛠᚪᛞ-/''', UnsolvedTranslation()),

        ('''
ᛋᚹ-ᚦ-ᚾᛋᛁᚻᛒ-ᛉᛠᛝ-ᛒᚢᛚᛟᚢᚾ-ᚢᚦᚩᛗᚪ-ᚾ/
ᛞᚫᛇ-ᚫᚣᚪᛋ-ᚣᛝᛡᛗᚷᛇᚾᛈ-ᛠᚳᚻᛝᛚ-ᚠᚷ/
ᛡ-ᛁᛡᚪᚠᛒᛈ-ᚳᛋᚦᛠᚦᚫᚱ-ᚷᛞᛚᛟ-ᚷᚱᛁᛇ-ᚣᚩ/
ᛟᚢᛝᚱᚷ-ᛗᛏᚷᛒᛈᚷ-ᛗᛏ-ᛗᚣᚹᛒᛏᛒ-ᚷᚣᛈ/
ᚷ.ᚾᚦᛇᛒᚳ-ᚷᛖᛇᛟᛚᛈ-ᚹᚾ-ᚻᚷᚱᛇᛏ-ᛈᚷᛒ-ᚹ/
ᛗᛋᚹᛟᚻ./
&
ᛡᚳᛋ.ᛈᛞᛋᛡ-ᚪᚹᛏᚳᚹᛟ-ᛗᚹᛁᛒᛞ-ᚷ/
ᛇᚢᛚ-ᛉᛋᚫ-ᛟᚻᛚᚦᛒ-ᚣᚪᛚᛞᚦᚠ-ᚻ-/
ᛞᛝᚩᚢᛋᚪᚫ-ᛖᚦᛁ-ᛏᛄᛏ-ᛝᚦᚾᚳᛉ/
ᛏᛝ-ᚳᛈᛁ-ᚾᛏ-ᛒᚾᛡᚱᛒ-ᚢᛈᛋᚦᛁᚳᛈᛋᛁᚹ-ᚹᛚᚣᚾ/
ᚢ-ᛒᛁᚪᛠ-ᚹᛟᚳ-ᛠᚢᚪ-ᛚᚦᚹ-ᚠᚾᛏᚳᛡᛁ-ᛚᚩ-ᚾ/
ᛗᛄᛠ-ᚦᛟᛄ-ᚪᚦᚹ-ᛡᚾᛖᛠᛈ-ᛒᛋᛄ./
&
$''', UnsolvedTranslation()),

        ('''
ᚠᚾᛗ-ᚣᚷᛞᚫᚻ.ᚪᛈᛉᚣᚻ-ᛇᛠᚩᛖ-ᛏᛝ/
ᛠ-ᛚᛁᛏᚦᚠ-ᛗᚪᚳᛖ.ᛞᚳ-ᛏᚱᛟᚷᛠᚾ/
ᚫᛒᚢᛖᛒᚢ-ᚦᚠᛟ-ᚷᛋᛟ-ᛁᛈ-ᛟᛉᛋᛒ-ᚹᛄᛒ/
ᚣᛗᚢᛠ-ᚱᛁᚢᛟᛄᛁ-ᛗᛖᚫ-ᚱᛋᛉᛝ.ᛠᛈᛚ-/
ᛞᚩᛚᛁᛉᛠᛝᛖᚱ-ᚾᛈᛖᚹᛡ-ᚾᛄᛏᚣ.ᛋᚩᛋ/
ᛏᛝ-ᚢᚾᛇᚪ-ᛖᛏᚪᛄᚳᚣ-ᛟᛒ-ᛚᛋ-ᛒᛞᛄ-ᛁᛝᚣᛖ/
ᚳ-ᛄᚻᛚᚣ-ᚷᚫᛚᛞ-ᛚᚫᛚᚦᛉ-ᛚ-ᛖᛉᚩᛉᛁᚳᚢᛗ/
ᚾᚢ-ᚩᚾᛇ-ᚻᛡᛚᛇᚩᚫᚪ-ᚩᛟᚩ-ᚣᚱ-ᛖᚠᚢ.ᛁᚻ-ᛟᛚ/
ᚾᛏ-ᚠᛞᚱᛠᚷ-ᛈᚩᛇᚩᛗᛠᛒ-ᛄᛡ-ᛋᛗᚠ-ᛏ/
ᚠᚫᚩ-ᛟᚳᛚᛞᛡᛚ-ᚩᚳᛝᚢ-ᛈᚹᛏ-ᚷᚳᛋ-ᚢᛟᚷᚦ-/
ᚠᛉᚠᛏ-ᚳᛋᛉᛟ-ᚷᚠᛉᚾᛞ-ᛒᛏᛠᛡ.ᛈᛡ/''', UnsolvedTranslation()),

        ('''
ᛠᛁᚪ-ᛋᚣᛗᛞᚣᛋ-ᛒᛞᛄᛞ.ᚩᚾᛏᛚ-ᚳᚪᛝ-ᚱᚷ/
ᚻᚷ-ᛄᚹᚠ-ᚪᚢᛇ-ᛞᛏᛗᛄᛁ-ᛝᚫ-ᛉᛈᚳᛈᛠ-ᛟᚪ/
ᛒᛁᛁᛋ-ᛇᚷᚻᛋ-ᛇᛡᛒ-ᚠᚹᛝ-ᚫᚪᚠᚩᚣᛡᚪᚾᚻ-ᛒᚦᛟ/
ᛇᚣᛟᛁᛒ-ᛟ-ᚩᛋᚹ-ᛞᚳᚠᚪᛁ.ᛉᛏᛟᚢᚩᛟᚦᛈᛋᚩ-/
ᚻᛇᚦᛝ-ᛏᛠᚠᛝᛠ-ᚩᛗ-ᛏᚠᚣᛚᚣ-ᚹᛚᛞ-ᚪᛉ/
ᛠ-ᚪᛄ-ᚩᛋᛒᛚ-ᚳᛖᚾᚪᚩᚱᛏᚦ-ᚱᛒᚳᚣ-ᛠᛗᚹᛚ-/
ᚻᛈ-ᛇᛈᛖ-ᛚᛄᚩᛡᚪ-ᛖᛋᚫᚩ-ᛠᛉᛝᚣ-ᛖᚫᛒ/
ᛗ-ᛖᚻᚱ-ᛈᚾᛗ-ᚹᛏᛟᚣᚢ-ᚠᛉᛈᛗᚩᚷᚾ-ᛡᛇᚳ/
ᚠᛒᛈᛗ-ᛋᛇᛁ-ᛖᛈᚢᚱᛏᚳᚣ-ᛄᛚᚠ.ᚱᛚᚱᚫᛖᚻᛟ/
-ᛇᚣᛡ-ᚩᛉ-ᚪᛋᚣᛁᛝ-ᛉᛚᛄᚳ-ᛖᚣᚢᛝᚦᛇᚱ-/
ᛠᛁᚫ-ᚦᚠᛟᚷᛠᛁ-ᛈᛋᛒ-ᛗᛒᛄᚠᚾᚳᛖ-ᚻᚫᚩᛄ-/
ᛉᛄᛚᛈᚪᛁ-ᛟᚹᚱᛁᚱᚦᛖᛉ-ᚪᚾ-ᛞᛄᚷ-ᛟᛟᚳᛏᛄ/''', UnsolvedTranslation()),

        ('''
ᛞ-ᛉᚾᛗᚦ-ᛁᛄᚱ-ᛈᛉᚢᚫᚦᛒᚠᛄᚦ-ᚠᚪᛝᛖ-ᚹᚹᚣ/
ᛚᛇ-ᚢᚣ-ᚾᚱᚪ-ᛈᚾᚹ-ᛚᚾᛏᛚᚢᛒᚱᛝᚪᛋ-ᚫᛈ-ᛄᛚ/
ᚢᚳᚷ-ᛚᛏᛄᚹᛈ-ᚫᛗᛚ-ᛉᛚᛗᛏᛞᚠᛈᛁ.ᚠᚳᚦ/
ᛗᛄᚹᚱᚪᛚ-ᚩᛝᚱᚢᛈᚱᛟᛡ-ᚳᛉᚱ-ᛇᛏᚦᚾ-ᚱᛇᚫ/
ᛞᛟᚻ-ᛒᚾᚣ-ᚠᛡᚪᛡᛖᚫᛞᛄᚢᛖ-ᚦᚱ-ᚩᛇᚱᛡ-/
ᚣᛁᛉᛇᚻᚩᛠ-ᚫᚻᛡᛝᛠᚦ-ᚾᚣ-ᚾᚠᛁᛝ.ᛏ/
ᚻᚹᚫ-ᛒᛇ-ᛡᚻᛉᛒ-ᛞᛝᚱᛄᚦᚻ-ᚪᚷᚣᛁᚠᚷ-ᛁᛏᛞ/
ᛠᛒᚠᚩᛈ-ᛇᛡᛟᚹᚱᚾᚩᛏ-ᛋᚹᚢ.ᛖᛡᛖᛡᚦ-ᛉ/
ᚪᚷᛈᚾ-ᛋᚱᚠᛞᛝᚻᛖᛄᛞ-ᛄᛡ-ᚱᚹ-ᚷᛝᚪᛒ-ᛄᛈ/
ᛄ-ᛏᚠᛉ-ᚪᛄ-ᛁᚠᛉᚢᚩᚣᚻᚦ-ᚻᚾᛁᛒ-ᛡᛟᛡᛋᛈᚣ/
ᛉ-ᛠᚢᛠᛚ-ᚠᛝᛗᚻ-ᚦᛒᚩ-ᛗᛚ-ᚩᛠᛋᚦᛠ-ᛇ/
ᛋᛉ-ᚠᛗᛒ-ᚫᛋᛇᚾᛡᚾ-ᚢᚫᚹ-ᛞᛠᚢᚾᛝᚠᚾᛖᚫ/''', UnsolvedTranslation()),

        ('''
ᚻᛄ-ᛁᛖᛏᛡ-ᚷᛁᚩᚾ-ᚳᚢᚫᛗᛈᛋᚪᛡ-ᚷᛚᚣᚹᛟ-/
ᚠᚢ-ᛉᚠᚫᛞᚠᛡᛄᚾ.ᚻᛋᚦᚠ-ᛏᚠᛄᚱᚹᚠᛋᚾᚹᛄ/
ᛖᛒᚢᚦ-ᚩᛇᚫᛈ-ᛡᛟ.ᚢᛁᚩᛄᚩᛇᛟᛄᛞᚩ-ᛈᚹᛞ/
ᚷᚱ-ᚠᛟ-ᛇᚷ-ᛄᛟᛇᚫᛋᚫᚣ-ᛒᛏᛞᛟ-ᛠᚻᛡᚱᛠ/
ᛠᛉᛋ-ᚠᚾᚣᚱᚠ.ᚪᚾᛡᚪᛖᚫ-ᚳᛇᛁᛝ-ᛒᛡᛞᛠ/
ᚫᛒᛠᚳᛉᚠ-ᚫᛏᛁᚱᚪᛗᚩ-ᛚᛉᛋᚪ-ᛒᚩᛈᚫᚩᛝᚻᛇ/
ᛖᛇᚫ-ᚻᛖᛇᛠ-ᚱᛗᛞ-ᚫᛇᛗ.ᚾᚾᚣᛡ-ᚱᚾᛗ/
ᛠ-ᛄᛉᛋᛄ-ᛟᛖᛒ-ᛏᚻᚾ-ᚠᚪᚠ-ᛒᚾ-ᚩᚾ-ᛖᛋᛏᛒᚹ/
ᛡ.ᚻᛏ-ᚩᛟᚩ-ᛒᚾᛖᚳᛁᚹᚣᛟ-ᛟᚩᛒ-ᛋᛖᚩ-ᚫᚻᛟ/
ᚠᚫᚷᚩᛄ-ᛟᛒᚻ-ᚳᛖᛁᛚᚫᚣᛚ-ᚢᛚᛁ-ᚾᛟᛏ-ᚫᛈᛟᛈ/
ᛝᛗ-ᚳᚢᛁ-ᚣᛋᚳᚢᛡᛇᚩ-ᚠᛖ-ᚷᛟ-ᚻᚫ-ᛝᚠ-ᛗᚠ/
ᛝᛉᛞᛁ-ᛗᛝᚣᚪᛝᚠᛉᛁᛟᚷᛚ-ᛇᚩ-ᚫᛡᛏ-ᛄᛏ/''', UnsolvedTranslation()),

        ('''
ᛠᚢ-ᚷᚦᚣ-ᚦᚾᛟᚣᚩᛖᚻ-ᛁᛋᛖᚣᚦᚪᛡᛝᛟᛇᛚ-/
ᛡᛏᛝ-ᛁᛚ-ᚠᛉᛡᛠᛏ-ᚠᚾᛄᚠᚻᚳ-ᚻᛞᛠᚣᛟ/
ᛝ-ᛉᛇᚻᚩᛋᚻ.ᛇᛏᚠ-ᛚᚱᛇᚦᚪᛁᛁ-ᛒᚠᛁᛚ-ᛄᛡᛒᚣ/
ᛗᚫᚫ-ᛞᚻᛟ-ᚪᚹᛉᛚᛏᛁᚪ-ᛟᛞᛖᚾᛈᚻᚣ-ᚦᛚᛖᛋ/
ᛖᛟᚫᛖ-ᛏᚱᚪ-ᛁᚫᚹᚫ-ᛋᛈᚱ-ᛄᛡᚪᛏ-ᚫᚦ-ᚠᛠᚢ/
ᛈᚣᚫᛝ-ᚣᚾᚻᛡ-ᚳᛗᚠᚾ-ᛞᛄ-ᛖᚩ-ᛒᚷᚻᚪ-ᛖᛞ/
ᛟᚠᛇᛞᛟ-ᛈᚳᛁᚪᛒᚷᛒᛈᛟ-ᛟᛄᚠᚪᛖ-ᛄᚣᚩᛄ-ᚣ/
-ᚫᛋ-ᚦᛁᚫᛄᚫᛏ-ᛖᛇᚻᛟ-ᚣᚠᚹᛞᚷ.ᛡᚱᛒᚢ-ᛒᛚ/
ᚢ-ᚷᛈᛄᚪ-ᛏᛡ-ᚳᛄᚠᛡᛝᛚᚣᛒ-ᛗᚻ-ᚱᛚᛟᛠᛋ/
ᚦᛝ-ᛏᚳᛟᛉᛁ-ᛄᚱᚳᛖᛏᛄᚷ-ᛡᛈᛏᛉᚩᛁᛄᛟ-ᚷ/
ᚩᚪᚢ-ᚣᛖᚪᛋᛟᛇᚢᚪᛡ-ᛗᚱᛚᚳᚠ-ᛒᛗᛝ-ᚻᛉ-/
ᛠᛄᚫ-ᛉᚪᚷᚻᚣᛏᛖᛝ-ᛉᛉᛗᚾᚫᛋ-ᚱᛗᛞᛋ/''', UnsolvedTranslation()),

        ('''
ᚳ-ᚦᛚᛟ-ᛝᛇᚢ-ᚻᚩ-ᛏ.ᚢᛁᚦᛄᚾᚠᚱᚦ-ᛋᛟᚷᛠ/
ᛗᚪ-ᛝᛚᚪᛁᛒᛠᚢᛋ-ᚩ-ᛖᛋᛝ-ᚠᛡᚢᛟᛞᛇᚪ-ᛞ/
ᛡᛒᚹᚩ-ᛄᛋ-ᛟᛝᛏᚳ-ᚻᚾᛇᛋ-ᛗᛚᚻᛞᛖᛈ-ᚫᛄᚱ/
ᚪᚢᚻᚱᚦᚱ-ᛟᛄ-ᛟᛗᚩᛟᛏ-ᚫᛇ-ᛉᛒᚳ-ᛄᛁ-ᚪᚩᛉ-/
ᚹᚪᚾᛈᛏᚢᚣ-ᛁᛒᚢ.ᚦᚩᛡ-ᛗᚳᚠᛉᚱᛁ-ᚪᛗᛏᛒ-/
ᛗᛚᛁᚦᛏᛠᛋᚾᚷᛚ-ᛏ-ᛇᛈ-ᚩᛚᛞ-ᛚᚹᚳᛄᚹᛉ-ᚪ/
ᛡᚹᛇ-ᛖᛖᚹ-ᛏᚪ-ᚣᚠᛉᚳ-ᛗᚩᚷᛞᚷ-ᛚᚳ-ᛒᚣᛋ/
ᚣᚠᛞᚣᛝ-ᛠᛇᛏᚩᚢᚫ-ᛟᛁᛒ-ᛏᚾᚫᚠ.ᛄᛟᛗᚾ/
ᛈ-ᛠᛡᚩᛏᛡᚪᚱᛞ-ᚪᛝᛈᚹᛗᛄᛟᛠᚩ-ᛚᚹᛉ-/
ᚱᛗ-ᚩᛏᚹᛄᚹᚾ-ᚷᚳᛠ-ᛄᚳᚢᚱ-ᛟᛇᛟᚾᚻᚫᛉ-/
ᚣᛚᚩ-ᚩᛡᚳᚻᛄ-ᛋᚣᚹᛁ-ᚣᚠᛋᚾᚪ-ᚷᛖᚾᛄᚪᚹᛠ-/
ᛞᚠᛟ-ᚢᛁ-ᛖᛇᚦ-ᚫᛞ-ᚳᛄ-ᚷᚢᚻᚣᚻᛁᛒᛉᚾ-ᚹᛝ/''', UnsolvedTranslation()),

        ('''
ᚻᛏᛉᚫᛁᛄᚢ-ᛞᚠᛡᚫ-ᛋᛁᚹᛝᛈ-ᛗᛉᛄᛈ-ᛞᛗ/
ᛝ-ᛇᛚᛞᚣ-ᚠᚩᛞ-ᛝᚷᚾᛇ-ᚷᛖ-ᛚᛉᚣ-ᚫᛚᛖᛉ./
ᛡᛝᛋ-ᚳᛁᚦ-ᚷᛏᚣ-ᚹᚩ-ᛝᛖ-ᛒᚪᛗᛏᚪᚷᛒ.ᛈᛡ/
ᛟ-ᚪᛉᛝᛒᛞᛉᛄᚦᚢ-ᛏᛇᛖ-ᚣᚪᚳ-ᛠᚦᚹ-ᛏᛉ/
ᚩᚳᛞᛒ-ᛟᚩᛠᚾᚠᚪ.ᛚᛗᛖᛁᚦᚫᚪᛡᛄᛁᚪᚱ-ᚦᚱᛖ/
ᛖᚣᛋᚾ-ᛖᛏᚢᚻᛈᚳᚦᛋ-ᚳᛇᛉᛖᛇᚠ-ᛞᛠᛏ/
ᛈ-ᚣᛇᛠᚢᛏ-ᛉᚦᚷᚻ-ᚫᚾᛠᚱ-ᛡᛒᛏᛁᛉ-ᚩᚢ/
ᛝ-ᛚᛒᛇᚩ-ᛟᛉ-ᚦᛞᚷᚠ-ᚩᚱᛈᚪᛏ-ᚫᛋᚪᚦ-ᛖᛟᚪᛝ/
ᚫ-ᚣᛒᛚ-ᛡᚦᚾᚠᛈᛟᛡᚾ-ᛖᚹ-ᛖᛗᚩ-ᛉᚹᚦᛠ-ᛁᚦ/
ᛒᛖᚱ-ᛟᚳᛉ-ᛈᛖ-ᛁᚢᚦ-ᛈᚠᛞᛈᛄ-ᛁᛟᚻ-ᛒᚦᛏᚩ/
ᚳᚢᛚ-ᛞᛄᛝ-ᚦᛄᛁᚪ-ᚹᚣ-ᚢᛝᚾ-ᛋᚾᛈᚠᚫᛒᛄᚫ-ᛡ/
ᛗᚹ-ᛇᚪᚩᚾᛄᚳᛚᛒᛉ-ᚣᛠᚦᚹ-ᛝᛚᛗᚳᛡᛇᚠᚫ/''', UnsolvedTranslation()),

        ('''
ᛠᛁᚦ-ᛒᛠᛚᚦᚳᛞᛁᛇ-ᚠᚢᛉᛋᛉᛁᚦᚫᛋᛗ-ᚦᚹ./
ᛈ-ᛒᛋᛏᚫᚾᚱᛁ-ᚦᛇᛡᚱᛚᛡᚹ-ᚢᚩᛋᚱ-ᚹᚫ-ᛒᚹᛡᛖ/
ᛟᛄ-ᛡᚣᛖᚩᛖᛡᚷᚫᚠᚾᚹ-ᛟᛏᚫᚠᛄᚹᛠ.ᚦᛞ-ᛁ/
ᚫᚩᚾ-ᛋᚷᛈᚪᛖᚩ-ᚣᚦᚹ-ᚾᚷ.ᛠᛋᚩᛇᛏ-ᛝᛚᚷᛞ/
-ᛒᛈᛈ-ᛗᛁᚪᛖ-ᛚᛏᛁ-ᚫᛄᛖ-ᛒᚾᚠᚪᛋᚷᛒᚠ-ᚫᚹᚣᚷ/
ᚢᛡᚠᛠ-ᛖᛋᛞ-ᛚᚳᛒᛞᛏᛈ-ᛖᚾᛈᚣ-ᚱᚠᚻ-ᚫ/
ᛝ-ᛟᚪᛗ-ᛒ-ᛡᛚ-ᛝᛋᚱᚢᚹᚱᚣᚻᚹ-ᚹᛡᛈ-ᛁᚻᚾᚻᚱ/
-ᚳᛖᛏᚫᚩᛋ-ᚣᛋ.ᛝᚫᛡᛝᚫ-ᚻᚦ-ᛇᚪᛞᛋ-ᛒᛁᚳᛈ/
-ᛇᛒᛟᚫ-ᛠᛝᛖ-ᛝᛠᚣ-ᛒᚣᛉᚻᚢᚠᚦᛞᚹ-ᛗ/
ᚢᛁᛡᛄᚩ-ᛋᛇᚫᛇᛝᚱ-ᛚᛇᛠ-ᛏᚩᛄ-ᚩᛝᛈ-ᚱᚻ/
ᛠᚢᛉᚦ-ᚣᚢᛋ-ᛡᛚᛖᚷᛗᛝᚹᚻᚱᛋ-ᚢᛟᚣᛠ/
ᚷᚩᚷ-ᛇᛁᛖ-ᛠᛄᛇᛁᚾᛄᚩᛗᚱᛡᛉ-ᚠᚻᚳ-ᚪᚩᚪᚫ/''', UnsolvedTranslation()),

        ('''
ᚻᚳᛁᚦ-ᛄᚷ.ᛝᛖᚢ-ᛡᛏᛁ-ᛚᚩᚱᛈ.ᚠᚪ-ᛈᛞᚱᛒ-/
ᛝᛁᛋ-ᚷ-ᚠᚾᛈᚠᛒ-ᛟᚦᛁᛠᚪ-ᛡᛏᚾᚳ.ᚦᛟᚻᛈᛖᛚ/
ᚫ-ᛟᚠᛗ-ᛡᛝ.ᛒᛝᚦᛝᛠᚠ-ᛇᛗᛟ-ᚩᛠᛈ-ᛁᛡᚱ/
-ᚹᚹᛟᚩᛒᚩ-ᚾᚩᛄᛟᚾ-ᚦᛡᚠ-ᚩᛄᛞᚦᛏᛁ-ᛈᚾᚪᚱᛄ-/
ᛉᚱᚣ-ᛝᛡ-ᛏᛗ-ᛈᛞᚣᚻ-ᛗᛝᚫᚳᛇ.ᛡᚣᛄᛟ/
-ᛝᚩᚢᛇᛁᚱ-ᛏᚪ-ᚩᚻᚪᛚᚫᛚᚪ-ᛋᛈ-ᛏᚪᛄᚳᚦᚢᛏᚹ/
ᚦ-ᛗᚷᛖᛗᚣᛡᛁᛞ-ᚢᛋᚠᛒ-ᛟᛚᛟ-ᚪᛒ-ᚦᛚᚣ-ᚳ/
ᛠᚣ-ᛞᛇᛁ.ᚹᛉ-ᛟᛝᛒᚢᛋᛞᚻᛞ-ᚢ-ᛠᚱ-ᚫᚩ/
ᚻᛝᛒᚪᚹ-ᛈᛡᚾᛚᛇ-ᛖᛟᛝ-ᛡᚠᛇᛡ-ᚳᚦᚹ.ᛚᚦᚪᛁ/
ᛈ-ᛞᛟᛄ-ᚢᛉᚢᚾᛠᚠ-ᚩᚾᚪ-ᚱᛠᚷ-ᛗᚢ-ᛗᛁᛄ/
ᛒᛗᚱᚾᛗ-ᚩᚾᚠᚣ-ᛗᚠᛇᚠᛄ-ᛒᛡᛈᛄᛖᛡᛏ-ᛈᛟ/
ᚫᛏᛟ-ᚻᛖᚾ-ᚳᛇᚩ-ᛋᚻᚫᛇ-ᛝᛁᛟ-ᛇᚠᚢᛞᚣᚪᛚᚠ/''', UnsolvedTranslation()),

        ('''
ᛡ-ᛖᛄ-ᚠᛚᛟ-ᛁᚳ-ᛁᛝᚷᚦ-ᛗᛋᚫᚷᚪᛠ-ᛗᛁ-ᛒᛡᛏ/
ᚾ-ᛝᛗᚦ-ᛏᚣᚫᛄ-ᛖᚻᚠᚪᛡᚷ-ᚪᛗᛁ-ᛞᛉᛏ-ᚢᛖ/
ᚦᚾ-ᛖᚪᛈᚹᛠᛚ-ᛒᚢᚱᛡᛟ-ᚪᚣ-ᛟᛇᚹᛄᛈᛞ./
&
3N  3p  2l  36  1b  3v  26  33/
1W  49  2a  3g  47  04  33  3W/
21  3M  0F  0X  1g  2H  0x  1R/
1n  3I  2r  0P  2U  16  2L  2D/
1t  1s  3H  0d  0s  1K  2D  05/
1K  1O  0S  1D  3o  1L  3J  1G/
4D  0G  0L  0x  1Q  2p  2a  1K/
4E  1w  2Q  19  1k  3G  24  0p/
22  4F  0P  3C  3J  1D  2n  1m/
2i  1J  3P  2v  1s  2O  0k  1M/''', UnsolvedTranslation()),

        ('''
2M  0w  3L  3D  2r  0S  1p  15/
3V  3e  3I  0n  3u  1O  0u  0Z/
3g  2U  1C  0Y  1N  3n  0W  3Q/
22  13  0V  3c  0E  34  0W  1t/
1D  2N  3H  47  0s  2p  0Z  34/
0g  3v  1Q  0s  0D  0K  2h  3D/
3L  2x  1Q  20  2n  2L  1C  2p/
0A  29  3r  0D  45  0k  2e  2W/
25  3U  1W  2r  46  2s  2X  39/
3p  0X  0E  1q  0q  4B  49  48/
3r  3b  3C  1M  1j  0l  4A  48/
40  3m  4E  0s  2s  1v  3T  0I/
3t  2B  2k  2t  2O  0e  2l  1L/''', UnsolvedTranslation()),

        ('''
28  2a  0J  1L  0c  3C  2o  0X/
00  2Z  2d  1T  2u  1t  1j  0l/
1o  1E  3T  18  3E  1G  27  0L/
0v  2t  06  11  1A  2U  4B  1O/
2M  3d  2S  0x  0w  0q  0p  2V/
18  0q  1D  49  2O  00  1v  2t/
1k  3s  3G  21  3w  0W  29  2r/
2O  2L  0g  3Y  0M  0u  3i  3C/
1r  2c  2q  3o  30  0a  39  1K/
&
ᚹᚹᛈ-ᚠᛡᛚᛉᛒᚾ-ᚳᛗᚾᚱᛗ-ᚻᚦᚫᛞᛄ-ᛒᛡᚫ-ᛇᚹ/
ᛗᚢ-ᚪᛈᛡ-ᛈᛁᛄ-ᚪᚢᚾᛠᛖᛞᛗᚪ-ᛏᛟᛗ-ᛋᛞ/
ᛝᚷᛚᛋᛞᛝ-ᛟ-ᛋᛄᛞ-ᛚᛟᚠᛄᚫᚠᚪ-ᛝᛟᚣᛈ-ᚣᚩ/
ᛒᚷᚳᛖᛏᚹ-ᚪᛋᛒ-ᛗᛠᚣᛇᛗᚫᛚᚱ-ᚹᛇᛄᛒ-ᛈᛚᚠ/''', UnsolvedTranslation()),

        ('''
ᛈ-ᚠᛗ-ᛝᚪᛇᚾᛟᚹᛇᛉ-ᚣᚫᛉᛞᛟᚱᛒ-ᛡᚱᛟ-ᚹᛏ/
ᚷᚱᛄᛖ-ᛠ-ᛈᛚᛞ-ᚻᚦᚱ-ᚦᚣᛚᛉ-ᛠᛈᚫᚠᚪ-ᚫᚪ/
ᛒ-ᛈᛋ-ᛗ-ᛏᚫᚳᛈᛝᚹᚦ-ᚻᛠ-ᛞᚩᛄᚷ-ᛋᚩᛠᚳ/
ᛖᛋ-ᚣᛖᚫ-ᛈᚦ-ᛁᛇᛈᚳᛝ.ᛈᚳᛇᚢᛏᚳᛡᛇᛝᚾ/
ᚢᚻᚦ-ᚣᚠᛗᚾ-ᛝᚠᛄᛉᛟᚱᛗ-ᛝᛠᛄᛏᚳ-ᚢᚷ/
ᚦ-ᚠᚦᛋ-ᚪᛈᚩᚪᚫᛞᛋᛝ-ᛒᛗᚩᚷ-ᚹᚠᛗᛖ-ᛠᛇᚻᚠ/
ᚻᚳᚱᚫ-ᛝᛗᛉᚳ-ᛋᚪᚹᛋᛠ-ᚩᚣᛚᛉᛝ-ᛠᛟᛉ/
ᛟᛠᛡᛝᛒ-ᛝᚳᚫᛁᚱ.ᛒᚠ-ᛏᚣᚣ-ᛠᛒ-ᚣᛚᚩ-ᛇ/
ᛉ-ᚩᚷᛗᚩ-ᚠᛚᛟᛝᚦᛠ-ᚦᚣᛖᚣ-ᚾᚷᚾ.ᛡᛏ-ᛄ/
ᛟᚾᛁ-ᛋᛟ-ᛠᚦᚣ-ᛋᛒ-ᚫᛚᚪᛄᛡᛖᚷᛉᛡᚾᛉᛏ-/
ᛡᛒᚻᛚᚷ-ᚢᚦᛠ-ᚢᚾᛁᚩᛗᛠᛁᚷ-ᛟᚦᚱᚣ-ᛒᛖ/
ᛠᚩᛈ-ᛗᛏᚱᚫᚢᚻᛁᛝ-ᛇᚳᚠ-ᛄᚾᚱᚷ-ᛟᚷᚻᚣᚻ/''', UnsolvedTranslation()),

        ('''
ᛇᚫᛠᚫᚣ-ᚢᛗᛈ-ᛉᛁᚢᚾᚩᛟᚾ-ᚷᛞᚦ-ᛡᚫᚹ-ᛞ/
ᛟᛖᚱ-ᛗᚾᛖᚻᚷᛒᚢᛄ-ᚢᚦᛗᛖᛞᛝ-ᛒᚷᚣᚱ-ᛖ/
ᛁᚢᛄ-ᚣᛡᛚᚢ-ᛄᛟ.ᛠᛉᚣᛇᚱ-ᚩᛈᛋᚳᚫᛗ/
ᛇ-ᚾᛄ-ᛖᚠᛋ-ᛖᚠᚪᛝ-ᚢᛝᛄᛇᚷᚠᛝᚱᛁᚦ-ᛄᚢᚫ-/
ᚣᛋᚠᛖᚢᛋᚫᚣᛠ-ᛁᛏᛟᚱᛏᛟᚩ-ᚷᚾᚻ-ᛞᛗᚩᚳ/
ᛞᛖᛏ-ᚹᛉᛞᛚ-ᚩᚫᛄ-ᛇᚢᛒ-ᛗᛏ-ᛞᛗᛖ.ᛏ/
ᛈᚹᛇᛋ-ᚹᛒᛇᚦ-ᚾᚻᚷᛄ-ᚱᛡᛞᛡᚦᚪᛁᛇᚫᛉᛚ-ᛇ/
ᛠ-ᛡᚪᛄ-ᚻᚱ-ᚦᛈᛞᛄᛝᚩ-ᚷᚠᛇᛗᚳ-ᚻᛞᚩᛏᚳ/
-ᚢᚱ-ᛈᚾ./
&''', UnsolvedTranslation()),

        ('''
ᚪ-ᛗᛝᛞᛡᚦᛉᛁᛗ.ᛡᛞᛈᛝᚢᚹᚪᛗ-ᛏᚪ/
ᛝ-ᛝᚦᛡᚹᛋᚻ-ᛁᚳ-ᚫᛈᚫᚷᚩ-ᛗᛁᚪ-ᛖᚩ-ᛏᚹ/
ᚩ-ᚠᚣᚢᛏᛄ-ᚦᛄᛠᛖᚳᚾᛠ-ᚳᛠᛖ-ᚱ/
ᚩᚢᛉ-ᛞᚹᚻᛒᛝᚠᚪᚳᛄᚢ-ᚩᛄᛡᛠᛁᛚᚷᚻ-ᛒᚢ/
ᛄ-ᛉᚪᚳᚹᛡ-ᛗᚩᛈᚣᛞᛡᛚᛈ-ᛇᛁᚦᚱ-ᚣᚷᛗ-ᛉ/
ᛟᚷᛋ-ᛗᛈᛄᛟᛞ-ᛟᛏᛡᛟ-ᛏᛝᛁ-ᛗᛝᚣᚪᚫ-ᛝ-ᚱ/
ᚣᛄ-ᚾᛚᚢᛉᛒ-ᚻᛈᛄᚩᛠ-ᚷᚫᚹ-ᛉᛋᛞᚳ-ᚢᛏ-/
ᛟᚻᛇᚾᛈᛏ-ᛠᚣᛒᚢᚷ-ᚷᚪᛇ-ᚾᚷᚩᛖᛚᛗᛒᚦ-ᚣ/
ᛡᛟᛇᚣ-ᛗᚳᛟᚦ-ᛖᛚᚱᛇᛈᚱᛞᚣ-ᛉᛞ-ᛝᚣᛈ-/
ᛋᛖᛉᚹ-ᚳᚷᚠᛞᚱᛖ-ᛞᛖᚹᚩᛇᛟ-ᚻᚩᛟ-ᛒᛋ-ᚻ/
ᛠᚪᚳᛁᛗᛉᛄᛗᛖ-ᛗᛚ-ᚷᚩᛏᚦᛉᛖᛠᚱᚷᚣ/''', UnsolvedTranslation()),

        ('''
ᛝ-ᚫᛗᛁᚹ-ᛋᛒ-ᛉᛗ-ᛋᛇᚷᛞᚦᚫ-ᚠᛡᚪᛒᚳᚢ-ᚹᚱ-ᛒ/
ᛠᚠᛉᛁᛗᚢᚳᛈᚻᛝᛚᛇ-ᛗᛋᛞᛡᛈᚠ-ᛒᚻᛇᚳ-/
ᛇᛖ-ᛠᛖᛁᚷᛉᚷᛋ-ᛖᛋᛇᚦᚦᛖᛋ-ᚦᛟ-ᚳᛠᛁᛗ/
ᚳᛉ-ᛞᛄᚢ-ᛒᛖᛁ''', UnsolvedTranslation()),

        ('''
ᚫᛄ-ᛟᛋᚱ.ᛗᚣᛚᚩᚻ-ᚩᚫ-ᚳᚦᚷᚹ-ᚹᛚᚫ.ᛉ/
ᚩᚪᛈ-ᛗᛞᛞᚢᚷᚹ-ᛚ-ᛞᚾᚣᛄ-ᚳᚠᛡ-ᚫᛏ/
ᛈᛇᚪᚦ-ᚳᚫ./
&
36367763ab73783c7af284446c/
59466b4cd653239a311cb7116/
d4618dee09a8425893dc7500b/
464fdaf1672d7bef5e891c6e227/
4568926a49fb4f45132c2a8b4/
&
ᚳᛞ-ᚠᚾ-ᛡᛖ-ᚠᚾᚳᛝ-ᚱᚠ-ᚫᛁᚱᛞᛖ-ᛋᚣᛄᛠᚢ/
ᛝᚹ-ᛉᚩ-ᛗᛠᚹᚠ-ᚱᚷᛡ-ᛝᚱᛒ-ᚫᚾᚢᛋ./''', SimpleTranslation(prime_substruction=True, skip_indices={ 221 })),

        ('''
ᛈᚪᚱᚪᛒᛚᛖ.ᛚᛁᚳᛖ-ᚦᛖ-ᛁᚾᛋᛏᚪᚱ-ᛏ/
ᚢᚾᚾᛖᛚᛝ-ᛏᚩ-ᚦᛖ-ᛋᚢᚱᚠᚪᚳᛖ./
ᚹᛖ-ᛗᚢᛋᛏ-ᛋᚻᛖᛞ-ᚩᚢᚱ-ᚩᚹᚾ-ᚳ/
ᛁᚱᚳᚢᛗᚠᛖᚱᛖᚾᚳᛖᛋ.ᚠᛁᚾᛞ-ᚦ/
ᛖ-ᛞᛁᚢᛁᚾᛁᛏᚣ-ᚹᛁᚦᛁᚾ-ᚪᚾᛞ-ᛖᛗᛖᚱᚷᛖ./''', SimpleTranslation()),

    ]
    
    @staticmethod
    def get_unsolved_pages():
        """
            Gets all the unsolved pages.
        """
    
        # Unsolved pages have unsolved translations
        return [ page[0] for page in LiberPrimusPages.PAGES if isinstance(page[1], UnsolvedTranslation) ]
