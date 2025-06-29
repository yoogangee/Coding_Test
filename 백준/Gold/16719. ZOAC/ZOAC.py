# 백준 16719 ZOAC

word = input()
ans = ['']*len(word)

def sol(part_word, start_index):
    if part_word == "":
        return
    
    min_char = min(part_word)
    min_char_index = part_word.index(min_char)

    ans[start_index + min_char_index] = min_char

    print(''.join(ans))

    sol(part_word[min_char_index+1:], start_index+min_char_index+1)
    sol(part_word[:min_char_index], start_index)


sol(word, 0)