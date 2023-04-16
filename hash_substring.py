# python3

def read_input():
    try:
        # Read input from keyboard or file
        input_type = input().rstrip().upper()
        if input_type == 'I':
            pattern = input().rstrip()
            text = input().rstrip()
        elif input_type == 'F':
            with open('tests/06', 'r') as file:
                pattern = file.readline().rstrip()
                text = file.readline().rstrip()
        else:
            raise ValueError('Wrong input, must be I or F')
    except ValueError:
        print('Wrong input, must be I or F')
        raise
    
    return pattern, text

def print_occurrences(output):
    print(' '.join(map(str, output)))

def get_occurrences(pattern, text):
    # Rabin-Karp algorithm for pattern matching
    p_len = len(pattern)
    pattern_hash = hash(pattern)
    text_len = len(text)
    text_hash = hash(text[:p_len])
    output = []
    
    for i in range(text_len - p_len + 1):
        if text_hash == pattern_hash and text[i:i+p_len] == pattern:
            output.append(i)
        if i + p_len < text_len:
            text_hash = hash(text[i+1:i+p_len+1])
    
    return output

if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))
