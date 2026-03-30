CREATE TABLE records (
    id LOAN_ID PRIMARY KEY,
    record TEXT,
    facility_id INT,
    SOR TEXT,
    SOO TEXT,
    LOB TEXT,
    SOR_Type TEXT,
    Analyst TEXT,
    completed TEXT,
    Analysis TEXT,
    Updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);