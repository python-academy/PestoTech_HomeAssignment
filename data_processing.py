def standardize_impressions(impressions):
    # Standardize timestamp format
    for impression in impressions:
        impression['timestamp'] = impression['timestamp'].replace('T', ' ')

def enrich_impressions(impressions):
    # Example: Add additional information to impressions
    for impression in impressions:
        impression['source'] = 'AdvertiseX'

def validate_clicks_conversions(clicks_conversions):
    # Example: Validate user IDs are not empty
    for event in clicks_conversions:
        if not event['user_id']:
            raise ValueError("Invalid user ID found in clicks/conversions data")

def filter_bid_requests(bid_requests):
    # Example: Filter bid requests for users under 30 years old
    bid_requests_filtered = []
    for request in bid_requests:
        if request['ad_targeting']['age'] < 30:
            bid_requests_filtered.append(request)
    return bid_requests_filtered

def deduplicate_data(data):
    # Example: Deduplicate data based on user ID
    unique_data = []
    seen_user_ids = set()
    for record in data:
        if record['user_id'] not in seen_user_ids:
            unique_data.append(record)
            seen_user_ids.add(record['user_id'])
    return unique_data

# Sample usage
if __name__ == "__main__":
    # Sample data from previous step
    # Replace these with actual data from ingestion step
    impressions = [{'ad_creative_id': 1, 'user_id': 'user1', 'timestamp': '2024-04-14 10:00:00', 'website': 'example.com'}]
    clicks_conversions = [{'event_timestamp': '2024-04-14 10:02:00', 'user_id': 'user1', 'campaign_id': 'campaign1', 'conversion_type': 'signup'}]
    bid_requests = [{'user_id': 'user1', 'auction_id': 'auction1', 'ad_targeting': {'age': 25, 'gender': 'male', 'interests': ['sports', 'technology']}}]

    # Step 1: Standardize impressions data
    standardize_impressions(impressions)
    print("Standardized Impressions:", impressions)

    # Step 2: Enrich impressions data
    enrich_impressions(impressions)
    print("Enriched Impressions:", impressions)

    # Step 3: Validate clicks/conversions data
    validate_clicks_conversions(clicks_conversions)

    # Step 4: Filter bid requests data
    bid_requests_filtered = filter_bid_requests(bid_requests)
    print("Filtered Bid Requests:", bid_requests_filtered)

    # Step 5: Deduplicate data
    deduplicated_impressions = deduplicate_data(impressions)
    print("Deduplicated Impressions:", deduplicated_impressions)
