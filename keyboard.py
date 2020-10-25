import os
import string
import sys
import AdvancedInput as AI

_VOWELS_     = {'a', 'i', 'u', 'e', 'o'}
_CONSONANTS_ = set(string.ascii_lowercase) - _VOWELS_

_HIRAGANA_ = { 'a': 'あ',   'i': 'い',   'u': 'う',  'e': 'え',  'o': 'お',
              'ka': 'か',  'ki': 'き',  'ku': 'く', 'ke': 'け', 'ko': 'こ',
              'sa': 'さ', 'shi': 'し',  'su': 'す', 'se': 'せ', 'so': 'そ',
              'ta': 'た', 'chi': 'ち', 'tsu': 'つ', 'te': 'て', 'to': 'と',
              'na': 'な',  'ni': 'に',  'nu': 'ぬ', 'ne': 'ね', 'no': 'の',
              'ha': 'は',  'hi': 'ひ',  'fu': 'ふ', 'he': 'へ', 'ho': 'ほ',
              'ma': 'ま',  'mi': 'み',  'mu': 'む', 'me': 'め', 'mo': 'も',
              'ra': 'ら',  'ri': 'り',  'ru': 'る', 're': 'れ', 'ro': 'ろ',
              'ya': 'や',               'yu': 'ゆ',             'yo': 'よ',
              'wa': 'わ',  'wi': 'ゐ',              'we': 'ゑ', 'wo': 'を',
              'ga': 'が',  'gi': 'ぎ',  'gu': 'ぐ', 'ge': 'げ', 'go': 'ご',
              'za': 'ざ',  'ji': 'じ',  'zu': 'ず', 'ze': 'ぜ', 'zo': 'ぞ',
              'da': 'だ', 'dji': 'ぢ', 'dzu': 'づ', 'de': 'で', 'do': 'ど',
              'ba': 'ば',  'bi': 'び',  'bu': 'ぶ', 'be': 'べ', 'bo': 'ぼ',
              'pa': 'ぱ',  'pi': 'ぴ',  'pu': 'ぷ', 'pe': 'ぺ', 'po': 'ぽ',
              'kya': 'きゃ',         'kyu': 'きゅ',          'kyo': 'きょ',
              'sha': 'しゃ',         'shu': 'しゅ',          'sho': 'しょ',
              'cha': 'ちゃ',         'chu': 'ちゅ',          'cho': 'ちょ',
              'nya': 'にゃ',         'nyu': 'にゅ',          'nyo': 'にょ',
              'hya': 'ひゃ',         'hyu': 'ひゅ',          'hyo': 'ひょ',
              'mya': 'みゃ',         'myu': 'みゅ',          'myo': 'みょ',
              'rya': 'りゃ',         'ryu': 'りゅ',          'ryo': 'りょ',
              'gya': 'ぎゃ',         'gyu': 'ぎゅ',          'gyo': 'ぎょ',
               'ja': 'じゃ',          'ju': 'じゅ',           'jo': 'じょ',
              'bya': 'びゃ',         'byu': 'びゅ',          'byo': 'びょ',
              'pya': 'ぴゃ',         'pyu': 'ぴゅ',          'pyo': 'ぴょ',
              'n': 'ん',   'v': 'ゔ', 'double': 'っ'}

_KATAKANA_ = { 'a': 'ア',   'i': 'イ',   'u': 'ウ',  'e': 'エ',  'o': 'オ',
              'ka': 'カ',  'ki': 'キ',  'ku': 'ク', 'ke': 'ケ', 'ko': 'コ',
              'sa': 'サ', 'shi': 'シ',  'su': 'ス', 'se': 'セ', 'so': 'ソ',
              'ta': 'タ', 'chi': 'チ', 'tsu': 'ツ', 'te': 'テ', 'to': 'ト',
              'na': 'ナ',  'ni': 'ニ',  'nu': 'ヌ', 'ne': 'ネ', 'no': 'ノ',
              'ha': 'ハ',  'hi': 'ヒ',  'fu': 'フ', 'he': 'ヘ', 'ho': 'ホ',
              'ma': 'マ',  'mi': 'ミ',  'mu': 'ム', 'me': 'メ', 'mo': 'モ',
              'ra': 'ラ',  'ri': 'リ',  'ru': 'ル', 're': 'レ', 'ro': 'ロ',
              'ya': 'ヤ',               'yu': 'ユ',             'yo': 'ヨ',
              'wa': 'ワ',  'wi': 'ヰ',              'we': 'ヱ', 'wo': 'ヲ',
              'ga': 'ガ',  'gi': 'ギ',  'gu': 'グ', 'ge': 'ゲ', 'go': 'ゴ',
              'za': 'ザ',  'ji': 'ジ',  'zu': 'ズ', 'ze': 'ゼ', 'zo': 'ゾ',
              'da': 'ダ', 'dji': 'ヂ', 'dzu': 'ヅ', 'de': 'デ', 'do': 'ド',
              'ba': 'バ',  'bi': 'ビ',  'bu': 'ブ', 'be': 'ベ', 'bo': 'ボ',
              'pa': 'パ',  'pi': 'ピ',  'pu': 'プ', 'pe': 'ペ', 'po': 'ポ',
              'kya': 'キャ',         'kyu': 'キュ',          'kyo': 'キョ',
              'sha': 'シャ',         'shu': 'シュ',          'sho': 'ショ',
              'cha': 'チャ',         'chu': 'チュ',          'cho': 'チョ',
              'nya': 'ニャ',         'nyu': 'ニュ',          'nyo': 'ニョ',
              'hya': 'ヒャ',         'hyu': 'ヒュ',          'hyo': 'ヒョ',
              'mya': 'ミャ',         'myu': 'ミュ',          'myo': 'ミョ',
              'rya': 'リャ',         'ryu': 'リュ',          'ryo': 'リョ',
              'gya': 'ギャ',         'gyu': 'ギュ',          'gyo': 'ギョ',
               'ja': 'ジャ',          'ju': 'ジュ',           'jo': 'ジョ',
              'bya': 'ビャ',         'byu': 'ビュ',          'byo': 'ビョ',
              'pya': 'ピャ',         'pyu': 'ピュ',          'pyo': 'ピョ',
              'n': 'ン',   'v': 'ヴ', 'double': 'ッ'}

