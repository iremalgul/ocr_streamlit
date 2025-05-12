import streamlit as st
from pdf2image import convert_from_path
import pytesseract
from PIL import Image
import tempfile

# Başlık
st.title("📄 PDF OCR ile Metin Çıkarma ve Analiz")

# Dosya yükleme alanı
uploaded_file = st.file_uploader("Bir PDF dosyası yükle", type="pdf")

# Dosya yüklendiğinde
if uploaded_file is not None:
    st.success("Dosya başarıyla yüklendi!")
    
    # Geçici bir dosya oluşturup, yüklenen PDF'i kaydediyoruz
    with tempfile.NamedTemporaryFile(delete=False) as temp_file:
        temp_file.write(uploaded_file.read())
        temp_file_path = temp_file.name

    # PDF'i görsele çevir
    images = convert_from_path(temp_file_path, 300)
    
    # Her bir sayfayı OCR ile işle
    extracted_text = ""
    for i, image in enumerate(images):
        st.image(image, caption=f"Sayfa {i+1}", use_container_width=True)  # Sayfayı göster
        
        # OCR ile metni çıkart
        page_text = pytesseract.image_to_string(image)
        extracted_text += f"--- Sayfa {i+1} ---\n{page_text}\n\n"
    
    # Çıkarılan metni göster
    st.subheader("Çıkarılan Metin")
    st.text_area("OCR Sonucu", extracted_text, height=300)

else:
    st.info("Lütfen bir PDF dosyası yükleyin.")
