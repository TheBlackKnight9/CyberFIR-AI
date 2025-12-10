import csv
import random

OUTPUT_FILE = "fir_dataset_1000.csv"

crimes = [
    "hacking",
    "phishing",
    "extortion",
    "harassment",
    "impersonation",
    "stalking",
    "fraud",
]

# 1000 rows total: 6 classes × 143 + 1 class × 142 = 1000
per_class_counts = {
    "hacking": 143,
    "phishing": 143,
    "extortion": 143,
    "harassment": 143,
    "impersonation": 143,
    "stalking": 143,
    "fraud": 142,
}

subjects = [
    "my Instagram account",
    "my Facebook account",
    "my Gmail account",
    "my bank account",
    "my Paytm account",
    "my Netflix account",
    "my Twitter account",
    "my phone",
    "my laptop",
]

money_phrases = [
    "₹2000",
    "₹4000",
    "₹5000",
    "₹8000",
    "₹10000",
    "₹15000",
    "₹25000",
]

cities = ["Delhi", "Mumbai", "Jaipur", "Pune", "Chennai", "Kolkata", "Bengaluru"]

# Templates per crime type
def hacking_sentence():
    return random.choice([
        f"Someone hacked {random.choice(subjects)} and changed the password",
        f"Unknown person logged into {random.choice(subjects)} without permission",
        f"My {random.choice(subjects)} was accessed from a different location and I was locked out",
        f"Malware was installed on {random.choice(['my phone','my laptop'])} and my data was stolen",
        f"My online game account was hacked and all items were taken",
    ])

def phishing_sentence():
    return random.choice([
        f"I received a fake SMS claiming to be from my bank asking for OTP for {random.choice(money_phrases)} refund",
        f"An email pretending to be from a courier service asked me to click a link to pay charges",
        f"A message said my KYC is incomplete and provided a suspicious link",
        f"I got a WhatsApp message saying I won a lottery and must pay a processing fee",
        f"A fake customer care number asked me to share card details over call",
    ])

def extortion_sentence():
    return random.choice([
        f"Someone threatened to leak my private photos unless I paid {random.choice(money_phrases)}",
        "He is blackmailing me using my personal chats and demanding money",
        "He said he will post my videos online if I do not send money",
        "He demanded money to return my hacked social media account",
        "He keeps asking for payment and threatens to ruin my reputation",
    ])

def harassment_sentence():
    return random.choice([
        "He sends abusive and vulgar messages to me every day",
        "He posts obscene comments on my social media photos",
        "He insults and humiliates me in group chats repeatedly",
        "He keeps body shaming me online and uses bad words",
        "He spreads false rumours about me in online groups",
    ])

def impersonation_sentence():
    return random.choice([
        "He created a fake profile using my name and photos",
        "Someone is pretending to be me on Instagram and messaging my friends",
        "A fake WhatsApp account was created in my name asking for money",
        "He used my photos to open a Facebook account without permission",
        "He is posing as me and sending messages to my relatives",
    ])

def stalking_sentence():
    return random.choice([
        "He keeps messaging me even after I blocked him several times",
        "He follows me on every social media platform and comments on everything",
        "He tracks my online status and messages me whenever I come online",
        "He keeps asking personal questions and does not stop even after warnings",
        "He constantly monitors my stories and reacts to each one in a creepy way",
    ])

def fraud_sentence():
    return random.choice([
        f"He tricked me into sending {random.choice(money_phrases)} for a fake product and then blocked me",
        f"He promised a job and took {random.choice(money_phrases)} as registration fee but disappeared",
        "He took money online for ticket booking and never sent any ticket",
        "A fake investment scheme cheated me and my money is gone",
        "A so-called baba promised to solve my problems, took money online and then stopped responding",
    ])

generators = {
    "hacking": hacking_sentence,
    "phishing": phishing_sentence,
    "extortion": extortion_sentence,
    "harassment": harassment_sentence,
    "impersonation": impersonation_sentence,
    "stalking": stalking_sentence,
    "fraud": fraud_sentence,
}

def main():
    rows = []
    for crime in crimes:
        gen = generators[crime]
        for _ in range(per_class_counts[crime]):
            text = gen()
            # add a random city sometimes to increase variety
            if random.random() < 0.3:
                text += f" This happened while I was in {random.choice(cities)}."
            rows.append({"text": text, "crime": crime})

    random.shuffle(rows)

    with open(OUTPUT_FILE, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["text", "crime"])
        writer.writeheader()
        writer.writerows(rows)

    print(f"Wrote {len(rows)} rows to {OUTPUT_FILE}")

if __name__ == "__main__":
    main()