_PUNCTUATION_ = {'-': 'ー', '.': '。', ',': '、',}
_HIRAGANA_.update(_PUNCTUATION_)
_KATAKANA_.update(_PUNCTUATION_)

active = "H"
kana   = _HIRAGANA_


def change_kana(buffer = None, **kwargs):
    global kana
    global active
    if   active == 'H': active = 'K' # Hiragana -> Katakana
    elif active == 'K': active = 'R' # Katakana -> Romaji
    elif active == 'R': active = 'H' # Romaji   -> Hiragana
    kana     = _HIRAGANA_ if active == 'H' else _KATAKANA_
    cursor = active + " > "
    return {'cursor': cursor}


def check_kana(buffer = None, key=None, **kwargs):
    global kana
    buffer = buffer + key
    if active == 'R':
        return {'buffer': buffer}
    # Table Lookup Function
    def look_up_char(buffer, i):
        if len(buffer) >= i:
            lookup = kana.get(buffer[-i:])
            if lookup:
                buffer = buffer[:-i] + lookup
        return buffer
    # Arrow key handling
    if buffer[-3:] in ['\x1b[A', '\x1b[B', '\x1b[C', '\x1b[D',
                                           '\x1b[H', '\x1b[F']:
        key    = buffer[-3:]
        buffer = buffer.replace(key, '')
        return {'buffer': buffer}
    # Conversion logic
    if not isinstance(buffer, str) or len(buffer) == 0:
        return {'buffer': buffer}
    if buffer[-1].lower() in ['a', 'i', 'u', 'e', 'o', '.', ',', '-']:
        if len(buffer) >= 3:
            # Check if a small 'tsu' is required
            if (buffer[-3].lower() == buffer[-2].lower()
                and buffer[-2].lower() in string.ascii_lowercase):
                double = kana.get('double')
                buffer = buffer[:-3]+double+buffer[-2:]
        # Convert rest
        buffer = look_up_char(buffer, 3)
        buffer = look_up_char(buffer, 2)
        buffer = look_up_char(buffer, 1)
    # Check if a N is in front of consonant
    if len(buffer) > 2:
        if buffer[-2].lower() == 'n':
            buffer = buffer[:-2] + kana.get('n') + buffer[-1]
    return {'buffer': buffer}


if __name__ == '__main__':
    import argparse
    argParser = argparse.ArgumentParser(description='Extract information from the MISP API')
    argParser.add_argument('-c', '--clip',   action="store_true", help='Copy to clipboard')
    argParser.add_argument('-s', '--silent', action="store_true", help="Don't print output")
    args = argParser.parse_args()

    if sys.stdin.isatty(): # Text piped from STDIN
        os.system('setterm -cursor off')
        interface  = AI.AdvancedInput()
        hooks      = {x: check_kana for x in string.ascii_letters+',.-'}
        hooks['\t'] = change_kana
        result = interface.input(cursor = "H > ", hooks=hooks)
        sys.stdout.write('\x1b[1A'+ '\r' + '\033[K' + '\r')
        if not args.silent:
            sys.stdout.write(result + '\n')
        sys.stdout.flush()
        os.system('setterm -cursor on')
    else:
        pass

    if args.clip:
        from subprocess import Popen, PIPE
        p = Popen(['xsel','-ib'], stdin=PIPE)
        p.communicate(input=result.encode())
