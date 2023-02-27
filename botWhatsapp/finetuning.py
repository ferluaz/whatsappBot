import json
from transformers import GPT2LMHeadModel, GPT2Tokenizer
import torch
from torch.utils.data import Dataset, DataLoader
import torch.optim as optim

# Load the JSONL file
with open('whatsapp_chat.jsonl', 'r') as f:
    conversations = [json.loads(line) for line in f]

# Initialize the GPT-2 tokenizer and model
tokenizer = GPT2Tokenizer.from_pretrained('gpt2')
model = GPT2LMHeadModel.from_pretrained('gpt2')

# Define a custom dataset class
class MyDataset(Dataset):
    def __init__(self, conversations, tokenizer):
        self.conversations = conversations
        self.tokenizer = tokenizer

    def __len__(self):
        return len(self.conversations)

    def __getitem__(self, index):
        conversation_text = '\n'.join([message['text'] for message in self.conversations[index]['messages']])
        input_ids = self.tokenizer.encode(conversation_text)
        return torch.tensor(input_ids)

# Create a dataset and data loader
dataset = MyDataset(conversations, tokenizer)
dataloader = DataLoader(dataset, batch_size=8, shuffle=True)

# Define the optimizer
optimizer = optim.Adam(model.parameters(), lr=1e-5)

# Train the model
model.train()
for epoch in range(3):
    for batch in dataloader:
        optimizer.zero_grad()
        outputs = model(batch, labels=batch)
        loss = outputs.loss
        loss.backward()
        optimizer.step()

# Save the fine-tuned model
model.save_pretrained('fine_tuned_model')
