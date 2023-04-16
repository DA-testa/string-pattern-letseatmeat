# python3

def read_input():
    try:
        input_type = input().rstrip().upper()
        if input_type == 'I':
            pattern = input().rstrip() 
            text = input().rstrip() 
        elif input_type == 'F': 
            filename = input().rstrip()
            with open(f"tests/{filename}", 'r') as file: 
                pattern = file.readline().rstrip()
                text = file.readline().rstrip()
        else:
            raise ValueError("Wrong input, must be I or F.")
    except ValueError:
        print("Wrong input, must be I or F.")
        pattern, text = '', ''
    return pattern, text


def print_occurrences(output):
    print(' '.join(map(str, output)))


def get_occurrences(pattern, text):
    pattern_length = len(pattern)
    pattern_hash = hash(pattern) if pattern else 0
    text_length = len(text)
    text_hash = hash(text[:pattern_length]) if text else 0
    occurrences = []
    for i in range(text_length - pattern_length + 1):
        if pattern_hash == text_hash and text[i:i+pattern_length] == pattern:
            occurrences.append(i)
        if i + pattern_length < text_length:
            text_hash = hash(text[i+1:i+pattern_length+1])
    return occurrences

if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))

