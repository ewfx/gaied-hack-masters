import google.generativeai as genai

def summarize_text_with_gemini(api_key, text):
    """
    Connects to the Gemini LLM and summarizes the given text.

    Args:
        api_key: Your Google Gemini API key.
        text: The text to summarize.

    Returns:
        The summary of the text, or None if an error occurs.
    """
    try:
        genai.configure(api_key=api_key)
        model = genai.GenerativeModel('gemini-2.0-flash')  

        prompt = f"I am banker and I have to route the following text to specific department such as 'adjustment', 'money-transfer':\n\n{text}\n\nSummary:"
        response = model.generate_content(prompt)

        return response.text

    except Exception as e:
        print(f"An error occurred: {e}")
        return None



if __name__ == "__main__":
    # Replace 'YOUR_API_KEY' with your actual Gemini API key.
    api_key = "Your_API_Key"

    text_to_summarize = """
    Subject: Covenant Compliance Adjustment Request – Project Orion Expansion

Dear Mr. Thompson,

We request an adjustment to the compliance requirements under the terms of our agreement for Project Orion Expansion. The revised compliance details are as follows:
	•	Deal Name: Project Orion Expansion
	•	Original Covenant Requirement: Maintain a minimum Debt-to-Equity ratio of 1.5 ￼
	•	Requested Adjustment: Increase allowable Debt-to-Equity ratio to 2.0
	•	Reason for Adjustment: To accommodate additional capital expenditure for facility expansion
	•	Effective Date: 04/15/2025

Please review this request and confirm if it can be accommodated.

Best regards,

Emily Davis
Stellar Manufacturing Ltd

    """

    summary = summarize_text_with_gemini(api_key, text_to_summarize)

    if summary:
        print("Summary:")
        print(summary)
    else:
        print("Failed to generate summary.")