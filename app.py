import streamlit as st
from app_home import run_app_home
from app_home import run_app_eda

def main() :
    
    st.title('자동차 가격 예측 앱')

    menu = ['Home', 'EDA', 'ML']
    st.sidebar.selectbox('메뉴', menu)

    if choice == 'Home' :
        run_app_home()
    if choice == 'EDA' :
        run_app_eda()
    if choice == 'ML' :
        pass




if __name__ == '__main__' :
    main()








