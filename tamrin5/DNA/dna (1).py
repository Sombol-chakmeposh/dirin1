# -*- coding: utf-8 -*-
"""DNA.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1j7hYEOhFUQUFwNGYSx0PC-sWQfHklVZL
"""

class MrKrabs:
    def __init__(self, data):
        self.data = data

    def process_data(self):
        result = ""

        if self.data.startswith("m") or self.data.endswith("m"):
            self.data = self.data[::-1] if self.data.endswith("m") else self.data
            result = self.process_mr_krabs_data()
        elif self.data.startswith("sb") or self.data.endswith("bs"):
            self.data = self.data[::-1] if self.data.endswith("bs") else self.data
            result = self.process_spongebob_data()
        elif (self.data.startswith("s") and self.data[1] != "b") or (self.data.endswith("s") and self.data[-2] != "b"):
            self.data = self.data[::-1] if self.data.endswith("s") else self.data
            result = self.process_octopus_data()
        else:
            result = "invalid input"

        return result

    def process_mr_krabs_data(self):
        result = self.data.replace("tt", "o")
        tee = self.data[:10].replace("tt","o")
        return result + tee

class SpongeBob(MrKrabs):
    def process_spongebob_data(self):
        def mergeSort(arr):
            if len(arr) > 1:
                mid = len(arr)//2
                sub_array1 = arr[:mid]
                sub_array2 = arr[mid:]
                mergeSort(sub_array1)
                mergeSort(sub_array2)
                i = j = k = 0
                while i < len(sub_array1) and j < len(sub_array2):
                    if sub_array1[i] < sub_array2[j]:
                        arr[k] = sub_array1[i]
                        i += 1
                    else:
                        arr[k] = sub_array2[j]
                        j += 1
                    k += 1
                while i < len(sub_array1):
                    arr[k] = sub_array1[i]
                    i += 1
                    k += 1
                while j < len(sub_array2):
                    arr[k] = sub_array2[j]
                    j += 1
                    k += 1

        def sort_dna_length(dna_sequence):
            length_str = list(str(len(dna_sequence)))
            dirin = [int(length_str[i]) for i in range(len(length_str))]
            mergeSort(dirin)
            sorted_length = ""
            for i in range(len(dirin)):
                if i == 0:
                    sorted_length += f"{dirin[i]+1}"
                else:
                    sorted_length += f"{dirin[i]}"
            return sorted_length

        return sort_dna_length(self.data)

class octopus(MrKrabs):
    def process_octopus_data(self):
        result = ""
        flag = False
        i = 0
        ffs = 0
        while i < len(self.data):
            count = 1
            if not flag and self.data[i] == "x":
                ffs += i
                flag = True
            while i + count < len(self.data) and self.data[i] == self.data[i + count]:
                count += 1
                if count + 1 == 4:
                    break
            if count >= 3:
                result += "(0_0)"
                i += count
            else:
                result += self.data[i]
                i += 1
        if flag:
            result += f"{ffs}"
        return result

input_data = input()

character = MrKrabs(input_data) if input_data[0] == 'm' else SpongeBob(input_data) if input_data[0] == 's' and input_data[1] == 'b' else octopus(input_data)

result = character.process_data()
print(result)