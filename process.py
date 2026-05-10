import json
import os
from openai import OpenAI

#choose a LLM and put the API key and the url.
api_key=('sk-da97a5d511f24081b5d68bdc8fccdc24')
base_url="https://dashscope.aliyuncs.com/compatible-mode/v1"
model_name = "qwen-turbo"

def process_data():
    print("1.Read the data...")
    try:
        with open('national_games.json', 'r', encoding='utf-8') as f:
            raw_news = json.load(f)
    except FileNotFoundError:
        print("Error：Can't find national_games.json")
        return

    #Limited 15, do not exceed the token
    news_text = ""
    for i, item in enumerate(raw_news[:15]):
        clean_snippet = item['summary_snippet'].replace('<', ' ').replace('>', ' ') 
        news_text += f"{i+1}. [{item['source']}] {item['title']} ({item['published']})\n"

    print("2. LLM is analyzing...")
    
    client = OpenAI(api_key=api_key, base_url=base_url)

    # Prompt
    prompt = f"""
You are a professional sports editor covering the 15th National Games.
Based on the following news list:
{news_text}

Please generate a structured JSON response (Strictly JSON only, no Markdown). 

Requirements for the JSON structure:
    1. "overall_summary": (String) A concise and powerful executive summary of the whole situation.
    2. "highlights": (List of Strings) Extract 3-5 core hot spots or major events.
    3. "regional_analysis": (String) Analyze the performance or preparations of major provinces/cities (especially Guangdong, Hong Kong, Macau).
    4. "deep_insights": (List of Strings) 2 deep value points beyond the competition (e.g., economic impact, technology, cultural integration).
    5. "keywords": (List of Strings) 5 key entities or buzzwords.
    6. "timeline": (List of Objects) Key time nodes, each having "date" and "event".

Output valid JSON only.
"""

    try:
        response = client.chat.completions.create(
            model=model_name,
            messages=[
                {"role": "system", "content": "You are a helpful data assistant. You strictly output valid JSON."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,
        )
        
        content = response.choices[0].message.content
        print("LLM return content", content) 
        
        #Analyze json
        clean_content = content.replace("```json", "").replace("```", "").strip()
        structured_data = json.loads(clean_content)
        
        # Link to the original text
        final_data = {
            "analysis": structured_data,
            "sources": raw_news
        }

        # save the result
        with open('processed_data.json', 'w', encoding='utf-8') as f:
            json.dump(final_data, f, ensure_ascii=False, indent=4)
            
        print("3. Finish, the data has been save as 'processed_data.json'")

    except Exception as e:
        print(f"error: {e}")

if __name__ == "__main__":
    process_data()