# -*- coding: utf-8 -*-
import dataiku
import pandas as pd, numpy as np
from dataiku import pandasutils as pdu

# Read recipe inputs
FAO = dataiku.Dataset("FAO")
FAO_df = FAO.get_dataframe()


# Compute recipe outputs from inputs
# TODO: Replace this part by your actual code that computes the output, as a Pandas dataframe
# NB: DSS also supports other kinds of APIs for reading and writing data. Please see doc.

Age = [21, 23, 24, 21]
FAO_df['Age'] = pd.Series(Age)

FAO_Python_output_df = FAO_df # For this sample code, simply copy input to output


# Write recipe outputs
FAO_Python_output = dataiku.Dataset("FAO_Python_output")
FAO_Python_output.write_with_schema(FAO_Python_output_df)
