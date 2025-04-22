import streamlit as st

shop_list = ['渋谷半個室側', '渋谷個室側' , '上野店' , '秋葉原2階' , '秋葉原3階' , '新橋' , '新宿西' , '池袋' , '新宿東' , '学芸大学' , '飯田橋' , '銀座' , '八重洲' , '立川']

st.markdown("<h2 style='text-align: center;'>エアコン設定温度</h2>", unsafe_allow_html=True)
st.write('\n')

#店舗切替ボタン
selected_store = st.selectbox('店舗を選択',shop_list,index=0)

temp_max = st.slider("9時〜19時の最高気温（℃）", min_value=-10.0, max_value=50.0, value = 25, step=1)
temp_min = st.slider("9時〜19時の最低気温（℃）", min_value=-10.0, max_value=50.0, value = 20, step=1)
humidity_max = st.slider("9時〜19時の最高湿度（％）", 0, 100, 70)
humidity_min = st.slider("9時〜19時の最低湿度（％）", 0, 100, 50)
weather = st.selectbox("天気", ["晴れ", "曇り", "雨"])

def setting(tmax , tmin , hmax , hmin , adjust):
    haverage = (hmax + hmin)/2
    if tmin < 16:
        if weather == '晴れ':
            set_temperture = 22 + 0.1 * (15 - tmin) + 0.05 * (50- haverage) + adjust - 1.0
        elif weather == '曇り':
            set_temperture = 22 + 0.1 * (15 - tmin) + 0.05 * (50- haverage) + adjust - 0.5
        elif weather == '雨':
            set_temperture = 22 + 0.1 * (15 - tmin) + 0.05 * (50- haverage) + adjust + 0.5
        
        set_temperture = round(set_temperture , 1)
        st.markdown(
            f"""
            <div style="text-align: center;">
                <span style="font-size: 28px; font-weight: bold; color: green;">
                    暖房で {set_temperture}℃ に設定してください
                </span>
            </div>
            """,
            unsafe_allow_html=True
        )
    else:
        if weather == '晴れ':
            set_temperture = 26 - 0.1 * (tmax - 30) - 0.05 * (haverage - 50) - adjust - 1.0
        elif weather == '曇り':
            set_temperture = 26 - 0.1 * (tmax - 30) - 0.05 * (haverage - 50) - adjust - 0.5
        elif weather == '雨':
            set_temperture = 26 - 0.1 * (tmax - 30) - 0.05 * (haverage - 50) - adjust + 0.5
        
        set_temperture = round(set_temperture , 1)
        st.markdown(
            f"""
            <div style="text-align: center;">
                <span style="font-size: 28px; font-weight: bold; color: green;">
                    冷房で {set_temperture}℃ に設定してください
                </span>
            </div>
            """,
            unsafe_allow_html=True
        )


if selected_store == '渋谷半個室側':
    shibuya_half = setting(temp_max , temp_min , humidity_max , humidity_min , 0.5)
elif selected_store == '渋谷個室側':
    shibuya_personal = setting(temp_max , temp_min , humidity_max , humidity_min , 0)
elif selected_store == '上野店':
    ueno = setting(temp_max , temp_min , humidity_max , humidity_min , 1)
elif selected_store == '秋葉原2階':
    akihabara_2f = setting(temp_max , temp_min , humidity_max , humidity_min , 0)
elif selected_store == '秋葉原3階':
    akihabara_3f = setting(temp_max , temp_min , humidity_max , humidity_min , 0)
elif selected_store == '新橋':
    shinbashi = setting(temp_max , temp_min , humidity_max , humidity_min , 0)
elif selected_store == '新宿西':
    shinjyuku_west = setting(temp_max , temp_min , humidity_max , humidity_min , 1)
elif selected_store == '池袋':
    ikebukuro = setting(temp_max , temp_min , humidity_max , humidity_min , 0.5)
elif selected_store == '新宿東':
    shinjyuku_east = setting(temp_max , temp_min , humidity_max , humidity_min , 1)
elif selected_store == '学芸大学':
    gakugei = setting(temp_max , temp_min , humidity_max , humidity_min , 0.5)
elif selected_store == '飯田橋':
    iidabashi = setting(temp_max , temp_min , humidity_max , humidity_min , 0.5)
elif selected_store == '銀座':
    ginza = setting(temp_max , temp_min , humidity_max , humidity_min , 0.5)
elif selected_store == '八重洲':
    yaesu = setting(temp_max , temp_min , humidity_max , humidity_min , 0.5)
elif selected_store == '立川':
    tachikawa = setting(temp_max , temp_min , humidity_max , humidity_min , 1.0)
