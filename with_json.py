import json
import openai
import streamlit as st

api_key = st.secrets["OPENAI_API_KEY"]

st.set_page_config(page_title="Letter from Hermione", page_icon="✉️")
st.title("✉️ Letter from Hermione")

def load_hermione_data(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as file:
            data = json.load(file)
        return data
    except FileNotFoundError:
        st.error("The data file was not found.")
        st.stop()
    except json.JSONDecodeError:
        st.error("Error decoding the JSON data.")
        st.stop()

def ask_hermione(letter, hermione_info):
    try:
        # 캐릭터 정보를 설명하는 맥락적 텍스트 생성
        context = f"Hermione Granger is a Muggle-born witch known for her intelligence and diligence. She loves reading books and is very loyal to her friends. {json.dumps(hermione_info)}"

        # 편지에 대한 답장 형식 구성
        prompt = f"{context}\n\nDear Hermione,\n{letter}\n\nSincerely,\nA Friend\n\nHermione's response:"

        openai.api_key = api_key
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": prompt}
            ],
            max_tokens=150  # 최대 토큰 수 설정
        )
        return response['choices'][0]['message']['content'].strip()  # 반환된 텍스트에서 불필요한 공백 제거
    except Exception as e:
        st.error("An error occurred: " + str(e))
        st.stop()

def main():
    hermione_data = load_hermione_data('hermione_granger_data.json')

    # 사용자 입력 텍스트 영역
    letter = st.text_area("Write a letter to Hermione:", height=250)

    if st.button('Send Letter'):
        if not letter:
            st.warning('Please write something in the letter.')
        else:
            response = ask_hermione(letter, hermione_data)
            st.write("Hermione's response:")
            st.write(response)

if __name__ == "__main__":
    main()
