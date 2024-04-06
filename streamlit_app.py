import streamlit as st
import pandas as pd

def clean_emails(df1, df2):
    # Předpokládá se, že emaily jsou v sloupci 'Email' v obou dataframe
    df1.columns = df1.columns.str.strip().str.lower()
    df2.columns = df2.columns.str.strip().str.lower()
    cleaned_df = df1[~df1['email'].isin(df2['email'])]
    return cleaned_df

def main():
    st.title("✂️ Email Contacts Excluder")
    st.write("Both files should have a column in a format 'Email', otherwise it will not work.")

    # Nahrání souborů uživatelem
    uploaded_file1 = st.file_uploader("Nahrajte první CSV soubor s kontakty:", type="csv")
    uploaded_file2 = st.file_uploader("Nahrajte druhý CSV soubor s existujícími klienty/kontakty, které chcete excludovat:", type="csv")

    if uploaded_file1 and uploaded_file2:
        # Načtení CSV souborů
        list1 = pd.read_csv(uploaded_file1)
        list2 = pd.read_csv(uploaded_file2)
        
        # Kontrola, zda oba soubory obsahují sloupec 'Email'
        if 'Email' not in list1.columns or 'Email' not in list2.columns:
            st.error("Jeden nebo oba soubory nemají sloupec 'Email'. Prosím, zkontrolujte CSV soubory.")
        else:
            # Vyčištění seznamu
            cleaned_list = clean_emails(list1, list2)
            
            # Umožnění uživateli stáhnout výsledný CSV soubor
            st.write("Vyčištěný seznam kontaktů:")
            st.dataframe(cleaned_list)
            csv = cleaned_list.to_csv(index=False).encode('utf-8')
            st.download_button("Stáhnout vyčištěné kontakty jako CSV", csv, "cleaned_contacts.csv", "text/csv", key='download-csv')

if __name__ == "__main__":
    main()
