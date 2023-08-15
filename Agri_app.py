import streamlit as st
import numpy as np
from PIL import Image
import pickle


def main():
    # Categorical inputs

    image = Image.open('images.jpg')
    st.title("AGRIGRAVITY TECHNOLOGIES PRIVATE LIMITED")

    st.image(image, caption=f"AGRIGRAVITY TECHNOLOGIES PRIVATE LIMITED", use_column_width=True)

    st.sidebar.subheader(""" Agrigravity Technologies Private Limited is a Private incorporated on 26 February 2022. It is classified as Non-govt company and is registered at Registrar of Companies, Jaipur. Its authorized share capital is Rs. 1,500,000 and its paid up capital is Rs. 200,000. It is inolved in Other computer related activities [for example maintenance of websites of other firms/ creation of multimedia presentations for other firms etc.]

Agrigravity Technologies Private Limited's Annual General Meeting (AGM) was last held on N/A and as per records from Ministry of Corporate Affairs (MCA), its balance sheet was last filed on N/A.

Directors of Agrigravity Technologies Private Limited are Sameer Lodha and Hemendra Kumar Lodha.

Agrigravity Technologies Private Limited's Corporate Identification Number is (CIN) U72900RJ2022PTC079892 and its registration number is 79892.Its Email address is sameerlodha07@gmail.com and its registered address is 106/127, Agrawal farm Mansarovar Jaipur Jaipur RJ 302020 IN """)
    st.sidebar.write("Ravi Ranjan ", "\n", "Chairman & CEO")
    st.sidebar.subheader('Contact Us.  \n'
                         'Email:-  ranjeet.suri241@gmail.com')

    st.sidebar.subheader("+91 75491 19745")

    st.subheader("Price Analysis of Commodities with ")
    list = ["Chosse an option", "Quality & Location", "Quality,Location,Date & Commodity"]
    suri = st.selectbox(" ", list)

    var1 = {'Coriander Seeds Eagle,GST & Freight extra at actual': 62,
            'Coriander Seeds Badami,GST & Freight extra at actual': 61, 'Singapore 99': 140,
            'Turmeric powder Curcumin content- around 3 % Moisture- less than5%': 171, 'Teja Stem': 163,
            'Teja stem less': 165, 'Teja Stem Cut': 164, 'Sannam with stem': 133, 'Sannam stem less': 132,
            'Syngenta Bydigi Stem': 153, 'Syngenta Bydigi Stem less': 154, '1.5 % Powder': 2, '2 % Powder': 5,
            '2.5 Powder': 8, '3 % Powder': 11, 'Yellow Powder': 188, 'Orange Powder': 113, 'Chilli Flakes (Low)': 43,
            'Chilli Flakes (Medium)': 44, 'Chilli Flakes (Reguler)': 45, 'Chilli Flakes (Deluxe)': 42,
            'M Lower (M Lower)': 106, 'Medium Grade': 107, 'Chilli Powder Lower Grade': 52,
            'Chilli Powder Medium Lower': 53, 'CHILLI POWDER (60 ASTA / 70k SHU )': 32,
            'CHILLI POWDER (60 ASTA / 30k SHU)': 31, 'Dehydrated Red Chilli powder': 75, 'Dehydrated Cumin powder': 74,
            '1%': 1, '1.50%': 4, '2%': 6, '2.50%': 10, '3%': 12, '4%': 14, '5%': 15,
            'Turmeric powder best quality': 172, 'Chilli powder': 55, 'Chilli flake': 54, 'Turmeric finger': 170,
            'Coriander seeds': 64, 'Coriander powder': 63, 'Cumin Seeds Singapore 99': 71, 'Cumin Seeds Powder': 70,
            'Turmeric Finger Selum': 168, 'Bulb Selum Premium Export Quality': 30, 'Eagle': 85, 'Eagle plus': 92,
            'Scooter': 134, 'Scooter plus': 138, 'Single parrot': 145, 'Double polished turmeric finger + Gst': 81,
            'Farmers Grade': 96, 'Domestic Quality': 78, 'Quality Scooter': 115,
            'Turmeric powder,Curcumin content- 1%': 173, 'Turmeric powder,Curcumin content- 1.5%': 174,
            'Turmeric powder,Curcumin content- 2%': 175, 'Turmeric powder,Curcumin content- 2.5%': 176,
            'Turmeric powder,Curcumin content- 3%': 177, 'Turmeric powder,Curcumin content- 4%': 178,
            'Turmeric powder,Curcumin content- 5%': 179, 'Chilli Powder (Kashmiri)': 50, 'Chilli Powder (A Grade)': 46,
            'Chilli Powder (B Grade)': 47, 'Chilli Powder (C Grade)': 48, 'Chilli Powder (D Grade)': 49,
            'Chilli Powder (Russia Grade)': 51, 'Cumin Powder (Premium)': 67, 'Cumin Powder (Medium)': 66,
            'Cumin Powder (Regular)': 68, 'Cumin Powder (Low)': 65, 'Coriander Powder (Premium)': 59,
            'Coriander Powder (Medium)': 58, 'Coriander Powder (Regular)': 60, 'Coriander Powder (Low)': 57,
            'SANIYA SUPER DELUX WITH STEM': 130, 'SANIYA SUPER DELUX WITHOUT STEM': 131,
            'REVA SUPER DELUX WITH STEM': 122, 'PUNJAB AVERAGE BEST WITH STEM': 114,
            'WONDERHOT SUPER DELUX WITH STEM': 186, 'WONDERHOT SINGAL PATTI WITH STEM': 185,
            'TURMARIC NIZAMABAD DOUBLE POLICE GATHA': 157, 'TURMARIC SALEM SINGAL POLICE FALI': 158,
            'TURMARIC NIJAMABAD DOUBLE POLICE': 155, 'Extra bold + 5% GST': 95, 'Diamond + 5% GST': 77,
            'Bombay bold + 5% GST': 29, 'Jupiter + 5% GST': 101, 'Vivo + 5% GST': 180, 'Bold Eagle + 5% GST': 24,
            'Bold Eagle plus + 5% GST': 25, 'Bold Scooter + 5% GST': 26, 'Bold Scooter plus + 5% GST': 27,
            'Bold Diamond + 5% GST': 23, 'Bold Singal parrot + 5% GST': 28, 'Split Eagle + 5% GST': 150,
            'Split Eagle plus + 5% GST': 151, 'Split Scooter + 5% GST': 152, 'Small Eagle plus(royal) + 5% GST': 146,
            'Small Scooter (seven star)+ 5% GST': 147, 'Small Single parrot (ever green) + 5% GST': 148,
            'Badami loose': 21, 'Eagle loose': 91, 'Scooter loose': 137, 'Double parrot and extra green': 80,
            'Dal(Eagle)': 73, 'Eagle + GST': 86, 'SANIYA SUPER DELUX STEMLESS': 129, 'REVA SUPER DELUX WITH STEAM': 121,
            'WONDERHOT PLAIN DOUBLE PATTA DELUX WITH STEM': 182, 'WONDERHOT SINGAL PATTA WITH STEM': 184,
            'TURMARIC NIZAMABAD DOUBLE POLICE': 156, 'SALEM SINGAL POLICE': 126, 'NIZAMABAD GATTHA DOUBLE POLICE': 111,
            'AADITYA 501 IROD GATTHA': 17, 'CUMIN POWDER': 38, 'CORIANDER POWDER': 35, 'TURMERIC POWDER': 159,
            'RED CHILLY POWDER KASHMIR': 116, 'RED CHILLY POWDER REGULAR': 118, 'RED CHILLY POWDER TEJA': 119,
            'RED CHILLY POWDER LOWEST': 117, 'Singapore 99.00%': 141, 'Singapore 99.50%': 142, 'Europe': 94,
            'Eagle Sortex': 89, 'Split': 149, 'Single Parrot': 143, 'GOOD GRADE': 97, 'EUROPE': 84, 'BULB': 19,
            'Yellow 1%': 187, 'Orange 1%': 112, 'Badami': 20, 'A grade': 16, 'Kashmiri red chilli': 104,
            'Tikhala chilli powder (diamond)': 166, 'Tikhala chilli powder (platinum)': 167,
            'CORIANDER EAGLE MACHINE': 33, 'CORIANDER EAGLE SORTEX': 34, 'CORIANDER SCOOTER': 36,
            'CORIANDER SINGLE PARROT': 37, 'CUMIN-JEERA SINGA-PORE 99': 41, 'CUMIN-JEERA EUROPE 99': 40,
            'CUMIN-JEERA BOLD': 39, 'NIZAMABAD DOUBLE POLICE': 108, 'SALAM FALI VASHNAVI 108 BRAND': 124,
            'NIZAMABAD GATHHA DOUBLE POLICE': 110, 'SALEM GATHHA': 125, 'saniya deluxe': 190, 'Eagle Split': 90,
            'Eagle Machine Clean': 87, 'Scooter Machine Clean': 135, 'Cumin Seeds': 69, 'singapor-99.99': 191,
            'europe quality': 189, 'third grade': 192, 'Eagle+': 93, 'Dry Chilli Powder': 82, 'Turmeric Powder': 169,
            'Coriander Powder': 56, 'Kashmiri Mirch Powder': 103, 'Bedgi Mirch': 22, 'Kashmiri Mirch': 102,
            'Lavangi Mirch': 105, 'Dhaniya(Coriander)': 76, 'Dry Red Chilli with stem,Deluxe Quality': 83,
            'NIZAMABAD DOUBLE POLISH': 109, 'Selam Finger': 139, 'Teja': 160, 'Akha Rai': 18, 'Eagle Plus': 88,
            'Scooter Plus': 136, '1 % CURCUMIN': 0, '1.5% CURCUMIN': 3, '2% CURCUMIN': 7, '2.5% CURCUMIN': 9,
            '3% CURCUMIN': 13, 'Single Polished, around 5% CURCUMIN': 144, 'Double Polished, around 5% CURCUMIN': 79,
            'Teja S-17 with Stem': 161, 'Teja S-17 with Stem (deluxe)': 162, 'Red Chilli powder': 123,
            'Cumin powder': 72, 'SANIYA SUP DEL.WITH STEM': 127, 'SANIYA SUP.DEL.WITHOUT STEM': 128,
            'REVA SUP.DEL.WITH STEM': 120, 'WONDERHOT DOUBLE PATTA SUPER DELUX WITH STEM': 181,
            'WONDERHOT SINGAL PATTA DELUX WITH STEM': 183, 'Haldi Nizamabad gulab brand': 99,
            'Haldi Salem singal polish': 100, 'Haldi GATHHA police': 98}
    var2 = {'Pratapgarh(Rajasthan)': 16, 'Sangli(Maharashtra)': 20, 'Guntur(Andhra Pradesh)': 6,
            'Unjha / Mundra Delivery': 23, 'Kanpur(Uttar Pradesh)': 8, 'Shirdi(Maharashtra)': 21, 'Baroda(Gujarat)': 0,
            'Nanded(Maharashtra)': 14, 'Rajkot(Gujarat)': 18, 'Behrampur(Odissa)': 2, 'Madhavpur(Gujarat)': 11,
            'Unjha(Gujarat)': 24, 'Mundra-port(Gujarat)': 13, 'Deesa(Gujarat)': 3, 'Jodhpur(Rajasthan)': 7,
            'Ramganj-Mandi(Rajasthan)': 19, 'Udaipur(Rajasthan)': 22, 'Kota(Rajasthan)': 10, 'Kolkata(West Bengal)': 9,
            'Malad East': 12, 'Orissa': 15, 'Gondal (Gujarat)': 4, 'Behrampur(Odisha)': 1, 'Guntur': 5, 'Raipur': 17}
    var3 = {'14-Jul': 0, '15-Jul': 1, '17-Jul': 2, '18-Jul': 3, '19-Jul': 4, '20-Jul': 5, '21-Jul': 6, '22-Jul': 7,
            '24-Jul': 8, '25-Jul': 9, '26-Jul': 10, '27-Jul': 11, '28-Jul': 12, '29-Jul': 13, '31-Jul': 14, '9-Aug': 15}
    var4 = {'Coriander': 0, 'Cumin seeds': 1, 'Turmeric': 3, 'Dry Chilli': 2}

    def get_value(val, my_dict):
        for key, value in my_dict.items():
            if val == key:
                return value

    def load_model(model_file):
        model = pickle.load(open(model_file, "rb"))
        return model

    if suri:
        if suri == "Quality & Location":
            st.subheader("Welcome to Prediction Price")
            location = st.selectbox("Location", tuple(var2.keys()))
            quality = st.selectbox("Quality", tuple(var1.keys()))

            if st.button("Predict Price"):
                feature_list = [get_value(location, var2),
                                get_value(quality, var1)]
                # st.write(feature_list)
                st.subheader("Your Input")
                user_input_data = {"Location": location,
                                   "Quality": quality}

                st.write(user_input_data)
                st.subheader("Predicted Price (Per KG)")
                data = np.array(feature_list).reshape(1, -1)
                model = load_model("final_model.pkl")
                prediction = model.predict(data)
                st.write("Predicted Price (Per KG) :" + " " + "₹" + " " + str(np.round(prediction[0], 2)))

                st.subheader(''' Thank you for your visit !''')

        if suri == "Quality,Location,Date & Commodity":
            location = st.selectbox("Location", tuple(var2.keys()))
            quality = st.selectbox("Quality", tuple(var1.keys()))
            date = st.selectbox("Date", tuple(var3.keys()))
            commodity = st.selectbox("Commodity", tuple(var4.keys()))
            if st.button("Predict Price"):
                feature_list = [get_value(location, var2),
                                get_value(quality, var1),
                                get_value(date, var3),
                                get_value(commodity, var4)]
                # st.write(feature_list)
                st.subheader("Your Input")
                user_input_data = {"Location": location,
                                   "Quality": quality,
                                   "Date": date,
                                   "Commodity": commodity}

                st.write(user_input_data)
                st.subheader("Predicted Price (Per KG)")
                data = np.array(feature_list).reshape(1, -1)
                model = load_model("final_model4.pkl")
                prediction = model.predict(data)
                st.write("Predicted Price (Per KG) :" + " " + "₹" + " " + str(np.round(prediction[0], 2)))

                st.subheader(''' Thank you for your visit !''')


if __name__ == "__main__":
    main()
