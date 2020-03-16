## Hello 😄

This deep learning model takes text inputs and ouputs an emoji that it sees fit based on the sentiment of the text. The model is trained on tweets randomly scraped from twitter.

| Input | Output  | 
| :---:   | :-: | 
| I just wanna get out of the friendzone | 🥺 |

## Scraping Data from Twitter

Uses [twitterscraper](https://github.com/taspinar/twitterscraper) to scrape random tweets containing one of the five emojis. In total, there are 2000 training examples for every emoji. 

| Emoji  | Y label |
| ------------- | ------------- |
| ❤️  | 0 |
| 😄  | 1  |
| 😔  | 2  |
| 🥺  | 3  |
| 😤  | 4  |

## Preprocessing

- Tokenize tweets using nltk's [word_tokenzie](https://github.com/hb20007/hands-on-nltk-tutorial/blob/master/1-2-Text-Analysis-Using-nltk.text.ipynb) 

- Find the maximum length of all the tweets and pad every example to the same length

- Convert each word in the tokenized sentence into an index corresponding the the word's index in the glove's word embedding


## Model Summary

Using a pre-trained 50-dimensional glove embedding layer and LSTM

<img src="https://github.com/laurie-gao/Emojify/blob/master/images/model_summary.png" alt="model" width="600"/>


## Result

<img src="https://github.com/laurie-gao/Emojify/blob/master/images/model_accuracy.png" alt="model" width="400"/>
<img src="https://github.com/laurie-gao/Emojify/blob/master/images/model_loss.png" alt="model" width="400"/>

Note: test in this case denotes the validation set

Due to the lack of training examples and the nature of the tweets used (there is a low correlation between the tweets and emojis), the model could not achieve a high accuracy on the validation set. Although the accuracy increased, the loss for the validation decreased, which may imply that the model is less confident with its predictions. 


