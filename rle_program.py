import console_gfx


def count_runs(flatData):
    runs = 0
    counter = 0
    for index in range(1, len(flatData)):
        if flatData[index - 1] != flatData[index]:
            runs += 1
            counter = 0
        else:
            counter += 1
        if counter % 15 == 0 and counter != 0:
            runs += 1
    return runs + 1


def to_hex_string(data):
    data = list(data)
    hex_string = ''
    final_string = ''
    for index in range(0, len(data)):
        if data[index] == 10:
            number = 'a'
        elif data[index] == 11:
            number = 'b'
        elif data[index] == 12:
            number = 'c'
        elif data[index] == 13:
            number = 'd'
        elif data[index] == 14:
            number = 'e'
        elif data[index] == 15:
            number = 'f'
        else:
            number = str(data[index])
        hex_string += number
    return hex_string


def encode_rle(flat_data):
    code = []
    new_run_position = 1
    counter = 0
    continue_ = True
    while len(code) < count_runs(flat_data) * 2 and continue_:
        if continue_ == False:
            break
        for index in range(1, len(flat_data)):
            if new_run_position > len(flat_data):
                continue_ = False
                break
            if flat_data[index - 1] == flat_data[index]:
                new_run_position += 1
                counter += 1
                continue
            else:
                code.append(counter + 1)
                try:
                    code.append(int(flat_data[new_run_position - 1]))
                except:
                    if flat_data[new_run_position - 1] == 'a':
                        code.append(10)
                    elif flat_data[new_run_position - 1] == 'b':
                        code.append(11)
                    elif flat_data[new_run_position - 1] == 'c':
                        code.append(12)
                    elif flat_data[new_run_position - 1] == 'd':
                        code.append(13)
                    elif flat_data[new_run_position - 1] == 'e':
                        code.append(14)
                    elif flat_data[new_run_position - 1] == 'f':
                        code.append(15)
                counter = 0
                new_run_position += 1
    counter = 0
    for index_two in range(len(flat_data) - 1, 0, -1):
        if flat_data[index_two] == flat_data[index_two - 1]:
            counter += 1
        else:
            code.append(counter + 1)
            try:
                code.append(int(flat_data[index_two]))
            except:
                if flat_data[index_two] == 'a':
                    code.append(10)
                elif flat_data[index_two] == 'b':
                    code.append(11)
                elif flat_data[index_two] == 'c':
                    code.append(12)
                elif flat_data[index_two] == 'd':
                    code.append(13)
                elif flat_data[index_two] == 'e':
                    code.append(14)
                elif flat_data[index_two] == 'f':
                    code.append(15)
        break
    return bytes(code)


def get_decoded_length(rle_data):
    size = 0
    for index in range(0, len(rle_data), 2):
        size += rle_data[index]
    return size


def decode_rle(rle_data):
    decompressed = []
    for index in range(0, len(rle_data), 2):
        number = rle_data[index]
        while number > 0:
            decompressed.append(rle_data[index + 1])
            number -= 1
    return bytes(decompressed)


def string_to_data(data_string):
    code = []
    for index in range(0, len(data_string)):
        if data_string[index:index + 1] == 'a':
            character = 10
        elif data_string[index:index + 1] == 'b':
            character = 11
        elif data_string[index:index + 1] == 'c':
            character = 12
        elif data_string[index:index + 1] == 'd':
            character = 13
        elif data_string[index:index + 1] == 'e':
            character = 14
        elif data_string[index:index + 1] == 'f':
            character = 15
        else:
            character = str(data_string[index:index + 1])
        code.append(int(character))
    return code


