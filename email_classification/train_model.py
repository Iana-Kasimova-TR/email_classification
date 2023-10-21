import fasttext

model = fasttext.train_supervised(input='fasttext_data.txt')

model.save_model('model.bin')