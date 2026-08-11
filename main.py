import streamlit as st


with st.sidebar:
    word = st.radio('Options',['Registration','Calculator','Palindrome','Questionnaire'])

if word == 'Registration':
    st.title('Registration')
    name = st.text_input('Name')
    email = st.text_input('Email')
    age = st.number_input('Age')
    description = st.text_input('Description')


    if st.button('Registration'):
        st.text(f'Hello {name}!')


elif word == 'Calculator':
    st.title('Calculator')
    num1 = st.number_input('First Number')
    num2 = st.number_input('Second Number')
    sign = st.radio('Sign',['+','-','*','/'])

    if st.button('='):
        if sign == '+':
            st.write(num1+num2)
        elif sign == '-':
            st.write(num1-num2)
        elif sign == '*':
            st.write(num1*num2)
        elif sign == '/':
            st.write(num1/num2)


elif word == 'Palindrome':
    st.title('Palindrome')

    word = st.text_input('Check word')

    if st.button('Palindrome'):
        if word == word[::-1]:
            st.write('Palindrome')
        else:
            st.write('Not a palindrome')


if word == 'Questionnaire':
    st.title('Questionnaire')
    name = st.text_input('Name')
    email = st.text_input('Email')
    age = st.number_input('Age',min_value=18,max_value=100)
    description = st.text_area('Description')
    photo = st.file_uploader('Upload photo')


    if st.button('Registration'):
        if age > 18:
            st.info(f'You are {age} years old')
        else:
            st.error(f'You are under {age} years old')


        if photo is not None:
            st.image(photo)
        st.text(f'Hello {name}!')











