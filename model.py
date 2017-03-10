import skipthoughts

#load skip thought model
model = skipthoughts.load_model()
encoder = skipthoughts.Encoder(model)

#get encoding
x = ["the cat ran", "the dog slid"]
vectors = encoder.encode(x)

print vectors