import pandas as pd
import json
from pathlib import Path

def convert_csv_to_json():
    # Create dataset directory if it doesn't exist
    dataset_dir = Path('dataset')
    dataset_dir.mkdir(exist_ok=True)
    
    csv_file = dataset_dir / 'dataset.csv'
    json_file = Path('submission.json')  # Save as submission.json
    
    # Check if CSV file exists
    if not csv_file.exists():
        print(f"Error: {csv_file} not found!")
        return
    
    try:
        # Read CSV file using pandas
        df = pd.read_csv(csv_file)
        
        # Convert DataFrame to JSON
        data = df.to_dict(orient='records')
        
        # Write JSON file
        with open(json_file, 'w', encoding='utf-8') as jsonf:
            json.dump(data, jsonf, indent=4)
        
        print(f"Successfully converted {csv_file} to {json_file}")
        
    except Exception as e:
        print(f"Error during conversion: {str(e)}")

if __name__ == "__main__":
    convert_csv_to_json() 