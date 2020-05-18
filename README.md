## Hello 😄

In this small NLP project, transfer learning with Google AI's BERT model is used to classify twitter tweets into one of five classes of sentiments. 

| Input | Output  | 
| :---:   | :-: | 
| I just wanna get out of the friendzone | 🥺 |

Results are presented in results.csv

## Where the data came from

The model is trained on tweets randomly scraped from twitter. Uses [twitterscraper](https://github.com/taspinar/twitterscraper) to scrape random tweets containing one of the five emojis. In total, there are 2000 training examples for every emoji. 

| Emoji  | Y label |
| ------------- | ------------- |
| ❤️  | 0 |
| 😄  | 1  |
| 😔  | 2  |
| 🥺  | 3  |
| 😤  | 4  |

## References

- [BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding](https://arxiv.org/pdf/1810.04805.pdf) 
- [Attention Is All You Need](https://arxiv.org/pdf/1706.03762.pdf)
- [Hugging Face Docs](https://huggingface.co/transformers/main_classes/optimizer_schedules.html)
- [Pytorch Documentation](https://pytorch.org/docs/stable/index.html)



