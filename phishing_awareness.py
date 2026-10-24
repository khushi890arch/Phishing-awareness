questions = [
    {
        "email": """
From: security@paypa1-support.com
Subject: Your account will be suspended!

Your account has been detected for suspicious activity.
Verify your account immediately by clicking the link below.

http://paypa1-security-verification.com
""",
        "answer": "P",
        "reason": "The domain is suspicious and creates urgency."
    },

    {
        "email": """
From: hr@company.com
Subject: Team Meeting

Hello Team,

This is a reminder that the weekly team meeting
will be held tomorrow at 11:00 AM.

Regards,
HR Team
""",
        "answer": "L",
        "reason": "The message contains no suspicious links or urgent requests."
    },

    {
        "email": """
From: bank-alert@gmail.com
Subject: URGENT! Account Blocked

Your bank account has been blocked.
Send your OTP and password immediately to restore access.
""",
        "answer": "P",
        "reason": "Banks do not ask users to share passwords or OTPs through email."
    },

    {
        "email": """
From: notifications@github.com
Subject: New login detected

A new login was detected on your account.
Please open GitHub directly and check your security settings
if you do not recognize this activity.
""",
        "answer": "L",
        "reason": "The message does not request sensitive information and recommends visiting the official website directly."
    },

    {
        "email": """
From: prizewinner2026@gmail.com
Subject: CONGRATULATIONS! You Won ₹50,000

You have won our special prize.
Pay ₹999 processing fees immediately to claim your reward.
""",
        "answer": "P",
        "reason": "Unexpected prizes and requests for advance payment are common phishing indicators."
    }
]


def show_tips():
    print("\n" + "=" * 60)
    print("           PHISHING SAFETY TIPS")
    print("=" * 60)

    tips = [
        "Check the sender's email address carefully.",
        "Do not click suspicious links.",
        "Never share passwords or OTPs.",
        "Be careful with urgent or threatening messages.",
        "Verify requests using official websites or phone numbers.",
        "Do not pay unexpected fees to claim prizes.",
        "Enable multi-factor authentication whenever possible."
    ]

    for i, tip in enumerate(tips, 1):
        print(f"{i}. {tip}")


def start_quiz():

    score = 0

    print("=" * 60)
    print("          PHISHING AWARENESS TRAINING")
    print("=" * 60)

    print("\nP = Phishing")
    print("L = Legitimate")

    for number, question in enumerate(questions, 1):

        print("\n" + "-" * 60)
        print(f"EMAIL {number}")
        print("-" * 60)

        print(question["email"])

        while True:
            answer = input("\nYour answer (P/L): ").strip().upper()

            if answer in ["P", "L"]:
                break

            print("Please enter only P or L.")

        if answer == question["answer"]:
            print("✓ Correct!")
            score += 1
        else:
            print("✗ Incorrect.")

        print("Explanation:", question["reason"])

    print("\n" + "=" * 60)
    print("                 FINAL RESULT")
    print("=" * 60)

    print(f"Score: {score}/{len(questions)}")

    percentage = (score / len(questions)) * 100
    print(f"Accuracy: {percentage:.1f}%")

    if percentage == 100:
        print("Excellent! You identified all phishing indicators.")
    elif percentage >= 60:
        print("Good job! Improve your ability to inspect suspicious messages.")
    else:
        print("More awareness training is recommended.")

    show_tips()


start_quiz()