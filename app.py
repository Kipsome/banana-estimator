import streamlit as st
from PIL import Image, ImageDraw
import random

st.set_page_config(page_title="Banana Estimator AI (Simulated YOLO)", layout="centered")

st.title("🍌 Banana Price Estimator (Simulated AI)")
st.write("Upload a banana image, and get a count & cost estimate based on visual detection.")

image_file = st.file_uploader("Upload a banana image", type=["jpg", "jpeg", "png"])
ref_count = st.number_input("How many bananas cost this much?", min_value=1)
ref_price = st.number_input("Total price (KSh) for that number", min_value=1)

def draw_fake_boxes(image, count=8):
    draw = ImageDraw.Draw(image)
    width, height = image.size
    for _ in range(count):
        x1 = random.randint(0, width - 100)
        y1 = random.randint(0, height - 100)
        x2 = x1 + random.randint(40, 100)
        y2 = y1 + random.randint(80, 150)
        draw.rectangle([x1, y1, x2, y2], outline="red", width=3)
    return image

if image_file and ref_count and ref_price:
    image = Image.open(image_file).convert("RGB")
    banana_count = random.randint(8, 14)
    image_with_boxes = draw_fake_boxes(image.copy(), banana_count)

    st.image(image_with_boxes, caption=f"Detected bananas: {banana_count}", use_column_width=True)

    price_per_banana = ref_price / ref_count
    total_price = round(price_per_banana * banana_count)

    st.success(f"✅ Estimated bananas: {banana_count}")
    st.info(f"💰 Estimated price: KSh {total_price}")
    st.caption("🧠 Detection is simulated. Real AI version coming soon!")
