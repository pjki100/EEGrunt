import EEGrunt

# Required settings #

# Data source. Options:
# 'openbci' for data recorded with OBCI GUI;
# 'openbci-openvibe' for OBCI data recorded with OpenViBE's csv writer

source = 'openbci'

# Path to EEG data file
path = 'data/ecg/'

# EEG data file name
filename = 'obci-ecg-data.txt'

# Session title (used in some plots and such)
session_title = "EEGrunt OpenBCI ECG Sample Data"

# Channel
channel = 1

# Initialize
EEG = EEGrunt.EEGrunt(path, filename, source, session_title)

# Here we can set some additional properties
# The 'plot' property determines whether plots are displayed or saved.
# Possible values are 'show' and 'save'
EEG.plot = 'show'

# Load the EEG data
EEG.load_data()

EEG.load_channel(channel)

print("Processing channel "+ str(EEG.channel))

# Removes OpenBCI DC offset
EEG.remove_dc_offset()

# Notch 60hz noise (if you're in Europe, switch to 50Hz)
EEG.notch_mains_interference()

# EEG.trim_data(0, 0)

# Plot some ECG
EEG.plot_rr_intervals()
EEG.plot_heart_rate()

EEG.hrv_window_length = 60

EEG.plot_hrv()

# When all's said and done, show the plots
EEG.showplots()
