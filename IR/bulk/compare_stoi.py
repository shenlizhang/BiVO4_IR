import matplotlib.pyplot as plt
from scipy.ndimage import gaussian_filter1d
import numpy as np
from matplotlib.ticker import MultipleLocator

# Define the file path
file_path = './OscillatorStrengths_bulk_pbe_221.txt'
file_path2='./OscillatorStrengths_bulk_exp_vasp_111.txt'
file_path3='./OscillatorStrengths_bulk_scan_111.txt'
file_path4='./OscillatorStrengths_bulk_pbe_monocell_221.txt'

# Read the file and extract data
with open(file_path, 'r') as file:
    lines = file.readlines()[1:]

with open(file_path2, 'r') as file2:
    lines2 = file2.readlines()[1:]

with open(file_path3, 'r') as file3:
    lines3 = file3.readlines()[1:]

with open(file_path4, 'r') as file4:
    lines4 = file4.readlines()[1:]

# Find the index of "Oscillator Strengths"
separator_index = None
for i, line in enumerate(lines):
    if "Oscillator Strengths" in line:
        separator_index = i
        break

if separator_index is None:
    raise ValueError("Could not find the separator 'Oscillator Strengths' in the file.")

def clean_and_convert(line):
    line = line.strip().lstrip('-').strip()  # Remove leading '-' and extra spaces
    return float(line) if line else None

# Extract x and y data
x_data = [clean_and_convert(line) for line in lines[:separator_index] if clean_and_convert(line) is not None]
y_data = [clean_and_convert(line) for line in lines[separator_index + 1:] if clean_and_convert(line) is not None]


separator_index = None
for i, line in enumerate(lines3):
    if "Oscillator Strengths" in line:
        separator_index = i
        break

if separator_index is None:
    raise ValueError("Could not find the separator 'Oscillator Strengths' in the file.")

def clean_and_convert(line):
    line = line.strip().lstrip('-').strip()  # Remove leading '-' and extra spaces
    return float(line) if line else None

# Extract x and y data
x_data3 = [clean_and_convert(line) for line in lines3[:separator_index] if clean_and_convert(line) is not None]
y_data3 = [clean_and_convert(line) for line in lines3[separator_index + 1:] if clean_and_convert(line) is not None]

separator_index = None
for i, line in enumerate(lines4):
    if "Oscillator Strengths" in line:
        separator_index = i
        break

if separator_index is None:
    raise ValueError("Could not find the separator 'Oscillator Strengths' in the file.")

def clean_and_convert(line):
    line = line.strip().lstrip('-').strip()  # Remove leading '-' and extra spaces
    return float(line) if line else None

# Extract x and y data
x_data4 = [clean_and_convert(line) for line in lines4[:separator_index] if clean_and_convert(line) is not None]
y_data4 = [clean_and_convert(line) for line in lines4[separator_index + 1:] if clean_and_convert(line) is not None]

separator_index = None
for i, line in enumerate(lines2):
    if "Oscillator Strengths" in line:
        separator_index = i
        break

if separator_index is None:
    raise ValueError("Could not find the separator 'Oscillator Strengths' in the file.")

def clean_and_convert(line):
    line = line.strip().lstrip('-').strip()  # Remove leading '-' and extra spaces
    return float(line) if line else None

# Extract x and y data
x_data2 = [clean_and_convert(line) for line in lines2[:separator_index] if clean_and_convert(line) is not None]
y_data2 = [clean_and_convert(line) for line in lines2[separator_index + 1:] if clean_and_convert(line) is not None]


# Plot the data
fig=plt.figure(figsize=(5.5, 8.5))
gs=fig.add_gridspec(4,hspace=0)
axs=gs.subplots(sharex=True, sharey=True)
axs[0].vlines(x_data,0,y_data,linewidth=2)
axs[1].vlines(x_data2,0,y_data2,linewidth=2)
axs[2].vlines(x_data3,0,y_data3,linewidth=2)
axs[3].vlines(x_data4,0,y_data4,linewidth=2)
for ax in axs:
    ax.label_outer()
    # enable minor ticks and set their spacing to 1
    #ax.minorticks_on()
    ax.xaxis.set_minor_locator(MultipleLocator(10))
    # increase tick label size
    ax.tick_params(axis='both', which='major', labelsize=12,length=6,width=2)
    ax.tick_params(axis='x', which='minor', labelsize=10,length=4)
fig.supxlabel(r'Wave number (cm$^{-1}$)',fontsize=14)
fig.supylabel('Oscillator Strengths (arb. units)',fontsize=14)
fig.subplots_adjust(left=0.12, right=0.98, top=0.98, bottom=0.1)
plt.ylim([0,11])
plt.xlim([0,800])
#plt.grid()
plt.tight_layout()
plt.savefig('bulk_compare.pdf')

#xy = np.column_stack((np.array(x_data4), np.array(y_data4)))
#np.savetxt('bulk_pbe_monocell_221.txt', xy, fmt='%g', header='wave_number(cm^-1) oscillator_strength(arb. units)', comments='')
