"""
Advanced Python Data Structures Practice
This file contains complex problems combining multiple data structures and operations
"""


# Problem 1: Advanced Dictionary and List Operations
def analyze_sales_data(sales_records):
    """
    Process sales records to get insights about top-selling products,
    sales by month, and customer purchasing patterns
    """
    # Initialize data structures
    product_sales = {}
    monthly_sales = {}
    customer_history = {}

    for record in sales_records:
        # Update product sales
        product = record["product"]
        quantity = record["quantity"]
        product_sales[product] = product_sales.get(product, 0) + quantity

        # Update monthly sales
        month = record["date"].split("-")[1]  # Assuming date format: YYYY-MM-DD
        if month not in monthly_sales:
            monthly_sales[month] = {"total": 0, "products": set()}
        monthly_sales[month]["total"] += quantity
        monthly_sales[month]["products"].add(product)

        # Update customer history
        customer = record["customer"]
        if customer not in customer_history:
            customer_history[customer] = []
        customer_history[customer].append(record)

    # Get top 3 products
    top_products = sorted(product_sales.items(), key=lambda x: x[1], reverse=True)[:3]

    # Get month with most diverse products
    most_diverse_month = max(monthly_sales.items(), key=lambda x: len(x[1]["products"]))

    return {
        "top_products": top_products,
        "monthly_sales": monthly_sales,
        "customer_history": customer_history,
        "most_diverse_month": most_diverse_month[0],
    }


# Problem 2: String and List Manipulation
def process_text_data(text):
    """
    Process text to extract information and statistics
    """
    # Convert to lowercase and split into words
    words = text.lower().split()

    # Remove punctuation and create word frequency
    import string

    word_freq = {}
    for word in words:
        word = word.strip(string.punctuation)
        if word:
            word_freq[word] = word_freq.get(word, 0) + 1

    # Find palindromes
    palindromes = [word for word in set(words) if word == word[::-1] and len(word) > 1]

    # Find word pairs that appear together
    word_pairs = []
    for i in range(len(words) - 1):
        word_pairs.append((words[i], words[i + 1]))

    # Get statistics
    return {
        "word_count": len(words),
        "unique_words": len(set(words)),
        "most_common": sorted(word_freq.items(), key=lambda x: x[1], reverse=True)[:5],
        "palindromes": palindromes,
        "common_pairs": word_pairs[:5],
    }


# Problem 3: Complex Data Transformation
def transform_nested_structure(data):
    """
    Transform a nested data structure while applying various operations
    """

    def process_value(value):
        if isinstance(value, dict):
            return transform_nested_structure(value)
        elif isinstance(value, list):
            return [process_value(v) for v in value]
        elif isinstance(value, str):
            return value.upper()
        elif isinstance(value, (int, float)):
            return value * 2
        return value

    if isinstance(data, dict):
        return {k.title(): process_value(v) for k, v in data.items()}
    return data


# Problem 4: Advanced Set Operations and List Comprehension
def analyze_user_interactions(user_logs):
    """
    Analyze user interaction logs to find patterns and relationships
    """
    # Extract unique users and actions
    users = {log["user"] for log in user_logs}
    actions = {log["action"] for log in user_logs}

    # Create user activity profiles
    user_profiles = {
        user: {
            "actions": {log["action"] for log in user_logs if log["user"] == user},
            "total_actions": len([log for log in user_logs if log["user"] == user]),
            "unique_days": len(
                {log["date"] for log in user_logs if log["user"] == user}
            ),
        }
        for user in users
    }

    # Find users with similar patterns
    similar_users = {
        user1: {
            user2
            for user2 in users
            if user1 != user2
            and len(user_profiles[user1]["actions"] & user_profiles[user2]["actions"])
            > 2
        }
        for user1 in users
    }

    return {
        "user_profiles": user_profiles,
        "similar_users": similar_users,
        "total_unique_actions": len(actions),
    }


# Example usage and test data
if __name__ == "__main__":
    # Test data for Problem 1
    sales_data = [
        {"product": "laptop", "quantity": 2, "date": "2024-01-15", "customer": "john"},
        {"product": "mouse", "quantity": 3, "date": "2024-01-20", "customer": "alice"},
        {"product": "laptop", "quantity": 1, "date": "2024-02-10", "customer": "bob"},
        # Add more test records...
    ]

    # Test data for Problem 2
    sample_text = """
    The quick brown fox jumps over the lazy dog. 
    A man, a plan, a canal: Panama! 
    The race car driver drove fast.
    """

    # Test data for Problem 3
    nested_data = {
        "user": {
            "name": "john doe",
            "scores": [10, 20, 30],
            "preferences": {"theme": "dark", "language": "python"},
        }
    }

    # Test data for Problem 4
    user_logs = [
        {"user": "user1", "action": "login", "date": "2024-01-01"},
        {"user": "user1", "action": "search", "date": "2024-01-01"},
        {"user": "user2", "action": "login", "date": "2024-01-02"},
        # Add more test records...
    ]

    # Run and print results
    print("\n=== Sales Analysis ===")
    print(analyze_sales_data(sales_data))

    print("\n=== Text Analysis ===")
    print(process_text_data(sample_text))

    print("\n=== Nested Data Transformation ===")
    print(transform_nested_structure(nested_data))

    print("\n=== User Interaction Analysis ===")
    print(analyze_user_interactions(user_logs))

# Practice Exercises:
"""
1. Extend the sales analysis to include:
   - Customer segmentation based on purchase frequency
   - Product recommendations based on purchase history
   - Seasonal trends analysis

2. Enhance the text processing to:
   - Find common phrases (3+ words)
   - Identify sentiment using a simple word-based approach
   - Generate word clouds (requires additional library)

3. Create a new function that:
   - Processes a nested JSON-like structure
   - Validates data types and formats
   - Applies transformations based on complex rules

4. Implement a cache system that:
   - Stores function results with timestamps
   - Handles cache invalidation
   - Supports different storage backends
"""
