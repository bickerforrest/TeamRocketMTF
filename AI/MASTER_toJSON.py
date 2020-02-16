from json import load, dump
import numpy as np

#---------------------#
# Specify input paths #
#--------------A-------#
climateNOAA_path = "/Users/forrestbicker/Documents/Code/Python/WorkInProgress/MTF/data/AI/RAW/ClimateVariablesNOAA.json"
OverallUSDA_path = "/Users/forrestbicker/Documents/Code/Python/WorkInProgress/MTF/data/AI/RAW/OverallUSDA.json"
IndemnifiedUSDA_path = "/Users/forrestbicker/Documents/Code/Python/WorkInProgress/MTF/data/AI/RAW/IndemnifiedUSDA.json"

#---------------------#
# Specify output path #
#---------------------#
output_path = "/Users/forrestbicker/Documents/Code/Python/WorkInProgress/MTF/data/AI/OUT"

#-------#
# Setup #
#-------#
climateNOAA_dict = load(climateNOAA_path)
OverallUSDA_dict = load(OverallUSDA_path)
IndemnifiedUSDA_dict = load(IndemnifiedUSDA_path)

MASTER_dict = {}
# final JSON to be in the following form
#
#   {
#       "countyID-yyyy-mm": [
#           [tMax, tAvg, tMin, pcpt],
#           [severity, frequency],
#       ]
#   }
#


with open(output_path, "w+") as outfile:
    dump(MASTER_dict, outfile)
