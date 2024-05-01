import openai
import streamlit as st

# API 키 설정
api_key = st.secrets["OPENAI_API_KEY"]

# Streamlit 페이지 설정
st.set_page_config(page_title="Letter from Hermione", page_icon="✉️")
st.title("✉️ Letter from Hermione")

# Hermione에게 편지를 보내고 답장을 생성
def generate_response(letter):
    try:
        context = "Hermione Granger is a character from the Harry Potter series known for her intelligence, loyalty, and resourcefulness."
        openai.api_key = api_key
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": context},
                {"role": "user", "content": letter}
            ],
            max_tokens=300
        )
        return response['choices'][0]['message']['content'].strip()  # 답장에서 불필요한 공백 제거
    except Exception as e:
        st.error("An error occurred while generating the response: " + str(e))
        st.stop()

def main():
    # 사용자 입력 텍스트 영역
    letter = st.text_area("Write a letter to Hermione:", height=250)

    if st.button('Send Letter'):
        if not letter:
            st.warning('Please write something in the letter.')
        else:
            response = generate_response(letter)
            st.write("Hermione's response:")
            st.write(response)

if __name__ == "__main__":
    main()
