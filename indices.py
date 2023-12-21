import netCDF4 as nc
import numpy as np
from datetime import datetime

# Open the NetCDF file
file_path = 'datasets\precip.V1.0.day.ltm.1981-2010.nc'
dataset = nc.Dataset(file_path, 'r')

# Prompt user for Latitude and Longitude values
input_lat = float(input('Enter your desired Latitude:\n'))
input_lon = float(input('Enter your desired Longitude:\n'))
adjusted_lon = input_lon + 360
print(f"Latitude: {input_lat}")
print(f"Longitude: {input_lon}")
print(f"Adjusted Longitude: {adjusted_lon}")

# Assigning April 8 as an initial value
# Update this to be based on user selection
# We only need the month and day value, so we are using 1800 as a reference year for datetime
input_month = int(input("Enter a month as a number: \n"))
input_day = int(input("Enter a day as a number: \n"))
input_date = datetime(1800, input_month, input_day)
print(f"User Selected Date: {input_date}")

# The Time Dimension is made up of 365 values, one for each day of the year
# Here we convert our input month and day to the number of days from January 1, or Time[0]
date_delta = input_date - datetime(1800, 1, 1)
print(f"Days since January 1: {date_delta}")

# Convert the input date to the same format as the 'time' variable
hours_since_reference = (input_date - datetime(1800, 1, 1)).total_seconds() / 3600
time_var = dataset.variables['time']
date_index = date_delta.days
# date_index = 4
print(f"Hours Since Reference Date: {hours_since_reference}")
# print(f"Dataset Time Variable: {time_var}")
print(f"Dataset Date Index: {date_index}")

# Find the indices for the specific latitude and longitude
lat_var = dataset.variables['lat']
lon_var = dataset.variables['lon']

# These expressions calculate the absolute difference between every value in the dataset's latitude/longitude arrays and the input latitude/longitude. 
# The result is an array of differences.
# numpy.argmin() finds the index of the minimum value, indicating the closest value to what we are looking for.
lat_index = np.argmin(np.abs(lat_var[:] - input_lat))
print(f"Available lat values: {lat_var[:]}")
lon_index = np.argmin(np.abs(lon_var[:] - adjusted_lon))
print(f"Available lon values: {lon_var[:]}")

# Print selected indices
print(f"Dataset Lat Index: {lat_index}")
print(f"Dataset Lon Index: {lon_index}")

# Extract the precipitation data
precip_var = dataset.variables['precip']
precip_data = precip_var[date_index, lat_index, lon_index]
print(f"Precipitation data: {precip_data}")

# Close the dataset
dataset.close()
