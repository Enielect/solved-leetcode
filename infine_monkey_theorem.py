import random

reference_str = 'methinks it is like a weasel'
def generate () :
    final_string = ''
    characters = [chr(i) for i in range(97, 123)]
    characters.append(' ')
    for k in range(27) :
        final_string +=random.choice(characters)
    return final_string;

def score (generated):
    count = 0
    #comparing string based on the number of words gotten
    word_list = generated.split(' ')
    # print(word_list, 'word-list')
    for word in word_list:
        if word in reference_str.split(' '):
            count = count + 1;
    print(count, 'count')
    return count / len(reference_str.split(' ')) * 100;


def compare ():
    number_of_iterations = 0
    generated_string = generate();
    print(generated_string, 'This is g_String')
    best_string_so_far = ['', 0]
    score_counted = score(generated_string)
    if(score_counted == 100) :
        print(generated_string, score_counted, '% successful')
    else :
        if(number_of_iterations % 1000 == 0): 
            print('generated String', best_string_so_far[0])
            print('score', best_string_so_far[1])
        if(score_counted > best_string_so_far[1]) :
            best_string_so_far[0] = generated_string
            best_string_so_far[1] = score_counted
        compare();

print(compare())
# print(score('it is my name'))