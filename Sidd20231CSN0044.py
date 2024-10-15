import random
import nltk
from nltk.stem import WordNetLemmatizer

nltk.download('punkt')
nltk.download('wordnet')

lemmatizer = WordNetLemmatizer()

#  Amazon Virtual Shopping Assistant 🤖🛒
# The Amazon Virtual Shopping Assistant helps customers with common tasks like tracking orders, finding products, handling returns, and more. It offers quick and accurate responses to your queries, ensuring a smooth and efficient shopping experience. Whether you need help with payment, shipping, or product recommendations, this assistant is here to support you 24/7.
intents = {
    "intents": [
        {"tag": "greeting",
         "patterns": ["Hi", "Hello", "Hey", "Good morning", "Good afternoon"],
         "responses": ["Hello! How can I assist you today?", "Hi there, welcome to Amazon!"]},
        {"tag": "goodbye",
         "patterns": ["Bye", "Goodbye", "See you later"],
         "responses": ["Goodbye! Have a great day!", "Thanks for visiting Amazon!"]},
        {"tag": "thanks",
         "patterns": ["Thanks", "Thank you", "That’s helpful"],
         "responses": ["You’re welcome!", "Glad to assist!"]},
        {"tag": "product_inquiry",
         "patterns": ["What products do you have?", "Tell me about your products", "Show me products"],
         "responses": ["We have electronics, clothing, home goods, and more. What are you looking for?"]},
        {"tag": "order_status",
         "patterns": ["Where is my order?", "Track my order", "Order status"],
         "responses": ["Please provide your order ID to check the status."]},
        {"tag": "return_policy",
         "patterns": ["What's your return policy?", "Can I return this?", "Return process"],
         "responses": [
             "You can return most items within 30 days of receiving them. Check the product page for return details."]},
        {"tag": "payment_methods",
         "patterns": ["What payment methods do you accept?", "How can I pay?", "Do you accept PayPal?"],
         "responses": ["We accept credit/debit cards, PayPal, UPI, Amazon Pay, and more."]},
        {"tag": "cancel_order",
         "patterns": ["How do I cancel my order?", "Cancel my order", "Can I cancel this order?"],
         "responses": [
             "You can cancel your order if it hasn't been shipped. Visit the 'My Orders' page to manage your orders."]},
        {"tag": "shipping_info",
         "patterns": ["When will my order arrive?", "Shipping time", "Delivery time"],
         "responses": ["Delivery typically takes 3-5 business days. Expedited options are also available."]},
        {"tag": "prime_membership",
         "patterns": ["What is Amazon Prime?", "How do I join Prime?", "Prime benefits"],
         "responses": [
             "Amazon Prime offers fast shipping, exclusive deals, and access to Prime Video. Would you like to join?"]},
        {"tag": "prime_benefits",
         "patterns": ["What are the benefits of Prime?", "Why should I join Prime?", "Prime perks"],
         "responses": ["Prime members enjoy free shipping, access to Prime Video and Music, and exclusive discounts."]},
        {"tag": "refund",
         "patterns": ["How do I get a refund?", "Refund process", "I want a refund"],
         "responses": ["Refunds are processed within 3-5 business days once we receive your returned item."]},
        {"tag": "best_sellers",
         "patterns": ["Show me best sellers", "What are the best-selling products?", "Top products"],
         "responses": ["Check out our Best Sellers section for the most popular products across all categories."]},
        {"tag": "order_modify",
         "patterns": ["Can I change my order?", "Modify my order", "Change order details"],
         "responses": [
             "You can modify your order before it has been shipped. Visit the 'My Orders' section to manage it."]},
        {"tag": "delivery_charge",
         "patterns": ["What is the delivery charge?", "How much is shipping?", "Do I need to pay for delivery?"],
         "responses": ["Delivery charges vary by location. Prime members enjoy free delivery on most items."]},
        {"tag": "damaged_item",
         "patterns": ["I received a damaged item", "My product is broken", "Received a faulty item"],
         "responses": [
             "We're sorry for the inconvenience. Please start a return or contact our support for assistance."]},
        {"tag": "track_package",
         "patterns": ["Track my package", "Where is my package?", "Track shipment"],
         "responses": ["Please provide your tracking number or order ID, and we’ll give you an update."]},
        {"tag": "wishlist",
         "patterns": ["How do I add to my wishlist?", "Save items to wishlist", "Where is my wishlist?"],
         "responses": [
             "You can add items to your wishlist by clicking the 'Add to Wishlist' button on the product page."]},
        {"tag": "customer_support",
         "patterns": ["I need to talk to support", "Contact support", "Help with customer service"],
         "responses": ["You can reach our support team via chat, email, or phone. How can I assist you further?"]}
    ]
}

# Sample product database with 10+ products, prices, and stock information
products = {
    "laptop": {"price": 799.99, "stock": 10, "delivery_time": "3-5 business days"},
    "smartphone": {"price": 599.99, "stock": 15, "delivery_time": "2-3 business days"},
    "headphones": {"price": 199.99, "stock": 20, "delivery_time": "3-5 business days"},
    "smartwatch": {"price": 299.99, "stock": 8, "delivery_time": "2-3 business days"},
    "tablet": {"price": 499.99, "stock": 12, "delivery_time": "3-5 business days"},
    "gaming_console": {"price": 399.99, "stock": 5, "delivery_time": "5-7 business days"},
    "camera": {"price": 999.99, "stock": 4, "delivery_time": "3-5 business days"},
    "tv": {"price": 1199.99, "stock": 6, "delivery_time": "5-7 business days"},
    "bluetooth_speaker": {"price": 149.99, "stock": 18, "delivery_time": "3-5 business days"},
    "keyboard": {"price": 89.99, "stock": 25, "delivery_time": "2-3 business days"},
    "mouse":{"price":599,"stock":23,"delivery_time":"2-3 business days"},
    "shooes":{"price":1499,"stock":10,"delivery_time": "3-4 business days"},
    "beatbox":{"price":3000,"stock":10,"delivery_time": "3-4 businees days"},

    }




def clean_up_sentence(sentence):
    sentence_words = nltk.word_tokenize(sentence)
    return [lemmatizer.lemmatize(word.lower()) for word in sentence_words]



def get_response(user_input):
    for intent in intents['intents']:
        for pattern in intent['patterns']:
            if user_input.lower() in pattern.lower():
                return random.choice(intent['responses'])
    return "I don't understand your query. Can you please rephrase?"


# Function to check product details
def product_query():
    product_list = ", ".join(products.keys())
    print(f"We have the following products available: {product_list}.")

    product_name = input("Which product would you like to know about? ").lower()

    if product_name in products:
        product_info = products[product_name]
        return (f"The price of {product_name} is ${product_info['price']:.2f}. "
                f"It will be delivered in {product_info['delivery_time']}. "
                f"{'In stock!' if product_info['stock'] > 0 else 'Currently out of stock!'}")
    else:
        return "Sorry, we don't have that product. Please choose from the available products."


# Function to simulate order tracking
def track_order():
    order_id = input("Please provide your order ID: ")
    return f"Your order {order_id} is on its way! Expected delivery is in 3-5 business days."


 
print("Amazon Bot is running! Type 'exit' to stop.")

while True:
    message = input("You: ")
    if message.lower() == 'exit':
        print("Bot: Goodbye! 🙋‍♂️")
        break

    if "buy" in message.lower() or "product" in message.lower() or "order" in message.lower():
        response = product_query()
    elif "track" in message.lower() or "order status" in message.lower():
        response = track_order()
    else:
        response = get_response(message)

    print(f"Bot: {response}")
