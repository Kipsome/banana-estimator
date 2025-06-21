import streamlit as st

st.set_page_config(page_title="Banana Estimator AI", layout="centered")

st.title("🍌 Banana Price Estimator")
st.write("Upload a photo of bananas and enter a price reference to estimate total cost.")

# Upload photo
image = st.file_uploader("Upload an image of bananas", type=["jpg", "png", "jpeg"])

# Input pricing logic
ref_count = st.number_input("How many bananas?", min_value=1)
ref_price = st.number_input("What is the price (KSh) for that number?", min_value=1)

# Simulate detection
if image and ref_count and ref_price:
    # For now, fake count = 12 bananas
    detected_count = 12
    est_price = int((ref_price / ref_count) * detected_count)

    st.image(image, caption="Uploaded image", use_column_width=True)
    st.success(f"✅ Estimated count: {detected_count} bananas")
    st.info(f"💰 Estimated price: KSh {est_price}")
