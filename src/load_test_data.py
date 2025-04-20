import pandas as pd
import numpy as np
from datetime import datetime, timedelta
from sqlalchemy import create_engine, text
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Get database connection string
DATABASE_URL = os.getenv("DATABASE_URL")

# Create test data
def generate_test_data(num_records=1000):
    # Sample data
    funds = [
        "Global Equity Fund", 
        "Tech Growth Fund", 
        "Emerging Markets Fund",
        "Sustainable Future Fund",
        "Income Fund"
    ]
    
    securities = [
        ("AAPL", "Apple Inc.", "Technology"),
        ("MSFT", "Microsoft Corporation", "Technology"),
        ("GOOGL", "Alphabet Inc.", "Technology"),
        ("AMZN", "Amazon.com Inc.", "Consumer Discretionary"),
        ("JPM", "JPMorgan Chase & Co.", "Financials"),
        ("JNJ", "Johnson & Johnson", "Healthcare"),
        ("V", "Visa Inc.", "Financials"),
        ("PG", "Procter & Gamble Co.", "Consumer Staples"),
        ("NVDA", "NVIDIA Corporation", "Technology"),
        ("HD", "Home Depot Inc.", "Consumer Discretionary")
    ]
    
    position_types = ["Long", "Short"]
    currencies = ["USD", "EUR", "GBP"]
    countries = ["USA", "UK", "Germany", "France", "Japan", "China"]
    
    # Generate random dates for the last year
    end_date = datetime.now()
    start_date = end_date - timedelta(days=365)
    dates = pd.date_range(start=start_date, end=end_date, freq='D')
    
    # Generate random data
    data = []
    for _ in range(num_records):
        # Fix: randomly select index instead of directly choosing from securities tuple
        security_idx = np.random.randint(0, len(securities))
        security = securities[security_idx]
        date = np.random.choice(dates)
        quantity = np.random.randint(100, 10000)
        price = np.random.uniform(10, 1000)
        
        record = {
            'date': date,
            'fund_name': np.random.choice(funds),
            'security_id': security[0],
            'security_name': security[1],
            'position_type': np.random.choice(position_types),
            'quantity': quantity,
            'market_value': quantity * price,
            'currency': np.random.choice(currencies),
            'sector': security[2],
            'country': np.random.choice(countries)
        }
        data.append(record)
    
    return pd.DataFrame(data)

def create_database_and_table():
    """Create the database and table if they don't exist"""
    engine = create_engine(DATABASE_URL)
    
    # Create table
    create_table_sql = text("""
    IF NOT EXISTS (SELECT * FROM sys.objects WHERE object_id = OBJECT_ID(N'fund_positions') AND type in (N'U'))
    BEGIN
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
        )
    END
    """)
    
    with engine.connect() as connection:
        connection.execute(create_table_sql)
        connection.commit()

def load_test_data():
    """Generate and load test data into the database"""
    try:
        # Create database and table
        create_database_and_table()
        
        # Generate test data
        print("Generating test data...")
        df = generate_test_data()
        
        # Connect to database
        print("Connecting to database...")
        engine = create_engine(DATABASE_URL)
        
        # Load data
        print("Loading data into database...")
        df.to_sql('fund_positions', engine, if_exists='append', index=False)
        
        print(f"Successfully loaded {len(df)} records into the database!")
        
        # Print sample statistics
        print("\nData Summary:")
        print(f"Number of funds: {df['fund_name'].nunique()}")
        print(f"Number of securities: {df['security_id'].nunique()}")
        print(f"Date range: {df['date'].min()} to {df['date'].max()}")
        print("\nSample records:")
        print(df.head())
        
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    load_test_data() 