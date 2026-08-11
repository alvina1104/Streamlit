import streamlit as st
import time

st.title("Эффекттер жана Статустар")

if st.button('Процессти баштоо'):
    # 1. st.toast - Оң жак төмөнкү бурчта кичинекей билдирүү чыгат
    st.toast('Иш башталды!', icon='🚀')

    # 2. st.spinner - Жүктөлүп жаткан анимация (контейнердин ичинде)
    with st.spinner('Сураныч, күтө туруңуз...'):
        # 3. st.progress - Прогресс тилкеси
        bar = st.progress(0)
        for percent_complete in range(100):
            time.sleep(0.02)
            bar.progress(percent_complete + 1)

    # 4. st.success - Ийгиликтүү аяктаганда чыгуучу билдирүү
    st.success('Баары даяр!')

    # 5. st.balloons - Шарларды учуруу
    st.balloons()

    # 6. st.snow - Кар жаадыруу
    st.snow()

# st.toast өзүнчө да иштете берсе болот
if st.button('Билдирүүнү көрүү'):
    st.toast('Бул кыска мөөнөттүү билдирүү!', icon='🔔')