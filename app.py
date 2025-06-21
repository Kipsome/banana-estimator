import streamlit as st
from PIL import Image
import random

st.set_page_config(page_title="Banana Estimator AI v2", layout="centered")

st.title("🍌 Banana Price Estimator (YOLOv8 AI)")
st.write("Upload a photo of bananas and enter a price reference to estimate total cost.")

image = st.file_uploader("Upload an image of bananas", type=["jpg", "png", "jpeg"])
ref_count = st.number_input("How many bananas cost how much?", min_value=1)
ref_price = st.number_input("Total price for that number (KSh)", min_value=1)

if image and ref_count and ref_price:
    img = Image.open(image)
    st.image(img, caption="Uploaded Image", use_column_width=True)

    # Simulated YOLO banana count (placeholder)
    detected_bananas = random.randint(8, 15)
    price_per_banana = ref_price / ref_count
    total_estimate = int(price_per_banana * detected_bananas)

    st.success(f"✅ AI Detected: {detected_bananas} bananas")
    st.info(f"💰 Estimated Total: KSh {total_estimate}")
    st.caption("⚠️ Real YOLO model integration coming next!")
