import random


knowledge_base = {
    "hello": "Hi there! How can I help you?",
    "hi": "Hello! What's on your mind?",
    "how": "I'm doing great, thank you! How about you?",
    "weather": "It's always sunny in the world of code!",
    "bye": "Goodbye! Have a great day!",
    "name": "I'm your friendly chatbot. What's yours?",
    "food": "I love pizza! What about you?",
    "book": "Reading is a great way to learn new things!",
    "python": "Python is my favorite programming language.",
    "ai": "Artificial Intelligence is fascinating, isn't it?",
    "love": "Love makes the world go round!",
    "happy": "I'm glad to hear that you're happy!",
    "sad": "I'm here for you. Tell me more.",
    "dog": "Dogs are amazing pets!",
    "cat": "Cats are adorable!",
    "school": "Education is the key to success.",
    "code": "Coding is both fun and challenging!",
    "friend": "Friends make life better.",
    "family": "Family is everything!",
    "music": "Music soothes the soul.",
    "movie": "I love movies! What's your favorite?",
    "game": "Gaming is so much fun. Do you play?",
    "coffee": "I could use some coffee too!",
    "tea": "Tea is great for relaxing.",
    "travel": "Traveling opens your mind to new cultures.",
    "hobby": "What's your favorite hobby?",
    "car": "What car do you like the most?",
    "dream": "Dream big and never give up!",
    "job": "What do you do for a living?",
    "sleep": "Getting enough sleep is important for your health.",
    "exercise": "Staying fit is always a great idea!",
    "help": "I'm here to help. What do you need?",
    "joke": "Why did the chicken join the band? Because it had the drumsticks!",
    "happy birthday": "Happy Birthday! Wishing you all the best!",
    "new year": "Happy New Year! Let's make it a great one!",
    "holiday": "Holidays are the best time to relax and recharge.",
    "money": "Saving money is a good habit.",
    "health": "Take care of your health. It's important!",
    "work": "Work hard, but don't forget to rest.",
    "study": "Studying helps you achieve your goals.",
    "fun": "Life is better when you have fun!",
    "flower": "Flowers make the world more beautiful.",
    "nature": "Nature is so calming and inspiring.",
    "party": "Parties are a great way to celebrate!",
    "computer": "Computers are amazing tools for creativity.",
    "phone": "Smartphones make life so convenient.",
    "internet": "The internet connects the world.",
    "bookstore": "Books are windows to new worlds!",
    "coding": "Coding is the future. Let's learn it!",
    "universe": "The universe is full of mysteries.",
    "science": "Science helps us understand the world.",
    "math": "Math is the language of the universe!",
    "history": "History teaches us valuable lessons.",
    "sport": "What's your favorite sport?",
    "football": "Football is a thrilling game!",
    "basketball": "Basketball is so exciting!",
    "cricket": "Cricket is a very popular sport in many countries.",
    "art": "Art inspires creativity.",
    "drawing": "Drawing is a great way to express yourself.",
    "painting": "Painting brings colors to life!",
    "dance": "Dancing is such a joyful activity!",
    "singing": "Singing makes everything better.",
    "technology": "Technology drives innovation!",
    "robot": "Robots are fascinating machines.",
    "space": "Space exploration is incredible!",
    "moon": "The moon looks so beautiful at night.",
    "stars": "The stars remind us how vast the universe is.",
    "planet": "Earth is our home, but there are many other planets out there.",
    "ocean": "The ocean is full of amazing creatures.",
    "animal": "Animals are wonderful beings.",
    "bird": "Birds bring music to nature.",
    "science fiction": "Sci-fi stories ignite imagination.",
    "movie star": "Who's your favorite actor or actress?",
    "culture": "Learning about new cultures is exciting.",
    "festival": "Festivals bring joy to everyone.",
    "car": "What's your dream car?",
    "garden": "Gardens are peaceful and full of life.",
    "music band": "Which band do you like the most?",
    "hero": "Heroes inspire us to be better.",
    "villain": "Villains make stories more interesting!",
    "weather": "How's the weather where you are?",
    "teacher": "Teachers shape the future.",
    "student": "Students are the leaders of tomorrow.",
    "child": "Children bring happiness to families.",
    "question": "Feel free to ask me anything!",
    "animal": "Which animal is your favorite?",
    "king": "Kings have ruled history for centuries.",
    "queen": "Queens have been powerful leaders too!",
    "city": "Which city do you live in?",
    "country": "Which country are you from?",
    "family": "Family time is precious.",
    "pet": "Pets bring joy to our lives."
}

def chatbot():
    print("Chatbot: Hello! I understand 100 words. Type 'exit' to end the chat.")
    while True:
        user_input = input("You: ").lower()
        if user_input == "exit":
            print("Chatbot: Goodbye! It was nice chatting with you!")
            break
        response = None
        for word in knowledge_base.keys():
            if word in user_input:
                response = knowledge_base[word]
                break
        if response:
            print(f"Chatbot: {response}")
        else:
            print("Chatbot: I'm sorry, I don't understand that. Could you try a different word?")


if __name__ == "__main__":
    chatbot()