def to_rle_string(rleData):
    rleData = list(rleData)
    hex_string = ''
    final_string = ''
    scova = False
    index = 0
    counter = 0
    while index < len(rleData):
        if rleData[index] > 15:
            scova = True
            rleData[index] -= 15
            hex_string += '15'
        else:
            hex_string += str(rleData[index])

        if rleData[index + 1] == 10:
            number = 'a'
        elif rleData[index + 1] == 11:
            number = 'b'
        elif rleData[index + 1] == 12:
            number = 'c'
        elif rleData[index + 1] == 13:
            number = 'd'
        elif rleData[index + 1] == 14:
            number = 'e'
        elif rleData[index + 1] == 15:
            number = 'f'
        else:
            number = str(rleData[index + 1])

        if scova:
            index -= 2
            counter += 1
            scova = False
        index += 2

        hex_string += number
        if index != len(rleData):
            hex_string += ':'
        else:
            break

    counter = 1
    for index in range(len(hex_string) - 1, 0, -1):
        if hex_string[index] == hex_string[index - 1]:
            counter += 1
        else:
            if counter > 15:
                wholes = (counter // 15)
                remainder = (counter % 15)
                while wholes != 0:
                    final_string += '15'
                    final_string += hex_string[index]
                    final_string += ':'
                    wholes -= 1
                if remainder != 0:
                    final_string += str(remainder)
                    final_string += hex_string[index]
                counter = 1
                break
            final_string += str(counter)
            final_string += hex_string[index]
            break
    return hex_string


def string_to_rle(rleString):
    code = []
    distance = 0
    scovad = False
    index = 0
    while index < len(rleString):
        distance += 1
        if index == len(rleString) - 1 or rleString[index + 1] == ':':
            if distance == 2:
                code.append(int(rleString[index - 1]))
                if rleString[index] == 'a':
                    code.append(10)
                elif rleString[index] == 'b':
                    code.append(11)
                elif rleString[index] == 'c':
                    code.append(12)
                elif rleString[index] == 'd':
                    code.append(13)
                elif rleString[index] == 'e':
                    code.append(14)
                elif rleString[index] == 'f':
                    code.append(15)
                else:
                    code.append(int(rleString[index]))
                distance = -1
                index += 1
                continue
            elif distance == 3:
                code.append(int(rleString[index - 2:index]))
                scova = True
                while scova == True:
                    if rleString[index:index + 1] == 'a':
                        code.append(10)
                        distance = -1
                        index += 1
                        scova = False
                        scovad = True
                        break
                    elif rleString[index:index + 1] == 'b':
                        code.append(11)
                        distance = -1
                        index += 1
                        scova = False
                        scovad = True
                        break
                    elif rleString[index:index + 1] == 'c':
                        code.append(12)
                        distance = -1
                        index += 1
                        scova = False
                        scovad = True
                        break
                    elif rleString[index:index + 1] == 'd':
                        code.append(13)
                        distance = -1
                        index += 1
                        scova = False
                        scovad = True
                        break
                    elif rleString[index:index + 1] == 'e':
                        code.append(14)
                        distance = -1
                        index += 1
                        scova = False
                        scovad = True
                        break
                    elif rleString[index:index + 1] == 'f':
                        code.append(15)
                        distance = -1
                        index += 1
                        scova = False
                        scovad = True
                        break
                    scova = False
            distance = -1
        else:
            index += 1
    return code


if __name__ == '__main__':
    isDone = False
    print('Welcome to the RLE image encoder!')
    print('\nDisplaying Spectrum Image:\n')
    console_gfx.display_image([16, 2,
                               0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15,
                               0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])
    the_data = []
    while not isDone:
        print('\nRLE Menu\n--------')
        print('0. Exit')
        print('1. Load File')
        print('2. Load Test Image')
        print('3. Read RLE String')
        print('4. Read RLE Hex String')
        print('5. Read Data Hex String')
        print('6. Display Image')
        print('7. Display RLE String')
        print('8. Display Hex RLE Data')
        print('9. Display Hex Flat Data')
        user_selection = int(input('Select a Menu Option: '))
        if (user_selection == 1):
            filename = input('Enter name of file to load: ')
            s = console_gfx.load_file(filename)
            v = [x for x in s]  # integer list
            the_data = v
            continue
        elif (user_selection == 2):
            print('Test image data loaded.')
            the_data = console_gfx.TEST_IMAGE
            continue
        elif (user_selection == 3):
            rle_data = input('Enter an RLE string to be decoded: ')
            the_data = string_to_rle(rle_data)
            continue
        elif (user_selection == 4):
            flat_data = input('Enter the hex string holding RLE data: ')
            result = string_to_data(flat_data)
            the_data = result
            print('RLE decoded length: ' + str(get_decoded_length(result)))
            continue
        elif (user_selection == 5):
            data = input('Enter the hex string holding flat data: ')
            result = encode_rle(data)
            the_data = result
            scrummy = list(str(count_runs(data)))
            print("Number of runs: " + str(count_runs(data)))
            continue
        elif (user_selection == 6):
            print('Displaying image...')
            try:
                console_gfx.display_image(the_data)
            except:
                print('(no data)')
            continue
        elif (user_selection == 7):
            if (len(the_data) != 0):
                print('RLE representation: ' + to_rle_string(the_data))
            else:
                print('RLE representation: (no data)')
        elif (user_selection == 8):
            if (len(the_data) != 0):
                print('RLE hex values: ' + to_hex_string(the_data))
            else:
                print('RLE hex values: (no data)')
            continue
        elif (user_selection == 9):
            if (len(the_data) != 0):
                print('Flat hex values: ')
                scrummy = list(decode_rle(the_data))
                final = ''
                for index in range(0, len(scrummy)):
                    if scrummy[index] == 10:
                        final += 'a'
                    elif scrummy[index] == 11:
                        final += 'b'
                    elif scrummy[index] == 12:
                        final += 'c'
                    elif scrummy[index] == 13:
                        final += 'd'
                    elif scrummy[index] == 14:
                        final += 'e'
                    elif scrummy[index] == 15:
                        final += 'f'
                    else:
                        final += str(scrummy[index])
                print(final)
            else:
                print('Flat hex values: (no data)')
            continue
        elif (user_selection == 0):
            isDone = True
        else:
            print('Error! Invalid input.')
