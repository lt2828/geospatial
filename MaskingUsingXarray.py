import xarray as xr

# Open the netCDF file
dataset = xr.open_dataset('your_netcdf_file.nc')

# Define a condition for creating the mask (e.g., values greater than a threshold)
threshold = 0.5
mask = dataset['your_variable_name'] > threshold

# Apply the mask using xarray's where() method
masked_data = dataset['your_variable_name'].where(mask)

# Close the netCDF file
dataset.close()

# You can save the masked data to a new netCDF file if needed
masked_data.to_netcdf('masked_data.nc')
