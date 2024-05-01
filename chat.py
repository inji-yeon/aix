import json
import openai

def load_hermione_data(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as file:
            data = json.load(file)
        return data
    except FileNotFoundError:
        print("The data file was not found.")
        exit()
    except json.JSONDecodeError:
        print("Error decoding the JSON data.")
        exit()

def ask_hermione(question, hermione_info):
    try:
        openai_api_key = 'key'  # OpenAI API 키를 설정하세요.
        openai.api_key = openai_api_key

        # 캐릭터 정보를 설명하는 맥락적 텍스트 생성
        context = f"Hermione Granger is a Muggle-born witch known for her intelligence and diligence. She loves reading books and is very loyal to her friends. {json.dumps(hermione_info)}"

        # 대화식 프롬프트 구성
        prompt = f"{context}\n\nFriend: {question}\nHermione:"
        
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": prompt}
            ],
            max_tokens=150  # 최대 토큰 수 설정
        )
        return response['choices'][0]['message']['content'].strip()  # 반환된 텍스트에서 불필요한 공백 제거
    except Exception as e:
        print("An error occurred:", e)
        exit()

def main():
    hermione_data = load_hermione_data('hermione_granger_data.json')
    question = "Would you like to skip the class and go to dring butter beer?"
    response = ask_hermione(question, hermione_data)
    print("Hermione:", response)

if __name__ == "__main__":
    main()
