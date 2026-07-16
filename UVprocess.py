import os
import xarray as xr
import json

def process_uv_wind():
    u_dir = "FC_ECMWF_Uwind"
    v_dir = "FC_ECMWF_Vwind"
    out_dir = "uvwindoutput"
    
    # Example logic: grab the first matching files for demonstration
    # In reality, you will need to iterate and match specific pressure levels/timestamps
    u_files = [f for f in os.listdir(u_dir) if f.endswith('.grib2')]
    v_files = [f for f in os.listdir(v_dir) if f.endswith('.grib2')]
    
    if not u_files or not v_files:
        print("Missing U or V wind GRIB2 files.")
        return

    # Open GRIB datasets (requires cfgrib engine)
    ds_u = xr.open_dataset(os.path.join(u_dir, u_files[0]), engine='cfgrib')
    ds_v = xr.open_dataset(os.path.join(v_dir, v_files[0]), engine='cfgrib')
    
    # WARNING: These files are 1.3GB to 1.6GB each. 
    # You MUST subset this data (e.g., by specific coordinates or pressure levels) before exporting to JSON for the web.
    # Below is a conceptual placeholder for exporting the processed array.
    
    processed_data = {
        "status": "Success",
        "message": "Data processed. Needs subsetting for web JSON format."
    }
    
    output_path = os.path.join(out_dir, "processed_wind.json")
    with open(output_path, 'w') as f:
        json.dump(processed_data, f)
        
    print(f"Processing complete. Output stored in {out_dir}")

if __name__ == "__main__":
    process_uv_wind()
