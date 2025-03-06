import openai
import tkinter as tk
from tkinter import filedialog
import os
from config_loader import load_keys_from_file

# Load the config file
config = load_keys_from_file("config.txt")

# Retrieve the OpenAI API key
api_key = config.get("OPENAI_API_KEY")

def upload_and_summarize(api_key):
    """
    Select a file from the file explorer and summarize its content
    into three sections: Introduction, Development, and Conclusion in Turkish,
    and save the summary in the 'gpt_summaries' folder.
    
    Args:
        api_key (str): OpenAI API key
    """
    # Set the OpenAI API key
    openai.api_key = api_key

    # Select a file
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename(title="Select a Text File", filetypes=[("Text Files", "*.txt")])

    if not file_path:
        print("No file selected.")
        return

    # Read the file
    with open(file_path, "r", encoding="utf-8") as file:
        content = file.read()

    # Prompt for summarization in Turkish
    prompt = (
    "I want you to write a summary of a fairy tale. The summary must follow these rules:\n"
    "1. I want an extractive summary. The summary must strictly adhere to the given story. No additional information or creative expressions outside the story should be added.\n"
    "2. It should not change the events in the text but should narrate them as they are.\n"
    "3. The narration should have a fairy-tale-like style but should not be exaggerated.\n"
    "4. Detailed dialogues and direct character reactions should be taken from the text and used.\n"
    "5. Instead of 'did' or 'made', use expressions like 'had done' or 'had made'.\n"
    "6. Cliché phrases (e.g., 'The fairy tale ends here' or 'And thus the adventure ended') should not be used.\n"
    "7. The narration should maintain the order of events and storyline. Unnecessary inferences should not be made.\n\n"
    "Divide the story into three main sections: Introduction (30%), Development (40%), and Conclusion (30%). "
    "Each section should be explicitly presented under the headings 'Introduction:', 'Development:', 'Conclusion:'. "
    "The total length should be approximately 1/6 of the original story.\n\n"
    f"Story:\n{content}"
)

    # OpenAI API call
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are an assistant that summarizes fairy tales in Turkish in a fairy-tale-like style."},
                {"role": "user", "content": prompt}
            ]
        )

        summary = response['choices'][0]['message']['content']
        
        # Save the summary to the 'gpt_summaries' folder
        summaries_folder = "gpt_summaries"
        if not os.path.exists(summaries_folder):
            os.makedirs(summaries_folder)

        # Generate a new file name based on the input file
        base_name = os.path.basename(file_path)
        summary_file_path = os.path.join(summaries_folder, f"{os.path.splitext(base_name)[0]}.txt")

        with open(summary_file_path, "w", encoding="utf-8") as summary_file:
            summary_file.write(summary)
        
        print(f"Summary saved at '{summary_file_path}'")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    if api_key:
        upload_and_summarize(api_key)
    else:
        print("OpenAI API key could not be retrieved from the config file.")