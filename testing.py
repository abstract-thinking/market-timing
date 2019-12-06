import unittest
import glob, os
import re


class FileNameChanger:

    def __init__(self, file_name):

        files = glob.glob('./*.mp4')
        print(files)

        self.current_file_name = file_name

        for file_name_in_loop in files:
            self.current_file_name = file_name_in_loop

            new_file_name = self.replace_parts()
            self.rename_file(new_file_name)

            new_file_name = self.replace_commas_before_hash()
            self.rename_file(new_file_name)

            new_file_name = self.add_space_before_hash()
            self.rename_file(new_file_name)

            new_file_name = self.replace_dots()
            self.rename_file(new_file_name)

    def rename_file(self, new_file_name):
        os.rename(self.current_file_name, new_file_name)
        self.current_file_name = new_file_name

    # def find_file_1(self):
    #     os.chdir("/mydir")
    #     for file in glob.glob("*.mp4"):
    #         print(file)
    #
    # def find_file_2(self):
    #     for file in os.listdir("/mydir"):
    #         if file.endswith(".mp4"):
    #             print(os.path.join("/mydir", file))
    #
    # def find_file_3(self):
    #     for root, dirs, files in os.walk("/mydir"):
    #         for file in files:
    #             if file.endswith(".mp4"):
    #                 print(os.path.join(root, file))

    def replace_dots(self):
        ending_index = self.current_file_name.rfind('.')
        temp_file_name = self.current_file_name[:ending_index].replace('.', ' ')
        ending = self.current_file_name[ending_index + 1:]
        return temp_file_name + '.' + ending

    def replace_parts(self):
        count_hyphen = self.current_file_name.count('-')
        if count_hyphen != 2:
            return self.current_file_name

        left_index = self.current_file_name.find('-')
        right_index = self.current_file_name.rfind('-')
        ending_index = self.current_file_name.rfind('.')

        part1 = self.current_file_name[:left_index].strip()
        part2 = self.current_file_name[left_index + 1: right_index].strip()
        part3 = self.current_file_name[right_index + 1: ending_index].strip()
        ending = self.current_file_name[ending_index + 1:]

        return part3 + ' - ' + part2 + ' - ' + part1 + '.' + ending

    def replace_commas_before_hash(self):
        return re.sub(r',#', ' #', self.current_file_name)

    def add_space_before_hash(self):
        return re.sub(r'(\w+)#', r'\1 #', self.current_file_name)


class FileNameChangerTest(unittest.TestCase):

    def test_replace_dot(self):
        file_name = "abc.def.ghi.mp4"
        new_file_name = FileNameChanger(file_name).replace_dots()

        self.assertEqual("abc def ghi.mp4", new_file_name)

    def test_replace_part1_and_part3(self):
        file_name = "abc - def - ghi.mp4"

        new_file_name = FileNameChanger(file_name).replace_parts()

        self.assertEqual('ghi - def - abc.mp4', new_file_name)

    def test_replace_nothing(self):
        file_name = "abc - def.mp4"

        new_file_name = FileNameChanger(file_name).replace_parts()

        self.assertEqual('abc - def.mp4', new_file_name)

    def test_replace_commas_before_hash(self):
        file_name = "abc, def - ghi #jkl,#mno.mp4"

        new_file_name = FileNameChanger(file_name).replace_commas_before_hash()

        self.assertEqual('abc, def - ghi #jkl #mno.mp4', new_file_name)

    def test_add_space_before_hash(self):
        file_name = "xyz #abc#def.mp4"

        new_file_name = FileNameChanger(file_name).add_space_before_hash()

        self.assertEqual('xyz #abc #def.mp4', new_file_name)


if __name__ == '__main__':
    unittest.main()
