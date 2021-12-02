from util import  trigram_dic
import streamlit as st



st.write("Tri-gram  autocomplete")

k = st.text_input("Enter your text","")

s = k.split()

if len(s)<2:
    st.write(k)
 
else:
    q = s[-2]+'_'+s[-1]

    try:
        l = trigram_dic[q]
        l = sorted(l.items(), key=lambda item: item[1],reverse=True)
        
        for i in range(5):
            out = f"{l[i][0]} : {l[i][1]}\n" 
            st.write(out)       

    except Exception:
        st.write(k)


