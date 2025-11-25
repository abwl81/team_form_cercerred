import streamlit as st
import pandas as pd
import os

FILE_PATH = "members_data.xlsx"

st.set_page_config(page_title="فرم ثبت اطلاعات اعضا",
                   page_icon="📝", layout="centered")

st.title("📋 فرم ثبت‌نام اعضا")

st.markdown(
    "لطفاً اطلاعات خود را وارد کنید. پر کردن گزینه «درجه امدادگری» اختیاری است.")

# --- فیلدها ---
full_name = st.text_input("نام و نام خانوادگی", placeholder="مثلاً علی رضایی")
phone = st.text_input("شماره تماس", placeholder="09xxxxxxxxx")
major = st.text_input("رشته تحصیلی", placeholder="مثلاً مهندسی صنایع")
rank = st.text_input("درجه امدادگری (اختیاری)", placeholder="در صورت وجود...")
num_tim = st.text_input("شماره تیم خودرا وارد کنید :", placeholder="7")

# --- دکمه ثبت ---
if st.button("📨 ثبت اطلاعات"):
    if not full_name or not phone or not major or not num_tim:
        st.error("⚠️ لطفاً فیلدهای ستاره‌دار را کامل پر کنید.")
    else:
        new_data = pd.DataFrame([{
            "نام و نام خانوادگی": full_name,
            "شماره تماس": phone,
            "رشته تحصیلی": major,
            "درجه امدادگری": rank,
            "شماره تیم": num_tim
        }])
        if os.path.exists(FILE_PATH):
            old_data = pd.read_excel(FILE_PATH)
            combined = pd.concat([old_data, new_data], ignore_index=True)
        else:
            combined = new_data

        combined.to_excel(FILE_PATH, index=False)
        st.success("✅ اطلاعات شما با موفقیت ثبت شد. سپاس از همکاری شما!")
