# Am I Fighting Well? Fighting Game Commentary Generation With ChatGPT ([Paper](https://dl.acm.org/doi/10.1145/3628454.3629551))

This repository contains the code for the paper "Am I Fighting Well? Fighting Game Commentary Generation With ChatGPT" accepted at [IAIT 2023](https://www.iait-conf.org/2023/).

## Abstract

This paper presents a new approach for leveraging ChatGPT in fighting game commentary generation task. Commentary generation often relies on deep learning techniques, which typically demand extensive data to achieve effectiveness. Large language models (LLMs) have become essential due to their remarkable ability to process data efficiently, thanks to their extensive training on vast datasets. Our proposed approach integrates the use of LLMs, specifically the GPT-3.5 model, for generating commentaries through the utilization of various prompts with data from the open-source fighting game, DareFightingICE. Four prompt variants are employed to assess the effectiveness of each prompt components. Objective evaluation using natural language metrics reveals that different prompt components significantly affect the generated commentaries. Additionally, subjective evaluation through a questionnaire reveals that prompts without parameter definitions received the highest preference from human evaluators. These results suggest that LLMs exhibit versatility in generating fighting game commentaries and hold promise for broader applications.

## File structure
- `main.py`: The main script for story generation and ending evaluation.
- `requirements.txt`: The requirements file for the project.
- `example.py`: example of how to utilize the code
- `eval.py`: evaluation runner
- `outputs/`: The directory containing the generated results from ChatGPT.
- `src/`: The directory containing utility files for `main.py`
- `data/`: The directory containing word lists used for data generation process.
- `logs`: The directory containing log of the experiment.

## Installation and Usage
0. Create a virtual environment (if needed):
```bash
conda create -n chatgpt-game-comment python=3.11
```
and activate it:
```bash
conda activate chatgpt-game-comment
```
1. Copy `.env.example` and rename it to `.env`. Follow instructions on [this page](https://platform.openai.com/docs/api-reference/authentication) to obtain your own OpenAI API key.
2. Install the requirements:
```bash
pip install -r requirements.txt
```
3. Change `src/config.py` as needed
4. Run the script for experiment:
```bash
python main.py
```
