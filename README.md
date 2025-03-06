# 🚀 GPT-Summarizer

🔗 Related Projects This project is part of a modular research framework for evaluating and improving fairy tale summarization models. Below are the related repositories:

| Children's Tale Summarizer - Flask App | The main Flask-based API that generates fairy tale summaries. (https://github.com/SinemCiftciDemirci/childrens-tale-summarizer-flask-app) |

| GPT Summarizer | Creates GPT-based fairy tale summaries. (https://github.com/SinemCiftciDemirci/gpt-summarizer) |

| Cosine Similarity Summarizer | Performs extractive summarization using cosine similarity. (https://github.com/SinemCiftciDemirci/cosine-similarity-summarizer) |

| Single Summary Evaluation | Measures the performance of a single summary using BERTScore and ROUGE score. (https://github.com/SinemCiftciDemirci/single-summary-evaluation) |

| Batch Summary Performance Evaluation | Compares model-generated summaries with GPT and Cosine-based reference summaries, calculating ROUGE and BERTScore collectively. (https://github.com/SinemCiftciDemirci/batch-summary-performance-evaluation) |

| Summary Performance Comparison | Creates visual performance comparisons from the Model_Performance.xlsx file produced in the Batch Summary Evaluation repo. (https://github.com/SinemCiftciDemirci/summary-performance-comparison) |

| Vision Model Test | Translates the generated summaries into English and creates three visuals: introduction, development, and conclusion. (https://github.com/SinemCiftciDemirci/vision-model-test) |

Each repository serves a unique role in evaluating or improving summarization models. You can use them individually or together for deeper analysis.

**GPT-Summarizer** is a Python script designed to generate an **extractive summary** of text files using OpenAI's GPT-4 model. It specifically generates summaries in Turkish, structured into three clearly defined sections:

- 📖 **Introduction (Giriş)**
- ⚙️ **Development (Gelişme)**
- ✅ **Conclusion (Sonuç)**

## 📂 Project Structure

```bash
GPT-SUMMARIZER/
├── config_loader.py
├── config.txt
├── gpt_summarizer.py
└── README.md
```

- **`config_loader.py`**  
  ⚙️ Loads OpenAI API keys from `config.txt` and manages CUDA/CPU settings.

- **`config.txt`**  
  🔑 Stores your OpenAI API key:
  ```
  OPENAI_API_KEY="your_openai_api_key"
  ```
  > 🚨 **Note:** Do **NOT** share your actual API key publicly.

- **`gpt_summarizer.py`**  
  📝 Core script to summarize text files:

  1. Loads the API key from `config_loader.py`.
  2. Opens a file dialog to choose a `.txt` file.
  3. Generates a fairy-tale style summary using GPT-4.
  4. Saves the summary to the `gpt_summaries/` folder.

## 🔧 Requirements

- 🐍 **Python 3.7+**
- 📚 **OpenAI Python Library** (`openai`)
- 🖥️ **tkinter** (usually pre-installed with Python)

Install required packages:

```bash
pip install openai
```

## ▶️ Usage

### 1. Set up your OpenAI API key

Edit `config.txt`:

```bash
OPENAI_API_KEY=sk-xxxxxxxxxxxxxxx
```

### 2. Run the summarizer

Execute the script:

```bash
python gpt_summarizer.py
```

### 3. Choose your file

Select the `.txt` file you'd like to summarize from the popup dialog.

### 4. Review your summary

The summarized output will be saved in:

```
gpt_summaries/your_file_summary.txt
```

> 📌 **Note:** The script automatically creates the `gpt_summaries/` directory if it does not exist.

## 🛠️ How It Works

- GPT-4 generates an extractive summary maintaining the original storyline and fairy-tale narration style.
- The summary is segmented clearly into **Introduction**, **Development**, and **Conclusion**.
- The final summary length is about **1/6th** of the original story length.

## ❗ Troubleshooting

- 🔑 **API Key Issues:**
  - Ensure `config.txt` includes the correct API key.
- 💻 **CUDA/CPU Issues:**
  - Check logs from `config_loader.py`. If CUDA isn't available, the script will default to CPU.

## 📄 License

This project is provided under an open license (MIT). Feel free to modify and distribute it as needed.
