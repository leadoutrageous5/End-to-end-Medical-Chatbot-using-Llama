# End-to-end-Medical-Chatbot-using-Llama2


## Steps to run the Project

### Step 1: Create and Activate a python envirnoment(virutal environment) after cloning the repo and opening it.
```bash
python3 -m venv mchatbot
```

```bash
source mchatbot/bin/activate
```

### Step 2: Install the Requirements
```bash
pip install -r requirements.txt
```

### Create a `.env` file in the root directory and add your Pinecone credentials as follows:

```ini
PINECONE_API_KEY="xxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
```

### Download the quanatize model from the link provided in model folder and keep the model in the model directory:

```ini

## Download the Llama 2 Model :

llama-2-7b-chat.ggmlv3.q2_K.bin

## From the following link:
https://huggingface.co/TheBloke/Llama-2-7B-Chat-GGML/tree/main

```
