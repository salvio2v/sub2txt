# VTT to Text Translator

This script reads a **VTT** subtitle file, converts it into **plain text**, and translates it from a source language to a target language using LangChain’s **ChatGroq** model.

---

## 📦 Requirements

* Python 3.10+
* LangChain with `ChatGroq` support
* `python-dotenv` to load environment variables
* A `.env` file containing any required credentials or configuration

Install dependencies with:

```bash
pip install langchain-groq python-dotenv
```

---

## 📝 Usage

1. Prepare a VTT file to convert (e.g., `example.vtt`).
2. Create a `.env` file if needed for your `ChatGroq` setup or other API service.
3. Set the variables in the script:

```python
source_language = 'english'  # language of the VTT file
target_language = 'italian'  # language to translate into
file_name = "example"        # file name without extension
```

4. Run the script:

```bash
python sub2txt.py
```

5. A `.txt` file (`example.txt`) will be generated containing the translated text.

---

## ⚙️ How it works

1. **`file_operation` function**:

   * Reads (`r`) or writes (`w`) files.
   * Checks that the operation is valid.

2. **Environment loading**:

   * `load_dotenv()` loads environment variables from `.env`.

3. **LLM setup**:

   * Uses `ChatGroq` with parameters like `model`, `temperature`, `max_tokens`, and `reasoning_format`.

4. **Messages for the model**:

   * The `system` message instructs the AI to translate and convert the VTT into text.
   * The `human` message contains the content of the VTT file to translate.

5. **Saving the result**:

   * The AI’s response is written to a `.txt` file.

---

## 🔧 Notes


* You can change `source_language` and `target_language` for any other language pair supported by the model.
* You can change the subtitles format into differents format by changing the system prompt