import json

with open('classic_837_blocks.json', 'r', encoding='utf-8') as f:
    blocks = json.load(f)

print("Type of blocks:", type(blocks))
if isinstance(blocks, list) and len(blocks) > 0:
    print("Keys of blocks[0]:", blocks[0].keys() if isinstance(blocks[0], dict) else type(blocks[0]))
    print("Sample content:", str(blocks[0])[:300])
