import streamlit as st
import uuid

# Set page config
st.set_page_config(page_title="TK Collection", layout="wide")

# Initialize session state
if "cart" not in st.session_state:
    st.session_state.cart = []

if "selected_product" not in st.session_state:
    st.session_state.selected_product = None

# Dummy product data with real fashion-style images
products = [
    {
        "id": "midnight-hoodie",
        "name": "Midnight Hoodie",
        "price": 49,
        "type": "Men",
        "colors": ["#000000", "#1a1a1a"],
        "image": "https://images.unsplash.com/photo-1618354691373-365b7d8efc70?auto=format&fit=crop&w=400&q=80",
        "description": "A sleek black hoodie for evening vibes."
    },
    {
        "id": "sunset-kurti",
        "name": "Sunset Kurti",
        "price": 39,
        "type": "Women",
        "colors": ["#ff5f6d", "#ffc371"],
        "image": "https://images.unsplash.com/photo-1620803361916-1735ef289df1?auto=format&fit=crop&w=400&q=80",
        "description": "A bright sunset colored kurti for all occasions."
    },
    {
        "id": "ocean-tee",
        "name": "Ocean Tee",
        "price": 25,
        "type": "Unisex",
        "colors": ["#006994", "#00bcd4"],
        "image": "https://images.unsplash.com/photo-1593032465171-8ee9d3d96f25?auto=format&fit=crop&w=400&q=80",
        "description": "A refreshing ocean blue t-shirt for summer."
    },
    {
        "id": "rose-gold-jacket",
        "name": "Rose Gold Jacket",
        "price": 89,
        "type": "Women",
        "colors": ["#b76e79", "#f7cac9"],
        "image": "https://images.unsplash.com/photo-1602810310473-265f60f2a06a?auto=format&fit=crop&w=400&q=80",
        "description": "Chic and elegant rose gold jacket."
    },
    {
        "id": "ice-grey-tracks",
        "name": "Ice Grey Tracks",
        "price": 35,
        "type": "Men",
        "colors": ["#dfe6e9", "#b2bec3"],
        "image": "https://images.unsplash.com/photo-1602810310310-e6a9b8bcd83e?auto=format&fit=crop&w=400&q=80",
        "description": "Comfortable grey tracks for everyday wear."
    }
]

# Search bar
search_query = st.text_input("🔍 Search for a product")

# Filter dropdown
filter_col = st.selectbox("Filter by:", ["All", "Men", "Women", "Unisex"])

# Filter and search products
filtered_products = [p for p in products if (filter_col == "All" or p["type"] == filter_col) and search_query.lower() in p["name"].lower()]

st.title("🧥 TK Collection")
st.subheader("Stylish clothing for every season")

# Product grid
cols = st.columns(3)
for i, product in enumerate(filtered_products):
    with cols[i % 3]:
        st.image(product["image"], use_column_width=True)
        st.write(f"### {product['name']}")
        st.write(f"💲 {product['price']}")
        if st.button("🛒 Add to Cart", key=f"cart-{product['id']}"):
            st.session_state.cart.append(product)
            st.success(f"Added {product['name']} to cart!")
        if st.button("View Details", key=f"view-{product['id']}"):
            st.session_state.selected_product = product

# Product detail view
if st.session_state.selected_product:
    product = st.session_state.selected_product
    st.markdown("---")
    st.image(product["image"], width=250)
    st.markdown(f"## {product['name']}")
    st.write(product["description"])
    st.write(f"**Price:** ${product['price']}")
    if st.button("🛒 Add to Cart (Detail)", key="detail-cart"):
        st.session_state.cart.append(product)
        st.success("Added to cart!")

# Show cart
with st.expander("🛍️ View Cart"):
    if st.session_state.cart:
        total = 0
        for item in st.session_state.cart:
            st.write(f"- {item['name']} - ${item['price']}")
            total += item['price']
        st.markdown(f"**Total: ${total}**")
    else:
        st.info("Your cart is empty.")
        

