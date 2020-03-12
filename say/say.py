WORDS = ['zero', 'one', 'two ', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten',
         'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen',
         'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']

GROUPS = ['', '', 'thousand', 'million', 'billion']


def say(number):
    number = int(number)

    if number < 0 or number > 999999999999:
        raise ValueError("Number '{}' is not an integer in range 0 to 999,999,999,999".format(number))

    if number <= 20:
        return WORDS[number]

    # Main loop for values over 20
    result = ''
    number_groups = '{:,}'.format(number).split(',')
    idx = 1
    for number_string in reversed(number_groups):
        if int(number_string) > 0:
            result = words_for(int(number_string)) + ' ' + GROUPS[idx] + ' ' + result
        elif int(number_string) == 0:
            result = 'and ' + result
        idx += 1

    # Remove unwanted words and chars added in main loop
    x = 0
    while x <= 4:
        if result[-5:] == ' and ':
            result = result[:-4]
        x += 1

    result = result.replace('   ', ' ')
    result = result.replace('  ', ' ')

    return result.strip()


def words_for(number):
    hundreds_value = number // 100
    tens_value = number - hundreds_value * 100
    result = ''
    if hundreds_value >= 1:
        result = WORDS[hundreds_value] + ' hundred '
        if tens_value > 0:
            result += ' and ' + get_tens(tens_value) + ' '

    elif number > 0:
        result += get_tens(tens_value)

    return result


def get_tens(number):
    result = ''
    if number > 20:
        result += WORDS[number // 10 + 18]
        if number % 10 > 0:
            result += '-' + WORDS[number % 10]
        else:
            result += ' ' + WORDS[number % 10]

    elif number > 0:
        result += WORDS[number] + ' '

    return result