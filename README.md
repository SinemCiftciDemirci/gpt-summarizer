##GPT-Summarizer
This repository provides a script to generate an extractive summary of a given text file using OpenAI’s GPT model (configured to use GPT-4 by default). The script prompts you to select a .txt file and then produces a summary divided into three sections in Turkish: Introduction (Giriş), Development (Gelişme), and Conclusion (Sonuç).

##Project Structure

GPT-SUMMARIZER/
│── config_loader.py
│── config.txt
│── gpt_summarizer.py
└── README.md

config_loader.py
Loads the OpenAI API key from config.txt and configures CUDA/CPU usage.

config.txt
Contains your OpenAI API key and any other configuration needed. An example key entry might look like:

OPENAI_API_KEY= "your_openai_api_key"

gpt_summarizer.py
The main script that uses the OpenAI API to generate an extractive summary. It:

1.Reads the OpenAI API key from config_loader.py.
2.Opens a file dialog to let you choose a .txt file to summarize.
3.Sends a prompt to GPT-4 to create a fairy-tale style summary in Turkish, broken down into three sections.
4.Saves the resulting summary in the gpt_summaries/ folder.

##Requirements
Python 3.7+
OpenAI Python Library (openai)
tkinter (built into most Python distributions on Windows; on some systems you may need to install it separately)

##Usage
1.Set up your OpenAI API key
##In config.txt, add a line like:
OPENAI_API_KEY=sk-xxxxxxxxxxxxxxx

2.Run the script
python gpt_summarizer.py

3.Choose a file
A file dialog will appear. Select the .txt file you want to summarize.

4.Check the output
Once processed, the summary will be saved inside the gpt_summaries/ folder (created automatically if it doesn’t exist).
The summary file will have the same name as the original text but with a .txt extension, for example:
gpt_summaries/your_file_summary.txt


##How It Works
The script uses GPT-4 via openai.ChatCompletion.create and a special prompt that forces the model to create an extractive summary in a fairy-tale style.
The generated summary is then split into Introduction, Development, and Conclusion sections.
By default, the summarized text’s length is about 1/6 of the original story.

##Troubleshooting
If you receive an API key error, ensure your config.txt has the correct key format and matches what config_loader.py expects.
If you encounter issues with CUDA/CPU selection, see the logs from config_loader.py. If CUDA is not available, it will fall back to CPU.

##License
This project is provided under an open license (MIT, Apache 2.0, or your preferred license). Feel free to modify and distribute as needed.