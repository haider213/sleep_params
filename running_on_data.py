import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sleeppy.sleep import *

subjects = 16

for subject in range(subjects):
    if subject < 10:
        subject_id = '00' + str(subject)
    else:
        subject_id = '0' + str(subject)
    print('Subject: ', subject_id)
    big_ideas = '/nesi/project/aut03802/Data/Data_uncompressed/Big Ideas Lab/big-ideas-lab-glycemic-variability-and-wearable-device-data-1.1.1/'
    file_acc_path = big_ideas + subject_id + '/ACC_' + subject_id + '.csv'
    file_temp_path = big_ideas + subject_id + '/TEMP_' + subject_id + '.csv'
    input_to_sleepy = [file_acc_path, file_temp_path]
    output_path='/nesi/project/aut03802/Data/sleep_features/'

    SleepPy(subject=subject_id, input_files=input_to_sleepy,
            results_directory=output_path,
            sampling_frequency=32,
            device_type='empatica')
