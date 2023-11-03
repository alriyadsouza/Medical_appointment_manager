
def get_response(message, question_number):
    if question_number == 0:
        return "Hi! How can I assist you today? What is your gender?"
        question_number+=1
    elif question_number == 1:
        return "Great! Could you please tell me your age?"
        question_number+=1
    elif question_number == 2:
        return "What is your neighborhood?"
        question_number+=1
    elif question_number == 3:
        return "Do you have any scholarship? If yes, please provide the details."
        question_number+=1
    elif question_number == 4:
        return "Please select your disease type from the options provided."
        question_number+=1

# constants.py

bot_name = "Sam"
question_number = 0


