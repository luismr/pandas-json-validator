# Pandas JSON Validator

[![Python](https://img.shields.io/badge/python-3.9+-green.svg)](https://www.python.org/downloads/)
[![Pandas](https://img.shields.io/badge/pandas-2.2.3-green.svg)](https://pandas.pydata.org/)
[![JSON](https://img.shields.io/badge/json-2.0.0-green.svg)](https://www.json.org/)

A simple tool to convert CSV data to JSON format using Pandas, with built-in validation.

## File Structure

```
pandas-json-validator/
├── dataset/
│   └── dataset.csv      # Input CSV file
├── convert_csv_to_json.py  # Main conversion script
├── submission.json      # Generated JSON output
├── requirements.txt     # Python dependencies
├── .gitignore          # Git ignore rules
├── LICENSE.md          # MIT License
└── README.md           # This file
```

## Dataset Format

The `dataset.csv` file should follow this structure:
```csv
id,name,age,city
1,John Doe,30,New York
2,Jane Smith,25,Los Angeles
3,Bob Johnson,35,Chicago
```

### CSV Requirements:
- First row must contain column headers
- Each subsequent row contains data
- Values should be comma-separated
- No spaces around commas
- Text values containing commas should be properly quoted

## Setup Instructions

### macOS
```bash
# Clone the repository
git clone git@github.com:luismr/pandas-json-validator.git
cd pandas-json-validator

# Create and activate virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### Linux
```bash
# Clone the repository
git clone git@github.com:luismr/pandas-json-validator.git
cd pandas-json-validator

# Create and activate virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### Windows
```bash
# Clone the repository
git clone git@github.com:luismr/pandas-json-validator.git
cd pandas-json-validator

# Create and activate virtual environment
python -m venv venv
.\venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

## Usage

1. Place your CSV file in the `dataset` directory as `dataset.csv`
2. Run the conversion script:
   ```bash
   python convert_csv_to_json.py
   ```
3. The script will generate `submission.json` in the root directory

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details. 