import pandas as pd
import numpy as np

filepath_example = './input/1_example.txt'
filepath_real = './input/1_real.txt'

def part_1(filepath):
    df = pd.read_csv(filepath, sep=r'\s{3,}', engine='python', header=None, names=['L1', 'L2'])

    list1 = df['L1'].tolist()
    list2 = df['L2'].tolist()
    list1.sort()
    list2.sort()

    difference = np.abs(np.array(list1) - np.array(list2))
    total_difference = np.sum(difference)
    return total_difference

def part_2(filepath):
    df = pd.read_csv(filepath, sep=r'\s{3,}', engine='python', header=None, names=['L1', 'L2'])

    count_in_L2 = df['L2'].value_counts()
    df['sim_score'] = df['L1'].map(count_in_L2).fillna(0) * df['L1']
    total_score = df['sim_score'].sum()
    return int(total_score)

print(f"""total difference part 1:
      example: {part_1(filepath_example)}
      real: {part_1(filepath_real)}""")

print(f"""total difference part 2:
      example: {part_2(filepath_example)}
      real: {part_2(filepath_real)}""")

"""
total difference part 1:
      example: 11
      real: 3574690
"""
"""
total difference part 2:
      example: 31
      real: 22565391
"""