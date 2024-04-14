-- create_tables.sql

-- Impressions table
CREATE TABLE impressions (
    ad_creative_id INT,
    user_id VARCHAR(50),
    timestamp TIMESTAMP,
    website VARCHAR(100),
    source VARCHAR(50)
);

-- Clicks/Conversions table
CREATE TABLE clicks_conversions (
    event_timestamp TIMESTAMP,
    user_id VARCHAR(50),
    campaign_id VARCHAR(50),
    conversion_type VARCHAR(50)
);

-- Bid Requests table
CREATE TABLE bid_requests (
    user_id VARCHAR(50),
    auction_id VARCHAR(50),
    age INT,
    gender VARCHAR(10),
    interests ARRAY,
    CONSTRAINT check_age CHECK (age >= 0)
);
