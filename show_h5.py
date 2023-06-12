#%%
import h5py
import matplotlib.pyplot as plt
from matplotlib import colors
import numpy as np
#%%
data_path = "../data/training_data/"
#file_name = "InVivo/MenisKI21_Prediction_InVivo_24.h5"
#file_name = "InVivo/MenisKI21_Prediction_InVivo_24_turned.h5"
#file_name = "InVivo/MenisKI21_Prediction_InVivo_24_turned_resized.h5"
file_name = "mixed/MenisKI21_Training_20_mixed.h5"
#file_name = "OAI_single/MenisKI21_Training_25_Femur_von_cloud.h5"
#file_name = "InVivo/MenisKI21_Training_10_InVivo_resized.h5"
#file_name = "InVivo/MenisKI21_Training_10_InVivo_resized_turned.h5"
#file_name = "OAI_6/MenisKI21_Training_25_6_Classes_cropped.h5"

#file_name = "OAI_6/MenisKI21_Training_25_6_Classes.h5"
#file_name = "MenisKI21_Prediction_hand_cropped_25.h5"

file_path = data_path+file_name
#%%
file = h5py.File(file_path,'r')

print(file.keys())
#%%


#%%

cmap=colors.ListedColormap(['blue', 'red', 'green', 'yellow', 'purple', 'orange'])
#cmap=colors.ListedColormap(['blue'])
rows = 3
cols = 3
start_with = 0
show_every = 1
bounds=[1, 2, 3, 4, 5, 6, 7]
#bounds=[0,2]
norm = colors.BoundaryNorm(bounds, cmap.N)
fig,ax = plt.subplots(rows,cols,figsize=[30,30])
#stack = file['MenisKI21_Training_0047_InVivo_dcm'][:]
stack = file['MenisKI21_Training_0080_dcm'][:] # 80 in mixed for OAI
#segmentation = file['MenisKI21_Training_0047_InVivo_seg'][:]
segmentation = file['MenisKI21_Training_0080_seg'][:]
m_s = np.amax(segmentation)
print(m_s)
keys = file.keys
print(keys)
for i in range(rows*cols):
    ind = start_with  + i*show_every
    ax[int(i/rows),int(i % rows)].set_title('slice %d' % ind)
    ax[int(i/rows),int(i % rows)].imshow(stack[ind],cmap='gray',interpolation='none')
    ax[int(i/rows),int(i % rows)].imshow(np.ma.masked_where(segmentation[ind] == 0, segmentation[ind]),interpolation='nearest', origin='lower',cmap=cmap, norm=norm)
    ax[int(i/rows),int(i % rows)].axis('off')
plt.show()
#%%
