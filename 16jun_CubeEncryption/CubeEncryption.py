from Cube import Cube
import random


class CubeEncryption:
    def __init__(self, file_path):
        self.file_path = file_path
        self.text = ''
        self.key = ''
        self.cubes = []
        self.encoded_text = ''
        self.decoded_text = ''

    def _creating_cubes(self):
        with open(self.file_path, 'r') as input_file:
            self.text = input_file.read()
        # print(text)
        len_of_text = len(self.text)
        cube_count = (len_of_text // 8) + 1
        lst_of_letters = []
        text_split_len_8 = []

        for i in range(cube_count):
            tmp_str = self.text[8*i:8*(i+1)]
            text_split_len_8.append(tmp_str)

        for word in text_split_len_8:
            for letter in word:
                lst_of_letters.append(letter)
            if len(lst_of_letters) < 8:
                for _ in range(8 - len(lst_of_letters)):
                    lst_of_letters.append('X')
            cor1, cor2, cor3, cor4, cor5, cor6, cor7, cor8 = lst_of_letters
            lst_of_letters = []
            self.cubes.append(Cube(cor1, cor2, cor3, cor4, cor5, cor6, cor7, cor8))

        return self.cubes

    def _generate_random_key(self):
        directions = ['l', 'r', 'u', 'd']
        key = []
        for _ in range(len(self.cubes)):
            part = ''
            while len(part) <= 4:
                direction = random.choice(directions)
                count = random.randint(1, 3)
                part += direction + str(count) + ','
            key.append(part[:-1])
        self.key = ' : '.join(key)
        return self.key

    def encode(self):
        res = []
        self.cubes = self._creating_cubes()
        # print(self.cubes)
        self.key = self._generate_random_key()
        rotation_for_each_cube = self.key.split(' : ')

        for i in range(len(rotation_for_each_cube)):
            actions = rotation_for_each_cube[i].split(',')
            for action in actions:
                if action.startswith('l'):
                    for time in range(int(action[-1])):
                        self.cubes[i].rotate_left()
                if action.startswith('r'):
                    for time in range(int(action[-1])):
                        self.cubes[i].rotate_right()
                if action.startswith('u'):
                    for time in range(int(action[-1])):
                        self.cubes[i].rotate_upward()
                if action.startswith('d'):
                    for time in range(int(action[-1])):
                        self.cubes[i].rotate_downward()

        for cube in self.cubes:
            res.append(cube.getting_word())

        self.encoded_text = ''.join(res)   # .replace('X', '')
        return self.encoded_text

    def create_encoded_text_file(self):
        with open(f'encoded_{self.file_path}', 'w+') as out_file:
            out_file.write(self.encode())

    def decode(self, file_of_encode):
        res = []
        for_decoding = CubeEncryption(file_of_encode)
        for_decoding.cubes = for_decoding._creating_cubes()
        for_decoding.key = self.key
        rotation_for_each_cube = for_decoding.key.split(' : ')

        for i in range(len(rotation_for_each_cube)):
            actions = rotation_for_each_cube[i].split(',')[::-1]
            for action in actions:
                if action.startswith('l'):
                    for time in range(int(action[-1])):
                        for_decoding.cubes[i].rotate_right()
                if action.startswith('r'):
                    for time in range(int(action[-1])):
                        for_decoding.cubes[i].rotate_left()
                if action.startswith('u'):
                    for time in range(int(action[-1])):
                        for_decoding.cubes[i].rotate_downward()
                if action.startswith('d'):
                    for time in range(int(action[-1])):
                        for_decoding.cubes[i].rotate_upward()

        for cube in for_decoding.cubes:
            res.append(cube.getting_word())

        self.decoded_text = ''.join(res).replace('X', '')
        return self.decoded_text

    def create_decoded_text_file(self):
        with open(f'decoded_{self.file_path}.txt', 'w+') as out_file:
            out_file.write(self.decode(f'encoded_{self.file_path}'))
            out_file.write(f'\n\nKey was -> {self.key}')
