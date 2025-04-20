# Fund Relationship Analysis Tool

A Python-based application for analyzing fund positional data using SQL Server backend and Streamlit frontend. This tool allows users to load fund position data from a database and analyze it through an interactive pivot table interface.

## Features

- SQL Server database integration for fund position data storage
- Interactive web interface built with Streamlit
- Dynamic pivot table functionality for data analysis
- Real-time data filtering and aggregation
- Export capabilities for analyzed data
- Support for multiple fund analysis

## Prerequisites

- Python 3.9 or higher
- Conda package manager
- SQL Server
- SQL Server ODBC Driver 18

### Installing SQL Server ODBC Driver

#### macOS
```bash
brew tap microsoft/mssql-release https://github.com/Microsoft/homebrew-mssql-release
brew update
brew install msodbcsql18
```

#### Linux (Ubuntu/Debian)
```bash
curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add -
curl https://packages.microsoft.com/config/ubuntu/$(lsb_release -rs)/prod.list > /etc/apt/sources.list.d/mssql-release.list
apt-get update
ACCEPT_EULA=Y apt-get install -y msodbcsql18
```

#### Windows
Download and install the driver from [Microsoft's website](https://learn.microsoft.com/en-us/sql/connect/odbc/download-odbc-driver-for-sql-server)

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd fund_relationship
```

2. Create and activate the Conda environment:
```bash
conda env create -f environment.yml
conda activate fund_relationship
```

3. Configure the database connection:
   - Copy `.env.example` to `.env`
   - Update the database connection string in `.env`:

DATABASE_URL=mssql+pyodbc://username:password@server_name/database_name?driver=ODBC+Driver+18+for+SQL+Server 

## Usage

1. Activate the Conda environment:
```bash
conda activate fund_relationship
```

2. Run the Streamlit application:
```bash
streamlit run src/app.py
```

3. Access the application in your web browser at `http://localhost:8501`

## Database Schema

The application uses the following database schema for fund positions:

```sql
CREATE TABLE fund_positions (
    id INT PRIMARY KEY IDENTITY(1,1),
    date DATE NOT NULL,
    fund_name VARCHAR(255) NOT NULL,
    security_id VARCHAR(50) NOT NULL,
    security_name VARCHAR(255) NOT NULL,
    position_type VARCHAR(50) NOT NULL,
    quantity FLOAT,
    market_value FLOAT,
    currency VARCHAR(3),
    sector VARCHAR(100),
    country VARCHAR(100)
);
```

## Features

### Data Loading
- Automatic connection to SQL Server database
- Real-time data loading and updates

### Analysis Capabilities
- Dynamic pivot table creation
- Multiple aggregation options
- Filtering by date range and fund
- Custom column and row configurations

### Export Options
- Download pivot table as CSV
- Export filtered data sets

## Development

### Adding New Dependencies

To add new packages to the environment:

```bash
conda activate fund_relationship
conda install package_name
# or
pip install package_name

# Update environment.yml
conda env export > environment.yml
```

### Running Tests

```bash
pytest
```

### Code Formatting

```bash
black src/
```

### Linting

```bash
pylint src/
```

## Troubleshooting

### Common Issues

1. Database Connection Issues
   - Verify SQL Server is running
   - Check connection string in `.env`
   - Confirm ODBC driver installation

2. Environment Issues
   - Ensure Conda environment is activated
   - Verify all dependencies are installed
   - Check Python version compatibility

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

[Your License Here]

## Contact

[Your Contact Information]