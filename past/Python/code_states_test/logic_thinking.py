'''
알파벳 기준으로 키가 3글자씩 앞으로 밀어낸 값이라고 할 때, 다음의 암호화된 메세지의 원본을 대문자로 작성해 주세요.

FRGHVWDWHV

'''

string = "FRGHVWDWHV"

new_str = ""
for i in string:
    new_str += chr(ord(i)-3)

print(new_str)