import random

num = random.randint(1, 9)

answerd = ["Yes - definitely.",
"It is decidedly so.",
"Without a doubt.",
"Reply hazy, try again.",
"Ask again later.",
"Better not tell you now.",
"My sources say no.",
"Outlook not so good.",
"Very doubtful."]

question = input("Ask a question: ")

print("Question: ", question)
print("Magic 8 Ball says: ", answerd[num])